# Restore seated human actors in Texas Holdem arena and add shared seated-human loader

### Motivation
- Reintroduce the seated human characters and their original seating/pose logic that had been removed, restoring the visual/player-facing human presentation in Texas Hold’em (and other arenas) to how it was two months ago.
- Centralize character loading/pose utilities into a shared seated-human module so multiple arenas (Texas Hold’em, Snake, Ludo, etc.) can reuse the same loader/restore behaviour.

### Description
- Re-added the shared seated-human model library and functions in `webapp/src/pages/Games/shared/seatedHumanActors.js`, including `loadSeatedHumanTemplate`, `createRestoredSeatedHumanActor`, bone rig save/restore, pose application and utilities for measuring/normalizing templates.
- Restored domino/ReadyPlayerMe character support and cloth/texture theme tables (polyhaven cloth maps, cloth combos and TEXAS_DOMINO_CHARACTER_THEMES) into `TexasHoldemArena.jsx` and reintroduced constants used to position/pose characters at seats.
- Re-integrated character attachment and pose logic into `webapp/src/pages/Games/TexasHoldemArena.jsx` (importing `cloneSkeleton` and calling `loadSeatedHumanTemplate` + `createRestoredSeatedHumanActor` for human seats) and restored helper routines for initializing per-seat actors and pose actions.
- Minor build/tooling adjustments: added imports and restored related helper functions so the restored humans match prior scale, offsets and idle/interaction poses.

### Testing
- Ran the Texas Hold’em unit tests with `npm test -- --runInBand test/texasHoldemGame.test.js test/texasHoldemOnlineState.test.js` and both test suites passed (2/2 passing).
- Built the webapp with `npx vite build` (production build produced `dist/index.html`) and ran `npx vite preview` to verify the arena; a headless Playwright preview run produced a portrait screenshot of the Texas Hold’em arena with restored humans (artifact generated).
- Ran ESLint which reported a file-ignore warning but no blocking errors. All automated checks in this environment completed successfully.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6aa66fe145f48329853a0f44b95f20cf)
