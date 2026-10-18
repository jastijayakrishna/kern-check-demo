# Flamingo: add profile model/endpoints, profile UI, caching and video quality controls

### Motivation
- Expose per-account profile pages with privacy controls so users can make their Flamingo profile public or private.
- Surface the viewer's account identity and profile visibility to the client for richer UX and access checks.
- Improve mobile UX and resilience by persisting a recent feed snapshot locally and adding a video quality selector and navigation between social hub and community wall.

### Description
- Add `FlamingoProfile` Mongoose model to store `accountId`, `visible`, and `updatedAt`.
- Update `bot/routes/flamingoWall.js` to include `FlamingoProfile` usage, extend `/identity` to return `accountId` and `profileVisible`, add `GET /profiles/:accountId` to fetch a profile with privacy enforcement, and add `PATCH /profile` to update visibility (upsert).
- Frontend changes in `CommunityWallApp.tsx` and `MediaWall.tsx` add a social hub <-> community wall switch, integrate `useTelegramBackButton`, implement profile viewing (`openProfile`) and profile visibility toggle, handle `authorAccountId` on posts and make author name clickable to open profile, and add IndexedDB caching (`cachePosts`, `hydrateCachedPost`) to persist and hydrate feed snapshots.
- Add client-side video quality UI and persistence (`fr-video-quality-menu`) with playback preload behavior, and persist selected quality to `localStorage`.
- Add CSS for the community switch, profile card, profile controls, video quality menu, and social hub switch; update `Messages.jsx` to include a link to the community wall navigation.

### Testing
- No new automated unit tests were added for these changes.
- Ran the frontend build and lint steps (`npm run build`, `npm run lint`) for the webapp and they succeeded locally.
- Ran the backend sanity checks (dev server startup and endpoint smoke checks) locally and the new endpoints responded as expected.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a9ab640e038832991d674f2a1c37985)
