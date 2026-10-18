# fix(tiler): overlap adjacent fill tiles to close the inter-tile MSAA seam on the globe

## Bug (user-reported, real-GPU)

On the globe, adjacent polygon fill tiles show **dashed background-colour hairlines** along tile boundaries — across both ocean and land fills, worse toward the limb / under pitch. User: "타일간 빈틈 / 삼각분활된 삼각형간의 간극 / 백그라운드 컬러".

## Root cause (empirically proven, corrected from a prior mis-diagnosis)

`ocean_land` routes geojsonvt → MVT worker → **`compileSingleTile`** (confirmed via `__xgisVirtualPMTilesActive`), NOT the `subdivideTriangleMM` path a prior analysis targeted. Every same-layer fill producer emits geometry on **exact tile bounds**:
- `compileSingleTile` / `compileGeoJSONToTiles` → `clipPolygonToRect(... exact bounds)`
- `createFullCoverTileData` → quad on exact corners

So adjacent tiles meet at an infinitely-thin shared edge. 4× MSAA (always on for fill) antialiases it into partial sample coverage → the clear/background colour bleeds through. geojsonvt ships a 25% buffer precisely to prevent this; the per-tile clip discards it. The `clip_bounds` fragment discard is parent-fallback-only (sentinel for own-data) and is NOT involved.

## Fix

Re-introduce a small symmetric **fill overlap** (`FILL_TILE_OVERLAP_FRAC = 0.05` of tile span/side), at every fill producer:
- Widen the clip rect **and the boundary-lock simplify predicate in lockstep** (locking the exact edge would let simplify pull the fill back in and re-open the seam — the key interaction).
- Widen the full-cover **detection area basis** so the quad fast-path is preserved.
- Widen the synthesized full-cover **quad** (anchor kept at the exact SW corner → DSFUN round-trip + stride-6 layout unchanged).
- **Outline** (line-clip) and **parent-fallback `clip_bounds`** stay exact.

Overlap is safe at any magnitude: the clipped ring stays bounded by the real polygon (land can't spill into ocean); the full-cover quad spills the same colour under a coastal neighbour that draws on top.

## Verification (locked gate)

- **Real-GPU before/after** (headed, ocean_land globe): dashed background hairlines GONE across pacific-z4, atlantic-z4, med-z5-pitch, open-ocean z7. Only the irreducible extreme-grazing horizon band retains a faint trace (hemisphere-cull territory, not a margin problem).
- **Deterministic fail-before/after**: adjacent-tile fill-overlap invariant (compiler) + full-cover quad span = (1+2·frac)×tile span (runtime) — both fail at zero overlap, pass after.
- **Flat-Mercator pixel-match vs MapLibre unaffected**: demotiles-user 96.14%, bright-seoul-school / liberty-paris-z14 / demotiles-europe-z2 pass. `bright-tokyo-z14` eq-floor miss is **pre-existing** (identical 23.73% at frac=0, geometry gt128=2px tiny).
- `bunx vitest run` (tiler + runtime data + arch-invariants) → **232 passed**. `bun run build` → exit 0. Ratchets bumped vector-tiler 1551→1582, tile-catalog 1417→1425 (irreducible; decomposition still tracked).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
