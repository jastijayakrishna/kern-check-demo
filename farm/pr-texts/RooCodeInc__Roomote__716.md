# [Improve] Gate the linked-issue fetch on the routing precheck; default routing to Gemini 3.6 Flash

## What changed

Follow-up to #693.

**Two-step gate.** `gatherContextFromConfiguredMcps` now runs a tool-free routing precheck first and only calls `gatherExternalIssueContext` when the precheck returns `needsExternalLookup=true` — finally wiring the signal that has been telemetry-only since the old two-step design. When context is fetched, routing runs once more with the issue as untrusted reference material and reports `phase: 'mcp'` with the tools used. Fail-open is unchanged: an unavailable integration, inaccessible issue, or empty fetch keeps the precheck decision (`phase: 'direct'`).

**Routing model default.** Workspace routing (Slack/Linear/Discord/etc. and GitHub paths) now resolves its model as `context.routingModel` → new `R_ROUTER_MODEL` deployment override → `google/gemini-3.6-flash`, instead of falling through to the deployment-wide small model. The decision's debug `model` field now reports the actual resolved model instead of the `roomote-small-model` placeholder.

## Why

#693 paid the issue-fetch deadline (up to 8s) on every routing call containing a pasted GitHub/Linear issue link, even when the message alone already routed. In the router external-lookup gate eval (24 labeled cases × 4 repetitions × 5 candidate models, run against the production routing prompt), roughly two-thirds of link-bearing messages routed correctly with no fetch — and Gemini 3.6 Flash was the only stable gate: 0% false lookups and 100% lookup recall in every repetition, at ~4.5s p50 per call. Fetched issue context took genuinely ambiguous links from ~50% blind accuracy to 100% for every model, so the fetch stays — it just only runs when it can change the decision.

Trade-off: when a lookup **is** needed, routing now costs two model calls plus the fetch (one extra call vs #693). The eval says that's the minority of link-bearing tasks.

## Tests

- Reworked the #693 routing test for the gated flow (precheck asks → fetch → informed re-route, `phase: 'mcp'`).
- New: precheck routes without external context → no MCP call, single model call, `phase: 'direct'`.
- New: precheck asks but fetch fails → precheck decision stands, fail-open.
- `vitest run src/server/router`: 12 files, 94 tests green; slack router-debug/auto-route consumers green; `tsc --noEmit` clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
