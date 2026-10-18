# fix: reduce floating translation UI interference

## 变更摘要

- 将收起态悬浮球调整为低透明显示，仅在悬停、聚焦、拖拽或主动展开时恢复清晰。
- 使用全文翻译会话的权威状态同步淡色勾选标记，快捷键切换不再自动展开菜单或弹出提示。
- 仅在存在运行中或排队任务时展示进度详情；仅剩离屏候选时，由悬浮球勾选或紧凑勾选承接状态。
- 保持鼠标点击后立即收起、键盘 Escape 焦点清理、拖拽和左右停靠标记可见性。
- 扩展 closed Shadow DOM 浏览器回归，覆盖翻译、恢复、再次翻译、滚动续译和仅进度面板配置。

## 验证

- `pnpm exec vitest run tests/floatingUiPresentation.test.ts tests/contentUiRuntime.test.ts tests/fullPageTranslationProgress.test.ts`：20 项通过
- `pnpm test:audit`：140 个测试文件、1381 个用例，状态正常
- `pnpm test:coverage`：语句、分支、函数、行覆盖率均为 100%
- `pnpm compile`
- `pnpm build`
- `pnpm build:firefox`
- `pnpm test:userscript`
- `node --check scripts/run-full-page-translation-test.cjs`
- 隔离后台 Edge + Chrome MV3 生产构建：全文翻译 → 恢复 → 再次翻译、滚动批次和仅进度面板流程通过；37 次本地 fixture 翻译请求，无意外外部网络请求或控制台错误

## 范围

- 未新增 popup/options 配置入口，保留现有功能开关和默认行为。
- 参考项目仅用于交互模式研究，未复制代码或引入跨仓库依赖。

