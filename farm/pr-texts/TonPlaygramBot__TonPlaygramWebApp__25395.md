# Improve Domino Royal video frames, turn popup, and lobby flow

### Motivation

- Make the Domino Royal live-video presentation consistent with the Murlan style by giving the remote/live frames the same circular appearance used for the local bottom player. 
- Surface an unobtrusive, portrait-friendly “Your turn” notification that appears only on the active player’s screen so turn feedback is clear on mobile in portrait. 
- Avoid tearing down the live-video call when the user chooses `Play Again` or `Return to Lobby` so the WebRTC session is preserved across SPA navigation.

### Description

- Updated `GameLiveAvatarOverlay.jsx` to support a circular remote video presentation when `gameSlug === 'domino-royal'`, and to size the overlay to match the local avatar frame using the detected `overlayRect` dimensions. (adds `circular` prop to `RemoteVideo` and `isDominoRoyal` checks). 
- Converted the Domino route in `App.jsx` to a nested `/*` route and mounted both `lobby` and `index` under the same `GameLiveAvatarOverlay` to keep the overlay mounted across lobby ↔ game navigation. 
- Added a portrait-friendly `#yourTurnPopup` element and CSS in `DominoRoyalArena.jsx` and injected the element into the DOM. 
- Wired the popup visibility in `public/domino-royal-game.js` so `yourTurnPopup` is activated only when `current === human` inside `updateInteractivity()`, and added a `yourTurnPopup` reference at top of the file. 
- Replaced hard navigation on `Return Lobby` with SPA navigation using `window.history.pushState()` and dispatching a `popstate` to preserve the mounted overlay instead of replacing the page; `Play Again` still restarts the match in place. 
- Commit created with message: `Improve Domino Royal turn and video flow` (changes in `webapp/src/components/GameLiveAvatarOverlay.jsx`, `webapp/src/pages/Games/DominoRoyalArena.jsx`, `webapp/src/App.jsx`, and `webapp/public/domino-royal-game.js`).

### Testing

- ✅ `npm run build` completed successfully and produced a production build. 
- ✅ `npx eslint --no-ignore --no-warn-ignored src/App.jsx src/components/GameLiveAvatarOverlay.jsx src/pages/Games/DominoRoyalArena.jsx` passed with no lint errors for the modified files. 
- ✅ `git diff --check` produced no whitespace/patch errors for the changed files. 
- ⚠️ Playwright screenshot attempt for a portrait visual verification failed due to a missing system library (`libatk-1.0.so.0`) in the container, so a headless browser screenshot could not be produced here.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a9053bf93008329a87cb280094115f2)
