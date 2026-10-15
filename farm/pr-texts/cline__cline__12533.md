# fix: center-align sign-in verification code box in chat

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
### Related Issue

**Issue:** #12531

### Description

After clicking "Sign in to Cline" from the logged-out error in chat, the "Enter this code in your browser" box rendered its label, code, and Copy button left-aligned, while the surrounding logged-out message and sign-in button are centered. This adds `text-center` to the box container and `justify-center` to the code/copy flex row in `ClineAuthStatus`, so the content is center-aligned everywhere the component is used (chat error row, account welcome view, settings account card).

### Test Procedure

Ran the VS Code extension in a dev host while logged out, started a task (which fails with the Cline provider auth error), clicked "Sign in to Cline", and verified the device-code box now renders centered. Ran `biome check` on the changed file and the webview `tsc`/vite build passes.

![Centered sign-in code box after fix](https://cursor.com/artifacts/c/art-d0f01547-dbed-4154-a6c9-b52b906a09ba)

<a href="https://cursor.com/agents/bc-16f93d67-52a8-4c63-808e-2e3d1edc61e9/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fsignin_code_box_centered_demo.mp4"><img src="https://cursor.com/artifacts/c/art-471b8e7e-da0c-4f4e-b1cb-3c6f204a71b7" alt="signin_code_box_centered_demo.mp4" /></a>

### Type of Change

-   [x] 🐛 Bug fix (non-breaking change which fixes an issue)
-   [ ] ✨ New feature (non-breaking change which adds functionality)
-   [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
-   [ ] ♻️ Refactor Changes
-   [x] 💅 Cosmetic Changes
-   [ ] 📚 Documentation update
-   [ ] 🏃 Workflow Changes

### Pre-flight Checklist

-   [x] Changes are limited to a single feature, bugfix or chore (split larger changes into separate PRs)
-   [x] Tests are passing (`bun test`) and code is formatted and linted (`bun run format && bun run lint`)
-   [x] I have reviewed [contributor guidelines](https://github.com/cline/cline/blob/main/CONTRIBUTING.md)

### Screenshots

Before (from the issue): the code hugs the left edge of the box. After: label, code, and Copy button are centered (see image and demo video in Test Procedure).
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-16f93d67-52a8-4c63-808e-2e3d1edc61e9"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-16f93d67-52a8-4c63-808e-2e3d1edc61e9"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
