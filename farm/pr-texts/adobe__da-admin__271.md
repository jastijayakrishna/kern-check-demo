# fix: treat versionsource 412 as success, eliminating ~860 500s/day

## Problem

Worker logs show ~860 `500` responses per 24 hours, all from `POST /versionsource/adobecom/da-cc/{locale}/…` endpoints hit by the localization pipeline.

Every entry has:
```
warn: "An error was encountered in a non-retryable streaming request."
```
A subset also have:
```
error: "writeAuditEntry failed"
      "PreconditionFailed: At least one of the pre-conditions you specified did not hold."
```

## Root cause

The localization pipeline processes many locales in parallel. Multiple concurrent workers read the same source document, all obtain the same `Version` UUID from the object's metadata, and all call `POST /versionsource` with a label at the same moment.

`putVersion` uses `If-None-Match: *` to write the version object (so it can only be created once per key). The first caller wins and gets `200`. Every subsequent concurrent caller gets a `412 PreconditionFailed` from R2, because the version key already exists.

In `putObjectWithVersion`:
```js
versionCreated = versionResp.status === 200;  // false on 412
```

Then in `postObjectVersionWithLabel`:
```js
if (!resp.versionCreated) return { status: 500, error: 'Version was not created' };
```

This returns `500` even though the version **was** created — by the first concurrent request.

## Fix

Treat `412` from `putVersion` as "version already exists = created by a concurrent call":

```js
// 412 means the version key already exists — a concurrent request created it first.
// The version IS persisted in R2, so treat it as created.
versionCreated = versionResp.status === 200 || versionResp.status === 412;
```

## Test plan

- [ ] Existing test `putObjectWithVersion sets versionCreated true when version already existed (putVersion 412 = concurrent race)` — updated to assert `versionCreated === true`
- [ ] Existing test `postObjectVersion returns 201 when version already exists in R2 (putVersion 412 concurrent race)` — updated to expect `201` instead of `500`
- [ ] New test `returns 201 when version PUT gets 412 (concurrent race — version already exists in R2)` via `postObjectVersionWithLabel` — verifies end-to-end that the caller gets `201`
- [ ] All 368 tests pass, lint clean

🤖 Generated with [Claude Code](https://claude.com/claude-code)
