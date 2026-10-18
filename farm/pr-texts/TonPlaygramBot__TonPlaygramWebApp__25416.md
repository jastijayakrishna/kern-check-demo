# Fix Telegram game invite deep links by opening Mini App root and preserving invite params

### Motivation
- Telegram game invite Accept buttons were opening a nested client-side route (`/games/:slug`) directly, and some static/proxy hosts returned 404 for those nested paths causing the bot-initiated accept to show “page not found”.
- The intent is to ensure Telegram opens the Mini App root and let the webapp read invite query parameters and navigate to the correct online table reliably.

### Description
- Change `bot/utils/notifications.js` so `getInviteUrl(...)` returns the webapp root (`/?...`) with full invite details as query parameters and includes the `game` slug as a query key instead of pointing directly to `/games/:slug`.
- Update `webapp/src/components/Layout.jsx` to prefer `params.get('game')` when resolving the invite after `inviteAccept`, so the app can accept the invite from the root URL and then navigate to the resolved game route and room.
- Update the notification unit test `bot/tests/gameInviteNotification.test.js` to assert the invite URL uses the root pathname and exposes the `game` query parameter instead of expecting a nested `/games/...` pathname.

### Testing
- Ran `npx jest test/gameInviteUrl.test.js --runInBand`, and the invite URL unit tests passed (3 tests). 
- Ran `npm --prefix webapp run build`, and the production build completed successfully. 
- Attempted `node --test bot/tests/gameInviteNotification.test.js`, but it failed in this environment due to a missing native `canvas` package (module resolution error), so that Node test could not be executed here.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a913c78a3788329988f3b97b901fcc4)
