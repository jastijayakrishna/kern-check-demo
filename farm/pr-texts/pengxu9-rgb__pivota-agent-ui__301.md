# feat(promotions): /ops/promotions becomes a self-contained Partner Preview demo (ADR-022)

## Summary

Per ADR-022 (pengxu9-rgb/pivota-backend#1733), the production promotions lane is deleted across all five repos — and this page is the one surface that survives, converted into the **partner-facing demo** of the target design. "Isolate" here means **severed, not preserved**: the demo depends on nothing.

## What changed

- **`src/app/api/promotions/*` proxy routes deleted.** The page and form now write to `src/lib/promotionsDemoStore.ts` — localStorage-backed, seeded with obviously-demo merchants ("demo_merchant_lumine") and three storyboard deals. Zero network writes; every visitor gets their own sandbox; **Reset demo** restores the seed.
- **Badged honestly**: "Partner Preview — demo data", with header copy naming the ADR-022 design: merchant authors an AI-channel-exclusive deal → Pivota materializes it as a Shopify discount code → the agent presents the code at checkout → Shopify, the checkout authority, enforces it.
- **New "See it apply at checkout" panel** — the piece the real pipeline could never honestly show. Pick a demo product and quantity; the best active deal applies, the strikethrough price and agent code render, and a numbered narrative walks the enforcement chain. Editing or creating deals in the console updates the simulation live — that's the pitch moment.
- **FLASH_SALE returns** in the demo type list. In production it was a type with no producer and no enforcement (deleted); in a sandbox it's the most compelling storyboard, and nothing here claims to be real.

## Why a mock rather than the kept pipeline

The live lane couldn't demo the vision: creation 404ed in remote mode, the quote engine skipped everything but MULTI_BUY, and checkout enforcement was lane-conditional. A labeled sandbox can show the full loop *as designed* — and per the fabrication-belt discipline, fakes belong in labeled sandboxes, never in live paths. This page doubles as the product spec for the rebuild; a partner commitment is the build trigger (ADR-022).

## Verification

`tsc --noEmit` clean · `next build` green — `/ops/promotions` emitted (9.93 kB), no `/api/promotions` routes.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
