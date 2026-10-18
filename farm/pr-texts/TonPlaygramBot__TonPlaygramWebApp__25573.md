# Simplify Flamingo media storage (drop GridFS/legacy paths), streamline uploads/downloads, and adjust social/live UI

### Motivation
- Simplify the Flamingo media pipeline by removing the GridFS-backed database storage and legacy multi-directory lookup so uploads are stored and served directly from the configured upload disk.
- Remove brittle MIME/type heuristics and legacy URL rewriting while ensuring withdrawn committee videos are removed from both feed and storage.
- Reduce surface area for social integrations (remove unused platforms) and simplify live-video and Domino Royal graphics/participant logic to avoid fragile multi-stream and low-memory heuristics.

### Description
- Deleted `bot/utils/flamingoStorage.js` and `bot/utils/mediaType.js` and refactored `bot/routes/flamingoWall.js` to rename pending parts directly into `FLAMINGO_UPLOAD_DIR`, serve files from disk with `res.sendFile`/`res.download`, and remove GridFS streaming and legacy-directory resolution.
- Normalizes authors and auto-removes posts from the withdrawn committee author (by normalized name), deletes their files from disk, and simplified download grant entries to reference on-disk basenames.
- Updated upload handling to persist the uploaded file to disk, simplified metadata handling (no DB media save), and adjusted price calculation and ownership checks accordingly.
- Frontend adjustments include replacing legacy URL resolution with direct API-based file URLs in `MediaWall.tsx`, simplifying upload parameter handling in the large-upload flow, removing `resolveWallMediaUrl` and related utilities/tests, and updating social provider lists and Social Admin UI/OAuth flow to the reduced platform set.
- Adjusted Domino Royal and live-video codepaths: removed the special 50 Hz low-memory profile and related automatic video-safety code, changed default preference logic to `fhd60`, and simplified multi-peer/live-chat constraints and UI avatar opponent selection.

### Testing
- Ran the backend unit tests with `npm test` (including the updated `bot/tests/socialProviders.test.js`) and they succeeded.
- Performed frontend build and basic smoke checks (`npm run build` / manual integration of Flamingo uploads/downloads and Social Admin connect flow) to verify end-to-end upload, publish, serve, download, and UI changes, and these checks succeeded.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a957c8fea688329a86140b0903a6a2e)
