# Restore legacy Protesta video playback (search both upload directories)

### Motivation

- Restore uploaded video playback that broke after switching the app to a persistent upload disk so previously uploaded files still play in the feed and on Home.
- Preserve the existing wall behavior and confirmations while fixing failed mobile playback caused by missing or generic stored MIME and storage-migration 404s.
- Ensure downloads and deletions continue to work reliably across both the new persistent location and the original application-local storage.

### Description

- Add `bot/utils/flamingoStorage.js` with `flamingoStorageDirectories`, `findFlamingoMedia`, and `removeFlamingoMedia` to safely locate and remove media across both primary and legacy upload directories.
- Update `bot/routes/flamingoWall.js` to compute `mediaDirectories`, use `findFlamingoMedia` for `GET /files/:name` and `GET /downloads/:grant`, and use `removeFlamingoMedia` for post deletion and committee-video cleanup so files are resolved/removed from either location. 
- Keep and use normalized MIME handling when serving files by calling into the existing `mediaType` helper so `Content-Type` is correct while preserving byte-range behavior. 
- Add `test/flamingoStorage.test.js` covering discovery of legacy uploads, persistent-copy preference, and safe removal of copies.

### Testing

- Ran `npm test -- --runInBand test/flamingoStorage.test.js test/flamingoWallMediaType.test.js` and both test suites passed.
- Ran `npm test -- --runInBand test/flamingoPostSparseIndex.test.js` and the existing wall-related tests passed.
- Ran the frontend production build with `npm --prefix webapp run build` and the build completed successfully. 
- Performed syntax checks with `node --check` on updated server files and ran `git diff --check`, both of which reported no issues.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a953d76c6608329aa80a079300becc4)
