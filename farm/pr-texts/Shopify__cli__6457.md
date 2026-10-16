# Fix Bugsnag inProject detection by setting projectRoot to null

## Summary

- Upgraded Bugsnag SDK from 7.25.0 to 8.6.0
- Set `projectRoot: null` explicitly in Bugsnag configuration to disable SDK-side inProject detection

## Problem

Bugsnag's `plugin-node-in-project` was incorrectly marking all CLI stack frames as `inProject: false` in Observe. This prevented proper error grouping and made it harder to identify which errors originated from CLI code vs dependencies.

The root cause: if `projectRoot` is not explicitly set, Bugsnag defaults it to `process.cwd()` (the user's current directory). Since CLI errors can occur from any working directory, this resulted in all frames being marked as outside the project.

## Solution

By setting `projectRoot: null` explicitly, we disable Bugsnag's client-side inProject detection entirely. This allows Observe's smarter server-side algorithm to determine which stack frames are in-project, resulting in better error grouping.

## Test plan

1. Make local code changes to point to sandbox and enable reporting in dev:
   - In `packages/cli-kit/src/public/node/error-handler.ts`:
     - Comment out the `isLocalEnvironment() || settings.debug` check (lines 67-70)
     - Change endpoints to sandbox URLs (lines 285-286)
   - In `packages/cli-kit/src/public/node/error.ts`:
     - Add line to `cleanSingleStackTracePath` to replace local paths with `@shopify/cli/` prefix:
       ```ts
       .replace('/Users/yourname/path/to/cli/packages/cli/', '@shopify/cli/')
       ```

2. Build and install the CLI locally:
   ```sh
   pnpm build && pnpm bundle-for-release
   npm install -g ./packages/cli
   ```

3. Trigger a test error:
   ```sh
   shopify app dev --invalid-flag
   ```

4. Check Observe (sandbox) to verify:
   - Stack frames show paths like `@shopify/cli/dist/chunk-XYZ.js`
   - Stack frames no longer have `inProject: false` incorrectly set
   - Error grouping works correctly for CLI errors

## Context

See https://github.com/bugsnag/bugsnag-js/blob/286caed5daae9349be8fb22ab0051204bfc1a813/packages/plugin-node-in-project/in-project.js for the plugin implementation.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
