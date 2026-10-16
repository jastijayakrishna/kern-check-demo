# perf(gsplat): O(n) adaptive counting sort + camera-epsilon resort skip

## What

Optimizes the Gaussian-splat sort worker. The worker previously re-sorted every splat every frame with a `BigInt64Array` comparison sort (`O(n log n)` with BigInt compares). This PR makes three changes that cut steady-state and per-sort cost while preserving the back-to-front ordering (up to depth-key quantization):

1. **Adaptive-precision counting sort** — extracted into a new pure module `splat-sort-core.ts` so it is unit-testable without the worker's `self`. A 32-bin density histogram allocates key space proportional to where splats actually are, and the key width adapts to the cloud (`2^clamp(round(log2(n/4)), 10, 20)`). `O(n)` stable scatter.
2. **Camera-epsilon resort skip** (`postSplatSortIfDirty`) — when the world matrix, camera-forward vector and camera position all drift under `1e-4` since the last sort, the frame reuses the previous ordering. Mirrors BJS `viewUpdateThreshold`. Large win for mostly-static views.
3. **Double-buffered transferable order buffers** (`_orderPool`) with latest-wins upload — a second sort can be in flight while the previous result is still in transit; stale results are recycled so at most one GPU upload happens per frame.

The world-matrix-aware depth recipe `cameraForward · (world·localPos − cameraPos)` is preserved verbatim, relocated into the core module.

## Why

The per-frame BigInt sort is the dominant CPU cost for large clouds, and it runs even when the camera is still. Counting sort removes the `log n` factor and the BigInt boxing; the epsilon skip removes the sort entirely for static frames; double-buffering keeps the worker from idling on the round-trip during continuous motion.

## Testing

- `tests/lite/unit/splat-sort-core.test.ts` — 14 assertions: reference-sort equality on well-separated depths, quantization-tolerance bound on a 5k random cloud, non-identity world matrix, all-equal depths, empty/single clouds, NaN/Inf centres routed to the back, and the epsilon-skip / double-buffer pool mechanics.
- `tsc --noEmit` clean on the `babylon-lite` package.
- **Not verified:** WebGPU visual output was not checked headlessly (no GPU harness in this environment). The change is exercised at the unit-test and typecheck level only; a maintainer should confirm rendering on a real device.

A note on correctness found while writing the tests: tracking the depth `min`/`max` from the `f64` accumulator while the depth scratch is a `Float32Array` let the nearest splat's f32-truncated depth fall just below `min`, mis-routing it to the far end (drawn behind everything). The range is now tracked from the round-tripped f32 value; the tolerance test covers it.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
