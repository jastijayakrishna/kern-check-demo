# Desktop: Fixes #16783: Fix AI chat counting tool results twice towards the size limit

Fixes #16783.

`assertWithinTokenBudget()` counted the content of tool messages twice: once for every message, and again in a `ChatRole.Tool` branch. Tool results hold the note body, other notes and search results. Because of the double count, chats hit "This conversation has grown too large to send" at roughly half the intended size, and a note over about 160,000 characters couldn't be used at all.

This removes the duplicate branch. The budget still counts every message's content plus assistant tool call arguments (added in #15881). The 80,000-token limit is unchanged.

### Testing

- New unit test: a tool result of about 75 tokens fits a 100-token budget, and one of about 125 tokens doesn't. The test fails before this change.
- The `services/ai` tests, type check and ESLint pass locally.

### AI Assistance Disclosure

The investigation, code, test and this description were produced with Claude Code (AI). The tests, type check and ESLint were run locally.

I reviewed the change and understand how it works.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
