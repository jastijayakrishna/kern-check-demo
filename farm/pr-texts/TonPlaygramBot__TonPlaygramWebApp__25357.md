# Add ten home themes with in-app theme store and picker integration

### Motivation

- Provide users with a richer set of home themes (10 total) matching the provided visual references and enable monetization of premium styles. 
- Ensure the UI only lets users apply themes they own while keeping five default themes free and the other five purchasable in-app.

### Description

- Added a new `webapp/src/utils/appTheme.js` which declares the 10 themes, tracks owned themes in `localStorage`, exposes `getOwnedThemes`, `unlockAppTheme`, `getStoredTheme`, and enforces ownership in `applyAppTheme`.
- Updated the theme picker at `webapp/src/components/ThemePicker.jsx` to show a compact 2-column portrait-friendly grid, display free vs locked state, show a lock icon for premium themes, and link locked selections to the new store page.
- Introduced a dedicated portrait-optimized store page `webapp/src/pages/HomeThemeStore.jsx` and registered the route at `GET /store/home-themes` in `webapp/src/App.jsx`, with preview cards, TPG balance display, `buyBundle` integration, and `unlockAppTheme` on purchase success.
- Added theme CSS variables and presentation styles in `webapp/src/index.css` for all ten themes and for the store UI so previews and app surfaces update when a theme is applied.

### Testing

- Ran `npm run build` for the webapp and the production build completed successfully.
- Started the dev server with `npm run dev` and Vite reported ready and reachable, confirming the new route and assets can be served in development.
- Attempted an automated Playwright screenshot of `/store/home-themes`; browser binaries installed successfully but the headless Chromium launch failed at runtime due to a missing system library (`libatk-1.0.so.0`) in this environment, so headless screenshot verification could not run here.
- Ran `git diff --check` and basic repository checks which reported no linting/diff errors for the modified files.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a7d77481f8483299814f24d32ef4a09)
