# fix: resolve pnpm hoisting issue with StorybookConfig type imports

## Problem

When using pnpm without hoisting (e.g., without `shamefully-hoist=true`), users cannot import types from `@storybook-vue/nuxt` directly because the package is not available at the top-level `node_modules`. This causes TypeScript compilation errors when trying to use:

```typescript
import type { StorybookConfig } from '@storybook-vue/nuxt'
```

## Solution

This PR fixes the issue by ensuring that all types from `@storybook-vue/nuxt` are properly re-exported through `@nuxtjs/storybook`, allowing users to import types directly from the main package:

```typescript
import type { StorybookConfig } from '@nuxtjs/storybook'
```

## Changes Made

1. **Fixed package.json exports**: Updated `packages/nuxt-module/package.json` to point to the correct `.d.mts` TypeScript declaration files instead of non-existent `.d.ts` files.

2. **Updated examples**: Changed import statements in playground and examples to use `@nuxtjs/storybook` instead of `@storybook-vue/nuxt`.

3. **Updated documentation**: Modified the configuration documentation to show the correct import pattern.

## Technical Details

The fix leverages the existing `export * from '@storybook-vue/nuxt'` in the nuxt-module source code, which already re-exports all types including `StorybookConfig`. The main issue was that the package.json exports weren't pointing to the correct TypeScript declaration files, preventing proper type resolution.

Now users can safely import types using either pattern, but the recommended approach is to import from `@nuxtjs/storybook` to avoid pnpm hoisting issues.

This solution works in both hoisted and non-hoisted pnpm environments without requiring users to configure `shamefully-hoist=true`.

Fixes #920.

> [!WARNING]
>
> <details>
> <summary>Firewall rules blocked me from connecting to one or more addresses</summary>
>
> #### I tried to connect to the following addresses, but was blocked by firewall rules:
>
> - `api.iconify.design`
>   - Triggering command: `node (vitest 1)` (dns block)
> - `fonts.bunny.net`
>   - Triggering command: `node (vitest 1)` (dns block)
> - `storybook.js.org`
>   - Triggering command: `node /home/REDACTED/work/storybook/storybook/playground/node_modules/.bin/../storybook/bin/index.cjs build` (dns block)
>   - Triggering command: `node /home/REDACTED/work/storybook/storybook/examples/starter/node_modules/.bin/../storybook/bin/index.cjs build` (dns block)
>
> If you need me to access, download, or install something from one of these locations, you can either:
>
> - Configure [Actions setup steps](https://gh.io/copilot/actions-setup-steps) to set up my environment, which run before the firewall is enabled
> - Add the appropriate URLs or hosts to my [firewall allow list](https://gh.io/copilot/firewall-config)
>
> </details>



<!-- START COPILOT CODING AGENT TIPS -->
---

💬 Share your feedback on Copilot coding agent for the chance to win a $200 gift card! Click [here](https://survey.alchemer.com/s3/8343779/Copilot-Coding-agent) to start the survey.
