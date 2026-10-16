# feat: support per-route error codes in Swagger build pipeline

## Summary

The OpenAPI build pipeline previously applied a fixed set of global `errorCodes` (400, 401, 404, 408, 429, 500) to every route's Swagger responses. Routes that return additional status codes (e.g. 409 Conflict for the Crawl cancel endpoint) had no way to surface them in the generated docs.

This PR adds an opt-in `errorCodes` property to the `Route` base class:

```ts
// src/types.ts — Route base class
errorCodes?: Record<number, ErrorCode>;
```

```ts
// Downstream usage example (e.g. in enterprise Crawl route):
class CrawlDeleteRoute extends HTTPRoute {
  errorCodes = {
    409: {
      code: 409,
      description: 'The crawl is already in a terminal state.',
      message: 'HTTP/1.1 409 Conflict',
    },
  };
}
```

`build-open-api.js` now reads `route.errorCodes` and merges it with the global defaults:

```js
responses: {
  ...errorCodes,           // global defaults
  ...(r.routeErrorCodes || {}),  // per-route additions
},
```

Also exports a reusable `ErrorCode` interface from `src/http.ts` and replaces `as const` with `Record<number, ErrorCode>` on the existing code/error code objects so the types are extensible.

Link to Devin session: https://app.devin.ai/sessions/692a681867f4413d9cf082e844cde851

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * API documentation now shows route-specific error responses alongside shared error responses, giving a more complete view of possible outcomes.
* **Bug Fixes**
  * Standardized error code definitions to improve consistency across generated API details and route behavior.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
