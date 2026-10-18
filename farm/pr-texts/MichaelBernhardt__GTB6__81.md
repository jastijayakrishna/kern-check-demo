# Physics deaths: verlet ragdolls, slam falls, grounded corpses

The complete NPC death overhaul, owner-tuned across four playtest rounds:

- **Verlet ragdoll deaths (90%)**: at death the body goes limp from its current animation pose — a 15-particle simulation (skeleton rods, rigid torso truss, loose anti-hyperextension hinges only; no scripted poses) collapses it under gravity with a shot-direction kick, slides it against ground and walls with friction, and freezes on rest (10s hard cap, 8 concurrent max, zero allocation per step). Bones are driven by particle-frame deltas derived from the shipped rig — no axis assumptions, so rig rebuilds can't break it.
- **Knockdowns ragdoll too**: sprint bumps and car hits use the same fall with a damage-scaled impulse (shoulder nudge ~3 m/s, highway hit ~8); non-fatal survivors simulate for their normal 2s recovery, then stand back up through the animation handback.
- **Pose deaths (10%)**: the mocap fall now accelerates 2×→7× (~0.3s, reads as gravity), whips away from the impact side, and every corpse is measured onto the ground — the death capture tips over at standing hip height, and the old hardcoded offset left bodies hovering; the floor curve is sampled from each rig at load, plus a deliberate 0.2u settle-sink so stiff limbs don't read as floating.
- Damage sources now report their origin (bullet path, melee attacker, blast centre, vehicle) to drive kicks and spins.

Gate: lint, tsc -b, 1464 tests green including pure sim suites, real-GLB settle tests, an away-from-origin regression, lifecycle-culling and concurrency-cap coverage.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
