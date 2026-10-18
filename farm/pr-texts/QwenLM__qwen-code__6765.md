# feat(web-shell): support custom composer placeholders

## What this PR does

Adds an optional `composerPlaceholders` API to WebShell so embedders can supply main-composer placeholder copy for the semantic `idle`, `loading`, and `processing` states. Omitted, partial, or whitespace-only entries keep the existing localized WebShell copy.

## Why it's needed

Different embedding products use different terminology and workflows, while the current main composer always owns its placeholder text. This change makes that copy configurable without forking WebShell and preserves the existing behavior for every caller that does not opt in.

## Reviewer Test Plan

### How to verify

1. Render WebShell with `composerPlaceholders={{ idle: 'Ask a question', loading: 'Preparing chat', processing: 'Working on it' }}`; confirm the main composer displays the configured value for each matching state.
2. Omit the prop, provide only one state, or provide whitespace-only text; confirm the affected state uses the existing localized WebShell placeholder.
3. Switch to shell mode and open a follow-up composer; confirm their existing specialized placeholders still take precedence.

### Evidence (Before & After)

Before: the main composer always used the WebShell localized placeholder for its current state. After: an embedding can provide state-specific main-composer copy while every unconfigured state falls back to that same localized default. The focused upstream tests cover all three states, partial-map fallback, whitespace fallback, and semantic state selection. A private embedding integration also rendered its configured idle copy; no public screenshot can be attached because that host is not publicly accessible.

### Tested on

|     OS     | Status |
| :--------: | :----: |
|  🍏 macOS  | ✅ |
| 🪟 Windows | ⚠️ |
|  🐧 Linux  | ⚠️ |

### Environment (optional)

macOS local checkout. Passed: `npx vitest run client/App.test.tsx client/utils/composerInputState.test.ts --config vitest.config.ts` (79 tests), `npm run typecheck --workspace=packages/web-shell`, and WebShell package build/test/coverage before the root preflight run.

## Risk & Scope

- Main risk or tradeoff: an embedding can intentionally replace only the main-composer copy; shell-mode, follow-up, and split-view placeholders retain their established behavior.
- Not validated / out of scope: Windows and Linux were not run locally. Root `npm run preflight` reached clean, install, format, lint, build, and typecheck, but its all-workspace test stage failed in unrelated CLI locale assertions and core managed-memory refresh tests.
- Breaking changes / migration notes: None. The API is optional and existing callers keep the current localized placeholders.

## Linked Issues

N/A (no user-provided issue).

<details>
<summary>中文说明</summary>

## 本 PR 做什么

为 WebShell 新增可选的 `composerPlaceholders` API，使嵌入方能够为主输入框的 `idle`、`loading` 和 `processing` 语义状态提供 Placeholder 文案。未传入、只传入部分状态或仅传入空白字符的条目，都会继续使用现有的 WebShell 本地化文案。

## 为什么需要

不同的嵌入产品有不同的术语和工作流，而当前主输入框的 Placeholder 文案始终由 WebShell 固定提供。本改动让这部分文案无需 fork WebShell 即可配置，并且保留所有未选择启用该能力调用方的现有行为。

## Reviewer 测试计划

### 如何验证

1. 使用 `composerPlaceholders={{ idle: 'Ask a question', loading: 'Preparing chat', processing: 'Working on it' }}` 渲染 WebShell；确认主输入框在每个对应状态下显示配置的文案。
2. 不传入该 prop、只提供一个状态，或提供仅包含空白字符的文本；确认受影响状态使用现有的 WebShell 本地化 Placeholder。
3. 切换到 shell 模式并打开 follow-up 输入框；确认它们现有的专用 Placeholder 仍具有更高优先级。

### 证据（改动前与改动后）

改动前：主输入框始终使用当前状态对应的 WebShell 本地化 Placeholder。改动后：嵌入方可以提供按状态区分的主输入框文案，而所有未配置状态都会回退到相同的本地化默认文案。上游定向测试覆盖了全部三个状态、部分 map 回退、空白字符回退和语义状态选择。私有嵌入环境也已验证其配置的 idle 文案能够渲染；由于该宿主环境无法公开访问，不能附上公开截图。

### 测试环境

|     操作系统     | 状态 |
| :--------------: | :--: |
|    🍏 macOS     | ✅ |
| 🪟 Windows | ⚠️ |
|  🐧 Linux  | ⚠️ |

### 环境（可选）

macOS 本地代码库。已通过：`npx vitest run client/App.test.tsx client/utils/composerInputState.test.ts --config vitest.config.ts`（79 个测试）、`npm run typecheck --workspace=packages/web-shell`，以及根目录 preflight 之前完成的 WebShell 包构建、测试和覆盖率检查。

## 风险与范围

- 主要风险或权衡：嵌入方只能有意替换主输入框文案；shell 模式、follow-up 和 split-vi
