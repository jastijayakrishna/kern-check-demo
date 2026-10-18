# feat(seo): 308-redirect removed post/section URLs to home instead of 404

## Why

When a phantom site is re-strategized, old posts/sections are removed from its collection and their URLs start returning **404** — but Google keeps them indexed for weeks. Real search traffic lands on dead pages and the URL's crawl equity is wasted. (Live example: themcpreport.com had ~450 impressions/28d on 10 removed marketing URLs, all 404ing.)

## What

`/posts/[slug]` and `/sections/[slug]` were fully static (`force-static` + `dynamicParams=false`), so any unknown slug served a static 404.

Switch to `dynamicParams=true` and replace `notFound()` with `permanentRedirect("/")`:
- Posts/sections that exist at build time stay **prerendered and fully static** (unchanged).
- Any *other* slug is rendered on-demand only long enough to **308-redirect to the homepage**, recovering equity and killing the dead link.

One change, no coupling to delphi, covers the whole fleet automatically.

## Companion PR
Prevention + a Search Console sitemap-status column live in the **delphi** repo: letterstory/Letterbrace#591.

## Validation
`tsc --noEmit` clean · `eslint` clean.

## Deploy note
Ships fleet-wide (touches every phantom's post/section rendering). Before promoting, verify on a staging site that a removed `/posts/<slug>` returns **308 → /** and that an existing post still renders 200 statically.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
