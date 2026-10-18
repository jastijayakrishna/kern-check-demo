# feat(seo): server-render the /products browse grid

## Why

`/products` was client-only, so the prerendered HTML — the bytes every crawler and no-JS agent reads — said **"The browse feed is empty right now"** to every user-agent, while the sitemap advertises the URL at **priority 0.9** and `robots.ts` explicitly allows GPTBot/ClaudeBot/Google-Extended onto it. The catalog therefore had **zero crawlable internal links**: PDP discovery was 100% sitemap-dependent and no link equity flowed. (Audit finding #1, 2026-08-08.)

## What

`page.tsx` is now an async RSC that fetches the feed and hands it to the extracted `ProductsPageClient`. Verified on a real build: **24 clean canonical `<a href="/products/sig_*">` links, no `?return=`, no self-links, no empty-state copy.**

Mechanics mirror the PDP server fetch — post to this deployment's own `/api/gateway` (the proxy injects the upstream key; direct upstream 401s), wrapped in `unstable_cache` since the call is a POST and Next's Data Cache only caches GET.

## Failure handling (review corrected this twice)

- **Throws instead of returning `[]`.** Returning `[]` rendered a 200 empty grid that Next stored as the route's ISR entry — pinning the defect for a full window and replacing a healthy page on every failed revalidation. Throwing is the PDP's `PDP_DEGRADED_RENDER_ERROR` contract: Next keeps the last good render.
- **Retries on throw, not just on empty.** The feed cold-fills *and* is slow enough to be flaky — 6.7s and 10.3s measured against a 12s budget. The first cut retried only on empty, so the dominant failure got none.
- **The build phase never fetches.** A Vercel build can't serve its own requests and `VERCEL_URL` points at the not-yet-live deployment (401 behind Deployment Protection on previews). The build now ships the client-only shell deliberately; the first revalidation on a live server fills the grid, and `revalidate = 300` keeps that window ~5 min. `resolveServerBaseUrl` prefers the stable public origin over `VERCEL_URL`.
- **`maxDuration = 30`** pinned — budget is 2×12s and an ISR fill killed mid-render is a 504.

## Bonus fix

A 24-attribute hydration mismatch this exposed: `CatalogProductCard` computed `?return=` inline, which is a no-op server-side, so every href differed between server HTML and first client render — and since React doesn't patch attribute mismatches, the param was silently lost anyway. Now applied post-mount: first render matches the server, and the return link actually works again.

## Tests

921 pass. New `serverGridHtml.test.tsx` asserts the **real** card's `renderToStaticMarkup` output — the sibling client test mocks the card away, so it could prove a title renders but never that an `<a href>` exists at all, which is the entire point of this change.

## Known follow-ups (documented, not dropped)

Grid inherits framer-motion's inline `opacity:0` initial (fine for raw-HTML crawlers, blank for a CSS-applying/JS-disabled reader); no ItemList JSON-LD or `rel=canonical` on the listing; server render discards `cursor_info`, so no-JS readers get the first 24 with no next-page link.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
