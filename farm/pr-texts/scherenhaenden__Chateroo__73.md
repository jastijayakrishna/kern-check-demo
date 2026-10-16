# feat: enable streaming chat responses

## Summary
- support Server-Sent Events in chat controller
- stream chunks from chat service to clients

## Testing
- `npm run lint --workspace=backend` *(fails: Unsafe member access errors)*
- `npm test --workspace=backend`


------
https://chatgpt.com/codex/tasks/task_e_68b49487367c8333b67bd9615edec39e

## Summary by Sourcery

Enable streaming chat responses in the backend chat controller using Server-Sent Events, while retaining the existing non-stream JSON endpoint.

New Features:
- Support streaming chat responses via Server-Sent Events in the chat controller
- Allow clients to trigger streaming mode via a payload.stream flag or Accept header

Enhancements:
- Set appropriate SSE headers, flush response, and stream chunks from the chat service
- Emit a [DONE] event on stream completion and handle errors by sending error events
