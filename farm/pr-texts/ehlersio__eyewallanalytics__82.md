# Add H2H AI narrative card; fix Compare popup edge-padding

## Summary
Two independent pieces bundled per the brief:

**1. Head-to-Head AI narrative (depends on [eyewall-poller#42](https://github.com/ehlersio/eyewall-poller/pull/42))**
- `HeadToHeadNarrativeCard` renders below the head-to-head scoreboard in the vs-Team Compare popup, auto-generating on mount via the poller's new `/team-seasons/head-to-head/narrative` routes.
- Same UX pattern as `PeriodSummary.jsx`'s game/period narratives: loading-dot state, "⚡ EyeWall AI" label, self-hides (renders nothing) on failure instead of showing a broken card.
- Posts only the derived-insight fields (record/window/streak/isThinSample), not the full `games` array.
- **Won't show anything until eyewall-poller#42 is merged and deployed** — verified locally that it fails gracefully (hides itself) against the current production Worker, which doesn't have the route yet.

**2. Compare popup padding fix**
- The "Full Stat Comparison"/"Head-to-Head" button row and the head-to-head scoreboard card were touching the popup's left/right edges.
- Root cause: `.pp-body` deliberately has no horizontal padding of its own — every other top-level block inside it supplies its own 16px inset (`.stat-section-header`/`.stat-section-body`/`.stat-section-peers` all do this so full-width dividers can still span edge to edge). These two Session 88 elements were added without that inset.
- Fixed with the same 16px margin convention, applied to the new narrative card too so it doesn't ship with the identical bug.
- Verified via computed styles in-browser: both elements now sit flush with their siblings' 16px inset.

## Test plan
- [x] `npx eslint` — clean
- [x] Unit tests (via pre-commit hook) — 162/162 passing
- [x] Targeted Cypress specs (`team.cy.js`, `pwhl-team.cy.js`) — 221/221 passing, no regressions
- [x] Manual verification in-browser: opponent picker → Head-to-Head tab, confirmed button row + scoreboard now have 16px inset from popup edges via computed `getBoundingClientRect()`
- [ ] Once eyewall-poller#42 is deployed, spot-check the narrative card renders real text for a real team pair

🤖 Generated with [Claude Code](https://claude.com/claude-code)
