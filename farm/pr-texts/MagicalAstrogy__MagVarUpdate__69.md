# feat: 增加对酒馆最低版本的检查 (#66)

## Summary
- 引入 `compare-versions` 依赖，并调整 `package.json` 中的依赖结构
- 在启动时检查酒馆助手版本，低于 `3.2.13` 时给出警告
- 调整相关单元测试的变量替换次数

## Testing
- `yarn test` *(失败：TS2304 无法找到全局函数定义)*

------
https://chatgpt.com/codex/tasks/task_e_68988f7dce808331a9e9960bc7386cdc
