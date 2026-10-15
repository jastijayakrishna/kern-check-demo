# Fix App Router locale path matching with Pages i18n

## Summary

Fix hybrid App Router and Pages Router projects using Pages i18n so explicit or rewritten locale segments remain available to App Router route matching, while Pages routes continue using locale-normalized paths.

The built-in filesystem matcher now carries each route owner through `RouteKind`, avoids duplicate App routes being treated as Pages routes in production, and preserves literal App path parameters through the router server, direct route-module invocation, and static export paths. The same ownership information is maintained by the development bundler.

Adds regression coverage for domain locales, proxy rewrites, exact and dynamic App pages, catch-all parameters, route handlers, inferred default locales, and Pages routes. Adapter-generated routing metadata is intentionally handled in the follow-up layers #97366 and #97500.

Closes #86048

## Verification

- `pnpm build-all`
- `NEXT_TEST_PREFER_OFFLINE=1 pnpm test-start-webpack test/e2e/app-dir/i18n-app-pages-domain-routing/i18n-app-pages-domain-routing.test.ts` (9 passed)
- Prettier and ESLint checks on all changed files

<!-- NEXT_JS_LLM -->
