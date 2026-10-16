# fix(rsc): tag middleware short-circuit responses as React-Router-Resource

Closes #15599

### Description

In RSC Framework Mode, when middleware short-circuits a document request by returning its own non-RSC `Response` (without calling `next()`), `routeRSCServerRequest` attempted to decode the response body as a Flight stream. This resulted in `Error: Connection closed.` and returned a 500 status to the client.

This PR addresses the issue by tracking whether the middleware execution called `next()` (invoking `generateMiddlewareResponse`):
1. When middleware short-circuits (`!didRender`) and returns a non-redirect `Response`, it is tagged with `React-Router-Resource: "true"`.
2. `routeRSCServerRequest` already checks `serverResponse.headers.get("React-Router-Resource") === "true"` and returns the resource response directly without attempting Flight stream decoding.
3. Added `middleware?: MiddlewareFunction<any>[]` to `RSCRouteConfigEntry` type declarations.
4. Added regression tests covering middleware short-circuit responses, `routeRSCServerRequest` pass-through behavior, standard `next()` RSC render responses, and short-circuit redirect responses.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
