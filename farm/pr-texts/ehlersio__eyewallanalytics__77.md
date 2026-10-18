# Team vs Team Head-to-Head (Mode 2)

## Summary
- Fills in the Head-to-Head placeholder from Session 86's "vs Team" mode with the real feature: all-time record, recent-window record, current streak, and a thin-sample qualifier — sourced from eyewall-poller's new `/team-seasons/head-to-head` routes (all derived-insight math lives server-side; this component only renders it).
- Opponent selection is now shared between Full Stat Comparison and Head-to-Head — one picker, rendered once by the parent popup, lifted out of `FullStatComparisonPanel`. Switching sub-tabs keeps the same opponent instead of losing the selection.
- The header's "Team A vs Team B" display (Session 86, Option C) now applies to both sub-tabs, not just Full Stat Comparison.
- Depends on eyewall-poller PR #41 (`/team-seasons/head-to-head`, `/pwhl/team-seasons/head-to-head`) — needs that merged/deployed first for real data in production.

## Test plan
- [x] `npm run test` (162/162), `npm run lint` clean
- [x] Cypress: replaced the stale "coming in a follow-up build" placeholder assertion with real coverage in both `team.cy.js` and `pwhl-team.cy.js` — opponent selection carries over across sub-tabs, all-time record renders (or the no-meetings state, whichever the live data supports), and a deterministic zero-meetings check against the PWHL DET expansion team. Full specs pass locally against `wrangler dev --remote` (93/93 and 128/128).
- [x] Manually verified in browser: CAR vs NYR (10-7 all-time, 8-2 last 10, "Carolina Hurricanes has won 2 straight"), Boston Fleet vs Montréal Victoire (9-9 all-time), and PWHL Detroit vs Boston Fleet correctly showing "No meetings on record between these teams yet."
- [ ] Matt: re-verify against production once eyewall-poller#41 is merged/deployed (tested against local `wrangler dev --remote`, not the deployed Worker).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
