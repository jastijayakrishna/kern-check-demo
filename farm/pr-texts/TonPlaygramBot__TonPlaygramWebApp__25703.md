# Wall: add profile pages & privacy plus per-video quality menu

### Motivation

- Provide per-user profile pages that surface a user's posts and let each user control whether their profile is visible to others. 
- Let viewers choose a preferred playback/download quality from the three-dot menu on a video frame while preserving the existing original media source and download behavior. 
- Keep all existing upload/download limits, premium pricing and playback semantics unchanged.

### Description

- Added a persistent profile model `bot/models/FlamingoProfile.js` to store `accountId` and `visible` state.  
- Extended the wall API in `bot/routes/flamingoWall.js` with an enhanced `GET /identity` (returns `accountId` and `profileVisible`), `GET /profiles/:accountId` (profile page + posts), and `PATCH /profile` (owner-only privacy toggle).  
- Frontend updates in `webapp/src/features/flamingo/MediaWall.tsx` add a three-dot video menu for selecting `auto|1080|720|480` (persisted to `localStorage` as `fr-video-quality`), make author names tappable to open a profile page, and add a `My profile` button and profile card with a privacy toggle.  
- Added UI styles in `webapp/src/features/flamingo/media-social.css` for the quality menu, profile card, and touch-sized controls; no changes were made to upload limits, premium pricing, or download endpoints.

### Testing

- Built the web app with `npm --prefix webapp run build`, which completed successfully.  
- Performed static checks with `node --check` against `bot/routes/flamingoWall.js` and `bot/models/FlamingoProfile.js`, both passing.  
- Ran unit tests `npm test -- --runInBand test/flamingoWallFeed.test.js test/flamingoMediaResponse.test.js test/flamingoDownloadGrant.test.js`, and all test suites passed.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a9a4e73c8f883299bb4faa134f72cf2)
