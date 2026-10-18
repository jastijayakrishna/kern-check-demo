# feat: 增加安全的 AI 多段翻译与上下文泄漏重译

## 改动摘要

- 检测 AI 译文是否泄漏页面上下文；命中后自动移除上下文重译一次，持续泄漏时拒绝展示和缓存
- 在翻译设置的全文翻译分组新增默认关闭的 AI 多段翻译开关
- 将同配置的相邻短段最多按 4 个文本槽、2000 字符合并为一次 AI 请求，并严格校验段落标记和映射
- 为多段缓存、异常降级、稀疏数组、重复原文槽位和上下文恢复补充完整测试
- 翻译缓存协议升级到 v2，避免历史上下文泄漏结果继续命中

## 验证

- pnpm test:audit
- pnpm test:architecture（454 tests）
- pnpm test:unit（955 tests）
- pnpm test:functional（353 tests）
- pnpm test:regression（168 tests）
- pnpm compile
- pnpm build
- pnpm build:firefox
- pnpm test:userscript
- pnpm verify:extension-manifests
- 隔离生产 Edge：设置持久化、全文翻译/恢复/再次翻译、真实 OpenAI 兼容上下文泄漏恢复与两段单请求均通过

Closes #352
