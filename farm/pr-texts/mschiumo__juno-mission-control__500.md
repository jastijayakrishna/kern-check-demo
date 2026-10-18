# feat: scroll-driven animations for landing feature sections

## Summary

Implements the scroll-animation handoff for the three landing-page showcase sections — **Equity Curve**, **Gap Scanner**, and **Morning Briefing**. Content, copy, and layout are untouched; this only adds animation.

- CSS scroll-driven reveals (`animation-timeline: view()`) with per-element stagger via `animation-range`; browsers without support play each animation once on load — no invisible-content failure mode
- **Equity Curve**: gridline fade, area grow, line draw, pulsing end-dot ring, staggered stat cells, KPI count-up (IntersectionObserver + setInterval; static text keeps final values for SSR/no-JS)
- **Gap Scanner**: scan-bar sweep, staggered rows, NVDA row ambient flash, alert toast with pop reveal → idle float → glow, bell swing, badge pulse
- **Morning Briefing**: staggered bias banner/tiles/chips/news rows; floating screener card with idle float, LIVE-dot pulse, refresh bar
- `prefers-reduced-motion`: every reveal and loop disabled — fully visible static page
- Fix uncovered during implementation: root wrapper `overflow-x-hidden` (and the showcase cards' `overflow-hidden`) create scroll containers that hijack every `view()` timeline inside them; switched to `overflow: clip`, which clips identically but creates no scroll container

## Test plan

- [x] `tsc --noEmit` and `next build` pass
- [x] Headless Chrome against prod build: all three sections render fully revealed; loop animations (dot ring, toast glow, refresh bar) captured mid-animation
- [x] Forced `prefers-reduced-motion`: complete static page, everything visible
- [ ] Scroll through the Vercel preview on desktop + mobile

🤖 Generated with [Claude Code](https://claude.com/claude-code)
