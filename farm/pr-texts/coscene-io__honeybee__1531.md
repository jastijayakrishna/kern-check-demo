# fix: match recommended layouts by device_type_match

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
**User-Facing Changes**
A record `deviceType` now selects one recommended-layout robot and configuration through `device_type_match`, including display names that are not the robot slug.

**Description**
Ports the shared `device_type_match` behavior from bombus #233 (https://github.com/coscene-io/bombus/pull/233).

Honeybee passes `record.customMetadata.attributes.deviceType` into `matchRecommendedLayoutDeviceType`. Listing and automatic selection read only that robot and configuration. Non-`_default` layout ids gain a `:config=` suffix so two configurations that share a file stay distinct. Existing `_default` ids stay the same.

If video metadata selects H.264 but the matched configuration has no selectable H.264 viewer layout, automatic selection falls back to the default viewer layout in that same configuration. The fallback uses the default layout ID and URL and never crosses configurations.

Not included, because they are Starbase-only: `getDeviceType`, collection-task upstream resolution, endpoint roles, and `hasH264Topic`. `useSyncLayoutFromUrl` is unchanged.

**Validation**
- Regression cases fail before the fallback fix and pass afterward.
- Related layout service, provider, URL synchronization, and layout button suites: 4 suites / 65 tests passed.
- `yarn run tsc --noEmit`, `yarn typecheck:ci`, targeted Oxlint/ESLint/Prettier, and `git diff --check` passed.
- Full application browser validation was not performed.

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-45217de9-e448-568f-8a29-3f73f6489c9b?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-45217de9-e448-568f-8a29-3f73f6489c9b&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
