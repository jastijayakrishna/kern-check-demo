# Match Snooker Royal spin controller to Pool Royale, tighten standing camera, keep cue visible

### Motivation
- Ensure Snooker Royal provides the same feel as Pool Royale for aiming and spin so cue-ball direction, contact tick and target guides remain consistent across games.
- Pull the standing camera framing slightly closer on portrait screens so the table and balls read larger and match the Pool Royale experience.
- Make sure the cue stick remains visible when the camera is in the standing orbit so the player sees the full address pose.

### Description
- Aligned Snooker Royal spin neutral bias by changing `SPIN_CENTER_TOPSPIN_BIAS` in `webapp/src/pages/Games/snookerRoyalSpinUtils.js` so controller response matches Pool Royale and avoids drift between cue/impact visuals and physics mapping. 
- Adjusted the standing camera framing scale by updating `STANDING_VIEW_DISTANCE_SCALE` in `webapp/src/pages/Games/SnookerRoyal.jsx` from `0.145` to `0.135` to tighten portrait framing. 
- Kept the cue visible for the standing camera by changing the `tableCueVisible` flag passed to the snooker cue pose updater in `webapp/src/pages/Games/SnookerRoyal.jsx` so the pose controller refines stance without hiding the cue. 
- Added a regression test `test/snookerRoyalAimExperience.test.js` that verifies Snooker Royal spin constants and mapping match Pool Royale and that the standing-camera / cue-visibility changes are present in the source.

### Testing
- Ran Jest suites: `test/snookerRoyalAimExperience.test.js`, `test/poolRoyaleSpinController.test.js`, and `test/snookerTableModel.test.js`, and all tests passed (3 suites, 17 tests total). 
- Built the webapp with `npm --prefix webapp run build` and the production build step completed successfully.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a926a7e264c8329b98aeaa2b6e06cab)
