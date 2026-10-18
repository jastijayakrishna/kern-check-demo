# landing: restore rebrand + vector NEAR Auth logo (black NEAR) + docs.auth.near.org

## Summary

Restores the landing rebrand from #96 (reverted in #99 while chasing an *unrelated* Helm deploy failure) and layers the requested brand updates on top. All commits authored cleanly by `vriveraPeersyst`.

## Changes

- **Restore landing rebrand** — reapplies the NEARauth / social-login / SEO work from #96 that #99 reverted. That revert was collateral from a stuck Helm release, not a problem with this code.
- **New logo (vector, "NEAR" in black)** — the lockup is now a crisp `<NearAuthLogo>` component: green NEAR "N" mark + **"NEAR" in ink-black** + "Auth" in NEAR green, per the design system (`preview/10_logo.html`). Fixes the previous raster whose baked-in white "NEAR" was invisible on the cream canvas. The square mark (favicon + phone icon) is unchanged.
- **Brand → "NEAR Auth"** — all user-facing copy, metadata, JSON-LD, and `lib/faq.ts` now read "NEAR Auth" (matches the live docs). `Fast Auth Status` → `NEAR Auth Status`.
- **Docs links → docs.auth.near.org** — repointed every documentation link to the new site with mapped paths: base `/`, `submit-your-application` → `/home/apply`, `select-your-sdk` → `/home/guides/choose-your-sdk`, `custom_issuer_service` → `/protocol/advanced/custom-issuer`.

## Intentionally preserved

These still say `fast-auth` on purpose — renaming them breaks real things: npm packages `@fast-auth-near/*`, the `FastAuthProvider`/`useFastAuth` API in code samples, the `fast-auth.near` / `jwt.fast-auth.near` contract ids, `FASTAUTH_*` env vars, the GitHub repo URL, the Halborn audit PDF, and the OG image filename.

## Not in this PR

The `fast-auth-spa` (`examples/spa`) Vercel build failure is a **separate** issue, unrelated to the landing: `browser-sdk`'s tsup DTS bundling emits a dangling `./provider` reference and drops the `@shared/core` re-exports (so `SignatureRequest` isn't exported). Tracked/fixed separately.

## Verification

- `tsc --noEmit` ✅ · `next build` ✅ (6/6 static pages)
- Logo + brand confirmed rendering on `/` and `/status`

🤖 Generated with [Claude Code](https://claude.com/claude-code)

