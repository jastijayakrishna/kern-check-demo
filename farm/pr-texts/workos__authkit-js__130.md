# fix: Preserve session on transient refresh failures

## Summary
`authkit-js` cleared browser session storage and fired `onRefreshFailure` on **any** non-2xx refresh response, including transient ones (429, 5xx, request timeouts). During a brief WorkOS blip this logs the user out even though their refresh token is still valid. This mirrors the fixes in `authkit-nextjs` (#461) and `authkit-remix` (#88).

The refresh client now classifies failures by HTTP status and only tears down the session for **terminal** errors:

```ts
// http-client.ts — was: throw new RefreshError(error.error_description) for any non-2xx
const RETRYABLE_REFRESH_STATUS_CODES = new Set([408, 429, 500, 502, 503, 504]);
throw new RefreshError(body.error_description, {
  status,
  error: body.error,           // e.g. "invalid_grant"
  isTransient: RETRYABLE_REFRESH_STATUS_CODES.has(status),
});
```

`RefreshError` gains `status`, `error`, and `isTransient` (exported so callers can branch), and `RefreshTimeoutError` is now `isTransient: true`.

In `create-client.ts`, the destructive path is gated on `!error.isTransient`:

```ts
// #doRefresh: was `if (error instanceof RefreshError)`
if (error instanceof RefreshError && !error.isTransient) {
  removeSessionData(...); // clear storage + org id
  onRefreshFailure?.(...);
  this.#state = { tag: "ERROR" };
} else {
  // transient (429/5xx/timeout/network): keep session, stay AUTHENTICATED so
  // a later getAccessToken() retries
  this.#state = { tag: "AUTHENTICATED" };
}
```

`getAccessToken()` and `switchToOrganization()` likewise rethrow a transient `RefreshError` (so the caller can retry) instead of converting it to `LoginRequiredError` / redirecting to sign-in. Terminal `400 invalid_grant` / `401` behavior is unchanged. A non-JSON 5xx body is now parsed safely so its status still drives classification.

## Test plan
- `npm run build` — passes
- `npm run format:check` — passes
- `npx jest` — 104 passing, including new `http-client` tests (transient 408/429/5xx classification, non-JSON 5xx body, terminal 400/401, raw network failure not wrapped) and `create-client` tests (session preserved + `onRefreshFailure` not fired on 408/429/500/503/504; terminal still clears).

Link to Devin session: https://app.devin.ai/sessions/fc39103abf694f90b1c92dd714a81461
Requested by: @m0tzy
