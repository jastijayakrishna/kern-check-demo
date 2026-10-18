# feat(operations): hide search pill until pulled down

## Summary

The Operations search pill is now **hidden by default** and revealed with a **light downward swipe** at the top of the list — a gentle pull brings it in well before the native pull-to-refresh reaches its trigger distance. A **light swipe back up** dismisses it, **unless a search/filter is active**, which pins it visible.

This reuses the existing `searchMode` state machine (`'closed'` = no filters → hideable; `'collapsed'` = filters active → pinned), so the "…unless there are active filters" rule falls out of state that already exists.

## How it works

- **`app/hooks/usePullToRevealSearch.js`** (new) — a `Gesture.Pan()` that only engages when the drag **begins at the top** (`scrollY ≈ 0`), driving a `revealProgress` shared value. Reveals over ~72px of pull, commits at ~45% (a light flick, far short of the refresh threshold); the same logic in reverse handles swipe-to-hide. `pinned` forces it visible and disables the pull.
- **`app/components/operations/OperationsList.js`** — composes the reveal gesture with the list's own scroll via `Gesture.Simultaneous(revealPanGesture, Gesture.Native())`, so **scrolling and native pull-to-refresh keep working** while the pull is also read. Falls back to the plain `SectionList` when no gesture is passed (unchanged for existing callers/tests).
- **`app/screens/OperationsScreen.js`** — wires the hook: feeds scroll offset, reports pill height, drops the list `topInset` to 0 while hidden (reclaiming the space), animates/masks the floating pill (`opacity` + `translateY`, `pointerEvents: 'none'` when hidden), and resets the peek when search returns to `'closed'`.

## Trade-off

Native pull-to-refresh is preserved, so a **hard** pull both refreshes *and* reveals the pill (the reveal commits far below the refresh distance); a **light** pull only reveals. This keeps single-pull refresh intact rather than gating refresh behind the revealed state.

## Testing

- Added `__tests__/hooks/usePullToRevealSearch.test.js` (6 tests) and `Gesture.Simultaneous`/`Race`/`Exclusive` to the jest gesture-handler mock.
- Full suite green: **150 suites / 4320 tests passing**, lint clean.
- ⚠️ Not yet exercised on a device — the gesture UX (pull thresholds, coexistence with native refresh/scroll) should be validated on an Android device/emulator before merge.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
