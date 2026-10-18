# Fix Domino Royal matchmaking: use TPC identity and exact-criteria matching

### Motivation
- The Domino Royal lobby sometimes failed to pair two ready players because identity binding and matchmaking criteria were not strict and the ready handshake could race the server-side registration. 
- Matchmaking must track the canonical TPC account number and group only players that request the exact same Domino criteria so seats are assigned predictably.

### Description
- Added `isDominoMatchCompatible` and `DOMINO_MATCH_KEYS` in `bot/utils/dominoRoyalOnline.js` to require exact equality for Domino matchmaking keys (`mode`, `variant`, `targetPoints`, `token`).
- Wired Domino-specific matching into the server by calling `isDominoMatchCompatible` from `isMatchMetaCompatible` in `bot/server.js` so Domino queues are partitioned by full criteria instead of treating missing keys as wildcards.
- Bound registration and seating to the canonical TPC identity by sending `tpcAccountNumber` during the Socket.IO `register` and `seatTable` handshake, and adjusted server `resolveTpcIdentity` usage so seating is tied to the TPC account.
- Made readiness atomic with seating by accepting a `ready` flag in the `seatTable` request and having the server mark the account ready, broadcast `lobbyUpdate`, and call `maybeStartGame` without waiting for a separate client `confirmReady` event; removed the client `confirmReady` emit in `webapp/src/pages/Games/DominoRoyalLobby.jsx` and updated `joinDominoRoyalLobby` to send `tpcAccountNumber` and `ready: true` in `webapp/src/pages/Games/dominoRoyalMatchmaking.js`.
- Added `bot/tests/dominoRoyalOnline.test.js` with unit tests that assert compatible and incompatible Domino criteria are handled as expected.

### Testing
- Ran unit tests with `npm --prefix bot test` and all tests passed (6/6).
- Ran client lint on changed files with `npm --prefix webapp run lint -- src/pages/Games/DominoRoyalLobby.jsx src/pages/Games/dominoRoyalMatchmaking.js` which completed without reported errors.
- Built the webapp with `npm --prefix webapp run build` which finished successfully and produced the optimized `dist` output.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a70c0480eec8329a2da1375767fd1eb)
