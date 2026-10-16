# Add explicit Twitter images for conf cards

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary
- add explicit Twitter card title, description, image, and image alt tags for `/conf`
- add the same Twitter image metadata for conference speaker pages
- keep the existing PNG Open Graph assets as the source image
- version the social image URLs with `?v=20260604` so X sees a fresh image URL instead of a previously cached failed/placeholder fetch

## Verification
- Confirmed the live `/conf` page currently points at a PNG OG image, not AVIF
- Confirmed `https://monorepo.tools/images/conf/og/conf.png` returns `200 OK`, `content-type: image/png`, 1200x630, 89 KB, including as `Twitterbot/1.0`
- Confirmed the versioned image URL returns `200 OK`, `content-type: image/png`
- `pnpm nx lint website`
- `pnpm nx build website`
- Confirmed generated HTML contains versioned `twitter:image` and `og:image` tags for `/conf` and `/conf/speaker/jeff-cross`
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-26fb0c1c-23ec-41f1-86d2-655ffc3bf3e2"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-26fb0c1c-23ec-41f1-86d2-655ffc3bf3e2"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
