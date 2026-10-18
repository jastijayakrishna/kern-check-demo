# Restore Ludo human dice pickup and throw choreography

### Motivation
- Restore the human-player dice pickup, throw motion and the right-hand landing positions to the behavior present the previous morning while leaving unrelated Ludo presentation and weapon-placement changes intact.
- Ensure seated human reach/pickup uses the exact landed die position so on-screen portrait choreography matches the authored motion and camera expectations.
- Add regression coverage to prevent regressions of this choreography in future edits.

### Description
- Restored pickup/hold logic in `moveDiceToRail` so the human player keeps the die where it landed (`if (player === 0 && !immediate) { ... beginDiceHoldPose(...) }`), and reintroduced `railTarget` + `resolveDiceHoldContactTarget` usage to compute precise hold targets. 
- Restored dice roll targets and wobble behavior by assigning `diceObj.userData.railPositions = rails` and `diceObj.userData.rollTargets = preferredLanding` and by removing the `tabletopDiceLane` wobble attenuation so `spinDice` uses the original wobble strength. 
- Kept the rest of Ludo presentation intact and added a unit test asserting the restored choreography presence in the source by updating `test/ludoBattleGameplay.test.mjs` to validate the pickup/landing code patterns.

### Testing
- Ran `node --test test/ludoBattleGameplay.test.mjs test/ludoBattleRules.test.mjs` and all tests passed (15/15).
- Ran `npx eslint webapp/src/pages/Games/LudoBattleRoyal.jsx test/ludoBattleGameplay.test.mjs` which reported no lint errors though both files matched repo ignore patterns (warnings only).
- Verified `git diff --check` and committed the changes; attempted a visual verification with Playwright at `390x844` but the first run failed due to missing Chromium system libraries and, after installing them, the full route did not finish loading within the capture window so no screenshot artifact was produced.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6aa8c9d591608329a1b49ccdf97e4d0e)
