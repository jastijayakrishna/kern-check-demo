# Move the game-picker from a grid tile to a header button (#356)

## Summary

- Extracted the "Spin the Wheel" tile's logic into `SpinPickerButton`, now rendered in the header's action row (next to Add Game) instead of as a permanent tile inside the games grid.
- Renamed it to "🎲 Pick a Game" - its old locked/unlocked hint text now shows as a tooltip instead of inline card copy.
- Removed the tile and its grid-insertion bookkeeping (`spinCard`, `spinCardInsertIndex`, `showSpinWheel`/`spinOwnershipMaxPrice`/`spinWheelTheme` props) from `GameGrid`, `ShelfView`, and `RoomView` - the grid itself no longer knows the picker exists, reclaiming a full card's worth of space (a full row on mobile) that was always there whether or not anyone was about to use it.
- Same underlying `SpinWheelModal` reveal and Steam auto-match resolution flow as before - only the entry point moved.

## Test plan

- [x] `npm test` - 169 tests pass
- [x] `tsc --noEmit` on both `web` and `server` - no errors
- [x] Verified live against a dev server: the header button opens the same reveal modal (screenshots below), and the grid renders with no tile taking up space.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01TL7AVdeMpr4MWYSQdiZYb6
