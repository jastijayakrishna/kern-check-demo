# fix(queries): stop retrying deterministic failures

## What

The query client ran react-query defaults - `retry: 3` with exponential backoff - everywhere, including SSR. Two changes:

- **SSR: `retry: false`.** A loader failure fails fast into its route boundary instead of running a backoff ladder inside TTFB. This is the standard posture for server-side react-query; the defaults target interactive clients where a spinner justifies waiting.
- **Client: retries skip 4xx, except 429.** The predicate only ever sees this API's own statuses - provider failures surface as 5xx (`PROVIDER_REQUEST_FAILED`), so a client 429 can only mean platform limiting of our endpoints: short-window and worth the standard backoff. The rest of 4xx does not heal on a seconds-scale retry.

## Provider 429s stay single-attempt at every layer

The provider fetch layer never retries, and SSR retries are now off, so an upstream 429 gets exactly one attempt by design. The reason is recorded where the failure is wrapped (`service.ts`): probed 2026-08-13, Smithsonian (api.data.gov) documents a rolling 1,000/hour window with `X-RateLimit-*` headers and **no Retry-After**; NASA IVL is keyless with no documented limits and no rate-limit headers at all. Honoring `Retry-After` would take three-hop plumbing (provider response header, API error response, `EyepieceApiError` field feeding a custom `retryDelay`) and there is nothing to honor today. A provider starting to send `Retry-After` is what reopens this.

## Trade-offs

- A genuinely transient SSR failure now surfaces instead of silently healing. Streamed sections (home strips, collection cards, search sections) self-heal on hydration: the query never dehydrated as success, so the client refetches under the client policy. Loader-critical data (asset detail) does not - the route error boundary renders and recovery is a reload. If real transient SSR failures show up there, the middle setting is SSR `retry: 1` with a flat ~200ms delay; not taken now for lack of evidence it is needed.
- Mutations already default to no retries and are untouched.

## What this does not fix

The 22s local / 12s production not-found pages that motivated the investigation are Netlify 404 URL-fallback behavior, tracked in #274 and measured unchanged by this change. This PR stands on its own merits: no retry ladder inside SSR TTFB under real transient failures, and no client-side retry bursts against deterministic 4xx responses.

## Verified

prettier, eslint, tsc green; unit suite 875 including the retry-predicate tests (4xx skipped, 429 retried, 5xx and shapeless errors retried).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
