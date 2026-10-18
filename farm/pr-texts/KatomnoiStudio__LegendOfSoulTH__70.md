# fix: ground battle sprites and curve combat controls

## What changed

- Lift only the nested entity visual container so legacy negative foot calibration no longer sinks characters below the gameplay ground plane.
- Restore a responsive curved `S1 → S2 → S3 → ULT` Combat Cluster around the primary ATK button.
- Use one deterministic layout model for CSS placement and collision tests across four landscape/safe-area profiles.
- Update project blueprint, task ledger, memory, changelog, and version metadata to `0.12.4`.

## Root cause

The sprite presentation calibration targeted a negative world-space foot position, while the controls had regressed to a straight flex row. This made characters appear below the floor and caused the skill controls to diverge from the locked mobile layout.

## Scope guard

Sprite-sheet replacement remains blocked pending new assets. This PR does **not** modify image frames, sprite sheets, animation registry, combat balance, damage, enemy AI, or Supabase.

## User impact

Characters visually meet the ground while gameplay coordinates, shadow, hitbox, and hurtbox remain unchanged. Skill controls form a thumb-reachable arc, honor safe areas, keep touch targets at least 48px, and avoid overlap on tested landscape profiles.

## Validation

- `npm run ci`
- TypeScript typecheck passed
- `oxlint --deny-warnings` passed
- 85 test files passed, 675/675 tests passed
- Production build passed
- Bundle-size gate passed
- Branch refreshed against `master` at `8ec6918` before publication
