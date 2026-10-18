# Persist Protesta Shqiptare videos in MongoDB GridFS with disk fallback and range streaming

### Motivation
- Ensure uploaded Protesta Shqiptare videos remain available after disk remounts or migrations by storing a durable copy in the database.
- Keep existing persistent-disk cache for fast local serving while preventing historic uploads from becoming 404s during migrations.
- Support reliable mobile playback and paid downloads even when the file is not present on disk by streaming from the database.

### Description
- Store completed uploads in MongoDB GridFS before publishing the `FlamingoPost` row by adding `saveFlamingoMediaToDatabase` and calling it during upload completion and direct `POST /posts` file flow in `bot/routes/flamingoWall.js`.
- Add database-backed helpers in `bot/utils/flamingoStorage.js`: `findFlamingoDatabaseMedia`, `saveFlamingoMediaToDatabase`, `openFlamingoDatabaseMedia`, and `removeFlamingoDatabaseMedia`, alongside existing disk helpers and `flamingoMediaName`.
- Change serving and download logic in `bot/routes/flamingoWall.js` to try disk first and fall back to GridFS for `GET /files/:name`, `GET /downloads/:grant`, and the pre-download existence check; GridFS streaming supports byte-range requests (`Range` / `Content-Range`) and responds with `206` when appropriate.
- Ensure deletion removes both disk and GridFS copies by extending `removeFlamingoMedia` to call `removeFlamingoDatabaseMedia`.
- Minor robustness: use `access` to avoid clobbering an existing disk file if present and import adjustments for new helpers.

### Testing
- Ran unit tests: `npm test -- --runInBand test/flamingoStorage.test.js test/flamingoWallPersistence.test.js`, both test suites passed (`Tests: 6 passed`).
- Ran full test run: `npm test -- --runInBand`, completed without failing suites.
- Lint: `npm run lint -- --no-warn-ignored bot/routes/flamingoWall.js bot/utils/flamingoStorage.js test/flamingoStorage.test.js test/flamingoWallPersistence.test.js` completed with no blocking errors.
- Build: `npm run build` completed successfully and `git diff --check` reported no new check failures.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a9552c9cb9c8329b589e1cc48b0ebec)
