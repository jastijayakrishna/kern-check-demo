# feat: one global ticker search for the whole Watchlist column

## Summary
Follow-up to #541 — that PR removed the Daily Favorites panel search, but the redundant pair MJ actually meant was the **Active Trades** search + the **Potential Trades** search (which sits directly above the Favorites subsection). This PR finishes the job so the tab has exactly **one** ticker search:

- Replace the three per-section search inputs (Active Trades, Potential Trades, Closed Positions) with a single search bar at the top of the Watchlist column, directly above Active Trades.
- One query filters every section at once: Active Trades, Potential Trades (Favorites + Other), and Closed Positions.
- While searching, collapsed sections that contain matches auto-expand, and the first matching card is smooth-scrolled into view.
- The Long/Short side pills on Potential Trades are unchanged; Select All keeps operating over the visible (filtered) list.

## Verification
- `tsc --noEmit` and `next build` pass.
- Exercised against a prod build with mocked data: searching a watchlist-only ticker filters all sections and scrolls to its card; a closed-positions-only ticker scrolls to the closed row; collapsed sections with matches auto-expand while no-match sections stay collapsed; clearing the query restores everything.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
