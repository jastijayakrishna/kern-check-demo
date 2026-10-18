# fix(web-shell): prevent composer tag update loop

## What this PR does

Keeps the imperative composer API stable across tag state updates and makes removal of a missing composer tag a true no-op for both React state and CodeMirror transactions. It also adds regression coverage for API identity and missing-tag removal.

## Why it's needed

Hosts that store the composer API in reactive state can synchronize tags from an effect. Previously, removing a tag triggered a render, each render published a new API object, and the host effect could run again until React raised maximum update depth error 185. This was especially visible when embedding the web shell in a Solid-based host, but the loop was not specific to React 18.

## Reviewer Test Plan

### How to verify

Mount the composer, retain the exposed API object, add a top tag, and confirm the API object retains the same identity after the resulting render. Then remove an ID that is not present and confirm that neither the hook nor CodeMirror performs an update. The focused DOM test covers both behaviors and passed together with the existing composer tag tests.

### Evidence (Before & After)

Before: both new regression assertions failed because the API identity changed and missing-tag removal rerendered the hook. After: all 8 focused composer tag DOM tests pass.

### Tested on

|     OS     | Status |
| :--------: | :----: |
|  🍏 macOS  |   ✅   |
| 🪟 Windows |   N/A  |
|  🐧 Linux  |   N/A  |

### Environment (optional)

Node.js 22; focused Vitest DOM tests, ESLint, Prettier on changed files, web-shell production build, and repository-wide TypeScript typecheck.

## Risk & Scope

- Main risk or tradeoff: Consumers now receive a stable composer API object while its methods continue to use the latest hook callbacks.
- Not validated / out of scope: A full integration fixture using the external Solid host and its private deployment bundle.
- Breaking changes / migration notes: None.

## Linked Issues

N/A

<details>
<summary>中文说明</summary>

## 此 PR 的改动

让命令式 composer API 在 tag 状态更新期间保持稳定，并使删除不存在的 composer tag 在 React 状态和 CodeMirror transaction 两侧都成为真正的无操作。同时增加 API 对象身份和 missing-tag 删除的回归测试。

## 为什么需要此改动

宿主可能会把 composer API 保存到响应式状态，并在 effect 中同步 tags。此前删除 tag 会触发渲染，每次渲染又会发布新的 API 对象，宿主 effect 因此可能反复运行，直到 React 抛出最大更新深度错误 185。这个问题在 Solid 宿主嵌入 web shell 时尤其明显，但并非 React 18 特有问题。

## Reviewer 测试计划

### 如何验证

挂载 composer，保存暴露的 API 对象，添加一个顶部 tag，并确认由此产生的渲染之后 API 对象身份保持不变。然后删除一个不存在的 ID，确认 hook 和 CodeMirror 都没有执行更新。聚焦的 DOM 测试覆盖这两种行为，并与已有 composer tag 测试一同通过。

### 证据（修改前后）

修改前：两个新回归断言均失败，因为 API 身份发生变化，且删除不存在的 tag 会使 hook 重新渲染。修改后：8 个聚焦的 composer tag DOM 测试全部通过。

### 测试平台

|     OS     | 状态 |
| :--------: | :--: |
|  🍏 macOS  |  ✅  |
| 🪟 Windows | N/A  |
|  🐧 Linux  | N/A  |

### 环境（可选）

Node.js 22；已运行聚焦的 Vitest DOM 测试、ESLint、修改文件的 Prettier、web-shell 生产构建及全仓库 TypeScript 类型检查。

## 风险与范围

- 主要风险或权衡：消费者现在会获得稳定的 composer API 对象，其方法仍使用最新的 hook callback。
- 未验证或范围之外：未使用外部 Solid 宿主及其私有部署 bundle 建立完整集成 fixture。
- 破坏性变更或迁移说明：无。

## 关联 Issue

N/A

</details>

