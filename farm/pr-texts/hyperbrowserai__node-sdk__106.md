# feat: add Claude Opus 5 to Claude computer use models

## Summary
Adds `claude-opus-5` to the `ClaudeComputerUseLlm` type so the Node SDK accepts Claude Opus 5 for the claude-computer-use agent API (mirrors browserctrl#1256).

## Changes
- `src/types/constants.ts`: add `"claude-opus-5"` to the `ClaudeComputerUseLlm` union.

## Validation
- `yarn build`
- `yarn lint`

Link to Devin session: https://app.devin.ai/sessions/56c4640a2f94473897fafe2b0af34244
Requested by: @shrisukhani

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Type-only SDK update with a patch version bump; no runtime or API client logic changes.
> 
> **Overview**
> Adds **`claude-opus-5`** to the `ClaudeComputerUseLlm` union so callers can pass Opus 5 when starting Claude computer-use tasks via the optional `llm` field on `StartClaudeComputerUseTaskParams`.
> 
> Bumps the package version from **0.91.6** to **0.91.7** for release.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit be4a3b3d7fc049cd37c7f3f2cbb2425cc3c3a36a. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
