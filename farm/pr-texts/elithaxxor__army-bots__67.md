# Add Pushover notification support

## Summary
- support sending alerts through Pushover
- call the new notifier from `bot.js`
- document env vars and setup steps in README
- cover the notifier with automated tests

## Testing
- `npm test`

------
https://chatgpt.com/codex/tasks/task_e_686047f0874c832bb542e97661c72e3f

## Summary by Sourcery

Add support for sending alerts via Pushover by introducing a dedicated notifier, integrating it into the bot’s notification flow, and covering it with configuration, documentation, and tests.

New Features:
- Add pushoverNotifier module to send messages through the Pushover API
- Integrate Pushover notifications into the bot’s alert and trend workflows

Enhancements:
- Load PUSHOVER_TOKEN and PUSHOVER_USER_KEY from environment in configuration

Documentation:
- Document Pushover setup steps and required environment variables in README

Tests:
- Add automated tests for sendPushoverMessage to verify API requests
