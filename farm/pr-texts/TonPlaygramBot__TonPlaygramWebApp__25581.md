# Keep newly uploaded wall videos visible (prevent stale feed overwrite)

### Motivation
- Users reported uploaded protest videos disappearing from the wall after adding the fullscreen/feed feature, which was caused by a race where an older feed response could overwrite a newer local upload.
- The change preserves posts the current browser just published until the server's live feed includes them, preventing successful uploads from disappearing.

### Description
- Add a reconciliation helper `reconcileWallPosts` in `webapp/src/features/flamingo/wallFeed.js` that preserves locally-published (pending) posts when merging remote feed responses.
- Track pending uploads with `pendingPostIds` and ignore stale feed responses using `latestFeedRequest` in `webapp/src/features/flamingo/MediaWall.tsx` so only the latest feed refresh updates the UI.
- Mark newly published posts as pending in the publish flow so they remain visible immediately after upload and are removed once the server feed contains them.
- Add a regression test `test/flamingoWallFeed.test.js` that verifies pending-post protection and release when the server returns the authoritative copy.

### Testing
- Ran unit tests with `npm test -- --runInBand test/flamingoWallFeed.test.js test/flamingoMediaRange.test.js test/flamingoMediaUrl.test.js test/flamingoStorage.test.js` and all 4 suites passed (`4 suites, 12 tests` — PASS).
- Built the web app with `npm --prefix webapp run build` and the production build completed successfully (Vite build finished, dist generated).
- Verified no `git diff --check` issues and executed a local commit of the changes for the branch (commit recorded locally).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a958da225b0832982a34cdd3cabaafb)
