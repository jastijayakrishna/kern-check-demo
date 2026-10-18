# fix(photo-gallery): memoize dynamicEl and plugins to prevent LightGallery slide index desync

## Summary

Fixes #636. Clicking through photos in a `PhotoGallery` lightbox and pressing prev/back repeatedly could trigger a fatal runtime error (`Cannot read properties of undefined (reading '__slideVideoInfo')`) because LightGallery was reinitializing on every render, causing its internal slide index to drift out of sync with `dynamicEl`.

- Memoize `dynamicEl` with `useMemo` so the slide array is stable across re-renders (only rebuilds when `photos` changes), matching the existing Instagram widget pattern
- Memoize `plugins` array inside `LightGalleryComponent` so LightGallery doesn't reinitialize unnecessarily
- Extract `onInit` as a stable `useCallback` instead of an inline function
- Add `loop={false}` to prevent wrap-around navigation from hitting invalid indices
- Drop now-unused `lightGalleryRef` prop from the inner `LightGalleryComponent`
- Add `PhotoGallery.spec.js` with 17 tests covering rendering, lazy load gating, `dynamicEl` shape, LightGallery config, `openLightbox` index handling, and empty photo array
- Bump `www.chrisvogt.me` to `1.22.9` (patch)

## Test plan

- [ ] Open a recap post with multiple `PhotoGallery` sections (e.g. `/personal/may-2026`)
- [ ] Open a gallery lightbox and click through all photos
- [ ] Press prev/back repeatedly — confirm no crash
- [ ] Confirm `loop={false}` stops navigation at the first/last photo rather than wrapping
- [ ] All 1,367 existing tests pass, lint and Prettier clean

🤖 Generated with [Claude Code](https://claude.com/claude-code)
