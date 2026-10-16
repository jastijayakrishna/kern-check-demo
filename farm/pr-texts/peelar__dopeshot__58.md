# Fix auth configuration to avoid localhost defaults

## Summary
- resolve the Better Auth base URL from configured app URLs or deployment host instead of defaulting to localhost
- align trusted origins with the resolved auth URL for consistent CORS configuration
- ensure the client auth SDK uses the configured app URL or the current browser origin

## Testing
- Not run (not requested)


------
[Codex Task](https://chatgpt.com/codex/tasks/task_e_6949b8e54ac483278eedaa43c3eb60af)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Chores**
  * Improved authentication configuration to dynamically determine the application URL based on environment variables and runtime context, replacing static defaults.
  * Updated origin verification to use flexible configuration instead of hardcoded URLs for better multi-environment support.

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
