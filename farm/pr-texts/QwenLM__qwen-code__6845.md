# fix(web-shell): improve file search and composer focus

## What this PR does

This PR makes Web Shell file mentions search matching names recursively across the active workspace instead of filtering only the current directory. Empty file queries continue to use the existing directory browser. It also restores composer focus after a new chat is started and after an existing session finishes loading, while preserving approval-overlay focus.

## Why it's needed

Typing a filename after `@` could not find matching files in nested directories during normal Web Shell use because directory listing always took precedence over workspace glob search. Starting a new chat or opening an existing session could also leave keyboard focus on the initiating control, forcing an extra click before typing.

## Reviewer Test Plan

### How to verify

- In a workspace with similarly named files under multiple nested directories, type `@` followed by the shared filename fragment and confirm results include the matching workspace-relative paths from each directory.
- Clear the file query and confirm directory browsing, drill-down, and Back navigation still work.
- Start a new chat from the sidebar and confirm typing immediately enters text in the composer.
- Open an existing session and confirm the composer receives focus only after the target transcript finishes loading.
- Open a session with an actionable approval and confirm the approval overlay retains focus instead of the composer.

### Evidence (Before & After)

- Before: non-empty file mention queries only filtered entries in the current directory; after: they use recursive workspace matching such as `**/*config*` and return complete relative paths.
- Before: new and loaded sessions could leave focus on the initiating sidebar control; after: successful session transitions restore composer focus, while failed transitions and approval overlays do not.

### Tested on

|     OS     | Status |
| :--------: | :----: |
|  🍏 macOS  | ✅ tested |
| 🪟 Windows | ⚠️ not tested |
|  🐧 Linux  | ⚠️ not tested |

### Environment (optional)

Local Node.js workspace; Web Shell Vitest suites, package build and typecheck, plus repository-wide build and typecheck.

## Risk & Scope

- Main risk or tradeoff: recursive filename matching can return more candidates than a single-directory listing, but the existing 50-item UI limit, debounce, cache, ignore rules, and workspace boundary remain in effect.
- Not validated / out of scope: manual verification on Windows and Linux; ranking changes beyond the existing glob result order.
- Breaking changes / migration notes: none.

## Linked Issues

N/A

<details>
<summary>中文说明</summary>

## 本 PR 的改动

本 PR 将 Web Shell 的文件引用搜索改为在当前活动工作区内递归匹配文件名，而不是只过滤当前目录。空文件查询仍保留现有目录浏览方式。同时，新建会话成功后以及已有会话加载完成后会恢复输入框焦点，并且不会抢占审批浮层的焦点。

## 修改原因

正常 Web Shell 同时具有目录枚举和工作区 glob 能力，但目录枚举始终优先，导致在 `@` 后输入文件名时无法找到嵌套目录中的匹配文件。新建会话或打开已有会话后，键盘焦点也可能停留在触发操作的控件上，用户必须额外点击输入框才能继续输入。

## Reviewer 测试计划

### 验证方式

- 在多个嵌套目录中放置名称相似的文件，在 `@` 后输入共同的文件名片段，确认结果包含各目录下匹配文件的完整工作区相对路径。
- 清空文件查询，确认目录浏览、进入子目录和返回操作仍然正常。
- 从侧边栏新建会话，确认无需点击输入框即可直接输入。
- 打开已有会话，确认目标 transcript 加载完成后输入框获得焦点。
- 打开存在待处理审批的会话，确认审批浮层继续持有焦点，而不是输入框。

### 修改前后证据

- 修改前：非空文件引用查询只过滤当前目录；修改后：使用 `**/*config*` 等递归工作区匹配，并返回完整相对路径。
- 修改前：新建或加载会话后焦点可能停留在侧边栏触发控件；修改后：成功切换会话后恢复输入框焦点，失败切换和审批浮层不会被错误抢焦点。

### 测试平台

|     系统     | 状态 |
| :----------: | :--: |
|  🍏 macOS    | ✅ 已测试 |
| 🪟 Windows   | ⚠️ 未测试 |
|  🐧 Linux    | ⚠️ 未测试 |

### 环境（可选）

本地 Node.js 工作区；运行了 Web Shell Vitest、包级构建与类型检查，以及仓库级构建与类型检查。

## 风险与范围

- 主要风险或取舍：递归文件名匹配可能比单目录枚举返回更多候选项，但现有 50 项 UI 上限、debounce、缓存、忽略规则和工作区边界均保持不变。
- 未验证或不在范围内：Windows 和 Linux 的人工验证；除现有 glob 结果顺序之外的排序调整。
- 破坏性修改或迁移说明：无。

## 关联 Issue

无

</details>

