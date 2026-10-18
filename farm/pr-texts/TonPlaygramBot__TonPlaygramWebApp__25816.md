# Improve Racing Royal tyre barriers and Tirana city detail

## What changed
- distribute tyre-wall instances by physical track-segment length so the red/white safety rows stay continuous on straights and curves
- preserve instancing and allocate only the required tyre capacity
- add mapped roof caps and rooftop utility silhouettes to nearby Tirana buildings
- add deterministic three-tree park groves for a denser, more natural cityscape

## Integration notes
The existing Racing Royal renderer already contains the supplied gameplay systems (boost, drift, shields, ammunition/fire, damage, effects, kart assets, mobile controls, AI racing, and local Tirana scenery). This change integrates the missing visual improvements into that actual renderer rather than replacing it with the standalone pasted component or adding remote runtime asset dependencies.

## Verification
- `npm run build` (webapp) ✅
- `git diff --check` ✅
