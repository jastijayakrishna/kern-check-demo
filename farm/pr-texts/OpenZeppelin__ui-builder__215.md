# Add .gitignore by default to generated project folder

- [x] Explore repository structure and understand export system
- [x] Create .gitignore file in template directory with node_modules entry
- [x] Update TemplateManager to explicitly include dotfiles in glob pattern
- [x] Add test to verify .gitignore is included in exports
- [x] Build and test to ensure .gitignore is included in exports
- [x] Verify the changes work with manual export test

## Summary
Added `.gitignore` file to the exported project template to address the issue where generated Stellar UI forms (and other exported apps) did not include a `.gitignore` file for Git version control.

### Changes Made:
1. Created `.gitignore` file in `packages/builder/src/export/templates/typescript-react-vite/` with standard Vite React project entries including `node_modules/`
2. Updated `TemplateManager.ts` to explicitly include dotfiles (`./templates/**/.*`) in the `import.meta.glob` pattern since Vite doesn't pick them up by default
3. Added test in `ExportStructureTests.test.ts` to verify `.gitignore` is present in exports and contains `node_modules` entry
4. Manually verified by exporting a test app and confirming `.gitignore` is present with correct content

All tests pass and the exported application now includes a proper `.gitignore` file.

<!-- START COPILOT CODING AGENT SUFFIX -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>Add .gitignore by default to the generated project folder</issue_title>
> <issue_description>I've tried to generate Stellar UI form using https://builder.openzeppelin.com/ and seems that it does not include a .gitignore file by default for Git version control. It would be helpful to add one with at least the following:
> ```
> node_modules/
> ```</issue_description>
> 
> <agent_instructions>add a .gitignore file with the `node_modules/` to the exported apps template directory</agent_instructions>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>

- Fixes OpenZeppelin/ui-builder#213

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/OpenZeppelin/ui-builder/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.
