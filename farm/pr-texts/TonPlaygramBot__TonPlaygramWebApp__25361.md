# Add 10 home themes (5 free, 5 premium) and wire store unlocks

### Motivation

- Provide users with ten home-page visual themes (preserving Neon and Emerald) while keeping five free and offering five premium palettes through the store. 
- Ensure the UI prevents applying premium themes until purchased and that purchases unlock themes immediately in the UI.

### Description

- Replaced and expanded the theme catalog in `webapp/src/utils/appTheme.js` to define 10 themes with `free`/`price` flags, and added `FREE_APP_THEME_IDS`, `APP_THEME_STORE_ITEMS`, `getOwnedAppThemes`, `isAppThemeOwned`, and `addAppThemeUnlock` to persist and manage ownership. 
- Updated `getStoredTheme` and `applyAppTheme` to respect ownership so only owned themes (free + unlocked) may be applied. 
- Enhanced the theme picker component in `webapp/src/components/ThemePicker.jsx` to show all 10 palettes, display `5 FREE · 5 STORE`, indicate locked themes with a lock icon and price, navigate to the store for premium themes, listen for `appThemeInventoryUpdate` events, and expose a store CTA. 
- Added additional palettes and CSS variables for new themes in `webapp/src/index.css`, and added styling for locked items, store CTA, and a scrollable options panel for portrait/mobile. 
- Integrated a `home` store category in `webapp/src/pages/Store.jsx` that exposes `APP_THEME_STORE_ITEMS`, maps purchases to `addAppThemeUnlock`, and wires the in-app purchase flow to update `appThemesOwned` so purchased themes become immediately available. 

### Testing

- Ran `npm run lint` and the linter completed without errors. 
- Ran `npm run build` and the production build completed successfully (Vite build finished; normal chunk-size warnings noted). 
- Verified repository `git diff --check` / status to ensure files are consistent. 
- Attempted an automated UI preview via Playwright to capture the theme picker on a 390×844 viewport, but the headless browser failed to launch due to a missing system library (`libatk-1.0.so.0`), so an in-container screenshot could not be produced; Playwright browser download step completed but runtime dependencies prevented launch.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a7d81676cc883298abd320d24d2d391)
