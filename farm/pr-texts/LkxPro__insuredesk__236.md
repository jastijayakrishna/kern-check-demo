# feat(agent-loop): commit message 由 worker 收尾生成,controller -F 提交

## 什么

agent loop 的 commit message 从硬编码 `agent: resolve issue #NNN` 改为 worker 收尾生成的 Conventional Commits:squash merge 后 main 上的提交即该 message。

- check 全过后,复用 implementation 会话跑收尾小轮(warm,~80 词一次性 prompt),按 `<type>: <摘要>` + 2–3 行 body + `Refs #N` 写 `.agent-commit-message`
- 文件经 `git rev-parse --git-path info/exclude` 对所有 git 检测隐身
- controller 仍是唯一 committer:`git commit -F`,缺文件兜底 `chore: <issue 标题>` 并在 Issue 评论留痕,管线不阻断
- **业务 prompt 零改动**,AGENTS.md 契约零改动(historyUnchanged 守卫原样)

## 顺带根治

repair 流程此前是双 commit(controller 在已推送 commit 上再 commit),squash 标题回落成 PR 标题;现改为 `--amend` 重写 + `--force-with-lease` push。

## 测试

- worker.test.ts:happy path 断言分支恰好 1 commit 且 message 为 worker 所写;pause_turn 断言缺 message 时兜底 `chore: Test task` 不阻断;hijack 测试原样(模型碰历史 → fatal)
- `make check` 全绿

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Automated workflows now generate standardized commit messages before publishing changes.
  * Published updates use the generated message to improve clarity in project history.
  * Recovery runs now update the existing commit instead of creating unnecessary additional commits.
* **Bug Fixes**
  * Added a fallback commit message when message generation is unavailable.
  * Publication comments now indicate when the fallback message was used.
* **Documentation**
  * Updated workflow documentation to clarify commit-message generation and publishing responsibilities.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
