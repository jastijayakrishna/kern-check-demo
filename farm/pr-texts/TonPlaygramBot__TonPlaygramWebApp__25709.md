# Recover GridFS-only Flamingo wall videos to disk, disable GridFS backups, and expand persistent media disk

### Motivation
- Uploaded protest wall videos were appearing as posts but returning 404 when played because GridFS-only copies were being pruned without first restoring bytes to the persistent media volume. 
- The change aims to avoid losing playable media during database cleanup and to ensure enough disk capacity for migration and future uploads.

### Description
- Add migration logic to `bot/utils/flamingoStorage.js` by adding a `migrateMissing` option and code that downloads GridFS files to a temporary file, validates the size, and atomically renames the file into the persistent upload directory using `pipeline`, `createWriteStream`, `mkdir`, and `rename`.
- Extend `pruneFlamingoDatabaseMediaCopies` to accept `{ migrateMissing }` and to only delete GridFS copies after a durable copy exists on disk.
- Change `bot/routes/flamingoWall.js` to call `pruneFlamingoDatabaseMediaCopies(mediaDirectories, { migrateMissing: true })` so pruning will evacuate missing GridFS media to disk before deletion.
- Update `render.yaml` to increase the persistent `protest-media` disk from `10 GB` to `50 GB` and set `FLAMINGO_GRIDFS_BACKUP=false` so multi-GB GridFS duplication is disabled by default.

### Testing
- Ran `npm install --prefix bot` to ensure server dependencies were present and the install completed successfully. 
- Ran the targeted test suites with `jest` and observed an initial failure due to a missing `busboy` module, then installed bot dependencies and re-ran the tests. 
- After installing bot dependencies, all targeted suites passed: `test/flamingoStorage.test.js`, `test/flamingoMediaRange.test.js`, `test/flamingoMediaResponse.test.js`, `test/flamingoMediaUrl.test.js`, and `test/flamingoWallFeed.test.js` (5 suites, 17 tests passed). 
- Built the frontend/server with `npm run build` and the TypeScript build completed successfully.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a9a8697d2688329a16d70ae9dc12d45)
