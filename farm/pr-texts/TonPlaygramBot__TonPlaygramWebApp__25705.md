# Recover missing wall videos before GridFS cleanup

### Motivation

- Feed posts were present in the database but video range requests returned `404` because older GridFS-stored video bytes had been removed without first ensuring a durable copy existed on the persistent media volume. 
- Ensure historical uploads remain playable during storage migrations and avoid breaking client playback when MongoDB quota or deployment changes are encountered.

### Description

- Add a `migrateMissing` option to `pruneFlamingoDatabaseMediaCopies` in `bot/utils/flamingoStorage.js` and implement streaming migration from GridFS to the persistent disk using `pipeline`, `createWriteStream`, `mkdir`, `stat`, and atomic `rename`, with temporary-file cleanup on failure. 
- Only delete a GridFS file after a durable disk copy is verified, preventing orphaned feed posts that point to missing media. 
- Call the updated prune function with `{ migrateMissing: true }` in `bot/routes/flamingoWall.js` so cleanup will evacuate missing GridFS bytes to disk before removal. 
- Add `FLAMINGO_GRIDFS_BACKUP=false` to `render.yaml` to make the persistent disk the canonical media store and prevent large GridFS duplication from exhausting MongoDB quota.

### Testing

- Ran the Flamingo unit suites with `jest --runInBand test/flamingoStorage.test.js test/flamingoMediaRange.test.js test/flamingoMediaUrl.test.js test/flamingoMediaResponse.test.js` and all tests passed (4 suites, 15 tests). 
- Installed backend dependencies with `npm install --prefix bot --ignore-scripts` and ran the TypeScript build with `npm run build`, which completed successfully.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a9a721403048329aa4046bcbb1d8ef4)
