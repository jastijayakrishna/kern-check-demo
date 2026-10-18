# refactor(lint): enforce statement-order strict on src, exempt tests

## Summary

Clears the second (and last) deferred lint rule. Enables `code-organization/enforce-statement-order` at full strict (`checkAllFunctionBodies:true, checkAwaitedCalls:true`) on `src/**`, driven to **zero** (52 violations fixed), and exempts test files.

### Fixes preserve behavior exactly

- Pure definitions hoisted above side effects where there's no dependency.
- Helpers extracted where a definition depends on an awaited result, or must stay *after* a guard to preserve HTTP error-status ordering (e.g. `403 → 401 → 400`).
- Fetch/timer concurrency and await ordering unchanged throughout.

### Tests exempt (by design)

Smoke/integration suites interleave arrange-act-assert with sequential awaited UI/HTTP interactions where the await **order is the test logic** — reordering would change behavior. Exempting tests is consistent with the existing `immutable-data`/`no-let`/`max-lines` test relaxations.

No `let`, no `any`, no `eslint-disable`, no ratcheting. Three files near the 300-line cap were reshaped (not relaxed) to stay under it.

With this, **both** previously-deferred lint rules (`type-declaration-immutability` in #1549, and `enforce-statement-order` here) are enforced and at zero — the lint debt is fully cleared.

## Verification

`bun run build` / `typecheck` / `lint` clean (both rules at 0); `bun run test` 714 pass.

🤖 Generated with Claude Code
