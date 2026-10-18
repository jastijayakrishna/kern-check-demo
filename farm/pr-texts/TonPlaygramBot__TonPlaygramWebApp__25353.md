# Add theme picker with five selectable app themes

### Motivation
- Provide users a compact, portrait-friendly control on the home page to switch the app visual style. 
- Ship five curated palettes so users can quickly change the app mood without affecting game layouts.

### Description
- Added a lightweight theme system in `webapp/src/utils/appTheme.js` that defines five palettes (`neon`, `sunset`, `forest`, `royal`, `daylight`) and exposes `getStoredTheme` and `applyAppTheme` for persistence and application.
- Added a floating, accessible theme picker UI component at `webapp/src/components/ThemePicker.jsx` with a compact trigger, a mobile‑sized panel, visual swatches, and radio-like selection behavior that closes on selection or outside tap.
- Applied the stored theme on app startup by calling `applyAppTheme(getStoredTheme())` from `webapp/src/App.jsx` and inserted the `ThemePicker` into the home page wrapper in `webapp/src/pages/Home.jsx`.
- Added CSS variables and styling rules to `webapp/src/index.css` to recolor shared surfaces, borders, accents, and text for non‑neon palettes while preserving existing layout and game-specific styles.

### Testing
- Ran a production build with `npm --prefix webapp run build`, which completed successfully and produced the site bundles. 
- Ran code style checks with `eslint` on the modified files, fixed issues, and re-ran linting; linting completed successfully after fixes. 
- Verified the theme picker visually by running the dev server and attempting an automated mobile screenshot with Playwright; this visual check failed because the environment is missing a required system library (`libatk-1.0.so.0`) for the headless Chromium, not due to the code itself. 
- Performed basic smoke checks (style application and local interactions) in the dev build; no runtime errors were observed in the app start-up sequence.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a7d71ad506c8329a284ddacf944fecc)
