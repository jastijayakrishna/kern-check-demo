# fix(daemon): lead the collaboration guidance with a tool-precedence rule (#800)

## What

Adds one leading bullet to the standing collaboration guidance (every session carries it): AgentConnect's MCP tools are the **only** channel that reaches other agents and humans; runtime built-ins with similar names (e.g. Claude Code's bare `SendMessage`) do not reach AgentConnect and anything sent through them is lost — never use them for messaging, reporting back, or collaboration. Cost: ~330 chars ≈ ~80 standing tokens per session. Pinned by a contract test that also asserts the bullet LEADS the section (the collision fires exactly when the model is choosing a messaging tool).

## Why

Issue #800, measured in the tool-surface A/B (PR #791, 2026-08-09): on the Claude Code runtime a child session's tool list contains both `mcp__agentconnect__sendMessage` and the runtime's own built-in `SendMessage` (agent-teams messaging). In 3 of 6 parent-report trials the model's first attempt went to the built-in — a literal name match for the report-back instruction — and 2 of 6 trials lost the parent's answer entirely, silently.

## Measured before/after (parent-session scenario, same harness as #791; criteria fixed before looking)

| Metric | Before (6 trials) | After (10 trials, 5 per surface arm) |
| --- | --- | --- |
| Trials with any built-in `SendMessage` attempt | 3/6 | **0/10** (verified in scored attempts AND raw ACP events) |
| Answers lost to the built-in | 2/6 | **0/10** |
| Total success (parent actually woken with the answer) | 4/6 | **10/10** |
| First-attempt correct form | 0/6 | 4/10 |

The collision is eliminated in this sample and no answer was lost. First-attempt behavior improved but is not perfect — the child still sometimes wraps the correct parent reply in extra (legal) postless calls — so #800's deeper fixes (suppress the built-in tool for daemon-owned sessions; reply-hint the exact pre-filled call; inferred reply) remain worthwhile hardening.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
