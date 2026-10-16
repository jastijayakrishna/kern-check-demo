# feat(analytics-browser): add reset listener API

## Summary
- add an "onReset" functionality that adds handlers that get run when "reset" is called

## Testing
- added unit tests
- made a test page and tested manually

Screen Recording 2025-11-10 at 9.34.43 AM

------
[Codex Task](https://chatgpt.com/codex/tasks/task_b_690ea22a4f44832ba652049aad5e935d)

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> Adds a new plugin `onReset` hook and calls it from the Browser client `reset()`, with supporting tests, mocks, and a demo page.
> 
> - **Core**:
>   - **Timeline**: Add `onReset()` to notify all plugins (`packages/analytics-core/src/timeline.ts`).
>   - **Plugin Types**: Extend `Plugin` interface with optional `onReset?(): Promise<void>` (`packages/analytics-core/src/types/plugin.ts`).
> - **Browser SDK**:
>   - **Client**: `reset()` now generates a new `deviceId`, clears `userId`, and calls `this.timeline.onReset()` (`packages/analytics-browser/src/browser-client.ts`).
> - **Tests**:
>   - Add unit tests verifying `onReset` invocation in timeline and browser client tests.
>   - Update mocks to include `getOptOut` and `getIdentity`; switch `BrowserClient` imports to `@amplitude/analytics-core` where needed; refactor helper mock creation.
> - **Test Server**:
>   - Add `test-server/browser-sdk/reset-test.html` to manually test `reset()` and plugin `onReset` behavior.
> 
> <sup>Written by [Cursor Bugbot](https://cursor.com/dashboard?tab=bugbot) for commit 59b5a3d8721587b75d5a5bf61b250bcfff5f2e66. Configure [here](https://cursor.com/dashboard?tab=bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
