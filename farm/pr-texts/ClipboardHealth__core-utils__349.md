# fix(eslint-config): correct @date-fns/tz package name

## Summary

Fixes the package name in the `no-restricted-imports` rule from `date-fns/tz` to `@date-fns/tz`. The previous PR (#347) incorrectly omitted the `@` prefix - `@date-fns/tz` is a scoped npm package.

Also removes the unnecessary subpath pattern (`@date-fns/tz/*`) since the package's documented public API only uses the root import path (`from "@date-fns/tz"`).

## Review & Testing Checklist for Human

- [ ] Verify that `@date-fns/tz` is the correct npm package name (it is: https://www.npmjs.com/package/@date-fns/tz)
- [ ] Confirm the package only exposes root-level imports (no subpath exports)

### Notes

Requested by @Davidster

Link to Devin run: https://app.devin.ai/sessions/57ad92df3fb246bbb831aec5c6eec61d
