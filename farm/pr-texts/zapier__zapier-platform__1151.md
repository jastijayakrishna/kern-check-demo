# feature(core): v18, Add throwForThrottling middleware with backward-compatible default behavior (PDE-5232)

Adds new `throwForThrottling` middleware that handles 429 responses before `afterResponse` middleware runs, preventing accidental suppression of throttling responses that could interfere with proper rate limiting.

## Key Changes

- **New middleware**: `throwForThrottling` throws `ThrottledError` for 429 responses by default.
- **A switch flag**: `z.request()`'s `throwForThrottlingEarly` flag defaults to `true` in v18, which enables the new behavior. When set to `false`, you get the old behavior, where `afterResponse` can see 429 responses.
- **Global configuration**: Flag can be set via `app.flags.throwForThrottlingEarly` for UI apps to upgrade without breaking.

## Breaking Change in v18

In v18, the `throwForThrottling` middleware will run before `afterResponse` by default. This is breaking change because `afterResponse` won't be able to see any 429 responses.

To opt out:

- Per-request: Set `throwForThrottlingEarly` to `false` when calling `z.request()`
- Global setting: Set `flags.throwForThrottlingEarly` to `false` (see [`AppFlagsSchema`](https://github.com/zapier/zapier-platform/blob/19dff28b0e56d2dd2d752cd8075f1beae85c5d06/packages/schema/docs/build/schema.md#appflagsschema))

The UI apps will set `throwForThrottlingEarly` to `false` in the global setting, so the new behavior won't affect them.

## Usage

```javascript
// New default behavior in v18 - ThrottledError is thrown for 429, afterResponse can't see 429s (breaking change)
const response = await z.request({
  url: 'https://example.com/api'
});

// afterResponse can see 429s (backward compatible)
const response = await z.request({
  url: 'https://example.com/api',
  throwForThrottlingEarly: false
});

// Global setting for UI apps (default is true)
const app = {
  flags: {
    throwForThrottlingEarly: false  // Disable new throttling behavior globally
  }
  // ... rest of app
};
```

Ticket: https://zapierorg.atlassian.net/browse/PDE-5232

<!-- START COPILOT CODING AGENT TIPS -->
---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [Copilot coding agent tips](https://gh.io/copilot-coding-agent-tips) in the docs.
