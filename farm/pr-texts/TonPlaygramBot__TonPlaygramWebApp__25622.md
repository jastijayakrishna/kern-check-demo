# Remove 2048/Hextris from Games Lobby and upgrade Underrun Arena with egg/tomato weapons, waves, and UI

### Motivation
- Remove two legacy arcade entries (2048 Royale and Hextris Battle) from the Games Lobby to simplify the catalog and prioritize the upgraded arcade entry. 
- Rework Underrun Arena into a more stylish, mobile-first portrait experience with richer gameplay loops (weapons, waves, pickups, combos) and clearer touch controls. 
- Add distinct, fun projectile types (eggs and tomatoes) and mechanics that enable fast onboarding, visible feedback, and replayable scoring loops.

### Description
- Removed `2048 Royale` and `Hextris Battle` entries from `webapp/src/config/gamesCatalog.js` so they no longer render on the Games Lobby. 
- Replaced the old Underrun implementation with an expanded arcade canvas in `webapp/src/pages/Games/UnderrunArena.jsx` that adds `WEAPONS` (`egg` and `tomato`), weapon selection UI, dash with temporary invulnerability, wave progression, combo multipliers, pickups (`heal` / `rapid`), and enemy types (`runner` / `zigzag` / `tank`). 
- Improved visuals and polish by adding particle bursts, weapon icons as projectiles, dynamic background/grid rendering, high-DPI canvas scaling, a shield/combo HUD, and a revised results overlay suitable for portrait mobile. 
- Added `gameOver` state and wiring with `useArcadeRace` so online match endings and local game-over behave consistently, and exposed weapon selection and dash buttons in the arena controls.

### Testing
- Ran `npm --prefix webapp run build` and the Vite production build completed successfully (build warnings for large chunks only). 
- Ran `npm --prefix webapp run lint -- src/pages/Games/UnderrunArena.jsx src/config/gamesCatalog.js` and linting was fixed/clean for the changed files. 
- Confirmed `git diff --check` / code checks show no remaining diff-check issues in the modified files. 
- Attempted a headless Playwright mobile screenshot of the new arena but it failed because Playwright browsers are not installed in the environment (no browser binary available).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a966640959483298bb68fb0318e3f16)
