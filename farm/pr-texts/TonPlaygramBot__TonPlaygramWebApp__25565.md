# Add mobile Social Manager card, route and multistream studio; add Telegram & Discord providers

### Motivation
- Provide a portrait-first Social Manager entry on the Social hub and a dedicated creator studio where users can link accounts, post and multistream to multiple social platforms (TikTok, Instagram, Facebook, YouTube, X, Telegram, Discord). 
- Make posting and live-broadcast workflows mobile-friendly with quick access from the Social hub and unified controls for posting, scheduling and live destinations.

### Description
- Added a prominent Social Manager card to the portrait Social Hub and wired it to a new `/social-manager` route to open a dedicated Social Manager page. 
- Implemented a mobile-friendly Social Manager UI with tabs for overview/accounts/post creation/scheduling/history/automations and a new multistream "Go Live" studio supporting phone camera or RTMP, destination selection, adaptive-quality hints and recording options. 
- Extended backend provider registry and validation in `bot/services/socialProviders.js` to include `telegram` and `discord`, and updated the unit test expectations accordingly. 
- Added CSS and small UX changes to `messages.css` and `index.css` for the Social Manager card and the portrait-first multistream studio, and preserved existing Social hub behavior.

### Testing
- Ran the webapp production build with `npm --prefix webapp run build`, which completed successfully. 
- Ran lint with `npm --prefix webapp run lint -- --quiet`, which completed successfully. 
- Ran unit tests `node --test bot/tests/socialProviders.test.js`, and all tests passed. 
- Attempted Playwright screenshot but the Chromium browser was not installed in the environment, so headless screenshot step was skipped; PR creation via CLI also could not complete due to no authenticated GitHub session.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a956ec015788329913969b89a22c83b)
