# fix: add early return for web platform in checkShouldMigrateV4OnMount

# 添加 Web 平台检查

## 修改内容
在 `ServiceV4Migration.ts` 的 `checkShouldMigrateV4OnMount` 方法中添加了对 `platformEnv.isWeb` 的检查，如果是 Web 平台则直接返回 false。

## 测试
已通过 lint 检查，确保代码风格符合要求。

Link to Devin run: https://app.devin.ai/sessions/f51034a9e06548b1a6aaa0c22313dfe2
