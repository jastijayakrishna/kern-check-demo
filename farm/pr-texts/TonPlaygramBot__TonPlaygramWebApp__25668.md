# Pin local avatar to bottom, ensure parked weapons visible, and parallelize parked-asset loading

### Motivation

- Fix portrait UX where the local player avatar could appear away from the bottom of the screen and parked weapons could get occluded by the table on some mobile GPUs.
- Reduce perceived empty-table time on phones by loading parked capture/weapon assets concurrently instead of sequentially.

### Description

- Raised parked capture-vehicle / firearm displays slightly by changing `CAPTURE_PARKED_LIFT_OFFSET_Y` from `0` to `0.008` to avoid z-fighting with the tabletop. (file: `webapp/src/pages/Games/LudoBattleRoyal.jsx`)
- Made the local player's avatar a screen-space affordance by replacing the offset approach with a pinned `SELF_AVATAR_SCREEN_POSITION` at bottom-center and using it when rendering the avatar overlay. (file: `webapp/src/pages/Games/LudoBattleRoyal.jsx`)
- Parallelized parked-asset preparation by replacing sequential `await` calls with `Promise.all([...])` for `createCapture*Fx()` so the parked models appear faster on mobile. (file: `webapp/src/pages/Games/LudoBattleRoyal.jsx`)
- Minor cleanup to the avatar positioning logic to prefer the pinned bottom position for player index 0 while leaving opponent avatars driven by their projected 3D seat anchors. (file: `webapp/src/pages/Games/LudoBattleRoyal.jsx`)

### Testing

- Ran lint: `npm --prefix webapp run lint -- src/pages/Games/LudoBattleRoyal.jsx`, which completed successfully.
- Ran full webapp build: `npm --prefix webapp run build`, which completed successfully and produced the production dist.
- Ran a quick code check: `git diff --check`, which returned no problems.
- Attempted an automated Playwright screenshot to validate the portrait rendering, but the headless Chromium run failed at runtime due to a missing system library (`libatk-1.0.so.0`), so the screenshot verification could not be completed in this environment.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a970a53276c83299bad6ee2a2b7bf1f)
