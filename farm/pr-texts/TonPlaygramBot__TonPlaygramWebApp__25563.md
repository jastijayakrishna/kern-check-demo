# Restore morning snapshot: re-enable Flamingo media wall, home UI, upload flow and back-button behavior

### Motivation
- Restore the tracked site state from the morning snapshot to re-enable a working public Media Wall and the matching homepage presentation. 
- Reintroduce reliable persistent media storage and resumable mobile-friendly uploads so user videos/photos survive restarts and deployments. 
- Restore the in-app navigation behavior (Telegram back button) and game overlay fixes so mobile flows and live-avatar UX behave as before. 
- Remove the interim GridFS/legacy media heuristics and align server + client MIME/price handling for premium downloads.

### Description
- Reworked the Flamingo media API to resolve the upload directory beside the `bot` module, keep pending chunked uploads, persist uploaded files to disk, and preserve the MIME type captured at upload time; added premium fields and a `/latest-post` endpoint in `bot/routes/flamingoWall.js`. 
- Extended the `FlamingoPost` schema to include `premium` and `priceTpg` on attachments and adjusted server download/payment logic to charge for premium assets (changes in `bot/models/FlamingoPost.js` and download endpoints). 
- Removed the legacy media-type heuristic module `bot/utils/mediaType.js` and deleted related tests that asserted the old configuration, and updated `render.yaml` to ensure the API service mounts the persistent media disk and matches the public host. 
- Restored and modernized the web UI: updated `HomeIntroduction.jsx` copy and featured-game presentation; significantly updated `MediaWall.tsx` to support multiple selected uploads, resumable chunked uploads, premium pricing, favorites, a portrait fullscreen video feed, and safer download calls; added related CSS updates in `media-social.css`. 
- Repaired mobile/navigation helpers and overlays: restored a consolidated `useTelegramBackButton` hook with fallback routing behavior, and updated `GameLiveAvatarOverlay.jsx` to support opponent anchors and improved overlay visibility handling; removed an older SiteBackNavigation usage in `App.jsx`.

### Testing
- Ran the full test suite with `npm test -- --runInBand`, and all automated suites passed: `93` test suites passed and `389` tests passed with `1` skipped. 
- Built the web client with `npm --prefix webapp run build`, and the production build completed successfully (Vite produced a large-chunk warning only). 
- Automated portrait screenshot via headless Chromium/Playwright was attempted but failed due to a missing system dependency (`libatk-1.0.so.0`) in the environment, which prevented the headless browser from starting.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a956727fa6c8329b5bd5e398db2b693)
