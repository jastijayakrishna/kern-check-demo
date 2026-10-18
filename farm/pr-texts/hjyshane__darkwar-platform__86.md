# fix(dashboard): the sync badge was watching the heartbeat, not the data

## What was wrong

`SyncStatus`'s own docstring said it answered **"is anything still arriving at all"** — explicitly the question a panel's freshness badge cannot answer. It did not answer it.

Its only input was `sync_status` (0060), which reports `collectors.last_heartbeat_at`: what `dw-sync` says about *itself* every ten seconds. That is not evidence that observations are landing.

The two come apart, and not hypothetically. `dw-capture` has **twice** stalled after a game reconnect in a way that leaves the process running, the heartbeat beating and the journal frozen — documented in `docs/runbooks/continuous-collection.md` and in handover's 「막힌 것 2」. The board stayed green through both.

## What it does now

The badge carries the newest collector-written notification next to the heartbeat, and lets the reader see the two ages disagree:

```
● Real-time sync · data 5h ago
```

Tooltip: `Last checked in moments ago · Newest observation arrived 5h ago`

**Counted topics are restricted to the ones the collector fills** (`COLLECTOR_TOPICS`). An admin renaming a hero writes a `data_change_notifications` row too, and letting that answer this question would move the same lie one table along.

**No threshold on the second number, deliberately.** Nothing walks the game's screens yet, so a multi-hour gap is currently *normal*; a badge that cried "stopped" over that would be wrong most of the day and ignored by the time it was right. When the ADB routine lands, a threshold goes on top of a number that is already on screen.

## Design notes

- **Two queries, not a widened view.** `sync_status` is deliberately one fact (0060 says so in as many words). A failure on the new query leaves the heartbeat half rendering instead of taking the whole badge down.
- **`undefined` (not known yet) and `null` (nothing has ever arrived) stay distinct**, so an unanswered query cannot render as a claim about the collector. Pinned by test.
- `.sync-data` sets no colour of its own, so the stopped state can tint the whole line — a fixed grey would leave half the badge looking calm while the other half says it is not.

## Verification

`pnpm check` ✓ · `typecheck` ✓ · **229 tests** (225 → 229) ✓ · `build` ✓

Rendered in the fixture harness (`dev:local`): one line at 1280 and at 375, no console errors, and `.sync-data` confirmed to inherit the stopped state's red rather than its own grey.

**Limit worth stating:** that harness bypasses PostgREST and RLS by construction. The new `data_change_notifications` query is confirmed **against the migrations** — 0006 grants select to `anon, authenticated` and adds `public_read using (true)`, and 0065 leaves this table alone — **not yet against a live stack.** Worth one look while signed in on the cloud.

## Docs — two stale claims, fixed while here

- `CLAUDE.md` said `contribution_type='alliance_battle'` had no writer and its dashboard column was permanently empty. 0028 split the ambiguous type three ways against labelled captures, 0029 wired each to a column, and the roster shows three duel columns that fill. The passage is rewritten rather than deleted: the parser *was* written, on a branch that was never pushed, so two documents recorded it as missing and a session re-planned work that already existed. **An unpushed branch is indistinguishable from unwritten work** is the lesson that survives.
- `docs/handover.md` item 3 said the rival alliance's 72 players should be handled "when an alliance-total screen gets built". That screen exists and already handles it — `OverviewPanel` filters contributions to members of `is_own` alliances.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
