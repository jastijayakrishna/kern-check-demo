# Guard transaction acquire failures in PgClient.fromPool

## Problem

In `packages/sql/pg/src/PgClient.ts`, `reserveRaw` (the transaction acquire path) attaches its `error` listener to `client` unconditionally after the `pool.connect` if/else:

```ts
pool.connect((err, client, release) => {
  if (err) {
    resume(Effect.fail(new SqlError({ ... })))
  } else {
    resume(Effect.as(...))
  }
  function onError(cause_: Error) { cause = cause_ }
  client!.on("error", onError)   // runs even when err is set
})
```

When `pool.connect` invokes the callback with `err` set (or returns no client), control still falls through to `client!.on("error", onError)`, which dereferences `undefined` and throws a `TypeError` synchronously inside the pg callback. That escapes the `SqlError` channel and surfaces as a defect — exactly the failure mode that should stay recoverable for transient connection errors (`08006`, pool exhaustion, etc.).

## Fix

- Early-return on the `err` branch via `return resume(...)`.
- Add an explicit `!client` branch returning `SqlError({ reason: new ConnectionError({ ..., operation: "acquireConnection" }) })`.
- Hoist `onError` so it is in scope for both branches without TDZ.
- Drop the `!` non-null assertions on the success path now that `client` is provably defined.

The shape mirrors the existing streaming acquire block in the same file (`PgClient.ts:264-297`), which already uses `classifyError` + `ConnectionError` with `operation: "acquireConnection"` and an `else if (!client)` early return. This change brings `reserveRaw` into consistency with that sibling.

## Prior art

This also matches the equivalent logic in `Effect-TS/effect`'s [`packages/sql-pg/src/PgClient.ts`](https://github.com/Effect-TS/effect/blob/ec5c50507b1a2f5ad712c148a7da0fadb8cb9f52/packages/sql-pg/src/PgClient.ts#L275-L310), where `reserveRaw` already handles both the `err` and `!client` branches with early returns before touching the client. The smol port appears to have dropped the early returns during the rewrite; this PR restores parity while adapting to smol's `classifyError` / `ConnectionError` idiom.

## Tests

`packages/sql/pg/test/TransactionAcquire.test.ts` — two `it.effect` cases driving a fake pool, following the existing `SqlErrorClassification.test.ts` idiom:

1. `withTransaction surfaces acquire failures instead of defecting` — exercises the `err` branch with a `08006`-shaped cause and asserts the error stays in the `SqlError` channel as a `ConnectionError` with `operation: "acquireConnection"`. Without the fix this case throws a `TypeError` defect.
2. `withTransaction surfaces missing-client acquire as ConnectionError` — exercises the defensive `!client` branch.

## Validation

- `pnpm --filter @effect/sql-pg exec vitest run test/TransactionAcquire.test.ts test/SqlErrorClassification.test.ts` → 4/4 pass
- `cd packages/sql/pg && pnpm exec tsc --noEmit` → clean
- Changeset: `@effect/sql-pg` patch

## Note

I scoped validation to the targeted test files because `packages/sql/pg/test/KeyValueStore.test.ts` has pre-existing failures in its `remove` cases on current `main`, unrelated to this patch.
