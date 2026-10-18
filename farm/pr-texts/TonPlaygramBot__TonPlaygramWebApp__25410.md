# Fix Ludo Royale online matchmaking synchronization

### Motivation
- Players could be split across tables or stuck in the lobby for Ludo Battle Royal because the server-side matchmaking policy and seat-ready logic did not match the portrait-lobby expectations (3-player tables) and could rely on a dropped `confirmReady` message.
- The client expects the authoritative game session to be available and synchronized (dice/moves) once all seats are locked, so the server must ensure all players join the same authoritative board and receive identical state updates.

### Description
- Allow 2, 3, and 4 player Ludo queues by updating `ludobattleroyal` `maxPlayers` to `[2, 3, 4]` in `bot/config/onlineGamePolicy.js` so quick-match 3-player requests are accepted.
- Canonicalize quick-match fields for Ludo on the server by treating `mode` as `online` and `token` as `TPG` for `ludobattleroyal` in `bot/server.js` to avoid rejecting compatible clients due to decorative metadata.
- Mark authoritative seats as ready immediately for quick-match Ludo tables by including `ludobattleroyal` in the server-side ready-on-join logic inside `bot/server.js`, preventing clients from being stuck when `confirmReady` is lost.
- Expand end-to-end tests in `test/allGamesOnlineMatchmaking.test.js` to include a 3-player Ludo scenario and assert that clients join the same authoritative board and receive synchronized `ludoBattleState` updates (including dice/roll synchronization).

### Testing
- Ran `node --test bot/tests/ludoBattleGame.test.js` and all Ludo unit tests passed (3 subtests passed).
- Ran `npx jest test/onlineGamePolicy.test.js --runInBand` and all policy unit tests passed (25 tests passed).
- Ran the full end-to-end flow with `node --test test/allGamesOnlineMatchmaking.test.js` and the matchmaking/integration assertions (including Ludo 3p/4p sync checks) passed.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a91202a6ec88329b9a394f379ae19be)
