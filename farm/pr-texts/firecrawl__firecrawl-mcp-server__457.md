# feat(mcp): log agent hints surfaced by hosted tool calls

## Summary
- Emit one `[MCP_AGENT_HINTS]` stderr line per hosted (`CLOUD_SERVICE=true`) tool call that surfaces Firecrawl API `agent_hints`, so we can count and inspect the hints agents receive through MCP.
- Hooked into the shared `guardHostedTool` wrapper, so every tool is covered: successful results, `isError` results, and thrown errors.
- Fields: `tool_name`, `status`, `request_id` (joins to `[MCP_ACTION]` for team/user/key), `auth_type`, `profile`, `hint_count`, `hints` (each capped at 1,000 chars).
- Written to stderr like `[MCP_ACTION]`, so stdio transport is unaffected; no-op outside the hosted service.

## Test plan
- [x] `tests/agent-hints.test.mjs` asserts one log line per tool call with correct tool, status, count, and hints across all 10 transport cases
- [x] `npm test` — 133/133 pass
- [x] `tsc --noEmit` clean

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated description by cubic. -->
---
## Summary by cubic
Tracks the Firecrawl API `agent_hints` surfaced through hosted MCP tool calls so the hints agents receive can be counted and inspected.

- Emits one `[MCP_AGENT_HINTS]` stderr line per hosted tool call, covering successful results, `isError` results, and thrown errors via the shared `guardHostedTool` wrapper.
- Each line carries tool name, status, `request_id` (joins to `[MCP_ACTION]`), auth type, session profile, hint count, and hint text capped at 1,000 characters.
- Uses the session profile so companion search calls aren't attributed to the primary profile; empty `agent_hints` arrays log as `hint_count: 0`.
- No-op outside the hosted service and written to stderr, so local usage and the stdio transport are unaffected.
- Adds test coverage asserting one log line per tool call across all transport cases, waiting on stderr to avoid flakes.

<sup>Written for commit ab42a5f2899cefa46b454539bd3dfc8b8e0911dc. Summary will update on new commits.</sup>

<a href="https://cubic.dev/pr/firecrawl/firecrawl-mcp-server/pull/457?utm_source=github" target="_blank" rel="noopener noreferrer" data-no-image-dialog="true"><picture><source media="(prefers-color-scheme: dark)" srcset="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://www.cubic.dev/buttons/review-in-cubic-light.svg"><img alt="Review in cubic" src="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"></picture></a>

<!-- End of auto-generated description by cubic. -->
