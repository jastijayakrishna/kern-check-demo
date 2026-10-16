# fix(init): use @sanity/icons v5 de-barrelled imports in templates

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
### Description

`sanity init` templates (especially Next.js blog schema) still barrel-imported from `@sanity/icons` and pinned v2/v3. With `@sanity/icons` v5, icons should be imported via de-barrelled paths like `import {UserIcon} from '@sanity/icons/User'`.

This updates:
- Next.js blog schema template strings
- Shopify / Shopify Online Storefront / get-started filesystem templates
- Template dependency pins to `@sanity/icons` `^5.0.0`
- Next.js blog package install to `@sanity/icons@5`
- Template `@sanity/ui` pins to `^3.5.0` (get-started was still on `^2.0.0`; shopify/app templates aligned)

`app-quickstart` does not use `@sanity/icons` / needs no icon changes.

### What to review

- Icon import path convention: `@sanity/icons/<Name>` (strip trailing `Icon`)
- Dependency version bumps in `getStarted` / `shopify` / `shopifyOnline` / `appSanityUi` templates
- Next.js init installs `@sanity/icons@5` for the blog template

### Testing

- Added unit tests in `packages/@sanity/cli/src/actions/init/templates/__tests__/icons.test.ts` covering Next blog schema sources, `@sanity/icons` v5 / `@sanity/ui` v3 template dependency versions, and a scan of filesystem templates for barrel imports
- `pnpm test:unit icons.test` passed
- Format / ESLint / `pnpm check:types` / `pnpm check:deps` passed for the change set

### Notes for release

Update init templates to use `@sanity/icons` v5 with de-barrelled import paths, and bump template `@sanity/ui` to v3.5

<!-- CURSOR_AGENT_PR_BODY_END -->

[Slack Thread](https://sanity-io.slack.com/archives/C3Q637VGW/p1785356866485649?thread_ts=1785356866.485649&cid=C3Q637VGW)

<div><a href="https://cursor.com/agents/bc-9d95db7a-d3be-5993-91e9-672d9906f987"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-9d95db7a-d3be-5993-91e9-672d9906f987"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
