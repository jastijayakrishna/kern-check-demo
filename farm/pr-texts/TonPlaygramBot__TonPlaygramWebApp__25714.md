# Make wall video publication durable (fsync before post creation)

### Motivation
- Prevent public Flamingo wall posts from being created while their uploaded video bytes are not yet durably persisted, which can leave viewers with a post record but a missing or truncated video after a host restart.
- Ensure mobile/resumable uploads remain safe to retry while guaranteeing that a successful `/uploads/:id/complete` call only exposes a post when its media file is fully written and synchronized to disk.

### Description
- Add `commitFlamingoMedia(pendingPath, finalPath, expectedSize)` in `bot/utils/flamingoStorage.js` to atomically move the pending upload to its final location, validate the final file size, call `fsync` on the file, and `fsync` the containing directory before returning the final path.
- Call `commitFlamingoMedia(paths.data, diskPath, metadata.size)` from the resumable completion endpoint in `bot/routes/flamingoWall.js` so the FlamingoPost is created only after durable media commit.
- Add regression tests in `test/flamingoStorage.test.js` to assert that a complete upload is committed successfully and that a truncated upload is rejected before publication.
- Update imports to include the new helper and remove the previous non-atomic `rename`-based publish path.

### Testing
- Ran the focused Jest suites with `npm test -- --runInBand test/flamingoStorage.test.js test/flamingoMediaPostLookup.test.js test/flamingoMediaRange.test.js test/flamingoMediaResponse.test.js test/flamingoMediaUrl.test.js test/flamingoWallFeed.test.js`, and all 6 suites (22 tests) passed. 
- Executed targeted linting on the changed files with `npx eslint bot/routes/flamingoWall.js bot/utils/flamingoStorage.js test/flamingoStorage.test.js` which passed for the modified files. 
- Performed project builds with `npm run build`, `npm --prefix webapp run build`, and `npm --prefix backend run build`, and the build steps completed successfully.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a9acce216348329be4e32fd0ee1d526)
