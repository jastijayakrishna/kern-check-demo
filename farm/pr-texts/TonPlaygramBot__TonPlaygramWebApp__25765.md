# Add Archery Royal 3D career and online game

## Summary

Adds **Archery Royal**, a new mobile-first 3D skill game that is not already represented in the games catalog.

- Play against deterministic Club, Tour, and Pro AI
- Full three-end / nine-arrow match rules with server-owned scoring
- Career tour with five events, XP, coins, equipment upgrades, wins, and losses
- TPG-stake multiplayer lobby with quick match and private room codes
- Three selectable arenas and a dedicated games-page card
- Touch drag-to-aim and hold/release draw controls, plus keyboard controls
- Procedural high-resolution target/terrain materials, ACES lighting, shadows, particles, bow/arrow animation, athlete characters, HDR environments, and synthesized sound effects

## Online integrity

- Reuses the existing TPG lobby and seat-table matchmaking flow
- Adds a dedicated `archeryroyal` game contract and stake policy
- Adds an isolated Archery match model and Socket.IO runtime
- Server validates identity, seat ownership, turn IDs, request IDs, shot bounds, timeouts, reconnects, forfeits, settlement, and refunds
- Scores, wind, turns, and winners are authoritative on the server

## Assets

No new binary assets are introduced. The game reuses the project's existing CC0 Poly Haven HDRIs and CC0 Quaternius athlete models, with original runtime-generated 2048×2048 target and 1024×1024 terrain textures. See `docs/archery-royal.md` for credits and architecture.

## Validation

- `node --test test/archeryRoyal.test.mjs` — 6/6 passing
- Strict TypeScript check — passing
- Production Vite build — passing (2,496 modules)
- Archery bundle: 24.15 kB JS / 7.91 kB CSS before gzip

## Release gates

This is intentionally a draft until physical iOS/Android touch, performance, audio, and live Mongo-backed multiplayer/settlement testing are completed.
