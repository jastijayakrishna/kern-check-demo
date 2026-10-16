# Update OpenUI logo mark

## What

Swaps the OpenUI mascot mark for the updated logo, uses the new mark + wordmark lockup in the site header, and applies a few related brand tweaks to the site. SVGs are copied byte-for-byte from the source export (no optimisation or re-encoding).

## Changes

- `docs/public/openui-logo-wordmark.svg` (new) → mark + wordmark lockup, rendered by `OpenUILogo` in the site header in place of the mascot + live "OpenUI" text
- `docs/public/shiro-logo.svg` → new mark; it is now the single mark file for the docs site (nav, favicon/apple icon, OG cards, OpenUI Cloud chat, stack chips, benchmark chart chips, example/integration fallbacks)
  - removed the duplicate `docs/public/favicon.svg`; `/favicon.svg` now 308-redirects to `/shiro-logo.svg` so existing external links keep working
  - removed the inlined path copy `docs/components/charts/openui-mascot.ts`; the chart `Mark` component now renders an `img` of `shiro-logo.svg` (sizing rules switched from `svg.mascot` to `.mascot`), and the chip tile behind it is transparent
  - storybook brand image and react-email starter prompts point at `shiro-logo.svg`
- Copies kept on purpose, since they ship outside the docs site: `templates/openui-{cloud,self-hosted}/src/app/icon.svg` (scaffolded standalone apps, updated to the new mark) and `packages/devtools/src/ui/ShiroLogo.tsx` (published package that stays asset-free, paths regenerated from the new mark)
- Site header: removed the Thesys mark and divider before the OpenUI lockup (`SiteHeaderBrand`); dropped the now-unused `ThesysLogo` from `docs/components/brand-logo.tsx`
- Footer: the Thesys wordmark now links to thesys.dev (new tab)
- Self-host Inter Display (`docs/public/fonts/inter-display/`, 400/500/600/700 woff2 + OFL license, unmodified from the Inter v4.1 release) with `@font-face` rules in `app/(home)/globals.css`. The home styles already reference `"Inter Display"` but it was never loaded, so visitors got the fallback sans-serif.
- Home hero title: `desktopTitleLeft` and phone `mobileTitle` 700 → 600
- ViewBox changes from `0 0 113 107` to `0 0 200 160`; all usages are `object-contain` / sized from the viewBox.

## Test Plan

- [x] Verified locally (`pnpm dev` in `docs`), prettier + eslint clean
- [x] Font files are served (200) and `document.fonts.check` confirms Inter Display 400/500/600 on the home page
- [x] `/favicon.svg` returns 308 to `shiro-logo.svg`; benchmark chart chips render the mark with a transparent tile

Home hero, before / after:

![Hero before and after](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmctYWM2YjJjM2JmY2I0NGZmMDk1OWIzMGUxMDkwZDNjMmYvNjkzYzk0MzMtMTZkMC00ZDBlLTlhZTItMWJjMGViZDY4NmIxIiwiaWF0IjoxNzkyMDQwNzg1LCJvcmdfaWQiOiJvcmctYWM2YjJjM2JmY2I0NGZmMDk1OWIzMGUxMDkwZDNjMmYiLCJmaWxlbmFtZSI6Imhlcm8tYmVmb3JlLWFmdGVyLnBuZyJ9.zg3SWBtQ8PH2oXeV0n5NNI9Y0z6qTrTTz6hZioBQ0ys)

Benchmark chip, before (inline paths on grey tile) / after (`img`, no tile):

![Chart chip before](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmctYWM2YjJjM2JmY2I0NGZmMDk1OWIzMGUxMDkwZDNjMmYvMDYwNzk1MjEtNWM0Yi00MjIzLTkwZDktMGQyMDEyNDdjNzYyIiwiaWF0IjoxNzkyMDQwNzg1LCJvcmdfaWQiOiJvcmctYWM2YjJjM2JmY2I0NGZmMDk1OWIzMGUxMDkwZDNjMmYiLCJmaWxlbmFtZSI6Im1hc2NvdC1iZWZvcmUucG5nIn0.OMd1Yf-wUp8PYte2E46I80_aEOqCwjRpayYcyteKpUI)
![Chart chip after](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmctYWM2YjJjM2JmY2I0NGZmMDk1OWIzMGUxMDkwZDNjMmYvNzYwYzAyNzEtYWY2Yi00ZjU4LThlOGMtZmM5YzU5YmY4YWVjIiwiaWF0IjoxNzkyMDQwNzg1LCJvcmdfaWQiOiJvcmctYWM2YjJjM2JmY2I0NGZmMDk1OWIzMGUxMDkwZDNjMmYiLCJmaWxlbmFtZSI6Im1hc2NvdC1ub2JnLnBuZyJ9.kLCNu8SfkTT6yGZurewv_WxQbzJ4yK-yryPdn9WXzyc)

Docs page header:

![Docs header](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmctYWM2YjJjM2JmY2I0NGZmMDk1OWIzMGUxMDkwZDNjMmYvMjYxMmE1NzktZGZjZC00YmM1LThlMDktNzg5YjRkN2ZlODg1IiwiaWF0IjoxNzkyMDQwNzg1LCJvcmdfaWQiOiJvcmctYWM2YjJjM2JmY2I0NGZmMDk1OWIzMGUxMDkwZDNjMmYiLCJmaWxlbmFtZSI6ImZpbmFsLWRvY3MucG5nIn0.uZBohC5ZX2hR8nT0IGnobqBTj1ma3sDxV5sGfMJ5R3Q)

Footer (Thesys wordmark is now a link):

![Footer](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmctYWM2YjJjM2JmY2I0NGZmMDk1OWIzMGUxMDkwZDNjMmYvYjIwZGU3ZGYtYWVjOS00OWRmLTk4Y2ItYWIzZjFjYjdiYzk5IiwiaWF0IjoxNzkyMDQwNzg1LCJvcmdfaWQiOiJvcmctYWM2YjJjM2JmY2I0NGZmMDk1OWIzMGUxMDkwZDNjMmYiLCJmaWxlbmFtZSI6ImZvb3Rlci1jcm9wLnBuZyJ9.7t9Rh4lmhKa1QJcaO2eQ3plm3t-Sb3zJ1_lkhIPaXGE)

Mobile:

![Mobile](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmctYWM2YjJjM2JmY2I0NGZmMDk1OWIzMGUxMDkwZDNjMmYvODljZjY3NGUtMTA1Ny00ODZlLWFiMzctOTAxMjk2NTAxMTZmIiwiaWF0IjoxNzkyMDQwNzg1LCJvcmdfaWQiOiJvcmctYWM2YjJjM2JmY2I0NGZmMDk1OWIzMGUxMDkwZDNjMmYiLCJmaWxlbmFtZSI6ImZvbnQtbW9iaWxlLnBuZyJ9.LbA3MHSwAQ29pAjhsexdvRkZQohhBoQPTis8NwZ9tuA)

## Checklist

- [ ] I linked a related issue, if applicable
- [ ] I updated docs/README when needed
- [x] I considered backwards compatibility

Link to Devin session: https://app.devin.ai/sessions/5544241335fc443388e348ea2e0bc1c6
Open in Devin Desktop: https://app.devin.ai/desktop/session/5544241335fc443388e348ea2e0bc1c6?variant=devin
Requested by: @zahlekhan
