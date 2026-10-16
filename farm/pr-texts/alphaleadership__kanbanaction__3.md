# feat: add Gemini clarification discussion when issue details are missing

### Motivation
- When the AI analysis detects missing information on an issue, the workflow should automatically generate concrete clarification questions and a list of requested inputs so authors can provide what's needed to move the task forward. 
- This reduces back-and-forth and helps ensure created Kanban tasks have actionable acceptance criteria and required context.

### Description
- Added `IssueAnalyzer.generateClarificationDiscussion(issueData, missingDetails)` which builds a French prompt and returns a JSON payload with `summary`, `questions`, and `requestedInputs` by calling `this.client.generateJson(...)`.
- Updated `WorkflowManager.processGitHubIssue(...)` to call the new method when `missingInformation` is detected and to append a `### 💬 Discussion avec Gemini` section to the GitHub issue comment containing the summary, clarification questions, and requested inputs.
- Added unit tests in `__tests__/clarification-discussion.test.js` to cover the no-op case and the case where the analyzer invokes Gemini, and removed an unused import from `src/gemini/analyzer.js`.

### Testing
- Ran the targeted test suites with `npm test -- --runInBand __tests__/clarification-discussion.test.js __tests__/properties/analyzer.test.js` and both suites passed. 
- Attempting the full test run with `npm test -- --runInBand` in this environment produced long-running processes, so validation was performed with the targeted tests above.

------
[Codex Task](https://chatgpt.com/codex/tasks/task_e_698c98151f988331920ccb8f1ce41025)

<!-- This is an auto-generated description by cubic. -->
---
## Summary by cubic
Automatically adds a “Discussion avec Gemini” when issue details are missing, and fixes action/workflow installation so dependencies are installed and the action runs reliably on the runner.

- **New Features**
  - Added IssueAnalyzer.generateClarificationDiscussion(issueData, missingDetails) returning a French JSON payload: { summary, questions, requestedInputs }.
  - Workflow now appends “💬 Discussion avec Gemini” with “Questions pour avancer” and “Éléments à fournir à Gemini” when missingInformation is detected.
  - Switched to a composite action and updated workflow installation to checkout the action source, run npm ci, and execute node action.js on the runner; added tests for action metadata and workflow installation.

<sup>Written for commit 794f10b4ea8f49de154d4fce45d768fcf81466eb. Summary will update on new commits.</sup>

<!-- End of auto-generated description by cubic. -->

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Issue comments now include a dynamic clarification section when details are missing: concise blocking summary, targeted follow-ups, and requested inputs.
  * Action now exposes a new debug input and uses a composite run that sets up Node and installs action dependencies before executing.

* **Tests**
  * Added tests for clarification discussion behavior, action metadata, and workflow installation validation.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
