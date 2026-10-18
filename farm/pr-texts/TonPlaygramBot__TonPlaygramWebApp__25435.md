# Murlan Royale: determine lowest spade opener for 1v1 and enforce opening-card rule

### Motivation

- Ensure 1v1 games open from the lowest spade actually held by a player (not a closed stock) so the correct player is forced to start and include that specific spade in the first play.
- Provide a deterministic fallback when 3♠ is not dealt to either player and update UI/AI to follow the same rule.

### Description

- Added `resolveOpeningCard(players, config)` to `lib/murlan.js` which scans spade ranks in rank order and returns the lowest spade owned by a player (skipping jokers).
- Updated dealing and turn logic in `lib/murlan.js` so `dealPlayers` exposes `players.openingCard` and `players.startingPlayer`, and `playTurn` enforces that the resolved opening-card holder must begin and that the first play must include that opening card.
- Updated the Murlan Royale UI and initialization in `webapp/src/pages/Games/MurlanRoyaleArena.jsx` to use the resolved `openingCard` for initial active player selection, human-play validation (`handlePlay`), AI behavior (`runAiTurn`), on-screen guidance, and the first-move prompt.
- Added unit tests in `test/murlan.test.js` covering selection of the lowest spade opener in 1v1 and enforcement of a non-3♠ fallback opening card being included in the first play.

### Testing

- Ran the unit test suite with `node --test test/murlan.test.js` and all Murlan tests passed (14/14).
- Built the webapp with `npm --prefix webapp run build`; the Vite production build completed successfully.
- Ran ESLint and project checks; no lint errors were reported (only a couple of ignored-file warnings).
- Attempted a Playwright-based portrait screenshot of the page but the environment lacked the browser binary, so that visual capture step could not run (build and logic tests are otherwise green).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a91790cd71c832994640404fe7b7f9c)
