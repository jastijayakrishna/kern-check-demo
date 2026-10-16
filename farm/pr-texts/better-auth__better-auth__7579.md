# test(telemetry): add coverage for undefined BETTER_AUTH_TELEMETRY_ENDPOINT

Addresses review feedback on #7578 requesting test coverage for the early return behavior when `BETTER_AUTH_TELEMETRY_ENDPOINT` is undefined.

**Changes:**

- Added test verifying noop publisher is returned when endpoint is undefined, without making HTTP requests
- Fixed early return condition to allow `customTrack` (test utility) to bypass the endpoint check: `!telemetryEndpoint && !context?.customTrack`
- Added defensive guard in `track()` to prevent calling `betterFetch` with undefined endpoint: changed `else` to `else if (telemetryEndpoint)`

The original early return logic broke existing tests that use `customTrack` to intercept telemetry events. The fix ensures tests work while still short-circuiting in production when no endpoint is configured.

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/better-auth/better-auth/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.

<!-- This is an auto-generated description by cubic. -->
---
## Summary by cubic
Adds test coverage and safeguards for telemetry when BETTER_AUTH_TELEMETRY_ENDPOINT is undefined, per feedback on #7578. Ensures customTrack works in tests and prevents HTTP calls without an endpoint.

- **Bug Fixes**
  - Return noop publisher when no endpoint unless customTrack is provided.
  - Guard track() to only call betterFetch if telemetryEndpoint exists.
  - Add test verifying betterFetch is not called when the endpoint is missing.

<sup>Written for commit 393824d932cf096a6184fcf7c1e5c0737267340a. Summary will update on new commits.</sup>

<!-- End of auto-generated description by cubic. -->
