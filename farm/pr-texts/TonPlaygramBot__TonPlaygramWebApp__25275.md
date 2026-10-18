# Fix Domino Royal TPC matchmaking search

### Motivation
- Matchmaking could fail to consolidate players because clients used inconsistent identity fields and could race seating before registration completed. 
- The lobby needed a way to keep searching for compatible open tables while a player remains queued so fragmented seats can be consolidated automatically. 
- Players who refresh matchmaking should not lose their previously-confirmed "ready" status just because the client resends a seat heartbeat. 

### Description
- Use the TPC account number as the canonical lobby identity by sending `tpcAccountNumber` (and preserving legacy `accountId`) when calling `register` and `seatTable` in `webapp/src/pages/Games/dominoRoyalMatchmaking.js` and by centralizing payload construction in `buildSeatPayload`.
- Add `searchDominoRoyalLobby` in `webapp/src/pages/Games/dominoRoyalMatchmaking.js` and wire a periodic 3s matchmaking refresh from `webapp/src/pages/Games/DominoRoyalLobby.jsx` that re-sends the same criteria to search compatible open tables and issues `confirmReady` when appropriate.
- Track queued TPC account and criteria in `DominoRoyalLobby.jsx` via refs (`queuedAccountIdRef`, `queuedCriteriaRef`) and avoid concurrent refreshes with `searchInFlightRef`; clean up interval and refs on unmount.
- Update server seat handling in `bot/server.js` to normalize ID comparisons (`String(...)`) and treat re-seating as a heartbeat so an existing `ready` confirmation is not revoked when the client refreshes its seat.
- Add/extend unit tests in `test/dominoRoyalMatchmaking.test.js` to cover registration-before-seating, failed registration, and repeated lobby search behavior.

### Testing
- Ran unit tests with `node --test test/dominoRoyalMatchmaking.test.js`, which passed (3 tests OK).
- Ran lint on modified client files with `npm --prefix webapp run lint -- --quiet src/pages/Games/DominoRoyalLobby.jsx src/pages/Games/dominoRoyalMatchmaking.js`, which succeeded.
- Built the webapp with `npm --prefix webapp run build`, which completed successfully.
- Attempted a Playwright portrait screenshot to visually validate the lobby, but Playwright Chromium failed to launch in the container due to a missing native library (`libatk-1.0.so.0`), so headless screenshoting could not be completed in this environment.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a70c03ff1388329b3d31a30b2da29f4)
