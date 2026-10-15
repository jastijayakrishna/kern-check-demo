# agentHost: ESLint rule for deprecated Copilot SDK members

## What

Adds a type-aware local ESLint rule that flags the agent host's usage of `@deprecated` Copilot SDK members, and clears the one existing deprecated usage by removing a now-unneeded fallback.

### The rule
`local/code-no-deprecated-copilot-sdk` (`.eslint-plugin-local/code-no-deprecated-copilot-sdk.ts`) reports `@deprecated` members **only** when their declaration originates from `@github/copilot` / `@github/copilot-sdk`. Because it reads the `@deprecated` JSDoc tag straight from the SDK's `.d.ts` files, it **automatically picks up newly deprecated members whenever the SDK is updated** — so we notice (and migrate off) new deprecations on every SDK bump.

Unlike `@typescript-eslint/no-deprecated`, it stays focused on the SDK surface and won't flag VS Code's own same-named members. Wired into `eslint.config.js` as a **warning** scoped to `src/vs/platform/agentHost/**/*.ts` (type-aware, via `parserOptions.project`).

### The cleanup
The only deprecated usage was the `data.parentToolCallId` fallback in the history-replay path (`mapSessionEvents.ts`), kept only for sessions persisted before the `agentId` migration. Sub-agent events are now routed purely via the envelope-level `agentId`, matching the live-event path. The fallback is removed, `resolveParentToolCallId` simplified to take only `agentId`, and the old-format subagent fixture test + `subagent-session.jsonl` deleted (the new-format envelope-`agentId` test still covers the path).

## Verification
- `eslint src/vs/platform/agentHost/**/*.ts` → 0 deprecated-SDK warnings.
- `npm run typecheck-client` → clean.
- `npm run test-node` → 11362 passing, 0 failing (includes the subagent replay tests).

(Written by Copilot)
