# Refine cue-ball spin integration and ball-ball collision resolution

### Motivation

- Match Pool Royale's cue-ball controller so selected spin is kept but cloth/omega translation and visible aim behavior remain authoritative until first impact.  
- Fix edge-case collisions (zero-distance / deep penetration) and remove brittle predictive repositioning logic that overrode physics for locked-aim shots.  
- Improve physical realism by computing angular impulse, tangential friction, and suppressing cue-tip omega on first contact to prevent english from throwing balls away from the shown line.

### Description

- Implement pre-impact spin locking for the cue: spin is stored but spin-driven translation (omega effects) only starts after the first ball or rail impact via `preImpactCueSpinLocked` gating.  
- Add explicit spin integration and rolling resistance when no lift is present using `SPIN_FIXED_DT`, `SPIN_*` constants, and velocity/omega updates.  
- Replace the earlier ad-hoc overlap/collision branch with a robust ball-ball collision resolver that uses `BALL_CONTACT_EPS`, `BALL_COLLISION_SLOP`, computes penetration, handles zero-distance by falling back to relative-velocity direction, and applies normal impulse, tangential friction, and angular (omega) updates.  
- Suppress cue-tip omega at first contact (`!impacted`) so the cue cannot impart unexpected angular throws on initial contact, and remove the prior `lockedAimCollision` path that positioned balls and set velocities from shot predictions.  
- Mark cue balls as `impacted` on contact and adjust sound/volume calculations to use computed impulse magnitudes, while keeping previous first-hit/shot-context bookkeeping.  
- Remove the previous single friction multiplication in favor of explicit rolling deceleration and refined stop thresholds and spin clearing logic.

### Testing

- Ran existing automated test suite via `yarn test`; local run reported all tests passing.  
- Performed a quick interactive smoke test of the table simulation in the dev build to validate cue pre-impact behavior, ball collisions, and audio triggers; no regressions observed.  
- No new unit tests were added in this change.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a95bf88bf88832987939bbec42dd146)
