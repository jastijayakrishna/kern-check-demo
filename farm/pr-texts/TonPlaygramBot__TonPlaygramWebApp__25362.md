# Unify Earn & Social hubs; replace Mining+Tasks nav with Earn, add Social page, update themes and API error messages

### Motivation
- Combine the separate Mining and Tasks experiences into a single, well-organised Earn hub for mobile portrait users. 
- Group community features (leaderboard, platform stats, social feed) into a single Social hub with a dedicated navbar icon. 
- Replace the legacy theme set with five new included color tones and make the picker reflect the new catalog. 
- Address repeated "Invalid server response" errors by improving API response handling and messaging.

### Description
- Added two new portrait-oriented hub pages: `webapp/src/pages/Earn.jsx` (contains Mining + Tasks sections) and `webapp/src/pages/Social.jsx` (contains HomeSocialHub, LeaderboardCard and PlatformStatsCard). 
- Replaced Mining + Tasks entries in the bottom navbar with a single `Earn` item and added a `Social` item, and wired routes so `/earn` and `/social` are first-class pages while old `/mining`/`/tasks` URLs redirect into the appropriate `#mining` / `#tasks` anchors. 
- Simplified theme catalog to five included tones (`aurora`, `rose`, `lavender`, `crimson`, `ocean`), made `aurora` the safe default, and adjusted `ThemePicker` UI/logic and `webapp/src/utils/appTheme.js` accordingly. 
- Added hub-focused CSS rules in `webapp/src/index.css` for the new hub layouts and adjusted a few page placements (removed duplicated social/stats/leaderboard cards from Home/Games where applicable). 
- Improved API client behavior in `webapp/src/utils/api.js` by adding `Accept: application/json` header and replacing generic "Invalid server response" messages with clearer, actionable messages for network failures, incomplete responses and non-OK HTTP status cases.

### Testing
- Ran production build with `npm --prefix webapp run build` which completed successfully. 
- Ran linter with `npm --prefix webapp run lint -- --quiet` which returned no errors. 
- Performed repository checks (`git diff --check`) and local static checks which showed no blocking issues. 
- Attempted an automated mobile screenshot via Playwright but the container was missing system libraries (`libatk-1.0.so.0`), so the headless Chromium run failed (environment dependency issue) and could not produce the screenshot.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a7d86ae9ee88329bb0ed49d4ada73d2)
