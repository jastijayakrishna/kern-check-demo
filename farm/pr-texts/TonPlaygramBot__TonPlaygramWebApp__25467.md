# Improve Pool Royale AI ghost-ball aiming and route checks

### Motivation

- Fix AI positional planning and aiming errors where the planner sometimes failed to validate live table lanes and aimed at the object-ball centre instead of the ghost (contact) point, causing missed cuts and incorrect spin choices.

### Description

- Add a dedicated live-table lane tester `isAiRouteClear` used by positional planning to check clearance against `ballsRef` instead of calling the evaluator's local `isPathClear`. (updated `webapp/src/pages/Games/PoolRoyale.jsx`)
- Replace out‑of‑scope `isPathClear` calls inside the advanced planner with `isAiRouteClear` so route/approach checks are consistent for next-shot positional selection. (updated `computePlanSpin` and next-route selection)
- Change emergency AI aiming so plans compute and aim toward the ghost-ball contact point (one ball diameter behind the object ball on the pocket line) instead of the object-ball centre to produce geometrically correct cut shots. (updated fallback aim generation in `PoolRoyale.jsx`)
- Commit recorded under message `Improve Pool Royale AI ghost-ball aiming` updating `webapp/src/pages/Games/PoolRoyale.jsx`.

### Testing

- Ran the targeted unit tests with `npx jest test/poolRoyaleAiAimCompensation.test.js test/poolUkAdvancedAi.test.js --runInBand`, and both suites passed (2 suites, 12 tests; all green). 
- Performed a production build with `npm --prefix webapp run build`, which completed successfully and produced `dist` assets. 
- Ran `npx eslint webapp/src/pages/Games/PoolRoyale.jsx`, which completed with no errors (one ignore warning due to repo ignore settings).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a9273b250888329b739c2e2b4f37de7)
