# fix: remove thumbnail image from public link previews

## Summary
Follow-up to #129 — the WhatsApp preview is now working correctly (title, description, link all render), but the branded AFJ CAS icon shows as a large thumbnail in the card. Removing `openGraph.images`/`twitter.images` from both public pages' metadata so the preview is text-only.

## Test plan
- `npm test` — 286 tests pass (unchanged).
- `npx tsc --noEmit` — clean.
- `npm run lint` — 0 errors.
- `npm run build` — succeeds.
- Verified via `curl` of the built HTML for both `/public/week1-campaigns` and `/public/temporary-upcoming-campaigns`: `og:image`/`twitter:image` are gone; `title`, `og:title`, `og:description`, `og:url`, `og:type`, `twitter:card`, `twitter:title`, `twitter:description` all still present.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
