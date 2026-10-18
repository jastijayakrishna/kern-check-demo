# Speed up Telegram profile loading

### Motivation
- Profile pages could be blocked waiting for slow Telegram Bot API calls when a Mini App launch already contains signed user fields, causing poor UX on Telegram WebView/cold loads.

### Description
- Forward Mini App launch user fields from the client in `createAccount` (`webapp/src/utils/api.js`) so `firstName`, `lastName`, and `photo` are included when available from `window.Telegram?.WebApp?.initDataUnsafe?.user`.
- Prefer the signed launch profile on the server during account creation in `bot/routes/account.js` and only call `fetchTelegramInfo` as a fallback when launch fields are unavailable.
- Persist the fast-path Telegram fields into the created user/profile so the UI can render immediately without waiting for Bot API enrichment.
- Add a regression test in `test/accountProfilePerformance.test.js` that asserts the fast-path uses Mini App launch data instead of blocking on the Bot API.

### Testing
- Ran the focused unit tests with `npx jest test/accountProfilePerformance.test.js --runInBand` and all tests passed. 
- Built the webapp with `npm --prefix webapp run build` and the production build completed successfully.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a970e194df08329bc0f86d9803e34e1)
