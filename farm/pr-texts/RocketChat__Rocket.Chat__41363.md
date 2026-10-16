# chore(api): migrate engagement dashboard messages/users endpoints to typed HTTP methods

## Proposed changes (including videos or screenshots)

Continues the API endpoint migration (`docs/api-endpoint-migration.md`), finishing the **engagement-dashboard** group. Batch 1 (#41361) migrated `engagement-dashboard/channels/list`; this PR migrates the remaining `messages/*` and `users/*` routes from legacy `API.v1.addRoute()` to the typed `API.v1.get()` pattern with AJV request/response validation. Endpoints already migrated in #41356 are excluded.

### Migrated endpoints (8 routes across 2 files)

`apps/meteor/ee/server/api/engagementDashboard/messages.ts`
- `engagement-dashboard/messages/messages-sent` (GET)
- `engagement-dashboard/messages/origin` (GET)
- `engagement-dashboard/messages/top-five-popular-channels` (GET)

`apps/meteor/ee/server/api/engagementDashboard/users.ts`
- `engagement-dashboard/users/new-users` (GET)
- `engagement-dashboard/users/active-users` (GET)
- `engagement-dashboard/users/chat-busier/hourly-data` (GET)
- `engagement-dashboard/users/chat-busier/weekly-data` (GET)
- `engagement-dashboard/users/users-by-time-of-the-day-in-a-week` (GET)

All routes are already declared in the local `Endpoints` augmentation in each file, so the manual entries are kept and **not** re-augmented (avoids `TS2717`).

### Elaborated response schemas (no weak `{ type: 'object' }`)

Each response schema fully specifies the item shape (typed properties, `required`, `additionalProperties: false`), matching the exact Mongo aggregation projections in `packages/models/src/models/Analytics.ts` and `Sessions.ts` (e.g. `{ day, month, year, usersList, users }` for active-users, `{ hour, users }` for hourly-data, `{ day: date-time, messages }` for messages-sent). `Date` fields are typed as `string`/`date-time` (Router coerces Dates to ISO strings before response validation).

### Behavior-preserving notes

- Consistent with batch 1, the internal `check()`/`Match` validation is **kept** inside each handler so the exact `Match error: ...` messages the e2e tests assert are preserved (no `query` validator introduced).
- Handlers converted to named `async function action()`; auth/permission/license options unchanged; `400/401/403` error validators added to each response block.

## Issue(s)

Follow-up to #41361 and #41356. Part of the ongoing `docs/api-endpoint-migration.md` effort.

## Steps to test or reproduce

- `tsc --noEmit` clean for both changed files.
- eslint + prettier clean for both changed files.
- Existing e2e suite `apps/meteor/tests/end-to-end/api/34-engagement-dashboard.ts` covers these endpoints and asserts unchanged status codes / error messages.

## Further comments

- No behavior change — pure refactor/typing; no changeset added (consistent with #41356/#41361).
- Draft while E2E is validated in CI.


Link to Devin session: https://app.devin.ai/sessions/daf03dc59cb54e958e31a9e9c72fb162

<!-- This is an auto-generated description by cubic. -->
<a href="https://cubic.dev/pr/RocketChat/Rocket.Chat/pull/41363?utm_source=github" target="_blank" rel="noopener noreferrer" data-no-image-dialog="true"><picture><source media="(prefers-color-scheme: dark)" srcset="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://www.cubic.dev/buttons/review-in-cubic-light.svg"><img alt="Review in cubic" src="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"></picture></a>
<!-- End of auto-generated description by cubic. --> 

 Task: [ARCH-2250]

[ARCH-2250]: https://rocketchat.atlassian.net/browse/ARCH-2250?atlOrigin=eyJpIjoiNWRkNTljNzYxNjVmNDY3MDlhMDU5Y2ZhYzA5YTRkZjUiLCJwIjoiZ2l0aHViLWNvbS1KU1cifQ
