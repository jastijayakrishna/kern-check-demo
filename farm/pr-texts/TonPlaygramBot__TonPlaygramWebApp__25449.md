# Align Snooker GLB pocket geometry and match Pool Royale shot/spin behavior

### Motivation
- Ensure pocket cutouts, nets and capture zones line up exactly with the loaded GLB snooker table so visual drop hardware matches the visible apertures.
- Make shot power, spin transfer and deflection behavior follow the same logic and input curve used by Pool Royale for consistent feel across modes.

### Description
- Add `alignPocketSystemsToOpenSourceModel(model)` in `webapp/src/pages/Games/SnookerRoyal.jsx` which detects the six pocket-cover centers from the loaded GLB, computes calibrated pocket centers, and repositions procedural pocket liners, nets, rings, holders and straps to those measured centers.
- Use the calibrated centers as the authoritative pocket positions by returning `openSourcePocketCenters` from `pocketCenters()` when available, and store calibration metadata on `table.userData.openSourcePocketCalibration`.
- Hook the pocket alignment into the GLB load flow so `alignPocketSystemsToOpenSourceModel(model)` runs after the GLB is fitted and added to the scene.
- Match Pool Royale shot input behavior by changing `SHOT_MIN_FACTOR` to `0` and `SHOT_POWER_RANGE` to `1` in `webapp/src/pages/Games/SnookerRoyal.jsx` so the full `0–1` UI pull range maps identically to Pool Royale power and spin/deflection math.
- Adjust spin controller bias by changing `SPIN_CENTER_TOPSPIN_BIAS` from `0.13` to `0.1` in `webapp/src/pages/Games/snookerRoyalSpinUtils.js` to align topspin behaviour with Pool Royale.
- Extend `test/snookerRoyalTableSpecs.test.js` to assert the presence of the GLB pocket calibration hook and the Pool Royale power curve constants.

### Testing
- Ran Jest for the affected suites with `npm test -- --runInBand test/snookerRoyalTableSpecs.test.js test/snookerTableModel.test.js test/poolRoyalSpinController.test.js`, and the two matched suites (`test/snookerTableModel.test.js` and `test/snookerRoyalTableSpecs.test.js`) passed (11 tests total passed); the third pattern did not match any suite in this run.
- Built the frontend with `npm --prefix webapp run build` and the Vite production build completed successfully.
- Ran ESLint on the changed files; no errors were reported but the repository ESLint ignore settings caused the files to be reported as ignored (warnings only).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a91e5fe8100832998cbfdfcaa44b2e1)
