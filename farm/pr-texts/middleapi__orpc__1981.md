# feat(ai-sdk): stream tool outputs for async generator handlers

`createToolFactory` now streams tool outputs whenever the procedure handler is an `async function*`, not only when the output schema is built with `asyncIteratorObject`. Previously a schema-less async generator handler (or one paired with a `type<AsyncIteratorObject<...>>()` schema) returned the iterator object as the tool result instead of streaming preliminary results, even though the inferred tool output type was already the yield type.

The detection lives in `@orpc/shared` as `isAsyncGeneratorFunction`, so other packages can reuse it.

## Fixes

- Async generator handlers stream each event as a preliminary tool result with or without an `asyncIteratorObject` output schema. Runtime behavior now matches the inferred `InferToolOutput` type.
- Output schemas remain the source of truth; the handler check is a fallback, so plain `async` handlers that happen to return an iterator are unchanged.

## Testing

- New unit tests for `isAsyncGeneratorFunction` (bound functions and async generator methods included, sync generators and plain async functions excluded).
- New AI SDK tests: streaming without an output schema, streaming with a non-`asyncIteratorObject` schema, and no streaming for a non-generator handler returning an iterator. Type test covers the schema-less yield type inference.
- Docs "Streaming Tool Outputs" section mentions the `async function*` path.

