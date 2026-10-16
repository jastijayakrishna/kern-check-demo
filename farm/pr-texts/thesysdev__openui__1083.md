# feat(devtools): tag outbound CTA links with UTM params

## What

Devtools CTAs (`Purchase Credits`, `Add your own key`, reliability banner `Learn more`) pointed at bare URLs, so clicks from the devtools panel were indistinguishable from other referrals. This tags them, mirroring the docs-site helper (`docs/lib/thesys-link-attribution.ts`).

## Changes

- New `withDevtoolsAttribution(href, content)` in `packages/devtools/src/lib/links.ts`: sets `utm_source=openui`, `utm_medium=referral`, `utm_campaign=openui_devtools`, plus a per-CTA `utm_content`; never overwrites params already on the URL and returns the input unchanged if it doesn't parse.
- `QuotaErrorRow` billing/BYOK buttons use it (`utm_content=quota_error_purchase_credits` / `quota_error_byok`).
- `ReliabilityBanner` link uses it (`utm_content=reliability_banner_learn_more`).
- Bumped `@openuidev/devtools` to `0.1.1` so this can ship via the "Publish NPM packages" workflow. Apps auto-mounting through react-lang pin jsDelivr `@0`, so they pick it up with no consumer change.

## Test Plan

- [x] Verified locally

`pnpm --filter @openuidev/devtools lint:check`, `format:check`, and `test` (30 passed). `typecheck` fails on `src/OpenUIDevtoolsWidget.tsx(364,30): Cannot find name 'DevtoolsPosition'` — reproduced on `main` with these changes stashed, so it is preexisting and untouched here.

## Checklist

- [ ] I linked a related issue, if applicable
- [ ] I updated docs/README when needed
- [x] I considered backwards compatibility


Link to Devin session: https://app.devin.ai/sessions/e3f8abfb369d491ebb4d64db43e17f51
Requested by: @zahlekhan
