# Align Snooker Royal aiming and standing camera

### Motivation
- Make Snooker Royal's aiming visuals and spin behavior match the Pool Royale experience so cue/target guides, cue follow, and collision predictions feel identical. 
- Pull the portrait standing/broadcast camera slightly closer so the table fills more of a phone portrait screen. 
- Keep the cue stick visible while standing and through the shot-return so the cue never vanishes on portrait screens.

### Description
- Updated aiming math to drive the visible cue-line, cue-follow, contact tick and target prediction from the spin-adjusted guide direction (use of `guideAimDir2D`/`guideDir`) so local and remote aims use the same spin-compensated vector; changes located in `webapp/src/pages/Games/SnookerRoyal.jsx` (aim/buildSwerveAim/remote aim paths). 
- Replaced various uses of the raw `baseDir` with the spin-adjusted `guideDir` for fallback end, cue-follow dot tests, and target fallback computations so visuals and follow behavior match Pool Royale. 
- Increased aiming line weight to match Pool Royale by adjusting `AIM_LINE_WIDTH` and tuned the standing camera distance with `STANDING_VIEW_DISTANCE_SCALE` in `webapp/src/pages/Games/SnookerRoyal.jsx`. 
- Force the cue stick to remain visible during standing view and when the camera returns (removed conditional hiding logic in the cue stroke flow) so the cue does not disappear when portrait camera height changes.

### Testing
- Ran lint: `npm --prefix webapp run lint -- src/pages/Games/SnookerRoyal.jsx` and it completed without errors. 
- Built the webapp: `npm --prefix webapp run build` and the production build completed successfully. 
- Ran unit tests: `npx jest test/snookerRoyalTableSpecs.test.js test/snookerTableModel.test.js --runInBand` and both suites passed (2 suites, 11 tests). 
- `git diff --check` ran cleanly; attempted a Playwright portrait screenshot but Chromium failed to launch in the container due to a missing system library (`libatk-1.0.so.0`).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a91d943d5bc8329842ffe8538e11dc7)
