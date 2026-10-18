# Improve ball spin & collision solver; add shared scratch vectors

### Motivation
- Align ball physics with Pool Royale behavior by keeping selected cue spin on the cue ball while suppressing spin-driven translation until first impact and by preventing english from throwing balls away from the visible aim line.
- Replace the simplistic 2D collision response with a more physically correct normal/tangential impulse solver that accounts for ball angular velocity and contact slop.
- Reduce per-frame allocations by promoting temporary 3D vectors to module scope for the spin/contact solver.

### Description
- Added several module-scoped scratch `THREE.Vector3` temporaries (`TMP_VEC3_B`..`TMP_VEC3_H`) to avoid allocating vectors in the frame loop. 
- Implemented a Pool Royale-style spin integration that keeps cue spin visually on the cue ball before first impact, integrates `omega`/spin forces using a fixed spin dt (`SPIN_FIXED_DT`), applies sliding vs rolling damping, and applies rolling resistance when no lift is present.
- Reworked ball-ball collision detection and response to use 3D impulse math: use `BALL_CONTACT_EPS` and `BALL_COLLISION_SLOP` to compute penetration and overlap, handle degenerate zero-distance cases by deriving a contact normal from relative velocity, compute normal impulse with restitution and a tangential friction impulse clamped by `BALL_BALL_FRICTION`, and update both linear velocities and angular velocities (`omega`).
- Suppressed cue-tip omega contribution at first contact for the cue ball (when `!impacted`) to prevent english from throwing the shown aim line, and set `impacted` flags and play collision sounds scaled by computed impulse for new impacts.
- Removed the previous simple 2D velocity swap logic and the locked-aim collision special-case, and adjusted the motion update flow (spin handling, rolling friction, and final stop thresholds) accordingly.

### Testing
- Ran the project unit test suite with `yarn test` and the tests completed successfully. 
- Ran the linter with `yarn lint` with no errors reported. 
- Executed a physics regression smoke test (automated scenario run) to verify collisions, spin behavior, and audio triggers; the smoke test passed.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a95bf88bf88832987939bbec42dd146)
