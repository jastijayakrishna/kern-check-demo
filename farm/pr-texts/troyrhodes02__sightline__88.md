# SIG-90: batch recommendation-snapshot writes (fix slate P2028 timeout)

## Symptom
Production slate: **"The slate could not be loaded."**
```
PrismaClientKnownRequestError P2028 — recommendationSnapshot.create()
Transaction API error: ... timeout was 5000 ms, however 5060 ms passed ...
```

## Root cause
`persistSnapshotTransitions` (`src/lib/slate/read.ts`) writes recommendation-transition snapshots inside a Prisma **interactive transaction** (default 5000ms) as a **loop of per-row `create()` calls** — one round trip each through Supabase's transaction-mode pooler.

While all Kalshi prices were null (pre-SIG-86) there were no recommendations → the loop was empty → the transaction never did work. **Once SIG-86 made real prices flow, the first slate read flips many contracts to `appeared` at once**, so the sequential creates exceeded 5000ms → P2028 → the whole read threw. Data-triggered, not the SIG-89 timezone change (which coincided in timing and was reverted first — harmless but not the fix).

## Fix
- Accumulate the transitions and write them in **one `createMany`** (single statement) instead of the per-row `create()` loop — the transaction now does 1 read + 1 bulk insert.
- `{ timeout: 20_000 }` headroom for a full slate through the pooler.

## Verification
tsc, eslint, prettier clean; slate Jest suites (**65**) green. The transition logic (appeared / state_changed) is unchanged — only the write is batched.

## Follow-up
SIG-90 note: persisting snapshots on every slate READ in the request path is heavy by design; consider moving it off the read path so a snapshot write can never take the shared read surface down.

Closes SIG-90.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
