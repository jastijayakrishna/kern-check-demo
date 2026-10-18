# fix(styles): load Material Icons locally so glyphs are not clipped (DEV-7068, DEV-7069)

Fixes two icon-rendering defects found in the same sweep. Shipping them together means one QA pass over the icons.

## DEV-7068 — icons clipped in production builds

`_config.scss` imported the Material Icons stylesheet from Google Fonts:

```scss
@import url("https://fonts.googleapis.com/icon?family=Material+Icons|Material+Icons+Outlined");
```

Every component SCSS that `@use`s that partial inherits the import — 20+ files, including the incoming-links pager. In a **production** build (`inlineCritical` / `fonts.inline`) the remote stylesheet is downloaded and **inlined into each component's styles**, where view encapsulation rewrites it as `.material-icons[_ngcontent-ng-cXXXXX]`. That attribute selector out-specifies Angular Material's `.mat-mdc-button > .mat-icon`, so `font-size` stayed 24px while the box remained 18px — and `overflow: hidden` cut 6px off every glyph.

Dev and every `start-*` config set `optimization: false`, leaving it a runtime `@import` in the global scope where Material's rule wins. **That is why this never reproduced locally** — including `npm run start-stage`, which only swaps the environment file. It was never a caching issue.

### Why the fix is two changes, not one

The remote stylesheet was not only supplying `@font-face`. It also defined the entire `.material-icons` **class**, including `font-feature-settings: 'liga'` — the property that turns an icon name into a glyph. Removing the import alone makes `mat-icon` fall back to Roboto and render literal ligature text (`arrow_circle_right` as 189px of words); this was caught in a production build before it went anywhere.

So the class is re-declared **globally** in `_font.scss`, deliberately **without `font-size`** — that single property is what caused the clipping once it became component-scoped. Global scope means Material's own sizing keeps winning.

`font-display: swap` was added to the self-hosted `@font-face`, matching the Roboto faces above it. The font was already self-hosted and ships via the asset glob; no new asset.

## DEV-7069 — "My Projects" tab icon rendered as text

`user.component.ts` asked for `assignments`, which is not a Material Icons ligature, so the browser printed the word. Verified against the font this app actually ships, at 24px with `liga` enabled:

| Name | Width | Resolves |
| --- | --- | --- |
| `assignment` | 24px | yes — one glyph |
| `assignments` | 48px | no — renders as text |
| `settings` (control) | 24px | yes |

## Verification

Production build (`nx run dsp-app:build:production`) served from `dist/`, pointed at the stage API:

| | Before (stage) | After |
| --- | --- | --- |
| Pager "Next" arrow | 18px box / 24px glyph → **6px clipped** | 18×18, **clip 0** |
| Pager "Previous" arrow | 18px box / 24px glyph → **6px clipped** | 18×18, **clip 0** |
| All font icons on the resource page | 2 of 41 clipped | **0 of 41 clipped** |

Both arrows were clipped all along — only `east` *looked* broken, because its arrowhead sits in the clipped right-hand 6px while `west`'s is on the left.

Also confirmed: no `fonts.googleapis.com` reference remains in the built output, and no `.material-icons[_ngcontent-…]` scoped rule is emitted. `dsp-app:test` and `vre-pages-user-settings-user:lint` pass.

## How to review

This cannot be checked with `npm run start-*` — those builds are unoptimised and look correct either way:

```bash
nvm use            # project requires Node ^22.13.0
npx nx run dsp-app:build:production
# serve dist/apps/dsp-app with SPA fallback, then run the check below
```

```js
[...document.querySelectorAll('mat-icon, .mat-icon')]
  .filter(el => el.getAttribute('data-mat-icon-type') === 'font')
  .filter(el => el.scrollWidth > el.clientWidth || el.scrollHeight > el.clientHeight)
  .map(el => ({ icon: el.textContent.trim(), box: `${el.clientWidth}x${el.clientHeight}`, glyph: `${el.scrollWidth}x${el.scrollHeight}` }));
```

Expected: `[]`. The `data-mat-icon-type === 'font'` filter matters — SVG icons are `display: 
