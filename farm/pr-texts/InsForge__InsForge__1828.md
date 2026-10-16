# Move dashboard internal events from Socket.IO to SSE

## Summary

- add a JWT-only `GET /api/dashboard/events` SSE endpoint for Dashboard cache invalidation and MCP connection notifications
- move all Dashboard event producers off the shared Socket.IO room while leaving application-facing realtime `/socket.io` unchanged
- replace the Dashboard Socket.IO client with an authenticated fetch stream, token refresh, heartbeat handling, reconnect backoff, and reconnect cache reconciliation
- add a shared event schema and restore the previously missing `compute_services` invalidation
- remove `socket.io-client` from the Dashboard package

## Why

Dashboard control-plane notifications and developer-application realtime traffic currently share the same transport. A dedicated, explicitly named SSE endpoint gives the Dashboard a simpler one-way channel and makes infrastructure traffic classification deterministic without changing the public realtime protocol.

The endpoint only accepts a `project_admin` JWT. API keys, anon keys, and authenticated end-user JWTs are rejected.

## Validation

- `npm run format:check`
- `npm run lint` (passes with 3 pre-existing webscraper warnings)
- `npm run typecheck`
- `npm run build`
- Dashboard unit suite: 75 passed
- focused SSE/auth suites: 16 passed
- backend full suite: 2,086 passed, 21 skipped; one unrelated migration-boundary test fails because it scans pre-existing `.claude/worktrees/*` migration copies
- [Build and Push Docker Image](https://github.com/InsForge/InsForge/actions/runs/30664854680) with `v2.2.10-dashboard-sse-events`
- [Deterministic Fixture E2E](https://github.com/InsForge/agent-e2e/actions/runs/30665038239)

No `agent-e2e` fixture changes were needed because the public SDK/realtime contract is unchanged.

<!-- This is an auto-generated description by cubic. -->
---
## Summary by cubic
Moves Dashboard internal events from Socket.IO to SSE. Adds an admin‑credentialed `GET /api/dashboard/events` stream with resilient reconnect and batched cache invalidations; public `/socket.io` remains unchanged.

- New Features
  - Added SSE endpoint `GET /api/dashboard/events` protected by `verifyAdmin`; accepts project admin JWTs and API keys.
  - Introduced backend `DashboardEventService` and shared event schema in `@insforge/shared-schemas` for `ready`, `data-update`, and `mcp-connected` (removed unused `realtime` resource).
  - Switched producers to `DashboardEventService`; restored `compute_services` invalidations and qualified record-change names with resolved schema.
  - Replaced the Dashboard Socket.IO client with a fetch-based stream (`ApiClient.requestStream`), token refresh, heartbeats, exponential backoff, inactivity watchdog, and debounced query invalidations.
  - Documented the endpoint in `openapi/dashboard.yaml` and marked event `data` as optional.
  - Removed `socket.io-client` from `packages/dashboard`.
  - Dropped the per‑IP rate limiter; rely on admin gating and client backoff.

- Bug Fixes
  - Isolated listener failures so one subscriber can’t break delivery; client guards per-event handler errors and ignores malformed frames.
  - SSE stream cleans up on response error/close and releases the reader; client aborts half‑open streams after 60s and cancels bodies on non‑OK responses.
  - Deployment updates now invalidate both metadata and the deployments list.
  - Database events with unparseable table names now fall back to broad `records` invalidation.
  - MCP-connected notification is best‑effort after the usage record is written.
  - Tests: stubbed `JWT_SECRET` before route imports to ensure CI runs without local secrets.
  - Stopped joining sockets to `role:`/`user:` rooms since dashboard events no longer use Socket.IO.

<sup>Written for commit 0c3c649c15d8612f4a7e5c289a1d907826a28b6c. Summary will update on new commits.</sup>

<a href="https://cubic.dev/pr/InsForge/InsForge/pull/1828?utm_source=github" target="_blank" rel="noopener noreferrer" data-no-image-dialog="true"><picture><source media="(prefers-color-scheme: dark)" srcset="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://www.cubic.dev/buttons/review-in-cubic-light.svg"><img alt="Review in cubic" src="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"></picture></a>

<!-- End of auto-generated description by cubic. -->

<!-- Macroscope's pull request summary starts here -->
<!-- Macroscope will only edit the content between these invisible markers, and the markers themselves will not be visible in the GitHub rendered markdown. -->
<!-- If you delete either of the start / end markers from your PR's description, Macroscope will append its summary at the bottom of the description. -->
> [!NOTE]
> ### Replace Socket.IO dashboard events with a Server-Sent Events stream
> - Introduces a `DashboardEventService` singleton on the backend that provides in-process pub/sub, replacing all `SocketManager` broadcast calls across auth, database, storage, functions, compute, and deployment routes.
> - Adds a `GET /api/dashboard/events` SSE endpoint protected by a new `verifyProjectAdminJwt` middleware that rejects API keys and anon tokens.
> - On the frontend, replaces `SocketContext` and `socket.io-client` with a `DashboardEventsProvider` that reads the SSE stream, parses events via a shared zod schema, and debounces react-query cache invalidations with backoff reconnect.
> - Adds `ApiClient.requestStream` for authenticated long-lived fetch requests with a single 401 refresh retry.
> - Behavioral Change: Socket.IO is no longer used for dashboard data updates; clients must connect to the SSE endpoint with a project admin JWT instead.
>
> <!-- Macroscope's changelog starts here -->
> #### Changes since #1828 opened
>
> - Added inactivity timeout mechanism to `DashboardEventsProvider` to detect and recover from half-open SSE connections [7e56a08]
> - Wrapped dashboard event listener invocations in error handling to isolate failures [7e56a08]
> - Added optional `onActivity` callback parameter to SSE stream consumption functions for stream liveness monitoring [7e56a08]
> - Changed dashboard data-update events to use schema-qualified table identifiers [7e56a08]
> - Updated `getDashboardInvalidationKeys()` to return both deployment metadata and deployments list query keys for deployment data-update events [7e56a08]
> - Added module-level test setup to establish JWT secret and mock SecretService before imports [a5f1433]
> - Added rate-limited SSE endpoint for dashboard events [1aff0df]
> - Implemented error handling and resource cleanup for SSE event streams [1aff0df]
> - Added fallback to broad invalidation key when database table references cannot be parsed [7b6e76a]
> - Updated SSE event schema documentation to clarify optional data field [7b6e76a]
> <!-- Macroscope's changelog ends here -->
>
> <!-- Macroscope's review summary starts here -->
>
> <sup><a href="https://app.macroscope.com">Macroscope</a> summarized 9adcd81.</sup>
> <!-- Macroscope's review summary ends here -->
>
<!-- Macroscope's pull request summary ends here -->

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Dashboard updates now stream in real time, keeping data and activity views synchronized without manual refreshes.
  * Improved reliability with automatic reconnection, keepalive handling, and batched updates.
  * MCP connection activity and onboarding analytics now update through the dashboard event stream.
  * Streaming requests automatically refresh expired authentication tokens.
* **Documentation**
  * Added API documentation for the authenticated dashboard event stream.
* **Tests**
  * Added coverage for event delivery, reconnection, parsing, authentication refresh, and cache invalidation.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
