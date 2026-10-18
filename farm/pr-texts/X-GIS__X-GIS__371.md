# fix(compiler): iterative Douglas-Peucker to stop tiler-worker stack overflow on huge rings

## Bug (live-site, user-reported)

`categorical` demo (countries.geojson) at z0 on mobile Safari floods the console with `[virtual-pmtiles worker] RangeError: Maximum call stack size exceeded` — one per tile — and the map is blank.

## Root cause

`dpStep` (Douglas-Peucker) in `compiler/src/tiler/simplify.ts` was **recursive**. Worst-case descent depth is O(n): a long run of boundary-locked vertices peels one vertex per level. At z0, country rings clamped along the antimeridian / ±85° Mercator boundary carry thousands of locked vertices, so the recursion overflows the JS native call stack inside the MVT tiler worker.

Confirmed by unminified dev repro:
```
RangeError: Maximum call stack size exceeded
    at dpStep (compiler/src/tiler/simplify.ts ... recursive)
```

## Fix

Convert `dpStep` to an **explicit heap-backed stack** (iterative). The `keep[]` output is independent of segment processing order, so the simplification result is byte-identical to the recursion — verified by semantics tests.

## Verification (locked gate)

- **fail-before**: a 60k locked-vertex run throws `RangeError` on the recursive form, passes now (`simplify-stack-overflow.test.ts`).
- **semantics preserved**: DP correctness tests (near-collinear drop, locked-vertex survival, known multi-point result) pass on both forms.
- **large-ring smoke**: 120k jagged ring + `simplifyPolygon` complete without error.
- `bunx vitest run` compiler/src/tiler + architecture-invariants → **193 passed**.
- `bun run build` (typecheck) → exit 0.
- **real-GPU (headed)**: `categorical` demo now renders all countries with categorical colors, **0 worker errors** (was ~100 RangeErrors/load).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
