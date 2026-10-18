# Reflow PWHL player card header to match NHL's layout

## Summary
- Item 1 of `PWHL_HEADER_AND_SHOTMAP_TEAMNAME_BRIEF.md` — Option A (match NHL's structure), confirmed via mockup before building.
- Top row: photo/name/number/position on the left, a 2x2 percentile-tile grid on the right in the radar chart's slot — substitutes for NHL's radar since PWHL only computes 4 percentile categories today (`pwhl_percentiles.py`), no radar-worthy stat set to plot.
- Full-width 6-column bio row underneath (Height/Weight/Shoots/Age/Birthdate/Hometown), reusing NHL PlayerPopup's exact `.pp-bio-row`/`.pp-header-radar`/`.pp-quickstats` CSS (already shared via `PlayersView.css`) — no new styles written.
- Height now renders from the `height_inches` column added in eyewall-pipeline#59 — shows `—` until the nightly backfill reaches a given player. Weight always shows `—`; HockeyTech has no real PWHL weight data.
- Scoped to skaters with percentile data (`showHeaderReflow`), matching NHL's own condition — goalies and the pre-percentiles loading flash keep the original single-block header.

## Test plan
- [x] `npx eslint` clean
- [x] Unit tests pass (162/162)
- [x] Verified live in browser (Taylor Heise, MIN): percentile tiles show correct values (91/96/46/38, matching the Stats tab's own percentile numbers), bio row renders all 6 fields with correct grid layout (confirmed via computed styles — 2-col tile grid, 6-col bio row), no console errors
- [ ] Height field will read real values once the manual nightly pipeline run (in progress) finishes backfilling `height_inches`

🤖 Generated with [Claude Code](https://claude.com/claude-code)
