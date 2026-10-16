# fix(cli): skip trial plan warning for credit-only orgs

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary (AI generated)

- Skip the CLI "Trial expires..." upgrade warning when the org has active usage credits but no subscription plan
- Add **new** `has_usage_credits_org` SECURITY DEFINER RPC (1-arg + optional `appid`) instead of selecting `orgs.has_usage_credits` via RLS
- Add shared auth helper `request_has_org_or_app_read_access` (org read **or** app read) for that new RPC only
- **Do not modify** existing `is_paying_org(uuid)` / `is_trial_org(uuid)` — old CLI versions keep working unchanged
- CLI still calls legacy trial/paying RPCs with `{ orgid }` only; credits use the new RPC (with optional `appId`)

## Motivation (AI generated)

Credit-only orgs are a valid billing path. The CLI still nagged for a plan upgrade during trial. Reading `orgs.has_usage_credits` directly is not reliably readable under RLS for API-key callers, so the credit flag must come from an authorization-aware RPC. Changing existing billing RPCs would break older CLI versions still in the field.

## Business Impact (AI generated)

Stops false upgrade pressure for credit customers, keeps older Capgo CLI releases compatible, and reduces support noise around plan warnings.

## Test Plan (AI generated)

- [x] `bun run test:trial-warning` in `cli/`
- [x] `bun run build && bun run typecheck` in `cli/`
- [x] CI `Run CLI tests` + Capgo CLI integration tests
- [x] CI `Run backend SQL checks` (`46_test_org_status_rpcs.sql`)
- [x] Credit-only org (no plan) does not show the trial warning — covered by `test:trial-warning`
- [x] Unpaid trial org without credits still sees the warning — covered by `test:trial-warning`

Generated with AI
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-019faeef-71bf-7f57-b558-fab56b05dfdc"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-019faeef-71bf-7f57-b558-fab56b05dfdc"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>



<!-- This is an auto-generated description by cubic. -->
<a href="https://cubic.dev/pr/Cap-go/capgo.app/pull/2789?utm_source=github" target="_blank" rel="noopener noreferrer" data-no-image-dialog="true"><picture><source media="(prefers-color-scheme: dark)" srcset="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://www.cubic.dev/buttons/review-in-cubic-light.svg"><img alt="Review in cubic" src="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"></picture></a>
<!-- End of auto-generated description by cubic. -->



<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Bug Fixes**
  * Trial-expiration warnings are now shown only when an organization is unpaid, has an active trial, has no usage credits, and warnings are enabled.
  * Organizations with available usage credits no longer receive unnecessary trial-expiration warnings.
  * Usage-credit checks now respect organization and application access permissions.

* **Tests**
  * Added coverage for trial-warning scenarios and usage-credit access controls.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
