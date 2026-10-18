# Remove human characters and voice commentary from Checkers Battle Royal

### Motivation
- Reduce runtime cost and visual/interaction latency by removing seated human character rendering, animation, and voice/commentary integration from the Checkers Battle Royal scene.
- Keep the board, pieces, table, chairs, and non-voice UI intact so gameplay and customization remain available.

### Description
- Removed the seated human actor pipeline by deleting the `seatedHumanActorsRef` and `seatedHumanMoveActionsRef` usage, associated constants, and the `seatedHumanActors` load/cleanup code in `webapp/src/pages/Games/CheckersBattleRoyal.jsx`.
- Removed imports and helpers related to human rigging and IK by eliminating `./shared/seatedHumanActors.js` imports and the `cloneSkinned` import, and simplified move animation logic to no longer synchronize piece motion with human hand animations.
- Removed the human-character customization UI and inventory wiring by stripping `CHESS_HUMAN_CHARACTER_OPTIONS` usage from the appearance `inv`, removing human-character selection UI tiles, and removing `humanCharacter` equip calls to `setChessBattleEquippedOption`.
- Removed voice/commentary overlay for Checkers by replacing the `GameLiveAvatarOverlay` wrapper with a plain `<CheckersBattleRoyal />` route registration in `webapp/src/App.jsx`, thereby disabling the overlay-driven commentary for this game.

### Testing
- Ran linting with `eslint` on the modified files and it completed successfully.
- Built the webapp with the production build (`node scripts/run-vite-build.mjs` / Vite) and the build completed successfully.
- Executed relevant unit tests with `npx jest test/checkersTurnControl.test.js test/checkersOnlineReadiness.test.js --runInBand` and both test suites passed (2 suites, 6 tests total).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a958f6735b48329b78d40d2a30abbcd)
