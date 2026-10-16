# Enforce deterministic install/tool invocation and stabilize TestCafe functional workflows

- [x] Reverted changes from the 4 specified commits:
  - `a6736196` fix(ci): pin failing TestCafe functional dispatch workflows to Node 20
  - `9ae2c367` fix(ci): default TestCafe functional workflow to Node 20
  - `4da18cdc` fix: update test script to handle Node 22 assert and ESM behavior changes
  - `a696d9fa` fix: use explicit major version extraction in Node version check
- Restored `.github/workflows/test-functional-testcafe-native-automation.yml`, `.github/workflows/test-functional-testcafe-proxy.yml`, and `test/functional/run-testcafe-functional-tests.sh` to their pre-change state via a new revert commit.

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

Fix the deterministic package installation command issues described in DevExpress/dxvcs#32108 for the repository DevExpress/testcafe-hammerhead.

Goal:
- Update invalid package installation and npx invocation commands to comply with policy.
- Prefer deterministic installs and prevent implicit package downloads from the registry.

Required changes:
- Replace `npm i` and `npm install` with `npm ci` where appropriate and safe.
- Replace `npx <cmd>` with `npx --no-install <cmd>` where appropriate.
- Carefully review any flagged commands that may not be safely transformed mechanically, especially:
  - `npm i testcafe-hammerhead ../testcafe-hammerhead --save`
- For edge cases, make the minimal safe change that satisfies the deterministic-install policy without breaking the workflow; if direct substitution with `npm ci` is not valid, adjust the workflow/command sequence appropriately.

Flagged files from the issue for DevExpress/testcafe-hammerhead:
- .github/workflows/deploy-to-artifacts.yml
- .github/workflows/health-monitor.yml
- .github/workflows/test-client-cloud.yml
- .github/workflows/test-functional-testcafe-native-automation.yml
- .github/workflows/test-functional-testcafe-proxy.yml
- .github/workflows/test-server-latest.yml
- .github/workflows/test-server-minimum.yml
- Gulpfile.js

Acceptance criteria:
- All issue-listed invalid commands in this repository are fixed.
- Changes are minimal and scoped only to the commands required by the issue.
- CI/workflows/scripts remain functionally equivalent.
- Open a pull request with a concise summary of the changes and mention that it addresses DevExpress/dxvcs#32108 for this repository.

The following is the prior conversation context from the user's chat exploration (may be truncated):

User: Create a PR for each of the following repositories: DevExpress/testcafe
DevExpress/testcafe-studio
DevExpress/testcafe-hammerhead
DevExpress/testcafe.io
DevExpress/generator-testcafe-reporter
DevExpress/testcafe-examples
DevExpress/testcafe-browser-tools
DevExpress/angular-testcafe
DevExpress/log-update-async-hook
DevExpress/testcafe-selector-generator
DevExpress/testcafe-browser-provider-electron
DevExpress/testcafe-legacy-api
DevExpress/testcafe-browser-provider-browserstack targeting master

Assistant: I’m waiting for your response to the approval prompt before I can continue creating the PRs for those repositories.

User: @Copilot Accepted Confirmation: Confirm agent session

Assistant: Started the first PR task for `DevExpress/testcafe`. Track it here:

````list type="task"
data:
  - title: "[WIP] Fix deterministic package installation command issues for DevExpress/testcafe"
    repository: DevExpress/testcafe
    url: https://github.com/copilot/tasks/pull/PR_kwDOAgrPSc7aWKKV?session_id=81c2f208-939a-444e-b91e-95a200f8b94c
    state: queued
````

I can continue with the remaining repositories next, but I’m currently unable to start additional PR tasks in this message.

User: Create a PR for DevExpress/testcafe-studio

Assistant: Started the PR task for `DevExpress/testcafe-studio`. You can follow its progress from the task page once it appears in GitHub.

User: @Copilot Accepted Confirmation: Confirm agent session

Assistant: Started the PR task for `DevExpress/testcafe-studio`. Track it here:

````list type="task"
data:
  - title: "[WIP] Fix deterministic package installation command issues for compliance"
    repository: DevExpress/testcafe-studio
    url: https://github.com/copilot/tasks/pull/PR_kwDOAny0l87aWg9l?session_id=9a638adc-b235-45ce-964f-4fe1279cabad
    state: queued
````

User: Could you attach links to all created PRS and PRs that will be created to the following issue https://github.com/orgs/DevExpress/projects/207/views/1?pane=issue&itemId=186240263&issue=DevExpress%7Cdxvcs%7C32108 ?

Assistant: I can do that, but I need the actual issue target rather than the project view link.

Please confirm that you want me to update this issue:

- `DevExpress/dxvcs#32108`

If yes, I can add the created PR links there as they become available. Right now, I only have task links for the PR creation jobs, not confirmed PR URLs yet. Once PRs are created, I can attach those PR links to the issue.

User: yes this is the issue

Assistant: Yes — once the PRs exist, I can attach their links to `DevExpress/dxvcs#32108`.

At the moment, I only have task links, not actual PR URLs:
- `DevExpress/testcafe` task
- `DevExpress/testcafe-studio` task

I can update the issue with PR links after the PRs are created. If you want, I can also continue creating PRs for the remaining repositories one by one, and then attach all resulting PR links to `DevExpress/dxvcs#32108`.

User: yes please

Assistant: I’ll use a single consolidated comment on `DevExpress/dxvcs#32108` and keep adding PR links as they become available.

Next up: `DevExpress/testcafe-hammerhead`.

When you’re ready, say:
- `Create a PR for DevExpress/testcafe-hammerhead`

and after approval I’ll continue through the lis...

</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

*This pull request was created from Copilot chat.*
>
