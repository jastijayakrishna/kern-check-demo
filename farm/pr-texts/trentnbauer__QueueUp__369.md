# Move Spin the Wheel from a grid card into a header button

## Summary
- Removes the `SpinWheelCard` grid tile (`GameGrid`/`RoomView`/`ShelfView`) — Spin the Wheel no longer occupies a slot in the games grid.
- Adds `SpinWheelButton` (renamed `SpinWheelCard.tsx`) in the shared `Header`, next to "+ Add Game", used by both Communal Rooms and the Personal Shelf.
- Renamed the trigger from "Spin the Wheel" to "🎲 Pick Tonight's Game" per the issue's request for a more relevant name. The modal itself (title, reveal copy, theming) is untouched.
- Same eligibility/gating logic as before (Room Settings ownership threshold, silent Steam auto-match walk for undecided games, manual picker fallback) — only the trigger UI moved.

Closes #356.

## Test plan
- [x] `npx tsc --noEmit -p web/tsconfig.json` — clean
- [x] `npx vitest run web` — 83/83 passing
- [x] `npm run build -w web` — production build succeeds
- [ ] Manual click-through in a browser — not done in this sandbox (no OAuth/DB secrets available for a full local stack); worth a quick eyeball on both a Room and the Personal Shelf before merging, including the "no eligible backlog games" disabled state.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_019y5AZAhBmecworWBhGUbga
