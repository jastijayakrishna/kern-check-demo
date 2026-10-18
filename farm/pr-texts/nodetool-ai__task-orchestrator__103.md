# cwd=none tool policy + lightweight in-server executor

## Summary

Makes repo-less agent runs (`cwd_strategy: "none"` — the plan executor, chat, planner) genuinely lightweight: they're denied the filesystem/shell built-in tools, and they now execute **in the orchestrator process** instead of dispatching a worker Machine. The plan executor becomes a pure control plane that delegates all repo work to child workers.

Design spec: `docs/superpowers/specs/2026-07-06-cwd-none-tool-policy-design.md`.

## What changed

**1. cwd=none tool policy.** Today every run gets all built-in tools (the Claude backend runs `bypassPermissions` + the `claude_code` preset; the `allowsRepoWrite` flag was computed and discarded). Now `disallowedBuiltinsFor(cwdStrategy, allowsRepoWrite)` drives a denylist:
- `cwd=none` → denies `Read, Write, Edit, Bash, Grep, Glob, LS` (useless with no checkout; `Bash` is arbitrary shell we don't want a repo-less run — or an in-server run — to hold).
- read-only checkout (`repo_read`) → denies `Write, Edit`.
- else → nothing (unchanged).

Enforced on both backends: Claude gets authoritative `disallowedTools` (never offered); a shared `toolPolicyFactory` interceptor is the enforcement on pi and a backstop on Claude.

**2. Executor is repo-less.** `<execute>` defaults flip to `cwd_strategy: "none"` + profile `orchestrator,gh_pr,spawn`; the persona prompt is rewritten to stop instructing local repo reads — it grounds PR decisions via `gh_pr__pr_view/pr_diff` (GitHub API, no checkout) and delegates code inspection to children.

**3. In-server execution.** `dispatchRun` (the single choke point all launch/wake paths use) drives `cwd=none` runs in-process via `driveDispatchedRun` instead of spawning a worker Machine — safe because `runTransport()` is the DB loopback in-process, and the tool policy above keeps the server's secrets out of the agent's reach. Bounded for the single `--ha=false` server by a concurrency cap (`TASK_ORCH_IN_SERVER_MAX`, default 4) and a kill switch (`TASK_ORCH_DISABLE_IN_SERVER_RUNS=1`); excluded from the worker admission budget; the pending pump drains the worker and in-server capacity pools independently.

## The rule this establishes

`cwd_strategy: "none"` = the in-server-eligible, lightweight class (executor, chat, planner). Any run that materializes a checkout — the **PR reviewer** (`worktree_at_pr`) and implementor (`worktree`) — stays a worker: it needs the checkout, and the reviewer reads untrusted third-party code that must stay isolated from the server's env.

## Review

An adversarial review verified the lifecycle is sound: heartbeat-based orphan reaping works for an in-server claim with no container, the atomic `workerScope` claim prevents double-drive, the claim is always released, and the cwd=none tool policy holds so an in-server agent can't read `DATABASE_URL`/secrets. It found one blocking bug — the pump's single FIFO break starved one capacity pool behind the other — **fixed** in `72020d6`.

Non-blocking follow-ups (not addressed here): no deadlock-breaker for an in-server↔in-server `send_message(await=true)` chain (currently unreachable via normal spawn); and blast-radius tuning (idle chats hold an in-server slot up to ~10 min against the shared cap — consider separate chat/executor caps).

## ⚠️ Production behavior change

On deploy, `cwd=none` runs stop getting their own Fly Machine and run inside the single web-server process (bounded by the cap + kill switch). Intended, but a real shift for chat/planner too — not just the executor.

## Behavior changes worth noting
- Read-only (`repo_read`) runs lose `Write/Edit`. The reviewer is unaffected (reads + comments only); the **qa** persona was switched to `repo_write` since its job is writing tests.

## Testing
- New unit tests: policy resolver, cross-backend interceptor, executor defaults, in-server dispatch (drive vs spawn, cap defer, admission accounting).
- Full suite: **995 passed, 1 skipped, 0 failed**; `tsc --noEmit` clean.

🤖 Generated with [Claude Code](https://claude.com/claud
