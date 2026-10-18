# fix(sanitize): enforce allowlist on SSR via serverless-safe sanitize-html (LAC-3638)

## Summary
Second attempt at [LAC-3638]. The first fix (#277, `isomorphic-dompurify`) enforced the allowlist correctly but its jsdom backend **crashed Vercel serverless functions** — /about, /privacy, /accessibility returned 500 on prod (~7 min outage) and it was reverted in #279.

This version:
- **Client**: DOMPurify, unchanged.
- **Server/SSR**: the pure-JS [`sanitize-html`](https://www.npmjs.com/package/sanitize-html) package (htmlparser2-based, no DOM, serverless-safe) with a mirrored allowlist and DOMPurify-equivalent scheme rules (`data:` URIs allowed only on `<img>`). `require()`d inside the `typeof window === "undefined"` branch so client bundles never include it.
- The regex-only SSR branch (the vulnerability) is gone.

## Parity between environments
The shared 18-case spec `tests/shared/sanitize-html-spec.ts` runs under BOTH vitest configs — `tests/node` (SSR path, which is what visitors get after hydration) and `tests/unit` (jsdom/client). Covers every bypass vector from the issue: `<iframe>`, `<form>/<input>`, `<object>/<embed>`, `<style>`, `<base>`, `<meta http-equiv=refresh>`, entity-encoded `&#106;avascript:` URIs — plus the secondary corruption bug (legit `data:` image URIs and prose containing "data:" are preserved now). The one permitted divergence is void-tag serialization (`<img ... />` vs `<img ...>`), which browsers parse identically.

## Testing
- 36/36 tests pass (18 node + 18 jsdom)
- `bun run typecheck` clean
- `bun run build` passes
- **`next start` locally: /about, /privacy, /accessibility all 200 with rich-text bodies rendered**
- Before merge I will curl those three routes on the actual Vercel preview deployment — the step that would have caught #277.

Paperclip: LAC-3638

🤖 Generated with [Claude Code](https://claude.com/claude-code)
