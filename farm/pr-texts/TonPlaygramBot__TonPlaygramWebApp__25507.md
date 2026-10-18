# Add mobile-first TPG Airdrop page with admin studio, backend claim flow, and social tasks

### Motivation
- Provide a mobile-first Air Drop experience where admins can publish campaign videos and verified users can download them to receive 2,500 TPG each.
- Encourage social growth by bundling a set of lightweight social-channel tasks next to the campaign videos so users can help grow TonPlaygram channels.

### Description
- Backend: added `AirdropVideo` and `AirdropVideoClaim` Mongoose models and new authenticated endpoints to list active videos, claim a video reward (`/api/airdrop/videos`, `/api/airdrop/videos/claim`), and an admin-only endpoint to publish videos (`/api/airdrop/videos/admin/create`), which updates user balances and records transactions. 
- Frontend: implemented a portrait-first `Airdrop` React page (`webapp/src/pages/Airdrop.jsx`) that shows campaign hero, list of videos with download+claim flow, admin studio form, and a socials task section. 
- Integration: added UI route entries for `/airdrop` and `/admin/airdrop`, placed an airdrop promotional card on the Home page, and exposed client helpers in `webapp/src/utils/api.js` as `airdropVideoApi` to list/claim/create tasks. 
- Styling: included mobile-first CSS rules in `webapp/src/index.css` for the airdrop screen and the home card, and wired server-side authentication middleware so rewards are limited to verified Telegram accounts and one claim per account/video.

### Testing
- `npm --prefix webapp run build` completed successfully and produced a production build without fatal errors. 
- `npx eslint ...` was executed against the new files and completed; repository ignore rules caused the linted files to be reported as ignored (no blocking lint errors). 
- The dev server (`npm --prefix webapp run dev`) started and Vite reported the app ready on the local host. 
- Playwright-based screenshot testing failed to run because the Playwright browser binaries were not installed in the environment (installable via `npx playwright install`).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a93cd1a193c832987c154f73f1a2358)
