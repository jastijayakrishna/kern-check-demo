# Replace 'Protesta shqiptare' with TonPlayGram Wall and embed per-profile Media Wall

### Motivation
- Replace the legacy "Protesta shqiptare" branding with a unified TonPlayGram Wall that becomes the app-wide community feed and supports per-user profile pages. 
- Surface the Wall on both the Home and Social tabs and allow filtering to a single profile feed for `/:accountId` profile pages.

### Description
- Rename UI text in `webapp/src/features/flamingo/CommunityWallApp.tsx` from `Protesta shqiptare` to `TonPlayGram Wall` and update the subtitle. 
- Extend `MediaWall` (`webapp/src/features/flamingo/MediaWall.tsx`) to accept props `profileAccountId`, `showComposer`, and `showHeading`, add `authorAccountId` to `Post` type, and filter `visiblePosts = profileAccountId ? posts.filter(post => post.authorAccountId === profileAccountId) : posts`. 
- Embed the wall on the home page by adding a compact `MediaWall` into `webapp/src/pages/Home.jsx`, and replace `Social.jsx` to render the wall UI (and add a small toolbar). 
- Add a new profile page `webapp/src/pages/WallProfile.tsx` and register the route `/wall/profile/:accountId` in `webapp/src/App.jsx`, plus small CSS in `webapp/src/features/flamingo/community-wall.css` to support the toolbar and profile shell. 
- Small server/db compatibility hooks were left intact (server still provides `authorAccountId` from Flamingo posts), and author links point to `/wall/profile/:accountId` when available.

### Testing
- Built the webapp with `npm --prefix webapp run build` and the Vite production build completed successfully (warnings about large chunks only). 
- Started the dev server with `npm --prefix webapp run dev` to exercise the UI during development and produced a mobile screenshot `artifacts/tonplaygram-wall-mobile.png`. 
- Ran unit tests `jest --runInBand test/flamingoWallFeed.test.js test/flamingoMediaUrl.test.js` and both test suites passed (`2 passed`).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a9660c44a0083299bb58d998770bd3a)
