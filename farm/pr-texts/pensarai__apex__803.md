# Fix: Extract message field from tool results for friendly status display

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
### What does this PR do?

This PR fixes the unfriendly UX status message that appears when a pentest worker completes.

**Issue:** When a pentest worker completed, the raw tool result object `{success, subagentId, findingsCount, objectiveResults, message}` was being displayed in the UI instead of extracting and showing the human-readable `message` field.

**Root Cause:** The `AgentMessage` component in `agent-display.tsx` was displaying the `message.content` field for tool messages, which is always an empty string. The actual tool result (including the user-friendly `message` field) was stored in `message.result` but wasn't being extracted for display.

**Solution:** Modified the `AgentMessage` component to check if a completed tool message has a `result` object with a `message` field. If present, it extracts and displays that message instead of showing empty content or stringifying the entire result object.

This change provides a much better user experience by showing friendly messages like:
- ✓ `Worker 'SQLi /api/users' complete. Documented 3 finding(s).`

Instead of the confusing raw object display shown in the issue screenshot.

### How did you verify your code works?

1. ✅ **Type check passed:** `bun run tsc` completed successfully
2. ✅ **All tests passed:** `bun run test` completed with all tests passing
3. ✅ **Lint check passed:** `bun run lint` completed without errors

The fix is a surgical change that only affects how completed tool results are displayed in the TUI. It extracts the `message` field from tool results when available, falling back to the existing behavior for tools that don't include a message field in their result.
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-95ee6837-a729-4fee-b1da-485b99bc4466"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-95ee6837-a729-4fee-b1da-485b99bc4466"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
