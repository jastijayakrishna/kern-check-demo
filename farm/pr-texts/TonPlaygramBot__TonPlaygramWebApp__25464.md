# Improve Pool Royale AI aim precision and scale-independent spin compensation

### Motivation
- Reduce apparent random AI misses on thin-cut pots and make AI aiming behave more like a professional player by removing ad-hoc world-space errors.
- Make spin and power deflection scale with ball size so aim compensation remains correct across different table/ball scales.

### Description
- Revised ghost-ball compensation in `webapp/src/pages/Games/poolRoyaleAiAimCompensation.js` to always place the object-ball contact point exactly one ball diameter from the object center (no cut-dependent shortening) and to return the precise ghost `aimDir` and `contactDepth`.
- Scaled side-spin and power deflection terms by ball diameter (used `radius * 2`) and increased the dimensionless deflection coefficients to express deflection as a fraction of ball diameter (`DEFAULT_SIDE_DEFLECTION_SCALE` and `DEFAULT_POWER_DEFLECTION_SCALE`).
- Removed the small default contact calibration bias and documented the new dimensionless deflection approach in comments.
- Added regression tests in `test/poolRoyaleAiAimCompensation.test.js` to validate thin-cut pocket-line alignment and that spin compensation is invariant to uniform scene scaling.

### Testing
- Ran the AI aim unit tests with `npx jest test/poolRoyaleAiAimCompensation.test.js --runInBand` and all tests passed (5/5).
- Verified the modified test file and implementation compile and run under the project test harness locally.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a926f012d40832996a772f6ab29067c)
