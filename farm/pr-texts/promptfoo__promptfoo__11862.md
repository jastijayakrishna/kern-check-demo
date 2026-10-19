# fix(deps): update dependency @hono/node-server to v2.1.4

Updates `@hono/node-server` from 2.1.3 to 2.1.4 in the root package and the maintained `simple-mcp` and `redteam-mcp-agent` examples, keeping their explicit adapter pins aligned.

The [upstream patch](https://github.com/honojs/node-server/compare/v2.1.3...v2.1.4) widens the Hono peer range to accept Hono 5. Published runtime and type files are byte-identical to 2.1.3; our lockfile retains Hono 4.13.13 and the existing direct HTTP adapter integration.

Validation:
- 260 MCP/manifest tests passed, with 1 existing skipped test; repeated after merging current main.
- Local build passed. The built HTTP MCP server passed initialization, Unicode streamed tool calls, invalid-session/malformed-JSON/oversized-batch rejection, ambiguous HTTP framing rejection, and SSE cancellation/recovery checks.
- Local CLI evaluations with `--no-cache`: all 14 simple-MCP example cases and 2 ERP MCP inventory/orders cases passed, with score 1 and no errors.
- Dependency version consistency, scoped Biome formatting, and `git diff --check` passed. Audit reports no Hono or adapter advisories.

Local clean installation was blocked by the existing Socket release-age policy for Undici 7.30.1. Local validation used a private copy of the 2.1.4 adapter with previously installed dependencies; hosted CI validates the complete updated lockfile. No package policy was bypassed and no manifest or lockfile versions were downgraded.

