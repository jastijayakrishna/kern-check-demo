# fix(useTheme): Safari ≤13 compatibility — fall back to addListener/removeListener

Safari 13.1.2 and earlier don't implement `MediaQueryList.addEventListener`, causing a `TypeError: e.addEventListener is not a function` crash in `useTheme`.

### 变更内容

- **`useTheme/index.ts`**: In `useCurrentTheme`, guard `addEventListener`/`removeEventListener` calls with existence checks and fall back to the deprecated `addListener`/`removeListener` API supported by older Safari:

```ts
if (matchMedia?.addEventListener) {
  matchMedia.addEventListener('change', onThemeChange);
} else if (matchMedia?.addListener) {
  matchMedia.addListener(onThemeChange);
}
// cleanup mirrors the same pattern with removeEventListener → removeListener
```

- **`useTheme/__tests__/index.spec.ts`**: Added test that mocks `matchMedia` without `addEventListener`/`removeEventListener` and asserts `addListener`/`removeListener` are invoked instead.

[[English Template / 英文模板](https://github.com/alibaba/hooks/blob/master/.github/PULL_REQUEST_TEMPLATE.md)]

### 🤔 这个变动的性质是？

- [ ] 新特性提交
- [x] 日常 bug 修复
- [ ] 站点、文档改进
- [ ] 演示代码改进
- [ ] TypeScript 定义更新
- [ ] 包体积优化
- [ ] 性能优化
- [ ] 功能增强
- [ ] 国际化改进
- [ ] 重构
- [ ] 代码风格优化
- [ ] 测试用例
- [ ] 分支合并
- [ ] 其他改动（是关于什么的改动？）

### 🔗 相关 Issue

Safari 13.1.2 下 `useTheme` 报错：`TypeError: e.addEventListener is not a function`（`MediaQueryList` 不支持 `addEventListener`）。

### 💡 需求背景和解决方案

**问题**：Safari ≤13 的 `MediaQueryList` 未实现标准的 `addEventListener`/`removeEventListener`，只支持已废弃的 `addListener`/`removeListener`，直接调用导致运行时崩溃。

**方案**：在订阅/取消订阅系统主题变化时，优先使用标准 API，检测不存在时降级为旧版 API，无需引入任何额外依赖。

### 📝 更新日志

| 语言    | 更新描述 |
| ------- | -------- |
| 🇺🇸 英文 | `useTheme`: Fixed crash on Safari ≤13 by falling back to deprecated `addListener`/`removeListener` when `addEventListener` is unavailable on `MediaQueryList`. |
| 🇨🇳 中文 | `useTheme`：修复在 Safari ≤13 中因 `MediaQueryList` 不支持 `addEventListener` 导致的运行时报错，降级使用 `addListener`/`removeListener`。 |

### ☑️ 请求合并前的自查清单

⚠️ 请自检并全部**勾选全部选项**。⚠️

- [x] 文档已补充或无须补充
- [x] 代码演示已提供或无须提供
- [x] TypeScript 定义已补充或无须补充
- [x] Changelog 已提供或无须提供

<!-- START COPILOT CODING AGENT TIPS -->
---

📍 Connect Copilot coding agent with [Jira](https://gh.io/cca-jira-docs), [Azure Boards](https://gh.io/cca-azure-boards-docs) or [Linear](https://gh.io/cca-linear-docs) to delegate work to Copilot in one click without leaving your project management tool.
