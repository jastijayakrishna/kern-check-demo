# Basket-targeted in-cart upsell

Part 3 of the targeting work — the **active lever** (highest AOV payoff).

Adds a **"Goes well with your order"** rail on the cart (filled state), targeted by the basket:
- Drinks-only cart → suggests a **bite** (and vice-versa) — the core attach play.
- New focused `/api/suggest-pairs`: **complement + co-purchase (`get_co_purchased_products`) + untried-by-member + price**, top 3 across distinct categories.
- Reuses `getMenuData` (pickup menu, cart-ready) + the member-history signal from the home personalizer. **Doesn't touch the live POS suggest-pairs engine** (self-contained, low-risk).
- Reactive to cart changes; cards link to the product page (one-tap add). Renders nothing until it has a suggestion.

Completes the 3-part plan: tighten (#406) → personalize (#407) → in-cart upsell (this).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
