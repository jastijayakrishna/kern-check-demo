# Fix Snake and Ladder human dice pickup and firearm grips

Snake and Ladder's seated humans were static while the die and weapons animated independently. Rolls moved the die to an airborne start position, and imported firearm scale overrides made the parked models inconsistent.

This connects the actual seated skeleton to dice reach, grip, lift and release. The die keeps its resting transform until pickup, and local/online presentation timing includes the hand animation. Firearms retain one parked/held size, with trigger and support-hand contacts, muzzle-based aiming, Ludo's shared firing effects, and a return to the parked position. Cancellation restores the pose and weapon visibility.

Validation: all 60 Snake tests pass; the production webapp build and TypeScript checks pass. The tests include the real board and parking layouts, all four seat directions, planted feet, contact through recoil, release continuity, 30/60/90 Hz, skipped frames, and local/online turn locks. Portrait geometry reviews using the actual avatar and imported rifle, pistol and shotgun caught and corrected finger-axis, resting-pose, reach and support-hand issues.

Includes a React + Three.js portrait preview with pause, scrub and repeat controls, plus reproducible frame checks. Live browser/Telegram validation remains pending because Chromium could not be downloaded in this environment. External store models without authored sockets use family contact profiles and have not all been individually visually calibrated. See docs/snake-human-interaction-review.md.
