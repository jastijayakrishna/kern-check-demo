# Fix missing original Albanian Forces in the active Tirana Streets Battlefield

## Why the original assets were invisible
PR #25838 was merged and deployed: the live server serves the original GLBs. However, the public Battlefield route mounts `blackwater/ui.tsx` / `GameEngine`, while the prior integration only connected `CityRenderer` / Street Career. Battlefield still used procedural opponents and generic cover.

## Changes
- Connect the actual Battlefield opponents to the original GLB loader, cycling all six uniforms. Hide only the procedural body after loading; retain gun/muzzle, hitboxes, AI, death timers and online ownership.
- Render all eight original vehicles as parked cover using their unscaled metre bounds in the shared client/server collision layout.
- Place the fleet 12–19 metres from the actual Skanderbeg sector deployment, avoiding buildings, fixtures, other vehicles and spawn/extraction points. The older city spawn is over 100 metres away; legacy road snapping also stacked several covers on one point.
- Retain byte-identical GLBs, embedded textures, rigs and clips, along with the existing near-distance/count limits and loading/distant fallbacks.
- Add actual-Game browser verification and regression coverage for uniforms, cleanup, cover dimensions and deployment clearance. Narrow the old source fingerprint to the unchanged gun because procedural body grouping intentionally changed.

## Validation
- 22 asset, city, Battlefield and multiplayer tests pass.
- Full production build and focused strict TypeScript checks pass.
- Actual Battlefield Game/GameEngine rendered an original officer and patrol car at 390×844, with HTTP 200 original-model responses, hidden procedural body and no page errors.
- Screenshot harness bypasses account/API wrappers and freezes AI/positions one existing opponent for deterministic evidence. Software WebGL is not a physical-phone performance measurement.
- Remote Git tree matches the tested local tree.

## Portrait evidence
![Original officer](https://github.com/TonPlaygramBot/TonPlaygramWebApp/blob/codex/tirana-force-visibility/docs/validation/tirana-forces/original-officer.png?raw=true)
![Original patrol car](https://github.com/TonPlaygramBot/TonPlaygramWebApp/blob/codex/tirana-force-visibility/docs/validation/tirana-forces/original-patrol.png?raw=true)

The parked fleet is near Skanderbeg deployment; uniform rendering also works in other Battlefield sectors. This PR does not merge or deploy itself.
