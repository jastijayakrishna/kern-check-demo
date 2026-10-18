# feat(agent-loop): daemon 常驻韧性 + 相耗时落账 + review∥check 并行

Dogfood 实证调优:issue #244 全闭环零人工介入(实现→复审→check→发布→合并→清理),期间发现并修复 6 个韧性/效率问题。

## 修复

- **daemon 脱离启动会话存活**:新增 `daemon --detach` / `make agent-loop-daemon-start`(setsid + 日志落 `.worktrees/daemon.log` + 幂等);`CLAUDE_CODE_SESSION_ID`/`CLAUDE_PID`/`VSCODE_*`/`GIT_ASKPASS` 等会话身份变量不再渗入 worker 与其 claude 子进程(父会话退出曾连带杀整树)
- **冷启动死锁**:全新 clone 无 `.worktrees` 时 DirLock 非递归 mkdir 永远拿不到锁,daemon 静默假死;启动前 `mkdir -p` 修复
- **关单远端 claim 槽位回收**:认领者死于发布窗口会永久占用 slot(实证 #242 关单后 slot 1 泄漏);每 tick 扫远端 claim ref,关单即 CAS 释放,远端残 worker 经心跳丢失自灭
- **biome 嵌套误报**:worktree 内 lint 关闭 VCS 集成后 biome 扫进嵌套 worker 检出,报 nested root config;显式排除 `.worktrees`/`.claude/worktrees`
- spawnWorker 父进程 log fd 泄漏;`commit-message.json` 纳入产物清理

## 可观测性

- PhaseTimer:发布/失败评论附 `⏱ implementation → review → check …` 相耗时分解(此前数据随产物清理消失,调优只能靠 GitHub 时间戳重建)
- daemon.log 每行带 ISO 时间戳

## 效率

- **review ∥ check 快照并行**:check 在快照 worktree(起跑头+diff)与 review 并发;review 未改码采信快照结果,改码作废重跑。质量门不变(发布的码必过 check)。按 #244 实测比例,干净 review 省约 25% worker 墙钟

## 测试

- 新增 5 个用例:env 净化、关单 claim 清扫(保留未关单)、快照采信、快照作废重跑;agent 套件 55/55,`make check` 全绿

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Added detached daemon startup with process ID and log-location reporting.
  * Daemons can continue running after the launching session exits, with macOS support to prevent sleep interruptions.

* **Bug Fixes**
  * Automatically releases claims associated with closed issues.
  * Improves worker isolation by removing inherited session-specific environment settings.

* **Improvements**
  * Enhanced worker progress reporting with phase timing and clearer retry updates.
  * Optimized review and validation checks, including safer retries and improved recovery behavior.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
