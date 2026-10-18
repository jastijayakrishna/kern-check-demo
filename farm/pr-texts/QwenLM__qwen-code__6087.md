# feat(core): Disallow plan lifecycle tools in subagents

## What this PR does

This PR makes plan mode lifecycle ownership stay with the caller/main session by preventing ordinary subagents, workflow subagents, and in-process teammates from entering or exiting plan mode themselves. Subagents still inherit the parent PLAN constraints, but when they finish planning they now return the plan or findings to the caller instead of requesting `exit_plan_mode`.

It adds a shared runtime policy for subagent-like execution contexts, applies that policy consistently to subagent tool declaration filtering, direct filtered tool-call errors, runtime tool execution guards, ToolSearch exact selection, workflow subagent disallowed-tool floors, and plan-mode blocked-tool reminders.

It also applies the existing subagent/teammate control-plane exclusion floor to inline `FunctionDeclaration` tool configs, so inline declarations cannot bypass restrictions for coordination, task, cron, worktree, workflow, agent recursion, or plan lifecycle tools.

## Why it's needed

Issue #6083 tracks the next phase after the subagent approval-mode state fix. The remaining risk is that a subagent can still be instructed to use plan lifecycle tools that should belong to the main session, which can create confusing loops or workflow contract breaks when a subagent is in PLAN mode but should simply return its plan to the caller.

Keeping plan lifecycle tools out of subagent and team-agent tool surfaces aligns the behavior with caller-owned approval flow while preserving the existing main-session plan mode behavior and the `exit_plan_mode` always-loaded regression guard.

## Reviewer Test Plan

### How to verify

Run the targeted core regression suite and confirm ordinary subagent, teammate, workflow, ToolSearch, scheduler, and existing agent override tests pass. In particular, verify subagent tool declarations do not include `enter_plan_mode` or `exit_plan_mode`, explicit or inline tool configs cannot re-enable them, direct calls return a dedicated unavailable message, ToolSearch does not reveal or setTools for these tools in subagent contexts, and main-session `exit_plan_mode` inspection still works.

Run the root build and typecheck to confirm the repository still compiles.

### Evidence (Before & After)

N/A

### Tested on

|     OS     | Status |
| :--------: | :----: |
|  🍏 macOS  | ✅ tested |
| 🪟 Windows | ⚠️ not tested |
|  🐧 Linux  | ⚠️ not tested |

### Environment (optional)

macOS, Node.js/npm workspace. Commands run locally: `cd packages/core && npx vitest run src/agents/runtime/agent-core.test.ts src/tools/enterPlanMode.test.ts src/tools/exitPlanMode.test.ts src/tools/tool-search.test.ts src/agents/runtime/workflow-orchestrator.test.ts src/core/coreToolScheduler.test.ts src/tools/agent/agent.test.ts src/tools/agent/agent-override.test.ts src/tools/tool-registry.test.ts`; `npm run build && npm run typecheck`.

## Risk & Scope

- Main risk or tradeoff: Subagents and team agents can no longer use plan lifecycle tools even if a custom config explicitly lists them; this is intentional so plan lifecycle ownership stays with the caller/main session.
- Not validated / out of scope: This does not implement a Claude Code style teammate leader approval protocol, a generic loop detector, or any change to main-session plan mode behavior.
- Breaking changes / migration notes: Custom subagent or teammate configs that relied on calling `enter_plan_mode` or `exit_plan_mode` must return the plan or findings to the caller instead.

## Linked Issues

Closes #6083

<details>
<summary>中文说明</summary>

## What this PR does

这个 PR 让 plan mode 生命周期继续归调用方/主会话所有，普通 subAgent、workflow subAgent 和进程内 teammate 不能再自行进入或退出 plan mode。subAgent 仍然继承父会话的 PLAN 约束，但完成规划后会把计划或发现返回给调用方，而不是请求 `exit_plan_mode`。

它新增了一个共享的 subAgent-like 运行时策略，并把该策略一致应用到 subAgent 工具声明过滤、被过滤工具的直接调用错误、工具运行时兜底、ToolSearch 精确选择、workflow subAgent 的 disallowed-tool floor，以及 plan-mode 阻断工具时的 reminder。

它也会把既有 subAgent/teammate 控制面 exclusion floor 应用到 inline `FunctionDeclaration` 工具
