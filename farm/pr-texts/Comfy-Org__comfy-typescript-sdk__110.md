# fix(models): follow Comfy Router's move to /v2/models

## What
The Comfy Router service moved its model routes from `/v1/models/{provider}/{model}` to `/v2/models/…`. The SDK's hand-written path template still said `/v1`, so every `models.run` against the live service answered a bare 404 — caught by the first-ever live run of the two-SDK Router smoke suite, and reproduced with a raw curl (`/v2` → 200 with a real generation, the SDK's path → 404).

This PR **includes the open vendored-spec sync PR** (which was sitting red precisely because the synced spec moved to /v2 while the code said /v1) and flips the path template, docs, and tests to match, so the spec↔code contract check passes again.

## Verified
- Full test suite green locally (python: 694 passed / ts: 389 passed; the 17 `credentials.test.ts` failures on the TS side pre-exist on the sync base unchanged — local Node environment, not this change)
- Hygiene + drift/contract checks pass locally
- Live: raw POST to `/v2/models/recraft/recraftv2` on staging returns 200 with a generation; the `/v1` path 404s

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Supersedes #109 (merging this closes it). Sibling: Comfy-Org/comfy-python-sdk#117.

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **API Updates**
  - Model catalog, lookup, execution, and schema endpoints now use the `/v2` API routes.
  - Model schema responses now include both input and output schemas.
  - API-key authentication is now supported alongside bearer authentication.
  - Added clearer retry, error, and idempotency behavior, including replay and conflict handling.
- **Documentation**
  - Updated SDK, API reference, and changelog documentation to reflect the new routes and capabilities.
- **Bug Fixes**
  - Corrected model execution requests to target the current router endpoint.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
