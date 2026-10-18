# Upgrade Tirana Streets battlefield maps and shared arsenal

### Motivation
- Improve the Tirana Streets FPS by adding multiple distinct battlefield sectors, expand the shared weapon set, and surface these choices in the operation UI for selectable deployments.
- Make battlefield runs more dynamic by letting defeated enemies drop weapons and ammunition that are mobile-friendly to collect on portrait devices.

### Description
- Add `BATTLEFIELD_MAPS` (10 collision-safe sectors) and `BattlefieldMapId` types and wire the selected sector into the FPS runtime so player spawn and extraction are sector-specific (`shared/layout.mjs`, `core.ts`, `engine.ts`).
- Expand the shared `WEAPONS` registry from 2 to 8 classes and expose `WeaponId` variants used throughout the FPS code and UI (`shared/physics.mjs`, `core.ts`).
- Implement loot crates that spawn when enemies die and automatically equip/collect when the player moves close, including runtime logic and cleanup (`engine.ts`).
- Expose map and expanded loadout selectors in the operation UI and accept URL query parameters to preselect weapon and map on launch (`baseUi.tsx`, `Blackwater.jsx`, `styles.css`).
- Add typing updates and declaration surface changes for the new maps and weapons (`*.d.mts`) and a small safety routine to find clear insertion points inside the shared city world (`shared/layout.mjs`).

### Testing
- Ran `npm run build` (webapp) which completed successfully and produced production assets.
- Ran `node --test test/blackwater.test.mjs test/blackwaterOperation.test.mjs test/tiranaFpsCity.test.mjs test/tiranaSocialExplore.test.mjs` which completed (39 tests executed; 32 passed and 7 environment-dependent tests were skipped).
- Executed a validation script that confirmed all 10 battlefield sectors are collision-free and the expanded arsenal contains 8 weapons (validation passed).
- Performed `git diff --check` and TypeScript checks during development; attempted a portrait screenshot with Playwright but the environment lacks the Chromium binary so the capture step did not run.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6aa16ba44ff88329925e219ae6f205f9)
