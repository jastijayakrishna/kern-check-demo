# Prevent Telegram bot conflicts in Render PR previews

### Motivation

- Prevent Render pull-request preview instances from taking ownership of the production Telegram bot webhook and starting a second polling loop, which caused conflicts and unexpected `409`/duplicate behavior. 

### Description

- Add `isTelegramBotEnabled` to `bot/telegramStartup.js` and make `startTelegramBot` return early with `{ mode: 'disabled' }` when `IS_PULL_REQUEST` indicates a preview. 
- Change server startup in `bot/server.js` to compute `telegramBotEnabled`, register the webhook route only when enabled, and only call `launchBotWithDelay` when the bot is permitted to start. 
- Add regression tests in `bot/tests/telegramStartup.test.js` that verify preview instances do not call Telegram and that normal environments still use polling or webhook modes as appropriate. 

### Testing

- Ran `node --test bot/tests/telegramStartup.test.js` and the startup/webhook-related tests passed (all assertions OK). 
- Ran the bot test suite with `npm test --prefix bot` where 23 of 24 tests passed and one unrelated test failed due to the optional native `canvas` package being unavailable in the environment. 
- Performed static checks including `node --check bot/server.js`, `node --check bot/telegramStartup.js`, and `git diff --check`, which reported no syntax or diff issues.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a9ad2b6e0a8832995805bb2fb83d196)
