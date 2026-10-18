# Restore morning snapshot and revert Flamingo/media/social changes

### Motivation
- Restore the codebase to the exact morning snapshot (Aug 31 08:00) to recover the prior, known-good behavior and undo later changes that regressed media, social and game flows. 
- Re-enable the original Flamingo media wall, Home UI and live-avatar/back-button behavior used by the mobile/portrait experience. 
- Remove the experimental/complex media persistence and social-linking features that were introduced after the snapshot so the app serves historical uploads reliably from disk.

### Description
- Reverted Flamingo post model and route logic to the morning design, simplifying uploads to a disk-backed `data/flamingo-uploads` directory, keeping chunked upload support and removing GridFS/database media helpers and premium fields from attachments. 
- Deleted the `bot/utils/flamingoStorage.js`, `bot/utils/mediaType.js` helpers and several related tests, and updated `/api/flamingo-wall` endpoints to serve files directly from disk and to use the captured upload MIME/type information. 
- Restored webapp client behavior for the Media Wall and Home page, including chunked upload flow, direct API attachment URLs, the Protesta card linking to `/wall`, and adjustments to `GameLiveAvatarOverlay` and Domino defaults to match the morning UI/UX. 
- Simplified social provider surfaces by removing Telegram/Discord from the hardcoded provider list and converting the Social Admin UI to the OAuth/connect flow for the remaining platforms.

### Testing
- Confirmed repository tree equality with the morning snapshot using local tree comparison checks, showing no diff versus the target snapshot (success). 
- Ran the JavaScript test runner with `npm test -- --runInBand`, which executed suites and reported passing for `test/poolRoyaleOnlineFlow.test.js`, `test/poolAi.test.js`, and `test/inventoryCrossGameConfig.test.js` during the run. 
- The full Jest run was not completed in this session (the run was terminated after an extended wait), so additional suites were not fully validated in this rollout.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a957c8fea688329a86140b0903a6a2e)
