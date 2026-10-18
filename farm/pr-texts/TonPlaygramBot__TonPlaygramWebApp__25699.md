# Social wall: download counters, OG share pages, profiles, and removal script

### Motivation
- Surface and persist download metrics for wall attachments so share/download activity is visible like reactions. 
- Provide crawler-friendly share URLs so social previews include the post media (image/video) when links are shared. 
- Give each user a public social profile page that shows their username, photo, bio and public wall posts. 
- Allow safe removal of two problematic posts authored by `Antar komiteti` via a guarded script for ops to run in production.

### Description
- Add persistent download counter to the wall post model by introducing `downloadCount` in `bot/models/FlamingoPost.js` and increment it on successful download grants in `bot/routes/flamingoWall.js`, then broadcast an update with `publishWallEvent` and return the new count in the download response. 
- Expose a crawler-friendly share endpoint `GET /api/flamingo-wall/share/:id` that emits Open Graph metadata (image or video) and redirects to the client `#/post-...` URL so social platforms can render thumbnails on share. 
- Update the frontend `MediaWall` (`webapp/src/features/flamingo/MediaWall.tsx`) to: display download counts next to downloadable attachments, update counts immediately after a successful download, and use the new share URL for sharing. 
- Add a public profile page `webapp/src/features/flamingo/SocialProfilePage.tsx` and register the route `/wall/profile/:accountId` in `webapp/src/App.jsx`, and link authors on posts to their profile when `authorAccountId` is present. 
- Add an ops script `bot/scripts/removeAntarKomitetiPosts.js` that connects to the target MongoDB and deletes exactly the two newest posts whose author matches `Antar komiteti`, refusing to run if the exact two posts are not found. 
- Small styling additions in `webapp/src/features/flamingo/media-social.css` to support profile views and author links, and an npm script entry (`remove:antar-komiteti-posts`) in `package.json` to run the removal script.

### Testing
- Built the frontend with `npm --prefix webapp run build`, which completed successfully. 
- Ran unit/integration tests with `npm test -- --runInBand test/flamingoWallFeed.test.js test/flamingoPostSparseIndex.test.js`, and both test suites passed. 
- Ran linter with `npm --prefix webapp run lint -- --quiet`, which completed without errors. 
- Performed syntax checks with `node --check` for `bot/routes/flamingoWall.js` and `bot/scripts/removeAntarKomitetiPosts.js`, both of which were valid JavaScript.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a99c7c33dcc8329828e8e9e64e0a418)
