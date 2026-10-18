# fix(home): stop cropping the hero cover art

## Summary
The homepage hero cover was rendering but visibly cut off at the top and bottom. The art is 941×1672 (≈9/16, tall and narrow), while the hero frame was locked to a 2/3 book ratio with `object-fit: cover` — so it cropped the art to fill the wider box. This shows the full cover instead.

## What changed
- **`src/app/page.tsx`** — hero `<Image>` `objectFit: 'cover'` → `'contain'`, so any cover displays in full (letterboxed rather than cropped).
- **`src/styles/global.css`** — `.hero-cover` `aspect-ratio: 2/3` → `941/1672` to match the art, so the frame hugs the current cover with no letterbox bars. Commented for the next art swap.
- **Removed `src/cover.png`** — a stray 3.8MB duplicate that slipped into `main`. Next.js only serves static assets from `public/`; the served file is `public/cover.png`.

## Testing
- Confirmed art dimensions (941×1672) via System.Drawing; frame ratio now matches exactly, so `contain` fills the frame edge-to-edge with no crop and no bars.
- Changes are CSS value swaps only (no logic) — build/validate CI covers compilation.

## Risk / follow-ups
- Low blast radius: homepage hero only.
- If the cover art is later swapped to a different ratio, `object-fit: contain` keeps it fully visible (bars, never cropped); update the `aspect-ratio` to match the new art to remove any bars.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
