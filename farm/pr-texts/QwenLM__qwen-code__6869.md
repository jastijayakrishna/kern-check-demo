# fix(shell): mark non-zero exits as failed

## What this PR does

Treats foreground shell commands with a non-zero exit code as failed tool calls while preserving their stdout, stderr, and exit diagnostics for the model and UI. Persisted failure status is respected during history replay, and web-shell chat summaries now show a localized failure label.

## Why it is needed

A shell process could exit with a non-zero code while producing no spawn error. That result was recorded and emitted as successful, so telemetry, ACP consumers, history replay, and web-shell could report completion even though the command failed.

## Reviewer Test Plan

### How to verify

Ask the agent to run `sh -c "echo non-zero-test; echo expected-failure >&2; exit 3"` exactly once. Confirm that the output and exit code remain visible, the tool result is recorded as error, telemetry reports `success: false`, ACP emits failed, and web-shell displays the localized failure label. Also confirm that zero-exit commands retain their existing completed display.

### Evidence (Before & After)

Before: the shell output contained `Exit Code: 3`, but the tool result was recorded as success and web-shell showed no failure status.

After: the raw session record contains `status: error` and `errorType: shell_execute_error`, telemetry contains `status: error` and `success: false`, the exported tool call is failed, and web-shell displays `Failed` or `执行失败` in the chat summary.

### Tested on

|     OS     | Status |
| :--------: | :----: |
|  🍏 macOS  |   ✅   |
| 🪟 Windows |  N/A   |
|  🐧 Linux  |  N/A   |

### Environment (optional)

Local source build with the daemon and web-shell.

## Risk & Scope

- Main risk or tradeoff: shell commands that intentionally use a non-zero code as control flow are now treated as failed unless the command handles that code, for example with `|| true`.
- Not validated / out of scope: legacy records already persisted as success cannot be inferred as failures, and signal-only termination without an exit code is unchanged.
- Breaking changes / migration notes: none.

## Linked Issues

N/A

<details>
<summary>中文说明</summary>

## 本 PR 做了什么

当前台 Shell 命令以非零退出码结束时，将其作为失败工具调用，同时为模型和 UI 保留 stdout、stderr 与退出诊断。历史回放会尊重持久化的失败状态，web-shell 会在聊天摘要中显示本地化失败标签。

## 为什么需要

Shell 进程可能以非零退出码结束，但不产生启动错误。此前该结果仍会被记录并发送为成功，导致 telemetry、ACP 消费方、历史回放和 web-shell 在命令失败时仍报告完成。

## Reviewer Test Plan

### 如何验证

要求 Agent 只执行一次 `sh -c "echo non-zero-test; echo expected-failure >&2; exit 3"`。确认输出和退出码仍然可见，工具结果记录为 error，telemetry 报告 `success: false`，ACP 发送 failed，web-shell 显示本地化失败标签。同时确认退出码为零的命令保持原有 completed 展示。

### Before 与 After 证据

Before：Shell 输出包含 `Exit Code: 3`，但工具结果记录为 success，web-shell 没有显示失败状态。

After：原始会话记录包含 `status: error` 和 `errorType: shell_execute_error`，telemetry 包含 `status: error` 和 `success: false`，导出的工具调用状态为 failed，web-shell 聊天摘要显示 `Failed` 或 `执行失败`。

### 测试平台

|     OS     | 状态 |
| :--------: | :--: |
|  🍏 macOS  |  ✅  |
| 🪟 Windows | N/A  |
|  🐧 Linux  | N/A  |

### 环境

本地源码构建，并运行 daemon 和 web-shell。

## 风险与范围

- 主要风险或权衡：有意将非零退出码用作控制流的 Shell 命令现在会被视为失败，除非命令自行处理该退出码，例如使用 `|| true`。
- 未验证或范围外：已经持久化为 success 的旧记录无法反推出失败；只有 signal 而没有退出码的终止行为保持不变。
- 破坏性变更或迁移说明：无。

## 关联 Issue

N/A

</details>
