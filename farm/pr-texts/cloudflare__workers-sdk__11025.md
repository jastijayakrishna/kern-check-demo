# Use the native `node:wasi` module when available

Adds support for using the native `node:wasi` module from workerd when available, following the pattern established in previous module conversion PRs.

This is part of a series to convert 9 remaining Node.js modules from unenv polyfills to native workerd implementations.

## Changes

- Added `getWasiOverrides()` function to enable/disable the native wasi module based on compatibility flags
- Integrated wasi overrides into the preset system (both nativeModules and hybridModules)
- Added E2E tests for enable/disable flag behavior
- Requires `experimental` flag and `enable_nodejs_wasi_module` flag to enable
- Can be disabled with `disable_nodejs_wasi_module` flag

## Key Differences: workerd vs unenv

The workerd implementation has complete constructor validation for all WASI options (version, args, env, preopens, stdin, stdout, stderr, returnOnExit), while unenv just throws immediately without validation. Both are non-functional stubs.

## Review Focus

- Verify flag naming follows convention: `enable_nodejs_wasi_module` / `disable_nodejs_wasi_module`
- Confirm implementation matches the pattern from cluster/punycode modules
- Check test coverage is consistent with existing module tests

---

**Link to Devin run:** https://app.devin.ai/sessions/f2a8f635e47b47e8baa9bc1b68af0635  
**Requested by:** @petebacondarwin (pbacondarwin@cloudflare.com)

---

- Tests
  - [x] Tests included
- Public documentation
  - [x] Documentation not necessary because: this is an experimental feature requiring the experimental flag
- Wrangler V3 Backport
  - [x] Not necessary because: unenv-preset changes are never backported to v3
