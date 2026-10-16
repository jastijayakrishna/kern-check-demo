# fix: accept `cacheTTL: Infinity`, keep rejecting `NaN`

`#640` inadvertently made `cacheTTL: Infinity` a breaking change by applying the same `Number.isFinite` guard used for the security fix on `clockTimestamp`/`clockTolerance`. Unlike those options, `cacheTTL: Infinity` is safe — the cache window is always clamped to the token's own `exp`, so no expired token is accepted.

## Changes

- **`src/verifier.js`** — relax `cacheTTL` guard from `!Number.isFinite` to `Number.isNaN`; `clockTimestamp` and `clockTolerance` keep their `isFinite` check
- **`test/verifier.spec.js`** — remove the assertion that `Infinity` throws; add a test confirming an expired token is still rejected when `cacheTTL: Infinity`
- **`README.md`** — note that `Infinity` is a valid value meaning "no cap beyond the token's own expiry"

```js
// Before (#640 behaviour — unintended breaking change)
createVerifier({ key, cacheTTL: Infinity }) // throws

// After — works as pre-#640, expired tokens still rejected
createVerifier({ key, cacheTTL: Infinity }) // ok
createVerifier({ key, cacheTTL: NaN })      // still throws
```

<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes #651
