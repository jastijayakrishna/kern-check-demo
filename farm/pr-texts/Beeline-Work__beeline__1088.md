# Render unmasked surfaces from a full-bleed icon

## What

The launcher's owner-approved 26%-larger margin is a home-screen treatment, but the favicon, iOS icon, both Android splashes and the desktop icons all inherited it. Every one of those files was a byte-identical copy of the inset `icon.png` (`0b1e95dbb65f`). The sign-in mark inherited it too, straight from `beeline-mark.json`.

This adds `icon-full-bleed.svg` — the same canonical loop on the same aubergine field, at its natural framing — and renders the unmasked surfaces from it. Android launcher icons keep the margin.

| Surface | Before | After |
| --- | --- | --- |
| Android legacy launcher (`icon.png`) | inset | **inset, unchanged** |
| Android adaptive + monochrome | inset | **inset, unchanged** |
| iOS app icon | inset | full-bleed |
| Web favicon | inset | full-bleed |
| Android splash, light + dark | inset | full-bleed |
| Desktop icons (`src-tauri/icons/`) | inset | full-bleed |
| Sign-in mark (`BeelineMark`) | inset | full-bleed |

iOS takes the full-bleed render despite landing on a home screen: it masks the icon itself and expects artwork that reaches the edges.

![launcher vs full-bleed](https://github.com/Beeline-Work/beeline/blob/feature/corner-d2758838821e/apps/mobile/docs/icon-margin/launcher-vs-full-bleed.png?raw=true)

Launcher framing left, full-bleed right — both are the actual generated 1024px renders.

## Verification

Measured brass bounding box on the 1024px masters:

| File | Mark bbox |
| --- | --- |
| `icon.png` (launcher) | 406x506 |
| `icon-adaptive.png` (launcher) | 408x519 |
| `icon-full-bleed.png` | 487x608 |
| `favicon.png`, `icon-ios.png`, both splashes | 487x608 |

`506 / 608 = 0.8322`, the exact inverse of the `0.83260274` inset — so the mark grew by precisely the inset that was removed, and the geometry is otherwise untouched (path SHA-256 unchanged at `819b2abe…`).

`node scripts/generate-tauri-icons.mjs --check` passes. `shellcheck` clean. `npm` is unavailable in this environment so `vitest` could not be executed here; every assertion in the updated `logoAssets.test.ts` was instead evaluated directly against the working tree (37 checks, all passing) — CI runs the real suite.

## Why the guard is now two-way

This inset has reached the flat surfaces **twice**, both times through a `cp icon.png`, after #116 first scoped it to launchers and #357/#464 restored the shared copy. A vector-only check missed it because the vectors were right — it was the rasterised copy that carried the inset.

So the scoping is asserted on both representations:

- `generate-monochrome-assets.sh` refuses to rasterize unless each source carries the inset exactly when it should, **in both directions**. Verified by deliberately breaking each direction and confirming it throws.
- `logoAssets.test.ts` hashes the shipped PNGs and requires every unmasked surface to be byte-identical to `icon-full-bleed.png` and different from `icon.png`.

`beeline-mark.json`'s `transform` is renamed to `launcherTransform`, so the one surface family it belongs to is named at every call site.

## Notes

- The six wordmark lockups and `favicon-active.ico` go through ImageMagick's SVG delegate, so their bytes shift with the local Inkscape/font versions. They were regenerated and reverted — their inputs did not change, and they are not in this diff.
- `apps/mobile/docs/icon-margin/README.md` was stale: it described the #116 scoping as still in force. Rewritten to match reality.
- The landing page wordmark in `relay-stack/web/index.html:234` still carries the inset. It is a marketing header lockup rather than one of the surfaces named here, so it is left alone — flagging it in case it should follow.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
