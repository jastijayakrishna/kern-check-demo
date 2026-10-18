# Fix Snooker Royal cue release and enlarge players

### Motivation
- Mobile portrait releases could reset the slider to zero before the cue-stick impact, resulting in no cue-ball launch.  
- The release callback sometimes ran while a cue stroke was already active, allowing duplicate commits.  
- The human player silhouette needed a small scale adjustment to better match visual proportions at runtime.

### Description
- Capture the released slider value by importing and using `resolvePoolRoyalReleasePower` and change `fire` to accept an optional `committedPowerOverride`, using the resolved value to drive the shot instead of reading a possibly-reset `powerRef`.  
- Prevent duplicate shot commits by passing a `busy` check into the release resolver using `shootingRef.current`, `cueAnimating`, and `shotImpactPending`.  
- Increase player avatar target height by updating the `PoolRoyalHumanPlayers` instantiation `targetHeight` from `cueLen * 1.34` to `cueLen * 1.38` to make characters slightly larger.  
- Add/adjust regression tests to cover captured-release preservation and duplicate-release rejection and update the scene-spec expectations accordingly (`test/poolRoyaleShotState.test.js` and `test/snookerRoyalTableSpecs.test.js`).

### Testing
- Ran unit tests with `npm test -- --runInBand test/poolRoyaleShotState.test.js test/poolRoyaleCueStrokeTimeline.test.js test/snookerRoyalQuality.test.js test/snookerRoyalTableSpecs.test.js`, and all 4 suites (21 tests) passed.  
- Ran the production webapp build with `npm run build --prefix webapp`, which completed successfully.  
- The newly added tests validate that a committed release value is preserved when the live slider has reset and that releases are rejected while a cue stroke is active.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6aa294b101108329816af61d01ee49fa)
