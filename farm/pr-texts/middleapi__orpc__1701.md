# refactor(pinia-colada): align key utils with tanstack-query

## Summary

Renames the Pinia Colada key utilities to match the `@orpc/tanstack-query` package, so both integrations share the same API shape:

- `buildKey` → `generateOperationKey`
- `BuildKeyOptions` → `OperationKeyOptions<TType, TInput>` (`fnOptions` now only allowed for `streamed`)
- `BuildKeyPrefixOptions` → `OperationKeyPrefixOptions`
- adds the `OperationKey<TType, TInput>` type; `utils.key()` now returns it

Pinia Colada specifics are kept: input is still serialized (entry keys must be JSON-serializable) and mutation keys still accept `input` (mutation keys are per-input functions).
