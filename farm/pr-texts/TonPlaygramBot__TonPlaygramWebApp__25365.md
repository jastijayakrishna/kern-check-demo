# Add developer-only Social Media Control Center with mock providers, scheduling and automation

### Motivation
- Provide a developer-only Social Media admin inside the existing TonPlaygram admin/profile experience so admins can compose, schedule and publish a single post to multiple providers while preserving the current product architecture. 
- Integrate publishing with the existing Task system so provider-level publish events generate Tasks via editable automation rules instead of a separate task service. 
- Allow full workflow testing locally before real OAuth credentials by using a configurable mock-provider mode and non-blocking background publishing.

### Description
- Added Mongoose models: `SocialAccount`, `SocialPost` (master post + embedded `publications`) and `SocialAutomationRule`, and extended the existing `Task` model with optional workflow fields and an `idempotencyKey` to avoid duplicate automation tasks. 
- Implemented server-side services: a provider registry and mock adapters (`bot/services/socialProviders.js`), publication processor and scheduler (`bot/services/socialPublishing.js`), and automation runner that creates idempotent Tasks from publication events (`bot/services/socialAutomation.js`). 
- Exposed a developer-protected JSON API at `/api/admin/social` for overview, validation, create/post, retry, accounts and automation management and added a scheduler poller to enqueue due scheduled posts; authorization is limited to API token, configured `DEV_ACCOUNT_ID`, or `OWNER_TELEGRAM_ID`. 
- Added mobile-first React UI (Overview, Create Post composer, Scheduled, Posts, Accounts, Automations) and a Social Post details page inside the existing app shell, plus client API helpers and CSS for the new screens; media upload is mocked for now and Connect/Test actions are disabled until OAuth adapters are implemented. 
- Deployment and configuration: introduced `DEV_ACCOUNT_ID`, `SOCIAL_PROVIDER_MODE=mock` and optional `SOCIAL_MOCK_<PLATFORM>_RESULT` env controls and added `DEV_ACCOUNT_ID`/`SOCIAL_PROVIDER_MODE` to `render.yaml` for developer/mock mode.

### Testing
- Built the webapp with `npm --prefix webapp run build` successfully and verified the new client bundles were produced. 
- Performed Node checks for the new server modules (`node --check` on changed files) which passed. 
- Ran the new unit tests `node --test bot/tests/socialProviders.test.js` and they passed (3 tests covering provider registry, validation and mock failure behavior). 
- Ran existing targeted test suites: `test/telegramAccountIsolation.test.js` passed, while `test/profileTransactionAuth.test.js` failed due to a pre-existing missing root dependency (`uuid`) unrelated to the Social changes. 
- Attempted Playwright screenshot of the running preview but the environment lacked Playwright browser binaries so the headless run could not complete; the app preview server started successfully (`vite preview`).

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a7d943d73e883299c0be394c43b28b7)
