# feat: 为 X 帖子提供稳定的 Grok 优先翻译入口

## 概要

- 为 X/Twitter 时间线和帖子详情中的每条正文帖子保留“翻译帖子”入口。
- 帖子进入视野后优先触发 X 原生 Grok 翻译；原生入口不可用时允许用户手动调用 FluentRead 兜底。
- 处理动态时间线、引用帖、虚拟列表复用、原生入口迟到和卸载清理，避免重复点击或双重翻译。
- 修复 X/Grok 与 FluentRead 自动整页翻译同时修改帖子 DOM 所导致的页面闪烁和抖动。

## 验证

- `pnpm test`：148 个测试文件、2098 项测试通过。
- `pnpm test:coverage`：Statements / Branches / Functions / Lines 均为 100%。
- `pnpm compile`、`pnpm build`、`pnpm build:firefox`、manifest 校验和测试审计通过。
- 隔离生产 Edge 中同时开启“所有网站自动翻译”和“X/Grok”：FluentRead 整页翻译节点新增 0、稳定期帖子高度变化 0、控制台错误 0；原生入口只触发一次并正确接管。

