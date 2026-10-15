# feat(unenv-preset): add support for native node:sqlite module

Devin PR requested by @petebacondarwin
Link to Devin run: https://app.devin.ai/sessions/aee2076b33074b209f3b96acc756ea48

Adds support for the native `node:sqlite` module when the `enable_nodejs_sqlite_module` compatibility flag is enabled.

## Implementation Comparison

Implementations are at:

- Node.js: https://github.com/nodejs/node/blob/main/lib/sqlite.js
- workerd: https://github.com/cloudflare/workerd/blob/main/src/node/sqlite.ts
- unenv: https://github.com/unjs/unenv/blob/main/src/runtime/node/sqlite.ts (stub with `notImplementedClass`)

| Feature | workerd | Node.js | unenv |
|---------|---------|---------|-------|
| DatabaseSync | Full implementation | Full implementation | `notImplementedClass` stub |
| StatementSync | Full implementation | Full implementation | `notImplementedClass` stub |
| constants | Full implementation | Full implementation | Empty object |
| backup | Full implementation | Full implementation | Not exported |
| Status | Experimental | Experimental | Stub |

## Breaking Changes Analysis

**No breaking changes expected.** The unenv implementation provides stub classes that throw when used, so users who enable this flag will gain access to the native workerd implementation where previously the module would throw.

## Usage

This feature is experimental and requires all three flags:

```jsonc
{
  "compatibility_flags": ["nodejs_compat", "experimental", "enable_nodejs_sqlite_module"]
}
```

## Human Review Checklist

- [ ] Verify flag names (`enable_nodejs_sqlite_module`, `disable_nodejs_sqlite_module`) match workerd's compatibility-date.capnp
- [ ] Confirm test assertions match workerd's sqlite module exports (DatabaseSync, StatementSync, constants, backup)
- [ ] Verify the `backup` function and `SQLITE_CHANGESET_OMIT` constant are reliable discriminators between native and stub

---

- Tests
  - [x] Tests included/updated
  - [ ] Tests not necessary because:
- Public documentation
  - [ ] Cloudflare docs PR(s):
  - [x] Documentation not necessary because: This is an experimental feature. The changeset provides sufficient usage documentation.
