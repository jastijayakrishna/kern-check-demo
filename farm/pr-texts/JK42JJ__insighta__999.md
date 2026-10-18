# fix(player): video-mode thumbnail fallback depth + placeholder detection (CP504 track B)

Video-mode (player) thumbnail bugs — **separate track, no feature flag** (player always active → prod-immediate; rollback = `git revert`). Independent of the note pipeline.

## Measured root causes (code SSOT; hypotheses refuted with evidence)
- **Bug 1 (black poster)**: `video-block.tsx` did a ONE-step `onError` fallback (`maxres→hq`) then hid the block; never descended to always-present `mqdefault`/`default`. Also YouTube serves a **120×90 grey placeholder with HTTP 200** for some videos → `onError` never fires → blank/blurry poster with no recovery (no `onLoad` handler).
- **Bug 2 (low-res after note→video remount)**: SW-cache hypothesis **REFUTED** (`vite.config.ts` runtimeCaching only caches fonts; `i.ytimg.com` not cached). Remount-latches-low-res **REFUTED** (src recomputes to maxres each mount). Actual = the same grey HTTP-200 placeholder surfacing on a given mount.

## Fix
- `image-utils.ts`: extracted pure `nextYouTubeThumbnail(src)` (deep descent `maxres→sd→hq→mq→default`, null at exhaustion); `handleThumbnailError`/`handleThumbnailLoad` delegate to it; `isYouTubePlaceholder` (120×90) detection.
- `video-block.tsx`: replaced one-step onError with deep descent + added `onLoad` placeholder-descent. Aligns video-block (the lone outlier) with the standard `thumbnailImgHandlers` used by 11+ components. Hide-deleted/private semantics preserved.
- +3 regression tests.

## Gates
- **P-THUMB-1** deep chain to always-present tiers · **P-THUMB-2** onLoad descends past grey placeholder (remount stays hi-res) · **P-THUMB-REG** tsc 0 / vitest **414** / build 0. **No SW/cache change** → no user re-caching.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
