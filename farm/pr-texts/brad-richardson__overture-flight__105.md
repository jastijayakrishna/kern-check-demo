# perf: extend expanded terrain radius to reduce edge-of-world

## What

Answering "should we optimistically load a little further out?" — **yes, on desktop.** Bumps the expanded ground/terrain ring one further (radius 4 → 5, an 11×11 area) so the horizon fills in while flying. Buildings' `CORE_RADIUS` stays 1 (they're the expensive layer).

## Adversarial review found + fixed

An adversarial review caught three issues with a naive constant bump, all fixed here:

| issue | fix |
|---|---|
| Expanded cache (72) < desktop active ring (112 tiles) → freshly loaded tiles evicted-then-re-uploaded each frame, orphaned texture could leak on unload | desktop `CACHE_MAX_SIZE` → **128** (≥ the 112-tile active ring), so loaded tiles stay resident |
| radius bump wasn't mobile-gated (mobile can't afford +55% tiles) | **mobile stays at radius 4** and its shipping cache (24); only desktop → radius 5. `UNLOAD_DISTANCE` derived as `TILE_RADIUS + 1` for consistent per-device hysteresis |
| unload + prune were inside the ≥30fps gate → under load the app stopped shedding its (now larger) working set | **always run unload/prune**; gate only *new* loads on fps, so a struggling frame can still release tiles and recover |

Confirmed correct by the review: hysteresis is thrash-free, the load queue is bounded, and no code assumes radius ≤ 4.

## Safety / watch-point

- **Mobile is byte-identical to what ships today** (radius 4, cache 24) — zero mobile risk.
- **Desktop memory** is the thing to watch: cache 128 × 512² textures ≈ ~170 MB of expanded-ground texture memory (up from ~72 MB), the cost of both the wider ring and eliminating the pre-existing evict-churn. Fine for discrete GPUs; if it's tight on integrated graphics, lower `CACHE_MAX_SIZE` (accepting some churn) or `TILE_RADIUS`.
- Residual (pre-existing, not a regression): during very rapid desktop motion the active set can briefly exceed 128 and churn transiently. A deeper fix (dispose orphaned textures in `removeExpandedTile`) would decouple correctness from cache size — noted as a follow-up.

Test derives the ring count from the constants, so it tracks future tuning. Full suite green, `tsc` clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
