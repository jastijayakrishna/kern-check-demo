# fix(photo-gallery): fix lightbox not opening on initial clicks

## Summary
- Moved the `useInView` IntersectionObserver ref from a sentinel div below the photo grid to the gallery container itself, so LightGallery starts loading as soon as the gallery approaches the viewport — not when the user scrolls to the bottom of the grid
- Added a `pendingIndexRef` that queues any photo click arriving before LightGallery initializes and replays it in `onInit`, covering slow-connection and in-app browser edge cases (e.g. Instagram WebView)
- Added website components directory to jest `roots` so PhotoGallery tests are discovered by the test runner; temporarily excluded pre-existing broken CareerPath tests that were never being run

## Test plan
- [x] 16 unit tests covering rendering, lazy loading, dynamicEl mapping, lightbox opening, pending click replay, and empty photos edge case
- [ ] Manual test in desktop browser: click any photo in a gallery → lightbox opens at correct index
- [ ] Manual test in Instagram in-app browser: click any photo on initial page load → lightbox opens without needing to scroll first
- [ ] Verify galleries with many photos work (previously required scrolling to bottom before clicks would register)

🤖 Generated with [Claude Code](https://claude.com/claude-code)
