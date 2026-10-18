# Portfolio status clarity, markets grid fix & application-only Live Activity

Batch of UX fixes from user feedback on the portfolio and markets pages.

## Changes

### `fix(portfolio)` — clarify open-position status + drop Entry column
- Open Positions showed **Expires: Closed** next to **Status: ACTIVE**, which read as a contradiction ("why is it closed but still active?"). A bet past expiry isn't tradeable — it's awaiting on-chain settlement. Status is now derived: **Active** (green) before expiry, **Settling** (gold) after, ticking in step with the countdown so both columns flip together.
- Removed the per-contract **Entry** column — it sat beside **Cost** and only muddied the read.

### `fix(markets)` — keep grid populated under narrow expiry filters
- Filtering to a narrow expiry like "Today 10:00" absorbed the entire matched set into the featured hero, leaving the "All markets" grid empty (looked like "nothing loaded"). When the filtered set fits entirely in the hero, the grid now shows the full list; the hero just highlights the top few above it.

### `feat(markets)` — Live Activity feed from Polynuts fills
- The Live Activity panel read the in-memory on-chain log poller, which sits empty on free-tier RPC ("No activity yet"). It now reads the persisted `trades` table (`useRecentTradesDb`) — **application fills only**, the same source the leaderboard uses — and each row is redesigned with a direction-colored accent, market label, PUMP/DUMP/RANGE tag + time-ago, bet size, and a live pulse in the header.

## Notes
- Trade-off: a user's own just-placed bet now appears within the ~30s DB refetch window rather than instantly (the old in-memory feed prepended it immediately). The panel is reliable now instead of usually-empty; happy to add an optimistic prepend on top if instant self-trade feedback is wanted.

## Testing
- `npx tsc --noEmit` clean. ESLint clean on touched files (one pre-existing `setPage`-in-effect warning, unrelated).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Added live position status updates that reflect market expiry changes in real-time
  * Introduced ETH and BTC price tickers in the sidebar
  * Enhanced sidebar with live activity feed displaying recent trades

* **Improvements**
  * Markets grid now remains populated when viewing narrow filter results
  * Simplified portfolio positions table layout by removing the Entry column

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
