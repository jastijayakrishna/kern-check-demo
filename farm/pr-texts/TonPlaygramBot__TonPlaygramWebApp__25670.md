# Fix parked capture visuals, portrait camera placement, and avatar positioning; parallelize parked asset loading

### Motivation
- Prevent parked capture models from sinking into the tabletop on low-end/mobile GPUs by giving them a small lift and keep selected weapons visually readable in portrait overview.
- Ensure the portrait camera is physically positioned behind the local/bottom seat so the local player is shown consistently when the arena is scaled.
- Keep the local player's avatar anchored to the portrait bottom as a screen-space affordance instead of nudging it based on 3D seat anchors. 
- Reduce perceived load latency of parked capture displays on phones by loading parked assets together instead of serially.

### Description
- Raised parked capture models by setting `CAPTURE_PARKED_LIFT_OFFSET_Y` to `0.008` and added `CAPTURE_PARKED_WEAPON_VISUAL_SCALE = 1.24` to enlarge weapon visuals in racks, and applied the scale to cloned weapon models in `applyCaptureWeaponDisplay` via `clone.scale.multiplyScalar(...)`.
- Replaced the portrait camera forward offset `PLAYER_VIEW_CAMERA_FORWARD_OFFSET_PORTRAIT` (previously `2.46`) with a smaller value `0.72` and added comments explaining the fix to keep the local seat visually correct after arena scaling.
- Replaced the `SELF_AVATAR_BOTTOM_OFFSET_PERCENT` approach with a fixed screen position `SELF_AVATAR_SCREEN_POSITION` and updated the avatar positioning logic to place the local player at that absolute portrait position while other players still use seat anchors or fallbacks.
- Parallelized parked asset creation in `rebuildParkedCaptureVehicles` by batching `createCapture*Fx()` calls with `Promise.all(...)` to start loading all parked assets concurrently and preserved the existing fit/positioning logic.

### Testing
- Ran the project's automated test suite and static checks (unit tests, linter, and build); the suite completed successfully with no failures.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a970a53276c83299bad6ee2a2b7bf1f)
