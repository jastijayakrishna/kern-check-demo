# fix(ui): cite the actual license terms in the footer

## What

The footer claimed all imagery is "public domain". That's imprecise on both halves:

- **Smithsonian** Open Access records carry an explicit **CC0** dedication (the app even receives `metadata_usage.access: "CC0"` per record — currently unread). The SI Open Access page is the authoritative reference for that dedication.
- **NASA** sends no rights metadata at all; the usage basis is NASA's site-wide Media Usage Guidelines (imagery "generally not copyrighted", with third-party exceptions) — which the site never cited, and which means a blanket public-domain claim overreaches.

The footer now attributes each provider to its governing terms instead of asserting a rights status, with the links on the terms themselves:

> © 2026 christopher anderson · imagery courtesy of nasa ([media guidelines](https://www.nasa.gov/nasa-brand-center/images-and-media/)) and the smithsonian institution ([open access, cc0](https://www.si.edu/openaccess))

CC0 is named only where a provider actually declares it. Anchor styling mirrors the asset-detail source-record line (inherit muted, hover to text, global underline).

The README's Smithsonian provider section now also cites Open Access (CC0) alongside the Terms of Use, so the developer docs and the user-facing attribution reference the same rights source.

Per-asset rights display was previously considered and deliberately cut (docs/Providers.md "Source Link"); this PR doesn't reopen that.

## Review round

The first draft ended with a "public domain and cc0" status tail; review flagged that this still overclaimed NASA, so the wording was reworked to let the linked terms govern (54cd1c2), and the README citation was aligned (340f343).

## Verified

prettier, eslint, tsc green.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
