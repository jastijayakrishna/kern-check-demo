# Personalize home carousel by member

Part 2 of the targeting work. When the customer is signed in, the home carousel re-fetches a **personalized** set after mount (`/api/home-posters?member=<loyaltyId>`) and swaps it in:

- Ranks high-AOV items the member **hasn't tried** ahead of their usual (discovery → trial → AOV), within the day-part window + drink balance.
- Uses `orders.loyalty_id → order_items.product_id` (last ~100 orders), best-effort.
- Guests / errors fall back silently to the server-rendered tight set, so the fast cached home render is untouched (no perf regression, brief swap on first paint only).

Shared `selectHomePosters({ memberId })` powers it, so web + native stay in sync.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
