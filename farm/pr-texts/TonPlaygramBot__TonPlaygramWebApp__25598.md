# Use signed, stateless grants for Flamingo wall video downloads

### Motivation
- Historical wall videos can become un-downloadable when a server process restarts or when the in-memory download grant map is lost, causing users to see failed downloads. 
- Make download links durable across instances and short-lived to allow safe, load-balanced serving without keeping grant state in a single Node process.

### Description
- Add a new utility `bot/utils/flamingoDownloadGrant.js` that provides `createFlamingoDownloadGrant` and `readFlamingoDownloadGrant` to produce and verify signed, five-minute download tokens. 
- Replace the in-memory `downloadGrants` map in `bot/routes/flamingoWall.js` so the `/posts/:id/download` endpoint returns a signed grant and the `/downloads/:grant` endpoint validates it before serving disk or GridFS media. 
- Add `test/flamingoDownloadGrant.test.js` covering valid, modified, and expired token cases. 
- Preserve existing pricing/TPG checks and the logic that prefers persistent disk copies and falls back to GridFS when serving media.

### Testing
- Ran unit tests with `npm test -- --runInBand test/flamingoDownloadGrant.test.js test/flamingoStorage.test.js test/flamingoMediaResponse.test.js`, and all test suites passed (3 suites, 9 tests). 
- Ran ESLint and fixed style issues for the new files with `npx eslint` and performed a TypeScript build with `npm run build`, both completed successfully. 
- Verified media download flow still serves from disk when available and streams from GridFS when necessary under validated grants.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a95b682f04483299cd4c33cf8324dba)
