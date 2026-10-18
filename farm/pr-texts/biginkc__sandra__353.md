# perf(polling): pause two background pollers while the tab is hidden

**Depends on: none**

## What
`job-failure-notifier.tsx` (5s interval, mounted on every page) and the 15s safety-net leg in `notifications-bell.tsx` polled with **no visibility guard** — they kept querying the database against a tab nobody was looking at.

Both now check `document.visibilityState` before firing, and both refresh immediately on `visibilitychange` so returning to the tab doesn't wait out the interval. **Intervals unchanged; behaviour while visible unchanged.**

`queue-stats-banner.tsx` already did this correctly and was used as the reference rather than inventing a pattern.

## This is hygiene, not a performance fix
Stating that plainly because the framing matters: all browser-UI polling combined measures **~2.2% of total database time**. The dominant consumer — `getOutboundSmsMetrics()` at **50.4% of ALL database time** — is handled separately in #348.

What this PR does is stop two timers burning queries while nobody is looking. That's worth doing; it is not a headline win, and shouldn't be reported as one.

## Deliberately out of scope
- `use-queue-stats.ts` — owned by #348; touching it here would collide
- `queue-panel.tsx` — its six effects were traced and contain **zero idle polling**. Its timers and Realtime subscription are real but **unsized**, and no optimisation is commissioned from them until measurement establishes them as defects

## Verification
- `npm run typecheck` — clean
- `npm test` — 1534 tests pass

🤖 Generated with [Claude Code](https://claude.com/claude-code)
