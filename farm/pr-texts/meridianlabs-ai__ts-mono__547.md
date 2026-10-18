# Configure jsdom for inspect-components tests

## Summary

- configure `jsdom` as the default Vitest environment for `@tsmono/inspect-components`
- remove redundant per-file `@vitest-environment jsdom` annotations from 43 tests
- include the Vitest config in the package TypeScript project for typed linting

## Why

`inspect-components` is a UI package whose tests broadly depend on DOM APIs. Keeping the environment in package-level configuration avoids boilerplate and ensures new tests inherit the expected environment automatically.

## Impact

Test behavior is unchanged; environment selection is now centralized. The full package suite also confirms that logic-only tests continue to pass under the package default.

## Validation

- `pnpm --filter @tsmono/inspect-components test` (86 files, 926 tests)
- `pnpm --filter @tsmono/inspect-components lint`
- `pnpm --filter @tsmono/inspect-components typecheck`
- `pnpm --filter @tsmono/inspect-components format:check`
