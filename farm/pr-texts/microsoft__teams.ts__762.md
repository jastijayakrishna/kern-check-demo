# Preserve textFormat through HttpStream's intermediate and final activities

## Summary

`HttpStream` rebuilds outbound activities on every flush/close and forwarded the last emitted message's attachments, entities, suggested actions, and channelData — but not `textFormat`. As a result, `stream.emit({ text, textFormat: 'extendedmarkdown' })` was accepted but dropped on every intermediate typing chunk and on the final message, so streamed Extended Markdown rendered as plain markdown.

## Fix

- Model `textFormat` on `ITypingActivity` / `ITypingActivityInput` / `TypingActivityInput` with a `withTextFormat()` builder (mirroring `MessageActivityInput`).
- `HttpStream` reads the last emitted message's `textFormat` (same "last message wins" state as attachments/entities/etc.) and applies it to the cumulative typing chunks and informative updates in `flush()`, the final message in `close()`, and the timeout fallback in `sendFinal()`.

## Testing

- Unit tests in `packages/api/src/activities/typing.spec.ts` and `packages/apps/src/http/http-stream.spec.ts` covering `textFormat` on typing activities and propagation across intermediate chunks, the final message, and the timeout fallback.
- Validated live in Teams: with the fix, streamed task lists and strikethrough render correctly; without it they fall back to plain markdown.

## Note on C#

This repo only contains the TypeScript SDK; the .NET streaming abstraction is out of scope here.
