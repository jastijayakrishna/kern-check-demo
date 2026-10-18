# Increase airdrop influencer reward to 5,000 TPG and wire Developer-only publishing + Earn tasks into Airdrop UI

### Motivation
- Raise the download airdrop for influencer-first rewards from 2,500 to 5,000 TPG and ensure only developer-authorised accounts can publish campaign videos while exposing related Earn tasks and influencer view-based bonus information on the Airdrop page.

### Description
- Server: changed `bot/models/AirdropVideo.js` default `reward` from `2500` to `5000` and updated the admin create route in `bot/routes/airdrop.js` to use `hasSocialDeveloperAccess(req.auth)` middleware (imported from `socialAdmin.js`) and default `reward` to `5000` in the request body. 
- Client: updated `webapp/src/pages/Airdrop.jsx` and `webapp/src/pages/Home.jsx` to show the new 5,000 TPG messaging, added a Developer studio publish form change, made the displayed reward dynamic (`video.reward`), added an Influencer bonus section with view-based reward tiers, and pulled Earn tasks from `listTasks` to surface actionable Earn tasks on the Airdrop page. 
- API surface: removed the now-unused admin token parameter from `airdropVideoApi.create` in `webapp/src/utils/api.js` and adjusted imports/usages accordingly. 
- UI: added a link to `/admin/airdrop` from the account admin area (`webapp/src/pages/MyAccount.jsx`) and introduced CSS rules for the influencer section in `webapp/src/index.css`. 
- Misc: small import and icon updates in the Airdrop component and wiring to reuse task utilities (`normalizeTasksResponse`) for Earn tasks display.

### Testing
- Ran the webapp linter (`npm --prefix webapp run lint`) which surfaced numerous existing JS/ESLint warnings in unrelated files (not caused by this PR) and was observed during the rollout. 
- Built the front-end (`npm --prefix webapp run build`) which completed successfully and produced the production `dist` output. 
- Ran the dev server and executed a Playwright-based render of `/airdrop` (installed Playwright dependencies during the run), which produced a mobile screenshot artifact (`artifacts/airdrop-mobile.png`) showing the updated Airdrop UI. 
- Performed a quick sanity check on the modified server route (`node --check bot/routes/airdrop.js`) and inspected diffs; build and smoke verification succeeded locally in the rollout environment.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a93d10d48608329a07f7187991c7556)
