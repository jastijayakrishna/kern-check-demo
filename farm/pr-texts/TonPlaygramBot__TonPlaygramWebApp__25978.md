# Snooker Royal: remove 6K/8K HDRI, trim player size, and improve AI shot planning

### Motivation
- Limit heavy HDRI texture options to improve memory and mobile portrait performance and remove the overly large 6K/8K choices from the graphics menu.
- Make the human player character slightly smaller so the silhouette does not overpower the table in portrait framing.
- Improve AI planning so the opponent evaluates cue-ball leave from the first shot of a visit and prefers continuation-friendly sequences for stronger positional play.

### Description
- Removed the `6k` and `8k` entries from `HDRI_RESOLUTION_OPTIONS` and capped automatic HDRI selection by returning `'4k'` in `resolveHdriResolutionForTable` in `webapp/src/pages/Games/SnookerRoyal.jsx`.
- Reduced the floor-anchored player `targetHeight` scale multiplier from `cueLen * 1.68 * 1.2` to `cueLen * 1.68 * 1.14` to trim the character silhouette for portrait screens.
- Updated AI planning: broadened `shouldAnalyzeLeave` so leave analysis runs on the first shot of a visit (`aiTurnShotCountRef` dependency removed), added next-shot legal-target sequencing for snooker (alternate red/colour continuation), and raised the cue-ball leave weight from `0.12` to `0.2` to favour better position play when ranking plans.
- Adjusted test expectations and added `test/snookerRoyalPresentation.test.mjs` to assert the HDRI menu ceiling and the AI/leave configuration, and updated `test/snookerCharacterCamera.node.mjs` to reflect the changed character sizing assertions.

### Testing
- Ran the unit/regression suite with `node --test test/snookerRoyalPresentation.test.mjs test/poolUkAdvancedAi.test.js test/poolUk8Ball.test.js` and all tests passed.
- Performed a TypeScript compile check with `tsc -p tsconfig.build.json --noEmit` and it completed without errors.
- Linted the modified source with `eslint` for the affected file `webapp/src/pages/Games/SnookerRoyal.jsx` and there were no outstanding errors for that path.
- Attempted an automated Playwright portrait capture, but Chromium failed to start in the container due to a missing system library (`libatk-1.0.so.0`), so screenshot verification was not captured in CI here.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6aa8d545d82483298301c86c046706ba)
