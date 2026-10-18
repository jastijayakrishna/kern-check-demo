# Restore persistent community wall feed

### Motivation

- The community wall could lose freshly uploaded posts when a slower server feed arrives, and cached attachments could become unusable after a restart. 
- The change aims to show posts immediately on mobile while the live API wakes and to keep a durable shared snapshot of the wall so media remains openable.

### Description

- Add `cachePosts(posts)` to persist a complete shared feed snapshot into IndexedDB and replace the previous per-post save helper. 
- Add `hydrateCachedPost(post)` to rebuild cached attachment URLs via `resolveWallMediaUrl` so photos and videos remain openable after reloads. 
- On mount, paint the last cached snapshot immediately via `savedPosts()` while the live feed request runs, and use the server response to reconcile posts with `reconcileWallPosts` so local pending uploads are preserved. 
- After a successful server refresh, store the merged feed snapshot back to IndexedDB and use cached posts as a fallback when the network/API is unavailable; changes are in `webapp/src/features/flamingo/MediaWall.tsx`.

### Testing

- Ran unit tests with `npm test -- --runInBand test/flamingoWallFeed.test.js test/flamingoMediaUrl.test.js`, and the suites passed (`2 passed, 2 total; 6 tests passed`).
- Ran lint on the modified file with `npm --prefix webapp run lint -- src/features/flamingo/MediaWall.tsx`, which succeeded. 
- Built the web app with `npm --prefix webapp run build`, which completed successfully.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a9a8cdb34e8832996e5bdb5d7fe1133)
