# Migrate 10 rate limits to assertRateLimit

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary
- Migrates 9 throw-on-failure `await ratelimit(...).limit(...)` call sites to `assertRateLimit` with shared `RATELIMIT_POLICIES`
- Preserves existing attempt/window limits and custom error messages
- Skips sites that need remaining/headers or use rate limit success as a soft throttle (auth last-used, publishable keys, Shopify pixel soft-skip, etc.)
- Leaves `ratelimitOrThrow` in `apps/web/lib/api/utils.ts` on the original `ratelimit().limit()` path

### Migrated call sites
1. `POST /api/links` (anonymous create)
2–3. Partner-profile + embed social content stats (shared policy)
4–5. Invite referral email (workspace + target)
6–8. Merge partner accounts (steps 1–3)
9. Domain search availability

## Test plan
- [ ] Confirm TypeScript/build passes for changed files
- [ ] Spot-check one API route (e.g. anonymous link create) returns `rate_limit_exceeded` with the same message when limited
- [ ] Spot-check invite referral / merge partner account actions still surface the previous rate-limit error text
- [ ] Confirm `ratelimitOrThrow` callers (metatags, qr, providers, etc.) are unchanged
<!-- CURSOR_AGENT_PR_BODY_END -->

[Slack Thread](https://dub.slack.com/archives/C07H0T3SX97/p1790321527880379?thread_ts=1790321527.880379&cid=C07H0T3SX97)

<div><a href="https://cursor.com/agents/bc-f05825ba-88d5-5ba3-ae59-cad3a41ae088?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-f05825ba-88d5-5ba3-ae59-cad3a41ae088&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>



<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **Usage Limits**
  * Limits apply to social content statistics, domain availability searches, anonymous link creation, partner account merges, and referral email invitations.
  * Social content statistics are limited to 10 requests per hour, domain searches to one every five seconds, anonymous link creation to 10 per day, and partner account merges to three attempts per 24 hours.
  * Referral invitations are limited to five per workspace per minute and two per recipient every two hours. These limits are applied consistently across the related actions.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
