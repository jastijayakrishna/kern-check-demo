# Use supplied Racing Royal game and precisely align Alpine track tires

## Summary

- Open the user-supplied Ferrari + Go-Kart Weapon Bubble game by default at the existing Racing Royal routes.
- Rebuild the Alpine tire rows with independent inside/outside arc-length spacing, exact edge tangents and an even closing seam. Tires no longer intersect within stacks or overlap neighboring stacks on turns.
- Join red/white curbs to the asphalt samples and fix overlapping starting-grid tiles.
- Retain the previous Tirana garage, kart choices, career and Explore behind **TPG / MODES**. Paid online/table/code URLs continue to use the existing authoritative multiplayer runtime; the supplied game is local-only.

## Attachment fidelity

The complete attachment is preserved byte-for-byte in `test/fixtures/racingRoyalSupplied-20260910.tsx`.

SHA-256: `1fd6efae1b9d61e049e98660e3154854191f010bb916ad60aee3ce55a23a783c`

The implementation preserves the supplied track points/width, Ferrari/Buggy URLs, all 18 weapon definitions and URL fallbacks, AI, speed/braking/boost formulas, pickups, inventory, projectile/shield damage, respawn, three-lap race and chase-camera logic. Source-parity tests protect these declarations.

Intentional exceptions:
- Track decoration/tire placement above; the same tire/rim geometry and material pattern are rendered in four instanced batches.
- One demonstrated steering sign bug: right drag / D / right arrow now moves the player screen-right. The rest of `updateVehicle` is source-identical.
- App exit/modes navigation, safe-area positioning and a minimap column that does not overlap the added buttons.
- Restart/exit resource disposal, cancelled-load cleanup, input release on blur/visibility loss, no firing on pointer cancellation, and startup error handling. This follows the React integration review without replacing gameplay.

## Verification

Passed:
- `node --test test/racingRoyalSupplied.test.mjs test/tiranaRepairCore.test.mjs test/racing-precision.test.mjs` — **52/52**.
- Tests cover source integrity, offsets/tangents, corner clearance, seam spacing, non-overlap, curbs, instancing, screen-left/right, three-lap supplied player/AI simulations, inventory, shield/projectile formulas, cleanup and paid-route isolation.
- `npm run build` in `webapp` — successful full production build; existing large-chunk warnings remain.
- Standalone kart Vite build — successful.
- Strict public-contract check of `test/tiranaRepairTypes.mts` — passed. Its legacy held-control example now supplies neutral shield/fire fields required by the existing Input contract.
- All 12 committed files were read back from GitHub and compared exactly against the tested local files.

Broader checks are not fully green:
- `tsc -p tsconfig.kart.json` reports four existing missing JS declaration errors in ExploreConnection, ExploreGame, useExploreMedia and SharedGameCast. Those files are unchanged.
- Existing Tirana tests still expect five rather than six tracks, no shield field, and an old legacySimulation blob hash. The tested legacy source/test files are unchanged by this PR. All 18 legacy six-kart AI races across three difficulties completed successfully.
- Server test entry points could not run because root `socket.io` / `mongoose` dependencies are not installed here.

Generated build metadata and native icon files are excluded.

## Required before release

This is a **draft**, not an end-to-end visual approval. Network approval was cancelled while checking the supplied external GLTF endpoints. No external assets were substituted or claimed verified.

- [ ] Load the original Ferrari, Buggy and all weapon assets on the target browser/device; distinguish successful downloads from the supplied procedural fallbacks.
- [ ] Inspect inside/outside tires and joined curbs through every turn and the start/finish seam.
- [ ] Test portrait mobile drag-drive + camera, FIRE/BOOST/BRAKE, restart/exit and notched-screen layout.
- [ ] Verify the retained TPG entry/exit flow in the normal test environment.

See `docs/kart-royale.md` for the
