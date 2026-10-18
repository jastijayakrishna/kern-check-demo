# fix(cache): bot-aware edge cache key + lower default fold threshold

## Summary

Two fixes for HTML bloat / slow SSR reported on miess-tanstack and bagaggio-tanstack:

### 1. Bot cache contamination (P0)

Bots render all sections eagerly (`shouldDeferSection` returns false for `isBotReq`), producing ~10x larger HTML. The edge cache key (`buildCacheKey`) had **no bot dimension**, so a Lighthouse/PageSpeed/crawler request poisoned the shared entry — real users then received the huge all-eager payload as `x-cache: HIT`.

**Critical detail:** two divergent `isBot` regexes existed — `resolve.ts` (matches `lighthouse|semrush|ahrefs`) vs `requestContext.ts BOT_RE` (does NOT). PageSpeed/Lighthouse rendered all-eager but was classified "human" in the cache key → contamination.

**Fix:** export the single `isBot` from `resolve.ts` (the same predicate that gates deferral) and add `__bot=1` to `buildCacheKey`. Bots get a separate cache bucket. Purge handler updated to clear both variants.

### 2. Default fold threshold (P1)

`foldThreshold` defaulted to `Infinity` — only CMS Lazy-wrapped sections deferred. Changed to `DEFAULT_FOLD_THRESHOLD = 3` so below-the-fold sections defer by default, dropping their resolved props from the `$_TSR` hydration blob. Above-fold content stays eager for LCP/SEO. Bots still get fully eager pages. Sites can override via `setAsyncRenderingConfig({ foldThreshold })`.

## Evidence (measured with curl)

| Site | Human UA | Bot/Lighthouse UA |
|------|----------|-------------------|
| miess `/` | 190 KB, 27 scripts, 0.17s | **1.89 MB, 168 scripts, 2.8s TTFB** |
| bagaggio `/` | 1.48 MB (87% = one `$_TSR` script), 1.15s | **2.89 MB** |

## Test plan

- [x] `tsc --noEmit` (typecheck) — passes
- [x] `tsc` (build) — passes
- [x] `vitest run` — 771/771 tests pass
- [ ] After deploy: `curl -A "Lighthouse"` vs `curl -A "Chrome"` on same URL → different `__bot` bucket, different HTML sizes
- [ ] Verify `x-cache: HIT` works for both UA types independently
- [ ] Verify LCP/CLS unchanged on sites after foldThreshold=3

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated description by cubic. -->
---
## Summary by cubic
Separates bot traffic in the edge cache and reduces HTML size by deferring below‑the‑fold sections by default for faster SSR.

- **Bug Fixes**
  - Bot-aware cache key: export a single `isBot` from `resolve.ts` and add `__bot=1` to the edge cache key so bots use a separate bucket; purge now clears both human and bot variants.
  - Deferral defaults: set `foldThreshold` to 3 and always init async config so the threshold applies even with no `eager` sections; the threshold overrides `eager` (below-the-fold sections defer) while layout stays always eager; add `neverDefer` (`export const neverDefer = true`) to keep critical sections eager regardless of the threshold; bots still render everything eagerly. Sites can override via `setAsyncRenderingConfig({ foldThreshold })`.

<sup>Written for commit 1c76f79799621c10f3ab8016fdb1521e174f4885. Summary will update on new commits.</sup>

<a href="https://cubic.dev/pr/decocms/deco-start/pull/262?utm_source=github" target="_blank" rel="noopener noreferrer" data-no-image-dialog="true"><picture><source media="(prefers-color-scheme: dark)" srcset="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://www.cubic.dev/buttons/review-in-cubic-light.svg"><img alt="Review in cubic" src="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"></picture></a>

<!-- End of auto-generated description by cubic. -->


