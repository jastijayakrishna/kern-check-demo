# fix(history): center timeline via viewport breakout (LAC-3627)

## Summary
- Builder.io wraps registered components in a constrained-width block div. The previous fix (PR #269) used `container mx-auto` which only centered content within Builder's wrapper, not the page — so timeline entries still appeared left-aligned.
- This fix uses the viewport-breakout technique (`width: 100vw` + `margin-left: calc(-50vw + 50%)`) so the section spans the full viewport regardless of Builder's wrapper width, then centers content with `max-w-7xl mx-auto` inside.
- Mobile layout uses `max-w-2xl mx-auto` for comfortable stacked cards.
- Desktop (lg+) alternating timeline line and cards now reference the true page center.

## Test plan
- [ ] Open `/history` on desktop (1024px+) — timeline line should be centered, cards should alternate left/right
- [ ] Open `/history` on mobile — cards should stack full-width with no timeline line
- [ ] Verify no horizontal scrollbar appears (overflow-x-hidden on section)
- [ ] Test in Builder preview mode to ensure visual editor still works

🤖 Generated with [Claude Code](https://claude.com/claude-code)
