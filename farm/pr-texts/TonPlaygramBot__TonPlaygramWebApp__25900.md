# Restore live Ludo Battle Royal humans and fix dice handling and weapon aiming

The live Ludo Battle Royal game needs the original humans to make contact with the dice and weapons, and weapon aiming must follow the actual muzzle. This updates `webapp/src/pages/Games/LudoBattleRoyal.jsx` and its production controllers on `main`. It follows the earlier preview PR #25894 with the live-game integration.

Changes:
- Restore the original human roster and bundled character, correct seating, and solve palm contact with fixed arm lengths. Reuse the historical grip, windup and release poses for local and server-authoritative dice rolls, starting from the die's actual position.
- Move the displayed weapon from table to hands and back. Normalize 33 weapon profiles to consistent relative dimensions, preserve source stocks/materials, and park them on each seated character's right within the tabletop.
- Align the bore with the target while maintaining grip/support contact, including recoil and close targets. Throwables use a pickup-and-release motion.
- Rebuild the six-wheel truck with cab, glazing, mirrors, lamps and tyre detail; instance its tread blocks and use consistent miniature vehicle dimensions.
- Give weapon families appropriate projectiles, impact sparks, blasts or fire, and shell ejection only where appropriate. Freeze each shot's trajectory at firing time and clean up cancelled/stale animations.
- Make the portrait interaction preview use the production controllers and original human model.

Validation:
- 25 tests pass: existing gameplay/rules tests plus contact, parking, aiming, dice release, sparse-frame volley, cancellation and cleanup checks.
- Motion checks use the bundled human skeleton across all four seats and all 33 profile fallback models. Source-model axis normalization is also tested with fixtures.
- TypeScript checks, a focused browser bundle of the live Ludo component, and `git diff --check` pass.
- Built the 492,012-byte portrait preview and inspected CPU-rendered idle, aim and dice poses.
- The branch merges cleanly with the latest main.

Verification limitation: the browser blocks the local preview with `net::ERR_BLOCKED_BY_CLIENT`, so browser playback and full live gameplay were not verified here. Every external artist model has not been visually inspected; the all-profile geometry checks use the corresponding procedural fallbacks.
