# fix(seo): real 404s for unknown gallery-image, artwork, artist and author slugs (#3376)

Fixes #3376.

## Problem

`/gallery/image/<nonexistent>` returns **HTTP 200** with the Next.js not-found body. Checking the neighbours the issue asked about turned up three more of the same shape. Measured against production:

| URL | status | 404 digest in body |
|---|---|---|
| `/gallery/image/definitely-not-real-9` | **200** | yes |
| `/gallery/collections/definitely-not-real` | **200** | yes |
| `/artwork/definitely-not-real` | **200** | yes |
| `/author/definitely-not-real` | **200** | yes |
| `/book/definitely-not-real` | 404 | — (fixed in #3277) |
| `/collections/definitely-not-real` | 404 | — (fixed in #3277) |

Fresh renders, not cache artefacts (`x-vercel-cache: MISS`).

## Root cause

The mechanism #3277 documented, in four more places: a `loading.tsx` at **or above** a route wraps it in an automatic `<Suspense>`, so Next.js flushes the 200 loading shell as soon as the data fetch suspends — **before** `notFound()` runs. Once the status is committed, `notFound()` can only swap the body.

`/gallery/image/[id]` is the instructive case: its layout has had a correct existence gate since #3049 (`imageResolves` → `notFound()`), and that gate was **silently defeated** by `src/app/gallery/loading.tsx` — three segments up, written for the gallery index grid. A correct check in the right place still fails if any ancestor opens a boundary above it.

## Fix

Delete the seven `loading.tsx` files that sit at or above an existence check. No skeleton is meaningfully lost:

- `/gallery` self-streams through its own inner `<Suspense fallback={<GalleryShell/>}>` — the segment file was redundant for the index and harmful for everything below it
- `/artwork` is `revalidate = false` (fully static)
- `/gallery/collections`, `/artwork/[slug]`, `/artwork/artist/[slug]`, `/author/[name]` are ISR (21600–86400s) and serve prerendered

`src/app/gallery/image/[id]/loading.tsx` is deliberately **kept** — it sits *below* the layout that 404s, so it cannot flush ahead of the gate.

The `/author/[name]` route resolves through the author thesaurus (variant slugs 301 to canonical) *before* its `notFound()`; that logic has to stay in the page, which is why the fix here is removal rather than a layout-level gate.

## Guard

`tests/unit/soft-404-loading-guard.test.ts` (added by #3277) is extended from 3 to 10 pinned absences, each with a comment saying what it protects. Re-adding any of these files silently reintroduces the soft-404.

## Verification

`npx tsc --noEmit` clean; guard test 10/10. Curl matrix against the preview once it builds — each of the four must return **404** with no `NEXT_HTTP_ERROR_FALLBACK;404` needed to detect it, and a real image / artwork / author / gallery collection must still return 200 and render.

## Out of scope

- The reader soft-404 (`/book/<slug>/page/<pageId>` with a real-but-missing page id) — still open from #3232's follow-up note. Numeric page numbers are already caught in `proxy.ts`.
- Backfilling `not_found_reports` for URLs that never 404'd.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
