# Persist social-wall media in MongoDB (GridFS) and require durable save before publishing

### Motivation
- Ensure videos and photos posted to the community wall remain retrievable after deploys or disk replacements by storing them durably in MongoDB GridFS. 
- Prevent published posts from pointing at missing or truncated media by making media persistence a precondition for creating public `FlamingoPost` records. 

### Description
- Enable GridFS by default via `flamingoDatabaseStorageEnabled` (env `FLAMINGO_GRIDFS_BACKUP`) and add `bot/.env.example` guidance to document the option. 
- Add `commitFlamingoMedia` to atomically move pending uploads onto the persistent volume and fsync the file and its directory before exposing the post. 
- Replace the previous optional/after-the-fact GridFS copy with `persistDatabaseMedia` and require the media to be saved to GridFS before creating the public post for both chunked (`/uploads/:id/complete`) and form (`/posts`) flows. 
- Prefer MongoDB-backed playback/downloads in `/downloads/:grant` and `/files/:name`, falling back to legacy disk locations while scheduling a lazy backfill into GridFS; update logic to stream from DB when possible. 
- Tidy error messaging for storage quota conditions and add a unit test asserting the new GridFS default behavior. 

### Testing
- Ran the focused flamingo tests with `npm test -- --runInBand test/flamingoStorage.test.js test/flamingoMediaRange.test.js test/flamingoMediaResponse.test.js test/flamingoMediaPostLookup.test.js test/flamingoMediaUrl.test.js` and the flamingo suites passed (`5` suites, `20` tests passed). 
- Installed bot dependencies and ran the full test run `npm test -- --runInBand`, which completed with the tested suites passing. 
- Linted and committed changes using `npm run lint` and `git commit -m "Persist social wall media in MongoDB"` without diffs or check failures.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a9af468a81083299dffae16279109d3)
