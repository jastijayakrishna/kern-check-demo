# Murlan Royale: 1v1 seating, hidden third hand, and rematch/reconnect flow

### Motivation
- Make online seating and character display match active player count and portrait mobile framing, with clear top/bottom layout for 1v1.
- Prevent information leaks in 1v1 by dealing a hidden third hand (kept face-down) so opponents cannot infer each other’s cards.
- Provide a short reconnect grace period after a finished match and expose clear actions to either replay or return to lobby.

### Description
- Only build chairs/characters for active seats by iterating up to `Math.min(players.length, CHAIR_COUNT)` and computing seat angles from `HEAD_TO_HEAD_SEAT_ANGLES` when `players.length === 2`. (edited: `webapp/src/pages/Games/MurlanRoyaleArena.jsx`)
- Add `HEAD_TO_HEAD_SEAT_ANGLES` and `ONLINE_REMATCH_GRACE_SECONDS` constants and a `rematchWaitSeconds` state to control reconnection grace timing. (edited: same file)
- Change dealing logic so 1v1 matches are dealt as three hands (`dealtHandCount = 3`) and store the unused hand in `gameState.stockCards`. The stock hand is rendered as a tight, face-down packet on the table and excluded from normal hand/table/discard visibility. (edited: dealing & `initializeGame`, and `applyStateToScene` to render `stockCards` face-down)
- Add an end-of-match overlay that shows the win message and a reconnect timer when online, with buttons for `Play again` (disabled while grace timer runs) and `Return to lobby`. Also implemented `handlePlayAgain` / `handleReturnToLobby` callbacks. (edited: UI overlay in `MurlanRoyaleArena.jsx`)

### Testing
- Ran `npm run lint` (ESLint) and it completed without errors.
- Ran `npm run build` (Vite production build) and build succeeded; assets were produced and chunking warnings reported but build finished.
- Attempted automated headless screenshot via Playwright to validate 1v1 portrait layout, but the container lacked required native Chromium runtime libraries causing Playwright to fail to launch (this is an environment limitation, not code failure).
- Basic repository checks (`git diff --check`) were verified during the change process.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a9054f3ccc08329914a8471f7dd2f6c)
