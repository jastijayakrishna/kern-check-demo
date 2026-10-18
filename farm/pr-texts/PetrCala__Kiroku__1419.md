# perf(home): re-apply scorecard window, loop-free (fixes #1414 regression)

Re-applies [#1414](https://github.com/PetrCala/Kiroku/pull/1414)'s home-scorecard windowing **without the infinite-loop regression** that forced its revert in [#1417](https://github.com/PetrCala/Kiroku/pull/1417).

## What #1414 got wrong

#1414 windowed the scorecard's stats compute to the visible + previous month (a real launch-latency win on top of #1409). But its windowed `useDrinkEvents` built the scoped session set in a `useMemo` and put **that derived object in the rebuild effect's dependency array**. Under React Compiler the object's identity churns every render (it keys on the fresh `{window}` object the caller passes each render), so the effect re-fired → `setState` → re-render → re-fired — **~69k rebuilds**, all via `runAfterInteractions`.

That runaway **saturated the JS interaction queue**, starving every async-gated screen:
- **Profile / Friends list / friend profiles** → fetches never resolved (endless spinners).
- **Fullscreen calendar** → it *had* its data (`calendarMonths` populated), but `onInitialScrollReady` never got a turn → stuck on the skeleton.
- Home only looked fine because its content had already painted.

Diagnosed on-device with the StatsPerf harness ([#1416](https://github.com/PetrCala/Kiroku/pull/1416)): `⚠️LOOP`, `useDrinkEvents.rebuild ≈ 69547`, 14.8 s of `buildDrinkEvents` in one flush — vs `rebuild:3` in the non-windowed path.

## The fix

Re-apply the windowing so the effect can't churn:
- The window filter runs **inside the rebuild** (`filterSessionsToWindow`), and the effect depends only on the **stable numeric bounds** (`windowStartMs` / `windowEndMs`) plus the stable `allSessions` ref — **never a render-derived object**. A fresh `{window}` with unchanged bounds no longer re-fires it.
- `earliestStartMs` moves to its own memo (a number, never in the effect deps → can't drive a loop).
- **No-window callers are byte-identical** (`scoped === allSessions`), so Statistics tabs / Badges / drill-down and the `backfillSessionTimeParts` contract are unchanged.

Net: Home keeps the #1414 launch win **and** profile/friends/calendar work.

## Tests
- Window filtering, scoped backfill, `earliestStartMs`, and the `buildMonthlyStats` windowed-vs-full **equivalence** guard (windowing is lossless).
- A new **loop guard**: a fresh-but-equal `{window}` object across re-renders must not re-fire the rebuild (asserts the effect depends on bounds, not object identity).
- `typecheck-tsgo`, `lint-changed`, `react-compiler check-changed`, prettier — all clean; 84 Statistics/calendar jest tests pass.

## Verification
Carries **`Ready To Build - iOS`** for an ad-hoc build. On-device with the heavy test account, confirm: Home is fast on launch **and** Friends list / profiles / fullscreen calendar all load (no stuck spinners/skeletons). The loop's gone, so the screens that #1414 starved should work. The StatsPerf branch (#1416) remains available if we want counter-level confirmation (`useDrinkEvents.rebuild` bounded, no `⚠️LOOP`).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
