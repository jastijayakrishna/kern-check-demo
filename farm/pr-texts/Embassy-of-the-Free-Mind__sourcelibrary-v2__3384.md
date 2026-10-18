# fix(seo): real 404 for unknown reader page ids (#3376 follow-up)

Closes the soft-404 family opened by #3232 and continued in #3376. Follow-up to #3381.

## The last one

Measured on production today:

```
/book/platonis-opera-plato/page/definitely-not-a-real-page-id   200
/book/platonis-opera-plato/page/abc123def456abc123def456        200
/book/curious-physics-hellwig/page/zzzzzzzz                     200
```

All three serve the "Page Not Found" body with the `NEXT_HTTP_ERROR_FALLBACK;404` digest baked in. Purely **numeric** page numbers are already caught by `proxy.ts` and 302 — this is the non-numeric id case that slips past it, and it's the one CLAUDE.md warns about under quote-and-link validation (*"`curl -w '%{http_code}'` returns 200 for these soft-404s"*).

## The fix is deliberately NOT the sibling fix

Same mechanism as #3277 / #3376 — `loading.tsx` wraps `page.tsx` in an automatic `<Suspense>`, the 200 shell flushes when the data fetch suspends, and `notFound()` arrives after the status is committed.

But #3277 **deliberately left this segment's `loading.tsx` alone**, and that was the right call: the reader is the one route where the skeleton earns its keep, because it shows on *every page turn*. Deleting it would trade a status code for a visible regression on the highest-traffic URL set in the site.

So instead the existence check moves **up into the segment's own `layout.tsx`**, which renders above the boundary `loading.tsx` creates.

The layout already had `getPageData()` for `generateMetadata`, and already **knew** about this case — it returns `title: 'Page Not Found - Source Library'` for it. It just never acted on it. Now it does, and the lookup is wrapped in `cache()` so the gate costs no extra query.

## Why this can't over-404

The layout's condition is a strict **subset** of `page.tsx`'s four `notFound()` cases:

| case | page.tsx | layout (this PR) |
|---|---|---|
| page id doesn't exist | 404 | 404 |
| book id/slug doesn't resolve | 404 | 404 |
| page.book_id ≠ book in URL | 404 | 404 (inside `getPageData`) |
| **book is hidden** | 404 (unless `allowHidden`) | **not checked — deliberate** |

The hidden-book gate stays in `page.tsx` alone. `findBookByIdOrSlug` does not filter on visibility, so the editor preview route (`page/[pageId]/preview`, which passes `allowHidden`) still renders hidden books through this same layout exactly as before. Gating on visibility here would have broken it.

No ISR concern: this route already reads `headers()` via `getTenantContext()` and is dynamic.

## Guard

The existing `tests/unit/soft-404-loading-guard.test.ts` gains a second `describe` block, because *"the loading.tsx is absent"* — the assertion shape used for every other route — **cannot express this fix**. The new block pins the opposite: the `loading.tsx` is still **present** (the skeleton is load-bearing), the layout calls `notFound()`, the lookup is `cache()`d, and the layout does **not** reference `isHiddenBook`.

722 unit tests pass; `npx tsc --noEmit` clean.

## Verification

Curl matrix against the preview once it builds — the three ids above must return **404**, and a real page (`/book/<slug>/page/<real-id>`) must still 200 and render with its skeleton intact. Status and body checked together, since status alone was 200 for all of these before.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
