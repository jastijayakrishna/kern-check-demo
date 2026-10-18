# Team vs Team comparison, Mode 1 (Full Stat Comparison)

## Summary
- New "vs Team" toggle on the Team page's Compare popup (`TeamComparisonPopup.jsx`), alongside the existing "vs Season" mode.
- **Full Stat Comparison** (Mode 1, per `TEAM_VS_TEAM_COMPARISON_BRIEF.md`): pick an opponent team + one season, see box-score stats side by side for both teams. Reuses `TeamCompareSeasonCard`'s existing "row present vs Not yet available" rendering and `SeasonComparisonPicker` (capped at 1 selection) — no new picker logic needed for the season side.
- **Head-to-Head** (Mode 2) is a placeholder ("coming in a follow-up build") — that's genuinely separate, larger work per the brief (league-specific `game_log` query patterns, all-seasons lookback, derived-insight logic). Not scoped into this PR.
- Depends on eyewall-poller PR #40 (`/team-seasons/compare-teams`, `/pwhl/team-seasons/compare-teams`) — needs that merged/deployed first for the new mode to return real data in production.

## Test plan
- [x] `npm run test` (162/162 unit tests pass)
- [x] `npm run lint` clean
- [x] Cypress: added "Compare Teams" coverage to `team.cy.js` (4 NHL teams) and `pwhl-team.cy.js` (4 PWHL teams + DET expansion-team gap case) — opponent-exclusion, two-card render, Head-to-Head placeholder. Full specs pass locally against `wrangler dev --remote` (89/89 and 123/123 respectively).
- [x] Manually verified in browser: CAR vs NYR (2025-26) renders real box scores for both teams; Boston Fleet vs PWHL Detroit (expansion team, no 2025-26 row) correctly shows "Not yet available for this season" instead of erroring.
- [ ] Matt: re-verify against production once eyewall-poller#40 is merged/deployed (this was tested against local `wrangler dev --remote`, not the deployed Worker, since the new routes don't exist there yet).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
