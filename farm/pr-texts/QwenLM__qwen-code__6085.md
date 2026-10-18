# Fix ACP daemon loop review follow-ups

## What this PR does

This PR lands the follow-up fixes from the review of the already-merged ACP daemon loop guard PR. It makes loop detection a terminal ACP turn path that preserves the final tool-response context, adds a stable invalid-tool bucket so changing error text cannot evade the 3-strike guard, stops unstarted concurrent Agent work once the shared guard fires, and applies the same invalid-call guard to early tool rejection paths.

## Why it's needed

PR #6076 was merged before these review fixes landed, so main still lacks several safety hardenings around daemon loop detection. Without this follow-up, Stop-hook continuations and concurrent Agent batches can still waste extra turns or work after a loop has already been detected.

## Reviewer Test Plan

### How to verify

Reviewers should confirm that repeated invalid ACP tool calls end the current turn without entering a Stop-hook continuation, that changing validation messages for the same tool still trips the 3-strike guard, that excessive tool-call batches stop before tool lookup, and that unstarted concurrent Agent calls are recorded as skipped once loop detection fires.

### Evidence (Before & After)

N/A. This is non-UI daemon control-flow behavior covered by focused unit tests.

### Tested on

|     OS     | Status |
| :--------: | :----: |
|  🍏 macOS  |   ✅ tested   |
| 🪟 Windows |   ⚠️ not tested locally   |
|  🐧 Linux  |   ⚠️ not tested locally   |

### Environment (optional)

Local macOS checkout, Node.js/npm workspace.

## Risk & Scope

- Main risk or tradeoff: loop detection now terminates ACP turns more aggressively in daemon paths after repeated invalid calls, which is intentional for the reported failure mode.
- Not validated / out of scope: full interactive tmux E2E and cross-platform CI matrix were not run locally.
- Breaking changes / migration notes: none.

## Linked Issues

Resolves #6084
Follow-up to #6076 and #6075.

<details>
<summary>中文说明</summary>

## 这个 PR 做了什么

这个 PR 补上已合并的 ACP daemon loop guard PR 的 review follow-up 修复。它把 loop detection 作为 ACP turn 的终止路径并保留最终工具响应上下文，使用稳定的 invalid-tool 分桶避免变化的错误文本绕过 3 次保护，在共享 guard 触发后停止未启动的并发 Agent 工作，并把同样的 invalid-call guard 应用到早期工具拒绝路径。

## 为什么需要

PR #6076 在这些 review 修复合入前已经被合并，所以 main 仍缺少几个 daemon loop detection 的安全加固点。没有这个 follow-up，Stop hook continuation 和并发 Agent batch 仍可能在 loop 已经检测到后浪费额外 turn 或额外工作。

## Reviewer Test Plan

### 如何验证

Reviewer 应确认重复的 invalid ACP tool call 会结束当前 turn 且不会进入 Stop hook continuation；同一工具即使 validation message 变化也会触发 3 次 guard；过量 tool-call batch 会在 tool lookup 前停止；并发 Agent 调用在 loop detection 触发后，未启动的调用会被记录为 skipped。

### Evidence（Before & After）

N/A。这是非 UI 的 daemon 控制流行为，由聚焦单元测试覆盖。

### Tested on

|     OS     | Status |
| :--------: | :----: |
|  🍏 macOS  |   ✅ tested   |
| 🪟 Windows |   ⚠️ not tested locally   |
|  🐧 Linux  |   ⚠️ not tested locally   |

### Environment（optional）

本地 macOS checkout，Node.js/npm workspace。

## Risk & Scope

- 主要风险或取舍：loop detection 现在会在 daemon 路径里对重复 invalid call 更主动地终止 ACP turn；这是针对已报告失败模式的有意行为。
- 未验证 / 不在范围内：本地没有跑完整 interactive tmux E2E 和跨平台 CI matrix。
- Breaking changes / migration notes：无。

## Linked Issues

Resolves #6084
Follow-up to #6076 and #6075.

</details>

