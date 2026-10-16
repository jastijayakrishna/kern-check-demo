# fix(cache): preserve abort reasons after completion

## This relates to...

Follow-up to #5818 and #5819.

## Rationale

In jsdom, we need to preserve cancellation and its reason across redirect hops, including after a cached response has completed. Currently, aborting such a response sets `controller.aborted` to `true` but leaves `controller.reason` as `null`, unlike the ordinary request controller.

## Changes

### Features

N/A

### Bug Fixes

Store the cached-response controller's abort reason independently of its backing stream, so it remains available after completion. Preserve the first reason on repeated aborts and the default `AbortError` when no reason is supplied.

### Breaking Changes and Deprecations

N/A

## Status

- [x] I have read and agreed to the [Developer's Certificate of Origin][cert]
- [x] Tested
- [ ] Benchmarked (**optional**; skipped)
- [ ] Documented (no documentation changes needed)
- [ ] Review ready
- [ ] In review
- [ ] Merge ready

[cert]: https://github.com/nodejs/undici/blob/main/CONTRIBUTING.md#developers-certificate-of-origin
