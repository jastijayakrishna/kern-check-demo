# [Refactor] Move external issue-link parsing onto a provider registry

## What changed

Follow-up to #693 / #716. `parseExternalIssueReferences` hardcoded the GitHub and Linear URL shapes, and `fetchExternalIssueContext` hardcoded each provider's MCP call sequence. Both now read from a declarative registry — new `external-issue-providers.ts` — where each provider states:

- the hostnames it owns (`github.com`, `linear.app`),
- the pathname pattern that identifies one of its issues (named capture groups),
- how a match becomes ordered MCP fetch attempts (`{serverId, toolName, args}[]`), preserving GitHub's `issue_read` → `get_issue` fallback chain.

`fetchExternalIssueContext` walks the attempts generically under the existing shared 8-second fail-open deadline.

## What did not change

Pure internal refactor — no behavior change. URL extraction from message text, `MAX_EXTERNAL_ISSUES=2`, `MAX_EXTERNAL_CONTEXT_CHARS=8000`, the `[EXTERNAL ISSUE CONTEXT - UNTRUSTED REFERENCE MATERIAL]` format, all fail-open semantics, and the design boundary that the model never chooses fetch targets or arguments (parsing and fetching stay in deterministic server code).

## Why

Adding SCM support (GitLab, Bitbucket, Azure DevOps) previously meant editing parser internals. Now it's one registry entry next to the MCP server integration and its `mcp-policy.ts` allowlist. Note the `serverId` field is typed as `RouterMcpServerId`, so the type system forces a new provider to also register its MCP server and policy — the registry can't silently point at an unregistered backend. No real new provider is added here; the extensibility is proven by a fake GitLab entry in the new test.

## Tests

- New `external-issue-providers.test.ts`: GitHub mapping incl. fallback chain, Linear mapping, unclaimed-URL rejection (PR links, unknown hosts), and a single-entry fake GitLab provider.
- Existing `external-issue-context.test.ts` and `router-service.test.ts` untouched and green — 13 files, 98 tests passing; `pnpm knip` clean; `tsc --noEmit` clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
