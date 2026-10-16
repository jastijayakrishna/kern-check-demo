# Add package-lock.json to .gitignore

This repo uses pnpm (`pnpm-lock.yaml`, `pnpm-workspace.yaml`, `.npmrc`). `package-lock.json` should not appear in the repository.

- Add `package-lock.json` to `.gitignore`

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>Proposal: rename RenderCanvas to RenderRoot</issue_title>
> <issue_description>One item that kept tripping me up was the name RenderCanvas.  It's odd because it owns a `<canvas>` in `this._el`.  What about RenderRoot?
> 
> - Clear: it's the root of the render tree
> - Follows existing convention (Render prefix)
> - Similar to React's FiberRoot, Flutter's RenderView
> - No confusion with canvas elements</issue_description>
> 
> <agent_instructions>根据 Issue 的要求，实现需求，不要忘记更新单元测试</agent_instructions>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes alibaba/canvas-ui#33

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/alibaba/canvas-ui/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.
