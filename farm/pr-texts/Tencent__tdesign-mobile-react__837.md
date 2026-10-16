# fix(swipe-cell): clear timers on component unmount

<!--
首先，感谢你的贡献！😄
请阅读并遵循 [TDesign 贡献指南](https://github.com/Tencent/tdesign/blob/main/docs/contributing.md)，填写以下 pull request 的信息。
PR 在维护者审核通过后会合并，谢谢！
-->

### 🤔 这个 PR 的性质是？

- [x] 日常 bug 修复
- [ ] 新特性提交
- [ ] 文档改进
- [ ] 演示代码改进
- [ ] 组件样式/交互改进
- [ ] CI/CD 改进
- [ ] 重构
- [ ] 代码风格优化
- [x] 测试用例
- [ ] 分支合并
- [ ] 其他

### 🔗 相关 Issue

#705

### 💡 需求背景和解决方案

SwipeCell 组件使用了多个 `setTimeout`，在组件卸载时未清理，可能导致内存泄漏或对已卸载组件进行状态更新。

**解决方案：**
- 添加 `timersRef` 跟踪所有定时器 ID
- 创建 `setTimer` 辅助函数，自动注册和清理已完成的定时器
- 在 `useEffect` 清理函数中清除所有待处理的定时器

**涉及的定时器：**
- `syncOpenedState` - 初始展开延迟 (100ms)
- `close` - 确认内容重置延迟 (300ms)
- `useDrag` handler - 拖拽标志重置
- `onActionClick` - 确认动画

### 📝 更新日志

- fix(SwipeCell): 组件卸载时清理定时器，防止内存泄漏

- [ ] 本条 PR 不需要纳入 Changelog

### ☑️ 请求合并前的自查清单

⚠️ 请自检并全部**勾选全部选项**。⚠️

- [x] 文档已补充或无须补充
- [x] 代码演示已提供或无须提供
- [x] TypeScript 定义已补充或无须补充
- [x] Changelog 已提供或无须提供

<!-- START COPILOT CODING AGENT SUFFIX -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>[SwipeCell]  该组件的定时器是否应该在组件卸载时被移除</issue_title>
> <issue_description>### tdesign-mobile-react 版本
> 
> 0.20.1
> 
> ### 重现链接
> 
> _No response_
> 
> ### 重现步骤
> 
> _No response_
> 
> ### 期望结果
> 
> _No response_
> 
> ### 实际结果
> 
> _No response_
> 
> ### 框架版本
> 
> _No response_
> 
> ### 浏览器版本
> 
> _No response_
> 
> ### 系统版本
> 
> _No response_
> 
> ### Node版本
> 
> _No response_
> 
> ### 补充说明
> 
> _No response_</issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>

- Fixes Tencent/tdesign-mobile-react#824

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/Tencent/tdesign-mobile-react/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.
