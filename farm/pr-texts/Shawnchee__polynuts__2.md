# Portfolio PnL correctness, trade-history clarity, and feedback widget

Batch of independent fixes/features, each landed as its own commit (split by logical unit; data-layer kept separate from UI).

## Data layer
- **fix(sync): match settlements via normalized `tradeKey`** — DB stores `0x`-prefixed/lowercased keys; the indexer returns bare/checksummed. The raw compare never matched, so settlements were never written and every settled trade stayed stuck on "FILLED" with no realized PnL. Adds a canonical `tradeKey()` + regression test (`tradeKey.test.ts`).
- **fix(positions): derive cost basis from indexer premium, not mmPrice** — `p.entryPrice` is the mmPrice (~0.005), which understated dollar cost by orders of magnitude and inflated PnL/ROI. New `premiumPaidUsd()` reads the indexer's authoritative `pnlEntries[].costUsd` (NaN → "—"). The leaderboard cron's recovery path stops synthesizing a bogus cost (records `side=null, notional=0, entry_price=null`).
- **fix(markets): only surface assets with a live price feed (ETH/BTC)** — markets we can't price/mark/settle (DOGE, XRP, SOL, …) are dropped in `buildMarketView`.
- **refactor(feed): drop redundant 30s orders invalidation** — `useOrders` already polls; the duplicate timer made the grid reshuffle up to twice per window.

## UI layer
- **feat(portfolio): readable trade-history statuses** — collapse raw FILL/SETTLE/EXERCISE/OPEN/FILLED into OPEN / WON / LOST / SETTLED / PENDING / CANCELLED; drop the unreliable Entry column.
- **refactor(portfolio): use `Countdown` for open-position expiry** — consistent live ticking.
- **fix(trade): portal confirm modal to `<body>`** — `animate-fade-in`'s lingering transform trapped `position: fixed`, rendering the modal off-screen on mobile (Bet looked dead).
- **feat(feedback): floating write-only feedback widget** — anon INSERT into `public.feedback` (no public SELECT); `0002_feedback.sql` migration is **already applied** to the project.

## Verification
- `tsc --noEmit` clean
- `vitest run` — 110/110 pass (incl. new `tradeKey` regression test)
- `eslint` — 0 errors

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Added in-app feedback widget for user submissions.

* **Bug Fixes**
  * Improved trade settlement matching and recovery accuracy.
  * Fixed activity feed deduplication and polling logic.
  * Restricted market display to supported underlying assets.

* **UI Improvements**
  * Replaced timer badge with countdown display in portfolio positions.
  * Redesigned trade history table with live/realized PnL status indicators (WON, LOST, SETTLED, CANCELLED, PENDING).

* **Tests**
  * Added regression test suite for trade key normalization.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
