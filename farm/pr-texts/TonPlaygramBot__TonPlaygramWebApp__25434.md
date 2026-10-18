# Domino Royal: fix 1v1 seat layout and live video avatar frames

### Motivation
- When Domino Royal is played 1v1 in portrait the two players must be shown bottom (local) and top (opponent) and live video frames should exactly match avatar positions/sizes so video replaces avatars cleanly.

### Description
- Remap two-player seat indices so when `N === 2` the opponent is presented directly across the table (local at bottom, opponent at top) by adjusting `getVisualSeatIndex` in `webapp/public/domino-royal-game.js`.
- Add `data-player-index` to seat badge DOM nodes so overlays can reliably identify seat elements in the arena and locate the opponent avatar.
- Reduce live-avatar frame scale from `FRAME_SCALE = 2` to `FRAME_SCALE = 1` so the video frame uses the avatar diameter instead of rendering at double size in `webapp/src/components/GameLiveAvatarOverlay.jsx`.
- Detect and track the opponent badge element for Domino Royal and compute an `opponentRect` (top/left/width/height) so the remote video `RemoteVideo` component is anchored exactly where the opponent avatar appears; the opponent avatar is hidden while live video is active and restored when live ends.
- Keep compact microphone/camera controls and adapt the live-chat panel sizing for Domino Royal so the remote video replaces the avatar while controls remain available.

### Testing
- Ran `npm run lint -- src/components/GameLiveAvatarOverlay.jsx` and the lint step completed successfully.
- Ran `npm run build` and a full production build succeeded without build-time errors.
- Ran `git diff --check` (whitespace / basic diff checks) with no reported issues.
- Attempted an automated headless preview/screenshot with Playwright; initial run failed due to missing browser binaries and later browser dependency installation was attempted, but headless screenshot could not be produced reliably in this environment (system-level shared-library constraints), so no runtime screenshot artifact was committed.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a91786a038083299181a47b1f6696e6)
