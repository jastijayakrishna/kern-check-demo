# Refine Pool and Snooker cue reach, hands and shot impact

## Summary

- restrict the cue extension and mechanical rest to genuine short-rail-to-opposite-half shots aligned with the table's long axis
- keep the bridge hand planted from address through pullback and impact while the rear hand follows the exact rendered cue grip
- tune the existing shared avatar's skin, eyes, hair and clothing materials for the games' PBR/HDR lighting without adding a new third-party asset or license
- apply the same shared character/reach behavior in Pool Royal and Snooker Royal
- fix Snooker Royal's frozen cue-ball release by snapshotting the slider's committed power before UI reset
- add an idempotent contact-time fallback so a throttled/dropped animation callback cannot prevent the physics impulse

## Validation

- `npm run test:pool-players` — 19 passed
- targeted cue stroke, shot lifecycle/state, impact and Snooker audio Jest suites — 26 passed
- targeted ESLint on all changed game sources — passed
- `npm run build` in `webapp` — passed (existing Rollup chunk-size warnings only)
- automated browser capture could not start because the headless browser daemon exits in this runner; real-device mobile WebGL/touch verification remains required

## Notes

DLSS is not available in this browser/Three.js renderer. Character fidelity is improved through the existing high-detail rig, precise two-hand IK/stroke behavior and calibrated PBR material response, avoiding a new asset with uncertain commercial redistribution rights.
