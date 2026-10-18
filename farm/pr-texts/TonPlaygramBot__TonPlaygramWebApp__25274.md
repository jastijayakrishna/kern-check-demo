# Fix Domino Royal online lobby socket handshake

### Motivation

- Prevent lobby race where the client emitted `seatTable` before the server finished identity registration, which caused players to fail to join online Domino Royal matches on high-latency/mobile conditions.
- Provide clear, actionable lobby errors when the client lacks an account identity or the socket/register step times out.

### Description

- Add a dedicated matchmaking helper `joinDominoRoyalLobby` (`webapp/src/pages/Games/dominoRoyalMatchmaking.js`) that waits for a socket connection, emits `register` with an acknowledgement and only then emits `seatTable` (implements `waitForSocketConnection` and `emitWithAck`).
- Update `DominoRoyalLobby.jsx` to use `joinDominoRoyalLobby`, show a friendly error when `accountId` is not available, and preserve the original matchmaking criteria (player count, stake, token, variant, target points) when joining the lobby.
- Add regression tests (`test/dominoRoyalMatchmaking.test.js`) using a `FakeSocket` to assert that `register` runs and is acknowledged before `seatTable` is sent and that seating is not attempted if registration fails.
- Keep using the existing Socket.IO client/server; this change fixes ordering and error handling rather than introducing a new networking stack.

### Testing

- Ran lints: `npm --prefix webapp run lint -- src/pages/Games/dominoRoyalMatchmaking.js src/pages/Games/DominoRoyalLobby.jsx` (passed).
- Unit tests: `node --test test/dominoRoyalMatchmaking.test.js` (new tests passed) and `npx jest test/dominoRoyalOnline.test.js --runInBand` (existing Domino Royal online sync tests passed).
- Built the web app with `npm --prefix webapp run build` and ran `git diff --check` to ensure no whitespace issues; build succeeded and checks passed.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a70b8651884832982cb4ac6bdce8e65)
