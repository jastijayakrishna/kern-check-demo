# Keep published protest videos on wall

### Motivation
- Prevent recently uploaded protest videos from disappearing from the public wall or the Home preview due to author-based filtering or removal logic.
- Make the database the single source of truth for the Flamingo/Media Wall feed so published content is preserved and shown consistently.

### Description
- Removed author-based removal/filtering logic and added `serializeWallPosts(posts, token)` which serializes DB posts and sets `canManage` based on the owner token without mutating the database in `bot/routes/flamingoWall.js`.
- Added `latestWallPost(post)` helper and updated the `/posts` and `/latest-post` endpoints to return DB-backed results directly and with `Cache-Control: no-store` so the feed and Home preview always reflect the latest persisted post.
- Added a regression test `test/flamingoWallPersistence.test.js` which asserts the wall preserves published posts and the Home preview picks the newest DB post.

### Testing
- Ran node native tests via `node --test test/flamingoWallPersistence.test.js test/flamingoPostSparseIndex.test.js` and they passed.
- Ran Jest suites via `npx jest test/flamingoStorage.test.js test/flamingoWallMediaType.test.js --runInBand` and they passed.
- Ran ESLint which reported repository ignore warnings for the modified files but no blocking lint errors were reported.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a95413bbf5c8329a528d522d30d95d4)
