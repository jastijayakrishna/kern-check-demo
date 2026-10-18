# fix(agent-loop): 关单杀 worker 并修 dispatch tick 清理韧性

## 背景

dispatch tick 的已关单清理段 (`dispatch.ts`) 有两个韧性缺陷,根因实例为 `.worktrees/issue-242` 空壳导致 daemon 30s 重试死循环:

1. 单个 worktree 清理失败(`git worktree remove` 等未保护调用抛错)会杀死整个 tick;
2. 已关 issue 的 worker 仍活着时只 defer 永不处理,worktree/branch/claim 永久悬挂。

## 改动

- **关单杀 worker**:新增 `killLiveWorker` — 首 tick `SIGTERM` 进程组并把 pid 记入 `.killing`,下轮同 pid 仍活升 `SIGKILL`;pid 变了(重领的新 worker)从 SIGTERM 重新计。
- **韧性修复**:清理循环 per-item try/catch,单条目失败打印日志继续;4 处未保护调用收敛进 `cleanupClosedIssue`。
- **目录壳兜底**:`worktree remove` 失败 → `worktree prune` + `rm -rf`;分支名读不到按 `codex/issue-N` 约定回退。
- **`.killing` 生命周期**:纳入 `artifactCleanup` 与 spawn 前残留清理。

## 测试

- `cleanupClosedIssue` 正常清理(worktree/分支/产物全清)
- 注册缺失只剩目录壳:不抛且壳被清
- `killLiveWorker` SIGTERM → SIGKILL 升级(真进程组)
- `make check` 全绿

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Bug Fixes**
  * Automatically stops workers associated with closed issues, escalating from a graceful shutdown to forced termination when needed.
  * Cleans up closed-issue resources, including claims, worktrees, branches, and related artifacts.
  * Prevents cleanup failures for one issue from interrupting processing of others.


<!-- end of auto-generated comment: release notes by coderabbit.ai -->
