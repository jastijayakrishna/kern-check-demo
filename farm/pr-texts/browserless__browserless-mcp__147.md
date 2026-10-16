# feat: include rationale in browserless_agent analytics event

## Summary

- Adds `rationale: params.rationale ?? null` to the `sendAnalytics` closure in `src/tools/agent.ts`, so every `MCP Tool Request` event for `browserless_agent` now includes the LLM-supplied intent string.

## Changes

In `src/tools/agent.ts` (the `sendAnalytics` closure ~line 367), the properties object passed to `analytics?.fireToolRequest(token, 'browserless_agent', {...})` now includes:

```ts
rationale: params.rationale ?? null,
```

`rationale` is a top-level optional string on `AgentParamsSchema` (defined in `src/tools/schemas.ts:700-716`) — a ≤50-char present-continuous label the LLM provides per call (e.g. "Logging in", "Filling the search form").

**Privacy note:** `event_properties` are sent to SQS (see `src/lib/analytics.ts`). This change now ships the free-text `rationale` string — which is LLM-generated intent, not raw end-user conversation — through the same pipeline. The field is capped at 50 chars by schema description and contains only action summaries, so the added PII exposure is minimal.

## Test plan

- [x] `npm test` passes locally (439 passing)
- [x] `npm run build` passes locally (type-checks clean)
- [ ] N/A — no new dependencies, no runtime behaviour change beyond analytics payload

## Checklist

- [x] My commits follow the conventional-commit prefix convention
- [x] I have not introduced new dependencies without flagging them in the summary

Link to Devin session: https://app.devin.ai/sessions/679a080a73264dda9026d574edb4874c
Requested by: @xsvfat
<!-- devin-review-badge-begin -->

---

<a href="https://app.devin.ai/review/browserless/browserless-mcp/pull/147" target="_blank">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://static.devin.ai/assets/gh-open-in-devin-review-dark.svg?v=1">
    <img src="https://static.devin.ai/assets/gh-open-in-devin-review-light.svg?v=1" alt="Open in Devin Review">
  </picture>
</a>
<!-- devin-review-badge-end -->

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **Bug Fixes**
  - Analytics events now include the reasoning field when available, improving completeness of recorded usage data.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
