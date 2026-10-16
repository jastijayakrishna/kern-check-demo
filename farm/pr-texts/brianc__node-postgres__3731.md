# Emit a deprecation warning when serializing an invalid Date

`new Date(undefined)` (or any invalid `Date`) is silently serialized to `"0NaN-NaN-NaNTNaN:NaN:NaN.NaN+NaN:NaN"`, a string Postgres cannot meaningfully parse, leading to confusing downstream errors instead of a clear signal at the source.

## Changes

- **`packages/pg/lib/utils.js`**: `prepareValue` now emits a `util.deprecate`-based process warning (code `PG_INVALID_DATE`) when serializing an invalid `Date`, without changing the current serialized output, for backwards compatibility. The warning explains that this will become an error in the next major version of `pg`.
- **`packages/pg/test/unit/utils-tests.js`**: added a unit test asserting `prepareValue` emits the `PG_INVALID_DATE` warning and still serializes the invalid date to the existing (garbage) string.

```js
const { Client } = require('pg')
const client = new Client()

// Still serializes to "0NaN-NaN-NaNTNaN:NaN:NaN.NaN+NaN:NaN" today,
// but now also emits a DeprecationWarning (code PG_INVALID_DATE)
await client.query('INSERT INTO events (occurred_at) VALUES ($1)', [new Date(undefined)])
```

- Fixes #3318
