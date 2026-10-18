# Synchronize Texas Hold'em online matches, add live-avatar frame and in-game TPC top-up

### Motivation
- Ensure two matched Texas Hold'em players join the same authoritative table and play the synchronized game state instead of each client creating independent opponents. 
- Reuse the existing live-video avatar overlay behavior from Murlan Royale so the poker arena uses the same portrait-friendly video frame placement. 
- Let players top up their table chips (TPC/TPG) without leaving the game UI to improve retention and UX.

### Description
- Persist matchmaking roster on match completion in the lobby so both clients can restore the same online player list (`texasHoldemOnlineMatch:<tableId>` stored in sessionStorage). 
- Add server-side authoritative table state for Texas Hold'em with `texasHoldemStates` and socket handlers: `joinTexasHoldemTable`, `texasHoldemSyncRequest`, and `texasHoldemState` to validate seats, cache authoritative state, increment revisions, and broadcast updates. 
- Update the Texas Hold'em arena to read online match metadata from the URL/session, build seats from the matched roster, and use socket sync to hydrate and emit authoritative state; introduce `onlineContext` and `onlineStateRef` to coordinate one-way hydration and avoid self-echo. 
- Prevent the local AI driver from acting for remote online opponents by checking `isOnlineRemote` before scheduling AI actions. 
- Integrate the shared live-avatar overlay pattern by adding a portrait bottom avatar anchor and a compact `+TPC` control so the table can host the same local video frame placement as Murlan Royale without layout regressions. 
- Add an in-game top-up modal that checks the TPC account balance, records a debit with `addTransaction`, and credits the local player’s synchronized table stack without leaving the arena. 
- Import and wire `socket` utilities and server auth refresh to support reconnects and seat restoration, and commit the changes on the current branch.

### Testing
- Ran unit/integration tests with `npm test -- --runInBand test/texasHoldemGame.test.js test/gameLiveVideoRoom.test.js`, and both suites passed (2 suites, 6 tests passed). 
- Built the webapp with `npm --prefix webapp run build` and the Vite production build completed successfully. 
- Attempted an automated Playwright capture to produce a portrait screenshot of the top-up dialog, but the headless Chromium runtime failed due to a missing system library (`libatk-1.0.so.0`) in the environment so the UI capture did not complete.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a90522300fc8329b3b739ca46045c43)
