# fix(sanitize): enforce DOMPurify allowlist on SSR via isomorphic-dompurify (LAC-3638)

## Summary

Fixes [LAC-3638](https://paperclip.local/LAC/issues/LAC-3638) (follow-up from the LAC-3559 Builder rich-text audit).

`sanitizeHtml`'s `typeof window === "undefined"` branch was regex-only: it stripped `<script>`, `on*=` attributes, and literal `javascript:/data:/vbscript:` strings, but never enforced the `ALLOWED_TAGS`/`ALLOWED_ATTRS` allowlist. React does not re-apply `dangerouslySetInnerHTML` on hydration, so this weak SSR output is exactly what visitors receive — on pure server components (`meeting-detail-body`, the about/privacy/accessibility static pages) DOMPurify **never** ran at all.

Vectors that survived the old SSR branch: `<iframe>`, `<form>`, `<object>`/`<embed>`, `<style>`, `<base>`, `<meta http-equiv=refresh>`, and entity-encoded scheme URIs (`&#106;avascript:`). The blanket `/(?:javascript|data|vbscript):/gi` replace also corrupted legitimate content (`data:` image URIs, prose containing "data:").

## Changes

- `src/lib/sanitize-html.ts` — import `isomorphic-dompurify` (jsdom-backed on the server) and delete the regex branch; the exact same DOMPurify allowlist now runs in both environments. Direct `dompurify` usage in client-only components is untouched.
- `next.config.ts` — `serverExternalPackages: ["isomorphic-dompurify"]`; jsdom can't be webpack-bundled (ESM-only transitive deps), verified by a failing → passing local `bun run build`.
- `tests/shared/sanitize-html-spec.ts` + `tests/node/sanitize-html.test.ts` + `tests/unit/lib/sanitize-html.test.ts` — one shared regression suite run under **both** vitest environments (node = SSR path, jsdom = client path), covering every bypass vector above plus the data:-URI/prose corruption bug, allowlist preservation, and `stripLinks`.

## Acceptance criteria

- [x] Same allowlist applies server- and client-side (isomorphic sanitizer; regex branch removed)
- [x] Regression tests for all listed bypass vectors — 10/18 fail against the old implementation, 18/18 pass now, in both environments
- [x] Secondary bug fixed: `data:` image URIs and "data:" prose no longer corrupted (DOMPurify permits data: URIs on `img` by default)

## Testing

- `bunx vitest run --config=vitest.config.node.ts` — 84 passed, 1 pre-existing failure (`hero-carousel`, fails on pristine main too; noted on LAC-3636)
- `bunx vitest run` (jsdom) — 198 passed; the 6 failing files are pre-existing on pristine main (verified via stash), all unrelated template tests
- `bun run typecheck` — clean
- `bun run build` — passes (this is what catches the jsdom bundling issue; CI does not run the build)

🤖 Generated with [Claude Code](https://claude.com/claude-code)
