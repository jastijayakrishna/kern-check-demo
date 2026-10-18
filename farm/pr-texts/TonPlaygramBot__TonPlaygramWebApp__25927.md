# Decouple Tirana lobby from city loading and add loading recovery

Follow-up to the user reverting #25921 after repeated lobby loading freezes. This patch starts from the revert on main and does not restore the scenery changes.

Confirmed issue:
The lobby imported the full city layout just to display map names. That decoded city data and computed collision-safe deployment positions before React could render the selectors. The direct game host had the same eager dependency.

Changes:
- Move all 113 map IDs/names/seed coordinates into a lightweight catalog shared by the lobby and runtime. Runtime spawn/extraction calculations retain the same seeds.
- Keep the city runtime behind lazy loading so the host can show a Return to lobby button. Explain slow loads after 12 seconds and clean up the timer on unmount.
- Cover online lazy-load failures with the existing error boundary; failed career loading returns to the outer lobby.
- Fix Tailwind config/content resolution for the monorepo-root preview, and align the navigation-test JSX transform with production.

Validation:
- 3 bundled dependency/catalog checks passed: no city/Three.js in the lobby or static host dependency graph.
- 14 navigation/component checks passed, including all 113 map selections, all eight weapon selections, deployment URLs, and pending/resolved loading recovery.
- Scoped TypeScript and the full production build passed.
- Isolated unminified lobby bundle: 14,264,263 → 1,289,047 bytes (~91% reduction). This includes shared dependencies and is not production download size or a phone timing measurement.
- Production lobby and catalog chunks are about 10 KB each; the existing shared app shell remains a dependency.
- App stylesheet compilation from the monorepo root passed.

Not ready to merge on automated results alone:
The exact phone failure has not been reproduced. This fixes a confirmed loading dependency and missing recovery controls, but does not establish the only cause of the reverted version's failure. Browser verification was blocked by preview infrastructure returning 502/connection refused after source configuration recovery and one reload. No final visual selector or touch check passed. Expensive synchronous game initialization still needs phone profiling.

Keep draft until the actual lobby → selection → game entry → return flow is verified in a working browser/phone preview. See docs/tirana-lobby-loading-fix.md for details.
