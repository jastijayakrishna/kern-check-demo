# Restore access to legacy Protesta Shqiptare videos

### Motivation
- Recent deployments moved Flamingo uploads to a persistent disk and some historical uploads became 404s because the server only checked the new upload directory.  
- The wall must continue to play and allow downloads of earlier phone videos (morning uploads / snapshots / legacy mounts) without changing current upload behavior.  
- Downloads that charge TPG must only be issued after confirming the original file can actually be read from any configured storage location.  

### Description
- Search and resolution: introduced `flamingoStorageDirectories` and support for multiple legacy snapshot directories plus `FLAMINGO_LEGACY_UPLOAD_DIRS`, and use these when locating files for playback and downloads (`bot/utils/flamingoStorage.js` and `bot/routes/flamingoWall.js`).  
- URL/name normalization: added `flamingoMediaName` to normalize historical attachment URLs (absolute URLs, querystrings, percent-encoding) so legacy filenames are resolved correctly.  
- Safe serving and pricing: use `findFlamingoMedia` to verify disk presence before charging TPG and issuing download grants, infer missing MIME types from original filenames via `mediaType`, and add `attachmentDownloadPrice` to centralize download price logic.  
- Cleanup and removal: update post deletion to remove copies across all configured storage directories using normalized media names.  
- Tests and coverage: added regression tests covering legacy snapshot directories, absolute legacy URLs, and behavior when older uploads lack stored MIME metadata (`test/flamingoStorage.test.js`, `test/flamingoWallPersistence.test.js`).  

### Testing
- Ran `node --test test/flamingoWallPersistence.test.js` and all subtests passed.  
- Ran `npx jest test/flamingoStorage.test.js --runInBand` and the suite passed.  
- Ran `npx eslint bot/routes/flamingoWall.js bot/utils/flamingoStorage.js test/flamingoStorage.test.js test/flamingoWallPersistence.test.js` which produced no errors (only ignored-file warnings from the repo ESLint ignore config).  
- Ran `git diff --check` with no reported problems.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a954cc6ae6c83298673308f9888420c)
