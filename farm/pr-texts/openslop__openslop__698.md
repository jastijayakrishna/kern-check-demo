# perf: nightly performance optimizations 2026-08-31

The canvas was downloading and decoding every generated image at its full 2560px generation size, to paint it at 64–128px. It no longer does.

## What was wrong

`ASPECT_RATIO_DIMENSIONS.image` is `2560×1440` for 16:9 (`1440×2560` for 9:16) — deliberately oversampled, because the Ken Burns effects in `MotionLayer` zoom into the still and need the headroom. That is right for the render.

It is not right for the UI. Every place a still is shown in the editor went through `next/image` with `unoptimized`, which serves the original bytes untouched:

| Where | Painted at |
| --- | --- |
| `AssetTile` (characters, reference images) | 64–80px |
| `ElementHistoryPopover` thumbnail | 64px |
| `TimelineClip` visual preview | ~48px |
| `ForegroundPreview` (collapsed scene, storyboard) | ~100–128px |
| `MediaPreview` (element card result) | up to ~1100px |

So a collapsed scene rail was pulling a multi-megabyte 2560×1440 asset per scene to fill a 128px box, and the browser was decoding each one to a full-resolution bitmap (2560×1440×4 ≈ 14.7 MB of RGBA) to downscale it on every paint.

Every one of these URLs is on a hostname `next.config.ts` already lists in `remotePatterns` — `BaseProvider.store` and `/api/upload/image` both go through `AssetBundle.upload` to Vercel Blob, and the mock providers serve `BLOB_BASE_URL`. `ProjectCard` already renders the same class of asset optimized. The canvas was the one opting out.

## The change

`MediaWithSkeleton` takes a required `sizes` and drops `unoptimized`; `AssetTile` does the same. Each call site now declares the width it paints at, so the browser picks the matching srcset entry and Next serves it as WebP/AVIF.

Making `sizes` required rather than defaulting it is deliberate: the default with `fill` is `100vw`, which would silently reintroduce the same over-fetch at any new call site.

## Measured

Through a production build's own optimizer (`npm run build && npm start`, `curl` with a browser `Accept` header), against the `image/mock/2` fixture — 2000×1308, 519,034 bytes of JPEG, i.e. **smaller than a real 2560×1440 still**:

| Requested width | Bytes | vs original |
| --- | --- | --- |
| 256 (tiles, timeline, foreground preview) | 2,228 (WebP) | **233× smaller** |
| 384 | 3,634 (WebP) | 143× smaller |
| 640 | 6,978 (WebP) | 74× smaller |
| 1200 (element card result) | 15,406 (WebP) | 34× smaller |

Decode drops with it: the 256px variant is ~0.17 MB of RGBA instead of ~10.5 MB for that fixture, or ~14.7 MB for a real still.

This is bandwidth in both directions. Vercel bills transformations per unique (url, width, quality) and caches them for 31 days — a few per generated image — against the served bytes it replaces.

## One deliberate imprecision

`MediaPreview` uses a single `sizes="(min-width: 1024px) 60vw, 100vw"`, which over-states the width inside `CharacterEditModal` (a `max-w-2xl` two-column layout). Threading a `sizes` prop through `MediaResult` → `ELEMENT_PREVIEWS` → three preview components to shave one modal would be more plumbing than it is worth, and the over-statement means the modal reuses the transform the canvas card already fetched rather than requesting a second one.

## Test change

`cancelOffset.test.tsx` asserted the raw URL appeared in the rendered HTML. An optimized `<Image>` emits `/_next/image?url=…`, so the assertion now checks for the host. Same intent: media renders instead of the placeholder.

## Skipped

- `<video>` card previews still mount the full asset. `preload="metadata"` is measured-dead here (Chromium buffers identically), and there is no equivalent of the image optimizer for video on this stack.
- Nothing else in the Slate, Remotion or React render paths met the bar; that surface is covered by prior nightly notes and remains clean.

## Open PR overlap check

One open PR, #697 (`ARCHITECTURE.md`, `PostPromptView.tsx`, `video/BottomDock.tsx`, `BottomViewContext.tsx`, `BottomViewToggle.tsx`, `bottomViews.tsx`, `storyboard/Storyboard.tsx`, `timeline/Timeli
