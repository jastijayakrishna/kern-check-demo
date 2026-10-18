# content: add May 2026 recap blog article

## Summary

- Adds the May 2026 monthly recap post with full prose covering the Celebrity Reflection cruise (Key West + Nassau), a working week in Fort Lauderdale, and a first trip to Medellín (El Poblado, Masaya hostel, Parque de la Conservación)
- Replaces placeholder banner and thumbnails with real Cloudinary images; sets publish date to 2026-06-06 at 11am COT
- Adds a new reusable `InstagramEmbed` component for embedding Instagram Reels in MDX posts
- Fixes `react/prop-types` warnings on the `Head` named exports in the `post` and `media` templates

## Test plan

- [x] Verify the May 2026 recap renders correctly at `/may-2026`
- [x] Confirm the Instagram Reel embed appears centered and links through to Instagram
- [x] Confirm banner and thumbnail images load from Cloudinary
- [x] Confirm no prop-types ESLint warnings remain in `post.js` and `media.js`

🤖 Generated with [Claude Code](https://claude.com/claude-code)
