# fix(core): honor an explicit spawn candidate even when Stage-1 contradictorily routes contexts=[simple]

## Problem

Live regression (demo-critical): for a genuine build request like **"build me a simple hello-world web page"**, Stage-1 sometimes returns the contradictory shape

```
contexts: ["simple"]  +  candidateActionNames: ["TASKS_SPAWN_AGENT"]  +  a chatty complete-looking ack
("Yep, you're the boss — I'm building it for you, no argument.")
```

`modelCommittedToDelegation` — the guard that protects an explicit spawn commitment from the complete-direct-reply override — required a **non-simple planning context** (`initialPlanningContexts.length > 0`). With `contexts=["simple"]` it never fired, so `shouldPreferCompleteDirectReply` treated `TASKS_SPAWN_AGENT` as a weak/injectable signal and kept the ack as the final reply. Net effect: **the bot said "I'm building it" and never spawned anything.**

## Fix

Drop the `initialPlanningContexts.length > 0` requirement from `modelCommittedToDelegation`. An explicit, **runnable** spawn/delegation candidate in the model's own candidate list — for a message that structurally looks like coding work (`looksLikeCodingWorkRequest`) — is a firm "delegate this" commitment, and must win even when the model *also* (contradictorily) routed `contexts=["simple"]`.

Still safe by construction:
- `looksLikeCodingWorkRequest` excludes creative-writing / explanation asks (a poem about an app, "how do I…") — those never trip it;
- the candidate must be a **registered** delegation action (`modelProvidedRunnableDelegationCandidate` resolves against the runtime registry), so a hallucinated action name never forces planning;
- when it fires, the `simple` marker is promoted to a real planning context (`["general"]`), the planner runs, and the spawn executes — the existing non-simple-context path is unchanged.

## Evidence (live, same agent, before/after)

- Before: cozy-dev users asked for builds; trajectory shows `contexts:["simple"] + candidateActionNames:["TASKS_SPAWN_AGENT"]` → ack delivered, no spawn, no app.
- After: "build me a simple hello-world web page please" → `TASKS_SPAWN_AGENT` executed, coding sub-agent built and deployed the page; live at a public URL within ~1 min (trajectory `tj-da1be617f605e3`, 2026-07-01).

## Tests

- New regression test: coding-work message + `contexts:["simple"]` + `candidateActionNames:["TASKS_SPAWN_AGENT"]` + complete-looking replyText → asserts `plan.simple === false`, `plan.requiresTool === true`, contexts promoted to `["general"]`, candidate preserved.
- The neighboring guards keep their existing tests: the non-simple-context spawn case, the only-acked case, and the poem/explanation direct-answer cases all stay green.
- Suites on this branch: `message-handler-bogus-candidates` + `message-routing` + `message-handler-output` → 3 files / 64 tests green. Core typecheck clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

