# feat(functions): derive default functions domain as function2.insforge.app

## Summary

Deno Deploy Classic (v1) is fully sunset, so the legacy `{appKey}.functions.insforge.app` domain no longer works. This PR points the SDK's derived default functions URL at the v2 CloudFront proxy domain `{appKey}.function2.insforge.app`, matching the backend's `FUNCTIONS_DOMAIN` default (`backend/src/infra/config/app.config.ts`).

## Changes

- `src/modules/functions.ts` — `deriveSubhostingUrl()` now derives `https://{appKey}.function2.insforge.app`; doc comment updated.
- `src/types.ts` — `functionsUrl` `@example` comment updated.
- `src/modules/__tests__/functions.test.ts` — test URLs updated. Note: the in-process dispatch short-circuit requires the configured `functionsUrl` to strictly equal the derived local URL, so the explicit URLs in tests must use the new domain.

## Behavior notes

- Explicitly configured `functionsUrl` is unaffected.
- Non-`.insforge.app` base URLs (self-hosted) still derive nothing and go through the `{baseUrl}/functions/{slug}` proxy path.
- If the direct subhosting URL returns 404, the SDK still falls back to the proxy path as before.

## Testing

- `npx vitest run src/modules/__tests__/functions.test.ts` — 11/11 pass.
- Full suite: 6 pre-existing failures in `ssr.test.ts` / `auth.test.ts` reproduce on clean `main` (verified via `git stash`), unrelated to this change. Same for the 5 pre-existing `npm run typecheck` errors caused by a local `@insforge/shared-schemas` version mismatch.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated description by cubic. -->
---
## Summary by cubic
Switch the SDK’s default functions domain to https://{appKey}.function2.insforge.app to align with Deno Deploy v2 and the backend default. Fallback to the proxy path remains; explicit `functionsUrl` and non-.insforge.app bases are unchanged.

- **Migration**
  - No action for most apps.
  - If you hardcode or test against https://{appKey}.functions.insforge.app, update to https://{appKey}.function2.insforge.app.

- **Dependencies**
  - Bump `@insforge/sdk` to 1.5.2.

<sup>Written for commit a1f4314ca62a674c38fbc43305f6e28147dae70e. Summary will update on new commits.</sup>

<a href="https://cubic.dev/pr/InsForge/InsForge-sdk-js/pull/121?utm_source=github" target="_blank" rel="noopener noreferrer" data-no-image-dialog="true"><picture><source media="(prefers-color-scheme: dark)" srcset="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://www.cubic.dev/buttons/review-in-cubic-light.svg"><img alt="Review in cubic" src="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"></picture></a>

<!-- End of auto-generated description by cubic. -->

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **Bug Fixes**
  - Updated Edge Functions URL routing to use the correct `function2.insforge.app` hostname.
  - Improved compatibility across subhosting, proxy fallback, in-process, and external deployment scenarios.

- **Documentation**
  - Updated configuration examples to reflect the current Edge Functions URL format.

- **Chores**
  - Updated the package version to 1.5.2.
<!-- end of auto-generated comment: release notes by coderabbit.ai --><!-- Macroscope's changelog starts here -->
> #### Changes since #121 opened
>
> - Derived default functions domain as `function2.insforge.app` [a1f4314]
> - Bumped package version from 1.5.1 to 1.5.2 and updated lock file [a1f4314]
> <!-- Macroscope's changelog ends here -->
>
<!-- Macroscope's pull request summary ends here -->
