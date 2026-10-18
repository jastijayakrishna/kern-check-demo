# covers: per-site cover-art family selection (SITE_COVER_SET)

## What
The fallback cover patterns (for posts with no image) were locked to **one of 9 families picked by hashing the site title** — stable, but a site couldn't choose. This adds **`SITE_COVER_SET`** so a deployment can pick the pattern family that fits its brand:

> tessellation · gradient-mesh · waves · rings · halftone · blobs · ridgeline · sunburst · scatter

e.g. a fintech blog → `rings`, a food blog → `blobs`, a tech blog → `tessellation`.

## How
`resolveCoverSet()` in `covers.ts` uses `SITE_COVER_SET` when it's a known family, otherwise falls back to the existing per-title hash — so **sites that don't set it are unchanged**. All 9 families are already generated per theme, so this ships with **zero new assets**.

## Verified
Same site (`signal` theme) renders `signal-waves-*`, `signal-rings-*`, `signal-sunburst-*` as `SITE_COVER_SET` changes — covers recolor to the theme automatically.

## Scope
Frontend only: `env.ts` + `src/lib/covers.ts` + `.env.example`. No data-flow changes. Only affects posts **without** a real image (real images always win).

## Follow-up (provisioning)
To actually vary per site, the scrambler (Letterbrace) should set `SITE_COVER_SET` per deployment — e.g. from the site's industry. This PR is the lettersprite knob that makes that possible.

_Red checks will be Vercel preview-deploy rate-limits, not build failures._

🤖 Generated with [Claude Code](https://claude.com/claude-code)
