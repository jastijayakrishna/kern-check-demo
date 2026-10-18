# Add Earn and Social hubs, update navbar/routes, expand themes and improve API error handling

### Motivation
- Consolidate earning features (mining and tasks) into a single `Earn` hub and add a dedicated `Social` hub for community features. 
- Refresh the app theme catalogue with new premium themes and expand styling for hub pages. 
- Update navigation and routes to reflect the new hubs and keep old URLs working via redirects. 
- Make `api` helpers more robust by adding a default `Accept` header and clearer error messages for partial/non-JSON responses.

### Description
- Added new pages `Earn.jsx` and `Social.jsx` and wired them into routing, including redirects from legacy paths (`/mining` -> `/earn#mining`, `/tasks` -> `/earn#tasks`).
- Updated `Navbar.jsx` to replace the Mining/Tasks items with `Earn` and `Social`, and changed icons accordingly. 
- Removed `LeaderboardCard` from `Games.jsx` top-level render and adjusted imports. 
- Reworked theme configuration in `appTheme.js` by renaming/adding many theme IDs, marking several as free, and adding a larger premium theme list; updated `ThemePicker.jsx` UI text to reflect new store counts. 
- Expanded CSS in `index.css` with many new `:root[data-app-theme='...']` palettes and added hub-related layout styles (e.g. `.hub-page`, `.hub-hero`, `.hub-section`).
- Improved `utils/api.js` by adding `Accept: 'application/json'` to `buildHeaders` and returning clearer, friendlier error strings when response reading or JSON parsing fails.

### Testing
- Built the webapp locally with `yarn build` and verified the dev build completed successfully. 
- Ran the existing test suite with `yarn test` and the tests passed without failures.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a7d86ae9ee88329bb0ed49d4ada73d2)
