# feat(eve): sign users in as the agent's Application through a stable callback route (ECO-452)

## Summary

Implements eve.md spec-version 6 (keycard-sdk-spec #83) for `@keycardai/eve`, with the two corrections the spec follow-up PR records: the export is a route, not a channel, and `applicationCredential` on `Keycard.interactive` is rejected until `@keycardai/oauth` supports client assertions on code redemption and refresh.

`keycardCallbackRoute({ path = "/keycard/callback", origin? })` returns `{ transport: "http", method: "GET", path, handler }`, typed as eve's `HttpRouteDefinition` through a type-only import from `eve/channels`, so the package still loads no eve code. The host mounts it with `export default defineChannel({ routes: [keycardCallbackRoute()] })`. The handler decodes the attempt's eve callback URL from `state`, requires `target.origin === request origin` (or the configured `origin`) and a path starting with `/eve/v1/connections/` containing `/callback/` (after stripping `EVE_PUBLIC_ROUTE_PREFIX` when set), and answers `302` to it with the incoming query string copied verbatim. Anything else is `400` with no `Location`.

`Keycard.interactive` with `clientId` and `clientSecret`:

```
redirectUri = new URL(attemptCallbackUrl).origin + callbackPath   // default /keycard/callback
redirect    = flow.begin({ clientId, redirectUri, ... })            // no flow.register call
state       = `${redirect.state}.${base64url(attemptCallbackUrl)}`  // replaces state= on the challenge URL
resume      = { state, codeVerifier, resources, callbackUrl: redirectUri, clientId }
complete    = flow.complete({ ..., state: resume.state, redirectUri: resume.callbackUrl, clientSecret })
refresh     = flow.refresh({ ..., clientId, clientSecret })
```

`@keycardai/oauth`'s `beginAuthorization` generates `state` itself, so the attempt callback URL is appended to the value it returns and the challenge URL's `state` parameter is rewritten; `completeAuthorization`'s exact-match check against `resume.state` is unchanged because the zone echoes the composite. Without `clientId` every call is byte-identical to before (row 49 pins the full record of registration, begin, resume, challenge URL, complete, and refresh).

Behavior change to flag: `clientId` used to mean "a static client whose registered redirect URIs already cover eve's per-attempt callback" and sent eve's callback as `redirect_uri`. The spec retired that reading (no such client can exist), so three existing tests that encoded it were updated: the two static-`clientId` tests now expect the stable route and composite state, and the "sends no client secret for a registered client" test drops its `clientSecret`-without-`clientId` setup, which is now a definition-time error.

## Proxy origin finding

eve builds the attempt callback URL from the workflow runtime's metadata URL (`resolveWorkflowCallbackBaseUrl` in `dist/src/execution/workflow-callback-url.js`: Vercel production URL, else `WORKFLOW_LOCAL_BASE_URL`, else the workflow's own `url`, plus `EVE_PUBLIC_ROUTE_PREFIX`), not from the incoming request. The route handler's `request.url` comes from eve's Node server (`dist/src/compiled/env-runner/node-worker.js`): `Host` (or `x-forwarded-host` only when the server is marked trusted) and `https` only when the socket is TLS or `x-forwarded-proto: https`. On Vercel both agree. Behind a proxy that terminates TLS without `x-forwarded-proto`, or rewrites `Host`, the request origin is `http://` or an internal host while the callback URL carries the public origin, and the strict check would answer 400 for every sign-in. Hence the optional `origin` on `keycardCallbackRoute`: the public origin to compare against instead of the request's. Documented in the README.

## Tests

Spec rows 45 and 46 in `src/callbackRoute.test.ts` (success and error-shaped forwards with every parameter; other origin, other path, non-callback path, random-only, empty, and non-base64url state, plus missing state, all 400 without `Location`; the `origin` override), rows 47, 49, 50 in `src/interactive.test.ts` (47 also covers a mismatched composite state still failing `INVALID_CALLBACK`). Row 48 is not implementable yet and its cases are in row 50 as the "not supported yet" error.

## Verification

```
pnpm typecheck   clean
pnpm test        Test Suites: 6 passed, Tests: 101 passed
pnpm build       ok
python3 scripts/changelog.py check-drift   No version drift
```

The repo defines no `lint` script (pr.yml runs typecheck, test, build). 0 em dashes in added lines. `feat(eve)` cuts the next `@keycardai/eve` minor.


Link to Devin session: https://app.devin.ai/sessions/bbc062cf32b548ef9c4b8b444d2ec67f
Open in Devin Desktop: https://app.devin.ai/desktop/session/bbc062cf32b548ef9c4b8b444d2ec67f?variant=devin
Requested by: @Larry-Osakwe
