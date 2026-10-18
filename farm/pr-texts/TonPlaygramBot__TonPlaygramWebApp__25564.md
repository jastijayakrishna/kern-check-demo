# Restore Flamingo media wall playback and recover historical Protesta media

### Motivation
- Historical Protesta videos stopped playing after a storage/storage-migration change; the wall must serve legacy uploads and recent uploads the same way. 
- Ensure the web UI resolves legacy absolute attachment URLs to the active API host so previously published media remain playable.
- Improve upload/download flow to support resumable mobile uploads, enforce MIME heuristics for playback, and preserve TPG pricing behavior.

### Description
- Server: enhanced `bot/routes/flamingoWall.js` to resolve media from both the persistent upload disk and legacy snapshot directories, persist uploads to a durable database store (GridFS helpers), include `originalName`/`size` in download grants, and stream fallback from the DB when disk files are missing; added download/grant and content-disposition handling with byte-range support and a safe owner-token flow. 
- Storage utils: added `bot/utils/flamingoStorage.js` to locate media on disk or in GridFS (matching by filename, originalName and size) and helpers to remove or open DB media; added `bot/utils/mediaType.js` to normalize MIME types from supplied type or filename. 
- Frontend: updated `webapp/src/features/flamingo/MediaWall.tsx` to normalize attachment URLs via a new `webapp/src/features/flamingo/mediaUrl.js` helper so legacy absolute paths are rewritten to `API_BASE_URL`, improved multi-file selection and upload metadata (premium/priceTpg/type propagation), and introduced a fullscreen video feed component with autoplay/visibility handling. 
- Home: updated `webapp/src/pages/Home.jsx` to resolve protest post media through the new URL resolver. 
- Tests: added and/or updated tests for storage lookup and URL resolution (`test/flamingoStorage.test.js`, `test/flamingoMediaUrl.test.js`, updated sparse index test coverage). 

### Testing
- Unit tests: ran Jest suites including `test/flamingoStorage.test.js`, `test/flamingoMediaUrl.test.js`, and `test/flamingoPostSparseIndex.test.js`; all 3 test suites passed. 
- Frontend build: ran the webapp Vite production build which completed successfully (assets emitted). 
- End-to-end verify: launched a local preview and ran a headless browser script (Playwright) that stubs the API responses and serves a sample MP4, navigated to `/wall`, played the video and captured a screenshot `wall-video-playing.png` showing the video playing; the check recorded a non-zero `currentTime`, `paused:false`, and `readyState:4` (playback succeeded).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a956c8a492c83299873d7dc8026be9a)
