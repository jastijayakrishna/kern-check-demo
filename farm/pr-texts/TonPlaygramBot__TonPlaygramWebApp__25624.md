# Add portrait Social Hub and reset Community Wall (fresh start from 2026-09-01)

### Motivation
- Provide a portrait-first Social Hub at the top of the Social page so users immediately see messages, friends and notifications before the wall. 
- Start the public community wall from a fresh checkpoint so legacy/old posts no longer surface while preserving posts published after the reset as durable records. 
- Ensure older client-side cached wall entries are cleared so a fresh wall view is consistent across browsers.

### Description
- Added a Social Hub UI above the wall in `webapp/src/pages/Social.jsx` that shows quick-access cards for `Messages`, `Friends` and `Notifications` and queries live counts via `getUnreadCount`, `listFriends` and `listFriendRequests` (uses `getTelegramId`).
- Added responsive portrait-first styles in `webapp/src/features/flamingo/community-wall.css` to keep the three hub cards visible on phone portrait screens.
- Bumped the wall IndexedDB version and clear legacy entries by changing `openMediaDb()` in `webapp/src/features/flamingo/MediaWall.tsx` to open `indexedDB.open(DB_NAME, 2)` and clear the store during upgrade to avoid stale cached posts.
- Introduced a wall cutoff in `bot/routes/flamingoWall.js` using `WALL_FRESH_START_AT` (default `2026-09-01T00:00:00.000Z`) and updated server endpoints `GET /posts` and `GET /latest-post` to only return posts with `createdAt >= WALL_FRESH_START_AT`, ensuring the public feed begins from the fresh start while new posts remain durable.

### Testing
- Ran `git diff --check` with no issues reported (passed).
- Ran lint: `npm run lint -- src/pages/Social.jsx src/features/flamingo/MediaWall.tsx` (passed).
- Built the webapp: `npm run build` (production build completed successfully).
- Attempted automated visual verification with Playwright at a `390x844` portrait viewport, but screenshot automation failed because the container lacked Chromium runtime dependency `libatk-1.0.so.0` (visual test could not complete).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a9666dc2268832998bb88e21d904f7f)
