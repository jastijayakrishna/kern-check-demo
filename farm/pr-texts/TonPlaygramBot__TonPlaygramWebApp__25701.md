# Flamingo wall: track downloads, add share/profile pages, and remove legacy 'Antar komiteti' posts

### Motivation
- Track how often attachments are downloaded so the UI can show download counts and owners can see popularity.  
- Provide shareable social preview pages with proper Open Graph/Twitter meta and a stable profile view for authors.  
- Perform a one-off moderation cleanup to remove recent posts authored as variations of "Antar komiteti" from the active production database.  

### Description
- Add `downloadCount` to the `FlamingoPost` schema and increment it on successful `/posts/:id/download` requests, then emit a wall `updated` event.  
- Return the updated `downloadCount` from the download POST response and surface it in the client UI so download buttons display counts.  
- Add `GET /profiles/:accountId` to return a public profile (username, photo, bio) and that user's wall posts, and add a client `SocialProfilePage` plus a route `'/wall/profile/:accountId'` that lists posts and download counts.  
- Add `GET /share/:id` to render an HTML share page with `og:`/Twitter meta for images/videos and a redirect to the frontend post anchor to improve link previews.  
- Hardened helpers: `escapeHtml` and `absoluteUrl` to compose safe meta tags and links in the share page.  
- Add maintenance utility `removeAntarKomitetiPosts` and a runnable script `bot/scripts/removeAntarKomitetiPosts.js`, plus run the removal once on DB `open` during startup, and add an npm script `remove:antar-komiteti-posts`.  
- Add unit tests `test/flamingoMaintenance.test.js` to validate the removal regex and deletion behavior.  
- Add client-side changes: download flow (`downloadAttachment`) now requests the download endpoint to take TPG when applicable and receives `downloadCount`; the MediaWall UI updates and displays the download counter; sharing links use the new backend share endpoint; author names link to the new profile page; supporting CSS added.

### Testing
- Added `test/flamingoMaintenance.test.js` which verifies the `ANTAR_KOMITETI_AUTHOR` regex and that `removeAntarKomitetiPosts` deletes at most the configured limit, and the test suite passed (`jest` ran and the test succeeded).  
- Startup path executes `removeAntarKomitetiPosts` on an open MongoDB connection guarded by try/catch, and logs success or failure during integration startup (no automated integration test included).  
- Existing endpoint behavior preserved and basic client flows (download, share, profile fetch) updated to use new API responses in the web app (no additional automated UI tests added).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a99c7c33dcc8329828e8e9e64e0a418)
