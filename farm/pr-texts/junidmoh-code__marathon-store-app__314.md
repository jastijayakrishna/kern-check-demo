# feat(health): Missing Products collapses to two chips — Sneakers and Clothing

Owner directive 2026-08-05: *"remove the rest of the categories and just leave sneakers and clothing which clothing is going to have everything in it."* Supersedes the 2026-08-04 per-subcategory directive (#308).

**Before:** one chip per subcategory (T-Shirts, Jerseys, Bags, Watches, Tracksuits… + Uncategorised + Sneakers).
**After:** exactly two — **Clothing (everything non-sneaker, uncategorised included)** and **Sneakers** (its own MissingFootwear list, unchanged).

- `groupOf` → one Clothing bucket; cards keep their `group`/`groupLabel` shape so `NetworkTransfer`'s `c.group === category` filter works unchanged. HealthView renders chips generically — no change there either.
- `buildChips` → two fixed chips, always rendered even at 0, so the row never reshuffles and `chips[0]` remains a safe fallback.
- A stale persisted per-type selection (e.g. "bags" from #308) falls back to Clothing via the existing `pickActiveTab` rule — pinned by test.
- The taxonomy-ordering machinery is deleted, not dead-coded.

**Tests:** 23 passing in `missingProductsCore.test.js`, rewritten to pin the new contract (a revert to per-type chips fails). Suite: 1086 passing; the 4 files failing to *collect* are the known environmental `.jsx`/react-test-renderer class in worktrees sharing the stale `node_modules` — none touched by this PR.

Review: Sonnet (CodeRabbit rate-limited on this repo; Codex quota-blocked until Sep 2). Client-only; deploy = hosting only per the standing autonomy rule.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_013QsDsqrsUw9dndPi7YTU4M
