# Restore playback for legacy Protesta Shqiptare videos

### Motivation

- Historical Protesta Shqiptare videos saved with absolute or legacy-host URLs were not playing in the webapp after deployments or storage migrations.
- Normalize and route stored media URLs through the current API host so legacy records remain playable while leaving external and local preview sources untouched.

### Description

- Add `resolveWallMediaUrl(apiBaseUrl, storedUrl)` in `webapp/src/features/flamingo/mediaUrl.js` to canonicalize stored attachment URLs and map legacy `/api/flamingo-wall/...` paths to the current `API_BASE_URL`.
- Use `resolveWallMediaUrl` when loading wall posts and when normalizing newly-published posts in `webapp/src/features/flamingo/MediaWall.tsx` so player `src` values are always usable.
- Apply the same resolver to the homepage protest preview in `webapp/src/pages/Home.jsx` so the latest post preview video/image also opens correctly.
- Add regression tests in `test/flamingoMediaUrl.test.js` covering relative API paths, legacy absolute-host API URLs, external CDN URLs, and `blob:` preview sources.

### Testing

- Ran `npm test -- --runInBand test/flamingoMediaUrl.test.js test/flamingoStorage.test.js test/flamingoWallPersistence.test.js` and all three suites passed (3 suites, 9 tests total).
- Built the monorepo with `npm run build` and the webapp with `npm --prefix webapp run build`, both completing successfully.
- Verified there are no `git diff --check` issues after the changes.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a955b35e34883299e5667c16d2c68d6)
