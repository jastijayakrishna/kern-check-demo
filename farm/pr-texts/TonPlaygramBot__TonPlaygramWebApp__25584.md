# Remove Snake & Ladder seated human characters and voice commentary

### Motivation

- Remove the seated human 3D avatars and the voice commentary system from Snake & Ladder to reduce render/CPU overhead and speed up gameplay.

### Description

- Removed seated human avatar/model loading, skeleton cloning, texture/material helpers, pose/animation code, and related caches from `webapp/src/components/SnakeBoard3D.jsx` so the arena only creates chairs, anchors, and weapon holders. 
- Removed all voice/commentary machinery including commentary presets, TTS integration, queuing, unlock logic, commentary UI, and deleted `webapp/src/utils/snakeAndLadderCommentary.js`. 
- Stripped commentary event calls (enqueue/commentary triggers) from `webapp/src/pages/Games/SnakeAndLadder.jsx` and adjusted constants/anchors so token, camera, capture FX, and core gameplay remain functional. 
- Preserved non-commentary audio SFX, token and weapon capture behavior, and camera/board logic while removing human-specific lifecycle and per-seat pose updates.

### Testing

- Ran `npm --prefix webapp run build` (Vite production build) which completed successfully.
- Ran ESLint with `npx --prefix webapp eslint --no-ignore --no-warn-ignored webapp/src/components/SnakeBoard3D.jsx webapp/src/pages/Games/SnakeAndLadder.jsx` and it finished with no blocking errors.
- Ran repository checks (`git diff --check` / code-sanity scans) which reported no blocking issues.
- Attempted a Playwright screenshot of `/games/snake` but it failed because the Playwright browser binaries are not installed in this environment (no browser executable available).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a958f088a2c8329b43c924106581c11)
