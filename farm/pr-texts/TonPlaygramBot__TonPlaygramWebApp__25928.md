# Restore Snake leg pose and place tabletop just above the thighs

The last table change turned the characters' legs outward. This restores the original seated leg rotations, bone lengths, character scale and foot positions as requested.

The Snake tabletop is raised to 0.835 world units and its edge profile is reduced to 40% thickness. On the octagon, the lowest underside is about 0.745, leaving approximately 0.030–0.037 world units above the tested character's thighs. The nameplate fits within the thin fascia. No leg or character resizing was necessary. The smaller table footprint and measured weapon parking remain in use.

Validation: 90 Snake tests pass, including original leg-pose/size preservation, flat weapon parking and pickup/throw/firearm regression checks. TypeScript checking and the production Vite build pass. Geometry review measures the underside-to-thigh gap and verifies dice visibility in all four portrait seats; CPU renders were inspected. A React + Three.js TypeScript preview can be rebuilt with scripts/build-snake-interaction-preview.mjs.

Physical-phone WebGL/performance verification and every optional imported avatar/table combination remain device acceptance checks. See docs/snake-table-parking-review.md.
