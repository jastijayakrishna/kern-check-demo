# fix(home): show the homepage hero cover image

## Summary
The homepage hero cover art wasn't showing. This wires it up — the image is now served correctly and the `SITE.cover` config is enabled — so the hero renders its two-column cover layout.

## What changed
- **Moved `src/cover.png` → `public/cover.png`.** Next.js only serves static assets from `public/`, so a request to `/cover.png` was 404ing while the file sat under `src/`.
- **Enabled `SITE.cover` in `src/lib/site.ts`.** The config was commented out, leaving `SITE.cover` undefined, so the hero (`src/app/page.tsx`) skipped rendering the `<Image>` entirely. Now set to `{ src: '/cover.png', alt: 'The Dominion Realm — Book One' }`.

No render-code changes: the `has-cover` hero layout and `<Image fill priority>` were already built and tested from the earlier hero-cover work — they just had nothing to render.

## Testing
- Verified `public/cover.png` is a valid PNG (magic bytes `89 50 4E 47 …`).
- Confirmed the wiring: `page.tsx` gates on `SITE.cover` truthiness and reads `cover.src` / `cover.alt`, which the config now provides.
- Not yet driven in a running dev server (node/pnpm not on this shell's PATH); the change is a one-line config enable + asset relocation onto an already-tested render path.

## Risk / follow-ups
- Low blast radius — homepage hero only; the rest of the site is untouched.
- The alt text uses a placeholder-style title treatment (`The Dominion Realm — Book One`); Mark may want to adjust wording.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
