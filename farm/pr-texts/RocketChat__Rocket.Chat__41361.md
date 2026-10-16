# chore(api): migrate audit/chat/ldap/engagement single-route endpoints to typed HTTP methods

## Proposed changes (including videos or screenshots)

Continues the API endpoint migration (`docs/api-endpoint-migration.md`): moves the simplest remaining legacy `API.v1.addRoute()` endpoints to the typed `API.v1.get/post` pattern with AJV request/response validation. Endpoints already migrated in #41356 (omnichannel) are excluded.

### Migrated (4 single-route files)

| Endpoint | Method | File |
| --- | --- | --- |
| `audit/rooms.members` | GET | `apps/meteor/ee/server/api/audit.ts` |
| `chat.getMessageReadReceipts` | GET | `apps/meteor/ee/server/api/chat.ts` |
| `ldap.syncNow` | POST | `apps/meteor/ee/server/api/ldap.ts` |
| `engagement-dashboard/channels/list` | GET | `apps/meteor/ee/server/api/engagementDashboard/channels.ts` |

All four routes are **already declared** in the `Endpoints` interface (in `rest-typings` or locally), so — following the moderation pattern — the manual type entry is kept and **not** re-augmented via `ExtractRoutesFromAPI` (avoids `TS2717`).

### Elaborated response schemas (no weak `{ type: 'object' }`)

Per review feedback, response schemas are fully specified instead of `array of object`:

- `chat.getMessageReadReceipts`: `receipts` items reference the typia-generated `#/components/schemas/IReadReceiptWithUser`. `IReadReceiptWithUser` was added to the typia schema collection in `packages/core-typings/src/Ajv.ts` so the `$ref` resolves (it is auto-registered at startup via `apps/meteor/server/api/validation/ajv.ts`).
- `audit/rooms.members`: `members` items get an explicit property schema (`_id`, `name`, `username`, `nickname`, `status` enum, `avatarETag`, `federated`, `_updatedAt`) matching the `findUsersOfRoom` projection.
- `engagement-dashboard/channels/list`: each channel item has an explicit `room` object schema (`_id`, `name`, `ts`, `t`, `_updatedAt`, `usernames`) plus the numeric message counters, matching the aggregation projection.

### Behavior-preserving notes

- `chat.getMessageReadReceipts`: `validateParams` was absent; now uses `query: isChatGetMessageReadReceiptsProps` (existing validator). The manual `messageId` check is dropped in favor of query validation (missing `messageId` still returns 400).
- `engagement-dashboard/channels/list`: the internal `check()`/`Match` validation is **kept** inside the handler so the exact `Match error: ...` messages the e2e tests assert are preserved (no `query` validator introduced).
- `ldap.syncNow` / `audit/rooms.members`: error paths (`throw`, `notFound()`, 2FA) are unchanged; response blocks include the relevant `400/401/403/404` error validators.

## Issue(s)

Follow-up to #41356. Part of the ongoing `docs/api-endpoint-migration.md` effort.

## Steps to test or reproduce

- `tsc --noEmit` clean for all changed files.
- eslint + prettier clean for all changed files.
- Response schemas validate only under `TEST_MODE`; existing e2e suites for `audit`, `chat`, `LDAP` and `engagement-dashboard` cover these endpoints and assert unchanged status codes / error messages.

## Further comments

- No behavior change — pure refactor/typing; no changeset added (consistent with #41356).
- Draft while E2E is validated in CI.


Link to Devin session: https://app.devin.ai/sessions/daf03dc59cb54e958e31a9e9c72fb162

<!-- This is an auto-generated description by cubic. -->
<a href="https://cubic.dev/pr/RocketChat/Rocket.Chat/pull/41361?utm_source=github" target="_blank" rel="noopener noreferrer" data-no-image-dialog="true"><picture><source media="(prefers-color-scheme: dark)" srcset="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://www.cubic.dev/buttons/review-in-cubic-light.svg"><img alt="Review in cubic" src="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"></picture></a>
<!-- End of auto-generated description by cubic. --> 

 Task: [ARCH-2249]

[ARCH-2249]: https://rocketchat.atlassian.net/browse/ARCH-2249?atlOrigin=eyJpIjoiNWRkNTljNzYxNjVmNDY3MDlhMDU5Y2ZhYzA5YTRkZjUiLCJwIjoiZ2l0aHViLWNvbS1KU1cifQ
