# Remove deprecated generate-lock command

The `generate-lock` command was a temporary migration tool from the pre-lockfile era. Since v1.2.0, `skills add` automatically maintains `~/.agents/.skills-lock.json`, making the command obsolete.

## Changes

- **Removed implementation**: `runGenerateLock()` and supporting functions (`getInstalledSkillNames`, `fuzzyMatchSkills`, `inferSourceType`, `buildSourceUrl`)
- **Removed types**: `MatchResult`, `SearchResponse` interfaces and `SEARCH_API_URL` constant
- **Removed routing**: `generate-lock` and `gen-lock` command cases
- **Cleaned up docs**: Removed from help text, banner, README.md, and AGENTS.md
- **Removed `--dry-run` flag**: Only used by generate-lock

Attempting to run the command now returns:
```
Unknown command: generate-lock
Run skills --help for usage.
```

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>generate-lock command fails to detect installed skills</issue_title>
> <issue_description>## Description
> 
> The `skills generate-lock` command reports "No installed skills found" even when skills are correctly installed and detected by `skills list`.
> 
> ## Steps to Reproduce
> 
> 1. Install skills using either symlink or copy method:
>    ```bash
>    npx skills add vercel-labs/agent-skills
>    ```
> 
> 2. Verify skills are installed:
>    ```bash
>    npx skills list
>    ```
>    Output shows 4 skills installed correctly.
> 
> 3. Attempt to generate lock file:
>    ```bash
>    npx skills generate-lock
>    ```
>    Output: "No installed skills found."
> 
> 4. Attempt to check for updates:
>    ```bash
>    npx skills check
>    ```
>    Output: "No skills tracked in lock file."
> 
> ## Expected Behavior
> 
> `generate-lock` should detect the installed skills and create a lock file for version tracking.
> 
> ## Actual Behavior
> 
> `generate-lock` reports no skills found, despite `skills list` showing them correctly.
> 
> ## Environment
> 
> - OS: Windows 11
> - skills CLI version: 1.2.0
> - Installation method tested: Both symlink and copy
> - Skills source: vercel-labs/agent-skills
> 
> ## Analysis
> 
> The issue appears to be that neither symlink nor copy installation preserves the source repository metadata needed for `generate-lock` to create lock entries. The lock file requires:
> - Skill name
> - Source repository (e.g., "vercel-labs/agent-skills")
> - Skill folder hash (GitHub tree SHA)
> 
> Without this metadata being stored during installation, `generate-lock` cannot function.
> 
> ## Suggested Fix
> 
> During skill installation, store source metadata in a file (e.g., `.skill-source.json`) within each skill directory containing:
> ```json
> {
>   "source": "vercel-labs/agent-skills",
>   "installedAt": "2026-01-29T10:00:00Z",
>   "commitSha": "abc123..."
> }
> ```
> 
> This would allow `generate-lock` to trace skills back to their origin.</issue_description>
> 
> <agent_instructions>remove the generate-lock command</agent_instructions>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> <comment_new><author>@quuu</author><body>
> generate-lock was only meant to be a temporary fix during the migration from no lock file -> having a lock file
> 
> as of a few versions ago (last week) - every install should automatically write to a lock file, let me know if you don't see one at ~/.agents/.skills-lock.json</body></comment_new>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes vercel-labs/skills#198

<!-- START COPILOT CODING AGENT TIPS -->
---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [Copilot coding agent tips](https://gh.io/copilot-coding-agent-tips) in the docs.
