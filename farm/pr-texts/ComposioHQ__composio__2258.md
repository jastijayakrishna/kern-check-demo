# fix: use SDKErrorCodes.NO_API_KEY_PROVIDED instead of hardcoded string

## Summary

Fixes #2254

The `ComposioNoAPIKeyError` class was using a hardcoded `'NO_API_KEY'` string for the error code, but `SDKErrorCodes.NO_API_KEY_PROVIDED` is defined as `'NO_API_KEY_PROVIDED'`. This mismatch meant that code trying to match error codes against `SDKErrorCodes` would fail.

Changed the error class to use `SDKErrorCodes.NO_API_KEY_PROVIDED` directly to ensure consistency.

## Review & Testing Checklist for Human

- [ ] Verify no existing code (internal or external) depends on the literal string `'NO_API_KEY'` - search the codebase and docs for this string
- [ ] Consider if this is a breaking change that needs to be called out in release notes (users matching against the old string will break)

### Test Plan
1. Create a simple script that initializes `Composio` without an API key
2. Catch the thrown `ComposioNoAPIKeyError` 
3. Verify `error.code === 'TS-SDK::NO_API_KEY_PROVIDED'` (the base class prefixes with `TS-SDK::`)

### Notes
- Link to Devin run: https://app.devin.ai/sessions/5bb0d7ec18744bbba32647cadb04817d
- Requested by: rahul@composio.dev (@CryogenicPlanet)
