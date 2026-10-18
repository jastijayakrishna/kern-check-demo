# fix(sync): reconcile kilter_id before the ratings upsert

## Summary

The kilter daemon's **user-data** half had not completed a single successful sync inside the
30-day log retention window. The catalog half was fine and the aurora daemon on the same VM
succeeded constantly, so this was never infra. Two users sat at attempt 63.

```
[KilterSyncRunner] Permanent sync failure for user 0df1d963-… (status=error, attempt 63):
  Failed query: insert into "board_climb_ratings" …
  cause: PostgresError: duplicate key value violates unique constraint
         "board_climb_ratings_kilter_id_unique"
    at async applyClimbRatings (packages/kilter-sync/src/sync/user-sync.ts:1146:3)
```

### Root cause

`board_climb_ratings` carries **two** independent uniques over the same row: the natural key
`(board_type, climb_uuid, angle, user_id)` and a **global** partial unique on `kilter_id`.
`applyClimbRatings` conflict-targets the natural key, and Postgres permits exactly one conflict
target per `ON CONFLICT` — so the surrogate unique was uncovered on **both** the `INSERT` branch
and the `DO UPDATE` branch (which writes `kilter_id` through `COALESCE`).

Two paths reached the violation:

- **Intra-statement** — the batch deduped on the *natural* key only. Two PUTs sharing one
  `climb_rating_uuid` at different natural keys (an upstream angle edit, or two source UUIDs that
  re-canonicalise differently) both survived into one `INSERT` with the same `kilter_id`.
- **Cross-row** — the incoming `climb_rating_uuid` already sat on a different row: this user's row
  at an older natural key, or a row owned by a *different* Boardsesh user (one Kilter account
  linked to two accounts).

The `23505` escaped `syncKilterUserData` entirely, so **the circuits phase never ran either** —
these users silently lost playlist sync too. The runner fails closed on a non-`KilterApiError`, so
a raw Postgres error was classified **permanent**. PowerSync re-delivers the full snapshot every
cycle, so it failed identically forever.

`applyLogs` has defended against all of this for `boardsesh_ticks` all along. Its own comment
claims it mirrors `applyClimbRatings` — that belief was the bug.

### The fix

- Dedupe by `climb_rating_uuid` **before** the natural-key dedupe (surrogate-first is the only
  order under which one upstream row maps to one output row at its *current* natural key).
- One global, deliberately un-user-scoped pre-SELECT, partitioned into own vs foreign owners. A
  foreign-owned id is **skipped and logged**, never stolen.
- **Repoint** a same-user id that moved: detach the stale row in the same transaction, then let the
  upsert stamp it. Nothing is ever deleted.
- Chunk the upsert at 100 with a savepoint and row-by-row replay, so a row Postgres refuses costs
  one rating rather than the buffer, the user, and the circuits phase.
- Take the per-user advisory lock so the read-then-write can't race.
- Isolate each sync phase so a ratings failure no longer cancels circuits.

### Why `kilter_detached_at` is stamped on a repoint

Worth a reviewer's attention, since "the rating moved" is not "Kilter deleted it". `push-back`
selects Boardsesh-origin ratings with `kilter_id IS NULL AND kilter_detached_at IS NULL`. Nulling
the surrogate *without* the marker would make the stale row look never-pushed, and the day the POST
is wired push-back would re-create it upstream as a duplicate. The marker's operational contract in
both consumers is "not backed by a live upstream rating", which is exactly true here. Trade-off:
the old `(climb, angle)` loses its `effectiveQuality` star — correct, since upstream no longer
asserts a rating there.

### The health reporter that hid it

Every cycle logged `Sync health summary failed: snapshot.oldestAttemptAt.toISOString is not a
function` — 28 of the 49 boardsesh error lines in 24h. The fleet summary has **never once
emitted**. A raw `sql` aggregate carries no runtime decoder (the `sql<Date>` generic is
compile-time only), and drizzle's postgres-js driver deliberately *strips* postgres.js's own
