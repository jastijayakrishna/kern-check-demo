# Prevent Telegram polling conflicts on hosted deploys

### Motivation
- A Telegram HTTP 409 (conflict) was traced to overlapping long-polling `getUpdates` calls from multiple deployed instances during rolling deploys, so hosted services must not silently fall back to polling.  
- Local development should keep long polling for convenience, and single-instance deployments must be able to explicitly opt into polling.  

### Description
- Add `canUseTelegramPolling(env)` to detect whether long polling is safe and to allow an explicit `TELEGRAM_UPDATE_MODE=polling` override.  
- Change `startTelegramBot` to refuse to start long polling on hosted/production instances when a webhook URL is not configured and instead throw a clear error.  
- Preserve existing webhook setup: when `getTelegramWebhookConfig` returns a webhook the bot registers it and does not start polling.  
- Add regression tests in `bot/tests/telegramStartup.test.js` that cover pull-request previews, webhook URL construction, local polling, hosted protection, and the explicit polling override.  

### Testing
- Ran `node --test bot/tests/telegramStartup.test.js` and all 9 Telegram startup tests passed.  
- Ran Prettier formatting with `npx prettier --write bot/telegramStartup.js bot/tests/telegramStartup.test.js` and `git diff --check` to ensure style and diff cleanliness.  
- Ran `npm test --prefix bot`, which executed the broader bot test suite and showed 26 tests passing while 3 tests failed due to missing bot-local production dependencies (`cannon-es`, `canvas`, `uuid`) in the current environment and not related to the Telegram startup changes.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6aa2a5957ae88329b583d316ecbef266)
