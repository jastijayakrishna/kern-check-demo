# Add three arcade race games (2048 Royale, Hextris Battle, Underrun Arena) with live scoring and lobby support

### Motivation
- Introduce three new arcade-style two-player score-race games and expose them to the online lobby and matchmaking system so players can queue, match, and view live opponent scores.
- Provide a shared realtime state and socket contract to support live scoring, sync, and finish validation for short timed matches.

### Description
- Backend: register the new games in `bot/config/onlineGamePolicy.js` and `bot/config/tpgGameContracts.js` and add `arcadeRaceStates` plus socket handlers (`joinArcadeRace`, `arcadeRaceSyncRequest`, `arcadeRaceScore`, `arcadeRaceFinish`) and `emitArcadeRaceState` in `bot/server.js` to manage realtime score race state and winner resolution.
- Frontend: add lobby and game UI and wiring, including `ArcadeRaceLobby.jsx`, `Game2048Royale.jsx`, `HextrisBattle.jsx`, `UnderrunArena.jsx`, `ArcadeMatchHeader.jsx`, and the `useArcadeRace` hook, update `App.jsx` routes, and add icons and thumbnails referenced from `webapp/src/config/gameAssets.js` and `webapp/src/config/gamesCatalog.js`.
- Configuration: mark the new games as `Online Ready` in `webapp/src/config/onlineContract.js` and include relevant match meta keys (`format`, `durationSeconds`) in the global policy and contracts so matchmaking accepts the new options.
- Tests: expand `test/onlineGamePolicy.test.js` to assert that the new games accept two-player score-race matchmaking and that `matchMeta` is normalized.

### Testing
- Ran the JavaScript unit test suite with `npm test`, and the test coverage including the updated `online game policy` tests passed.
- Confirmed the new `onlineGamePolicy` tests (`accepts 2048royale/hextrisbattle/underrunarena two-player score-race matchmaking`) succeed under the test runner.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a965c070d448329b1c2263e76da0062)
