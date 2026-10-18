# feat(landing): add schema.org JSON-LD structured data (#1643)

## What

Adds schema.org JSON-LD structured data to the landing site, the biggest
remaining SEO item after the #1641 baseline (which shipped OG/Twitter, canonical,
sitemap, and deliberately left structured data out).

Closes #1643.

## Scope

- **Site-wide (root route):** `Organization` + `WebSite` — the latter with a
  `SearchAction` targeting `/search-results` for a Google sitelinks search box.
- **Public service pages (`$.tsx`):** `GovernmentService` (name/description from
  frontmatter, `provider` = the Organization, `areaServed` = Barbados) +
  `BreadcrumbList` (Home → Category → Subcategory → Page).
- **Gated (preview/draft) pages emit nothing** — reuses the existing `isPublic`
  gate that already suppresses canonical/OG, so noindex pages stay clean.

## How

- New pure, unit-tested builder module `src/lib/structured-data.ts`
  (`buildOrganizationLd`, `buildWebSiteLd`, `buildGovernmentServiceLd`,
  `buildBreadcrumbLd`) — same pattern as `seoTags`/`buildSitemapXml`.
- Injected via TanStack `head()` `scripts` (`type: application/ld+json` with
  inline `children`), the mechanism the issue pointed at.
- Absolute URLs from `SITE_URL`; logo = `/images/coat-of-arms.png` (real served
  asset). Organization carries a stable `@id` that `WebSite`/`GovernmentService`
  reference so the entity isn't repeated.
- Breadcrumb titles reuse the same registry lookups the visible `<Breadcrumbs>`
  component uses.

## Notes / out of scope

- `sameAs` (official social profiles) omitted — no confirmed URLs; easy follow-up.
- `FAQPage` schema and dynamic OG images are out of scope per the issue.

## Verify

- `pnpm exec nx run landing:test` — 217 passed (6 new builder tests)
- Reviewer: validate the rendered service page + homepage against Google's Rich
  Results Test and the schema.org validator on the PR preview (needs rendered
  output; can't run offline).

## Acceptance criteria

- [x] `Organization` + `WebSite` JSON-LD on every public page
- [x] `GovernmentService` + `BreadcrumbList` on public service pages; absent on gated
- [ ] Passes Google Rich Results Test (verify on preview)
- [x] Unit tests for the builder functions

🤖 Generated with [Claude Code](https://claude.com/claude-code)
