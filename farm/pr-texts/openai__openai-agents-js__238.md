# feat(realtime): make websocket URL configurable

## Summary
- allow passing a `url` in `OpenAIRealtimeWebSocket` constructor
- forward `url` from `RealtimeSession.connect` to the transport layer
- add related tests
- add changeset for `@openai/agents-realtime`

## Testing
- `pnpm lint`
- `pnpm build`
- `CI=1 pnpm test`


------
https://chatgpt.com/codex/tasks/task_i_687e86dc9b3c833188d28264766aa580
