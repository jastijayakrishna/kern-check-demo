# Fix Snake & Ladder dice roll and jump layout

### Motivation
- Make the Snake & Ladder 3D dice roll match the Ludo Battle Royal physical throw so the cube performs a full spin arc instead of appearing to "shake" and to ensure the visible animation completes before the authoritative result is applied.
- Ensure the authoritative dice result is revealed only after the physical landing so token movement is synchronized and precise.
- Prevent visual overlap between snakes and ladders by assigning crossing jumps to distinct lanes/heights for a cleaner board layout.

### Description
- Aligned dice timing by changing `DICE_ROLL_DURATION` in `webapp/src/components/SnakeBoard3D.jsx` to `900` ms and kept the reveal timing comment/constant in `webapp/src/pages/Games/SnakeAndLadder.jsx` (`DICE_BOARD_ROLL_REVEAL_DELAY_MS = 930`) so the face is applied right after landing.
- Made lane resolution consider both snakes and ladders by passing the opposite jump map into `updateLadders` and `updateSnakes` and building a combined `allJumpEntries` list before calling `createJumpLaneResolver`, so crossing jumps are given distinct lane/side assignments (changes in `webapp/src/components/SnakeBoard3D.jsx`).
- Kept the 3D jump renderers synchronized by updating effect dependencies and calling the updated `updateLadders`/`updateSnakes` with the additional parameters so layout refreshes when either snakes or ladders change (hook dependency updates in `SnakeBoard3D.jsx`).

### Testing
- Ran ESLint: `npx eslint --no-ignore --no-warn-ignored src/components/SnakeBoard3D.jsx src/pages/Games/SnakeAndLadder.jsx` (succeeded).
- Built the frontend: `node scripts/run-vite-build.mjs` (production build completed successfully and assets updated).
- Ran repository checks: `git diff --check` (no check errors) and committed the changes as `Fix snake dice roll and jump layout`.
- Attempted automated visual validation with Playwright at a 390x844 portrait viewport, but the headless browser failed to launch in the container due to a missing system library (`libatk-1.0.so.0`).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a716238ff3c8329b6482b146a21ad07)
