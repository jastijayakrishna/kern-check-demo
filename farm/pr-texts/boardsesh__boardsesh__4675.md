# fix(web): stop /api/internal/board-render OOM-killing its instances

## Summary

`/api/internal/board-render` OOM-killed its Vercel instances **507 times in three days** — 61% of all error volume — at roughly 50k renders/day. Three things were stacked on top of each other:

1. **Per-request decode → encode → decode waste.** Every request loaded each board photo, resized it, re-encoded it to WebP, then handed the first buffer straight back to sharp to be decoded again for compositing. `dim_background` then allocated and PNG-encoded a full W×H×4 black scrim, and the OG variant rasterised a blurred 1200×630 SVG per request. On the tallest Kilter board (1080×2498) that is several 10 MB planes per request, none of them reusable.
2. **No caching at all.** The long-running backend OG renderer has cached its composed base and its final bytes in a `BoundedLru` pair since #3829; the web route cached nothing, so every climb on a board re-did that board's photos.
3. **Untuned libvips + unbounded concurrency.** sharp's defaults (50 MB operation cache, one worker thread per core) assume a long-lived server with the machine to itself, and nothing limited how many renders ran at once — so peak memory tracked the arrival rate, and a traffic spike killed the instance instead of slowing it down.

What changed:

- **`composeBoardBaseBuffer`** decodes layers one at a time and folds them as raw RGBA, so peak stays around three planes regardless of layer count and nothing is re-encoded. The OG variant reuses the cached `composeOgBaseBuffer` + `encodeOgImage` pair the backend already uses.
- **Three module-level caches in the route**: composed board base (64 MB / 24), OG base (32 MB / 8), final encoded bytes (32 MB / 2000, keyed on the full canonical param tuple). Plus in-flight coalescing at two levels — one render per identical request, and one *base compose* per board, so two climbs on the same board arriving together don't each fold that board's ~10 MB of photos.
- **A FIFO semaphore** (`BOARD_RENDER_CONCURRENCY`, default 2) around the WASM render and the sharp pipeline, `sharp.cache({ memory: 16, files: 4, items: 100 })` + `sharp.concurrency(1)` at the route (the backend keeps libvips defaults), and a 3 MP output guard — the largest real board is 1080×2498 ≈ 2.70 MP, so anything larger is hand-crafted and gets a 400 rather than being resampled. A data-driven test fails if a future board grows past that ceiling, so it surfaces as a red test rather than a production 400.
- **Load shedding**: past 40 queued renders, new work gets a fast `503` + `Retry-After: 5` + `no-store` instead of a slot in a queue it can't clear inside the 30s budget. A request that can join an in-flight render is never shed — it costs nothing to serve.
- **`vercel.json`**: 3009 MB / 30s for this function as the stopgap that stops the bleeding while the above lands.

`Server-Timing` now carries `cache;desc=hit|base-hit|miss|none` and `queue;dur=<ms>`, so the hit rate and queue depth are readable straight off production traces.

Measured by QA: roughly **2× lighter and faster** on the render path.

Part of #4650 (Vercel burn hunt). The Rust follow-up that moves this render off Node entirely is #4664 — this is the fix that stops the kills today, not a replacement for it.

## Byte-level changes

Output bytes are not identical to `main` everywhere. Every affected URL is immutable and content-addressed by its params, so an old and a new copy simply coexist in the CDN.

- **`dim_background` output is unchanged — deliberately.** An earlier revision replaced the black scrim with an RGB scale (`rgb × (1 - dim)`), which is equivalent only for opaque pixels. QA measured every board WebP: they all carry alpha, and the photos are transparent everywhere except the holds, so ~77% of pixels came out with different alpha and up to 127 of RGB delta. `dim_background` is a full-bleed wash — that is what the iOS Live Activity widget asks for with `dim_background=0.18`, and what mobile's `LayeredClimbImage` draws as a full-bleed `rgba(0, 0, 0, 0.18)` view. The scrim
