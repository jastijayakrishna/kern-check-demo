# fix(live): verify CORS via /check/cors (credentials-aware) before reporting CorsOriginError

## Summary

Today, `live.events()` reports a `CorsOriginError` on _any_ failure of a side-band OPTIONS preflight, so transient network issues (offline, DNS, certificate, 5xx, etc.) get misreported as CORS rejections.

This PR replaces that probe with a `GET /check/cors` request that asks the server whether the current origin is actually allowed, and only raises `CorsOriginError` when the server explicitly says it isn't.

- New `checkCorsObservable(url, projectId, requireCredentials)` helper in [`src/data/live.ts`](src/data/live.ts) encapsulates the probe; the call site is a single line.
- The cors-check URL is resolved via `client.getUrl('/check/cors')`, so it respects the existing `useProjectHostname`, `apiHost`, `apiVersion`, and `projectId` config (e.g. `https://api.sanity.io/v<apiVersion>/check/cors` or `https://<projectId>.api.sanity.io/v<apiVersion>/check/cors`).
- Errors with `CorsOriginError` only when `/check/cors` responds with `result.allowed === false` (or, in the credentialed case below, `result.withCredentials === false`). Every other outcome (`allowed: true`, non-2xx response, network error, malformed body, aborted subscription) is intentionally silent: the probe emits a single `void` value and completes so downstream `mergeMap` consumers can continue, and the EventSource's original underlying error propagates unchanged.
- The outer `catchError` in `events()` short-circuits when the error is already a `CorsOriginError`, so a CORS rejection results in exactly one `/check/cors` call (previously two: one from the `reconnect` event, then a redundant second one from `catchError` swallowing the same error).

### Credentials-aware probe

Following review feedback from @rexxars: an origin can be allow-listed for CORS _without_ credentials, in which case `/check/cors` returns `{result: {allowed: true, withCredentials: false}}`. Previously we only inspected `result.allowed`, so a credentialed listener (`includeDrafts: true` + `withCredentials: true`) would silently swallow the CORS issue and let an opaque error from the EventSource propagate instead.

The probe is now credentials-aware:

- `checkCorsObservable` takes a `requireCredentials` flag set from `esOptions.withCredentials`.
- When `requireCredentials && result.withCredentials === false`, a `CorsOriginError` is raised with `credentials: true` so its `addOriginUrl` deep-link includes a `credentials=` query param. The Sanity management CORS form opens with the "Allow credentials" toggle pre-selected.
- When `result.allowed === false`, the error is raised with `credentials: requireCredentials`, so the deep-link still pre-selects credentials whenever the caller needed them - regardless of which rejection branch fired.

### `CorsOriginError` shape change

`CorsOriginError`'s `projectId` is now optional and the constructor accepts a new `credentials?: boolean`. Existing callers passing `{projectId}` remain source-compatible.

Although the type signature change (`projectId: string` -> `projectId?: string`) _looks_ breaking, it isn't:

- The internal call site has always passed `projectId!` from `client.config().projectId`, which is itself `string | undefined`. The non-null assertion was lying - in resource-config mode (`resource: {...}`) there is no `projectId`.
- When that happened at runtime, the template literal `` `https://sanity.io/manage/project/${projectId}/api` `` interpolated the string `"undefined"`, producing the broken URL `https://sanity.io/manage/project/undefined/api`.
- Making `projectId` optional finally lets us drop the `!`, and in the missing-`projectId` branch we now construct a generic message without the broken URL (the deep-link is skipped because it can't actually route the user anywhere useful).

Users who construct `CorsOriginError` themselves (uncommon - it's primarily a class the SDK throws, not one consumers instantiate) lose no real capability; the new shape is a strict superset of what was actually safe to do before.

## Live test deployments

Both apps use `@sanity/client`; one runs `@latest` (before) and one runs this branch (after). Open DevTools' Network tab to compare behaviour.

### Transient network loss (offline -> back online)

| | Before (`@latest`) | After (this PR) |
| --- | --- | --- |
| URL | https://next.sanity.dev/ | https://next-sanity-git-test-no-cors.sanity.dev/ |
| When you toggle offline | Reports a **false-positive** ``next.sanity.dev is blocked by CORS policy`` error. The failing OPTIONS preflight is interpreted as a CORS rejection. | No CORS error: `/check/cors` is unreachable too, so CORS is treated as unknown and the EventSource's own error is allowed to propagate. |
| When you go back online | Stays broken - the client believes CORS is denied, so it never reconnects. | Auto-reconnects: console logs a few ``<SanityLive> is attempting to reconnect`` lines followed by ``<SanityLive> is connected and listening for live events to published content.`` |

### Origin not in the project's CORS allow-list (actual CORS rejection)

| | Before (`@latest`) | After (this PR) |
| --- | --- | --- |
| URL | https://next-sanity-no-cors.vercel.app/ | https://next-sanity-no-cors-preview.vercel.app/ |
| Failing requests | ~5: the EventSource itself, then the OPTIONS preflight, then the preflighted request behind it, etc. | 2: one failing EventSource request, then one successful `/check/cors` request that returns `{result: {allowed: false}}`. |
| Reported error | `CorsOriginError` (correct, but reached via the noisy path above). | `CorsOriginError`, confirmed by the API itself - so the diagnosis is now actually trustworthy. |

## Test plan

- `test/live.test.ts` updated: existing CORS-related tests rewired to mock `GET /check/cors` instead of the OPTIONS preflight, plus new regression tests:
  - `does not report CorsOriginError when /check/cors returns a non-2xx response` (covers the `!response.ok` short-circuit)
  - `does not report CorsOriginError when /check/cors returns invalid JSON` (covers the JSON-parse / `.catch` branch)
  - `uses non-project hostname for /check/cors when useProjectHostname is false`
  - `reports CorsOriginError when EventSource needs credentials but /check/cors reports withCredentials: false` - asserts both the `CorsOriginError` and that `addOriginUrl.searchParams.get('credentials') === ''`
  - `does not report CorsOriginError when /check/cors reports allowed: true, withCredentials: true and the EventSource needs credentials`
- `npm test -- test/live.test.ts` (27 passing).
- `npm test` (full suite, 989 passing).
- `npm run lint`.
- Manual verification on the live test deployments linked above.

Made with [Cursor](https://cursor.com)
