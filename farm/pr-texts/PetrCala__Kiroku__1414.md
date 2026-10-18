# perf(home): scope scorecard stats engine to the visible+previous month

## Context

[#1409](https://github.com/PetrCala/Kiroku/pull/1409) removed the calendar's per-session `Intl` freeze that caused the ~5s "scrolls but taps are dead" window on launch. Testing confirmed it's much better but **not fully gone** — a smaller residual stall remains.

## Root cause (the residual stall)

The home screen also mounts the Statistics v2 event engine to feed the Units scorecard:
`useHomeStats` → `useDrinkEvents` → `buildDrinkEvents`. That engine walks the **entire drink history** (one `DrinkEvent` per drink × type), deferred via `InteractionManager.runAfterInteractions`, so the heavy synchronous JS walk lands ~300 ms **after paint** (the early-tap window) and re-fires on every `CACHED_DRINKING_SESSIONS` identity change at boot (disk hydrate → time-parts backfill write → `app/open` network merge).

`Intl` is now mostly cached (stored parts / cached per-month offset), so what's left is the pure-JS array build + the downstream `buildMonthlyStats` pass — hence "a fraction of what it was."

## Key insight

The scorecard only reads the **visible month + previous month**. `buildMonthlyStats` windows events by `anchorTs` (= session `start_time` ms), and its only whole-array scan (`earliestMs`) is **skipped when `earliestSessionAt` is supplied** — which `useHomeStats` already does. So the home path was materialising multi-year, all-user history just to render two months.

## Fix

- **`useDrinkEvents`** gains an optional `window: {startMs, endMs}`. When set, it pre-filters the sessions fed to `buildDrinkEvents` (and the launch-time backfill) to that window. Because the filter uses the same `start_time` bound `buildMonthlyStats` windows by, the result is **byte-identical** — it just turns the launch-path walk from `O(whole history)` into `O(~2 months)`. It also returns the current user's cheap all-history min `start_time` (`earliestStartMs`, numeric only, no `Intl`) as a comparison-baseline fallback.
- **`useHomeStats`** computes `[prevStart, monthEnd]` from `visibleDate` and passes it, using `earliest_session_at ?? earliestStartMs` so `comparisonAvailable` stays correct even before the floor hydrates.
- **No-window callers are untouched** (Statistics tabs, Badges, drill-down): the sessions object keeps its identity, so the full-stream and `backfillSessionTimeParts` contracts are unchanged. The full-history time-parts backfill now happens when the Statistics tab opens (behind its skeletons) instead of on the home launch path — deliberate.

### Why not the alternatives
- **Reuse the calendar's per-day `unitsMap`**: the compact calendar starts at the current month only, so the previous month isn't loaded at cold launch and the month-over-month delta would break.
- **Chunk `buildDrinkEvents` to yield**: keeps the whole-history walk and forces an async rewrite across all callers. Windowing is strictly less work.

## Tests
- `useDrinkEvents`: window filters out-of-window sessions, `earliestStartMs` reflects full history (not the window), backfill is scoped to the windowed object, and the no-window path still reports `earliestStartMs` undefined (the existing `backfill === sessions` identity test still guards the default path).
- `buildMonthlyStats`: a windowed-vs-full **equivalence guard** — feeding only `[prevStart, monthEnd]` yields a deep-equal summary to the full multi-month history (with the floor supplied).

## Verification
- `TZ=utc jest` for `useDrinkEvents`, `events`, `buildMonthlyStats`, `overview`, `localParts` — 106 passed.
- `typecheck-tsgo`, prettier, `lint-changed`, `react-compiler-compliance-check check-changed` — all clean.
- **Not verifiable in a web/V8 preview on purpose** (consistent with #1409): the win is Hermes-specific JS-thread cost. Confirm on a release/Hermes build with a large session history — the FAB / calendar / banners should be tappable immediately after the home screen paints, and the scorecard numbers must match the pre-change values for the visible and previous months.

## Follow-ups (out o
