# Lower Chess Battle Royal missile and drone flight lanes

### Motivation
- Improve portrait-screen readability by moving inventory air attacks (Short Missile, Shahad Drone, Ukrainian Drone) onto dedicated, lower flight lanes without affecting jet/helicopter flyovers.

### Description
- Introduce portrait-friendly constants in `webapp/src/pages/Games/ChessBattleRoyal.jsx`: `CAPTURE_SHAHAD_DRONE_STRIKE_ALTITUDE`, `CAPTURE_UKRAINIAN_DRONE_CRUISE_HEIGHT`, `CAPTURE_UKRAINIAN_DRONE_MISSILE_CLEARANCE`, and `CAPTURE_SHORT_MISSILE_STRIKE_ALTITUDE` to separate inventory attack lanes from aircraft flyovers.
- Apply the new low-lane constants to Short Missile and Shahad Drone capture flows by replacing prior `strikeAltitude` usages with the new values.
- Lower the Ukrainian Drone cruise path and adjust its missile release altitude to use the new cruise and clearance constants.
- Add a regression test in `test/chessBattleInventoryConfig.test.js` that verifies the presence and use of the new constants in the source.

### Testing
- Ran unit tests with `npx jest test/chessBattleInventoryConfig.test.js --runInBand`, all tests passed (6/6).
- Built the webapp with `npm --prefix webapp run build`, production build completed successfully.
- Lint check reported file-ignore warnings for the two edited files when running ESLint (no lint errors reported for changed code); this is due to repo ignore configuration.
- Attempted automated Playwright screenshot of the preview but it failed because the environment does not have the Playwright Chromium executable installed.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a7091d94c6883299071ca86d43a4556)
