# feat(lex-password-session): export `extractPdsEndpoint` as public API

`PasswordSession` internally routes requests via `extractPdsUrl(didDoc)` but that function was never exported, forcing consumers to vendor a copy or use `getPdsEndpoint` from `@atproto/common-web` — which has stricter semantics (`type: 'AtprotoPersonalDataServer'` required) and can diverge from the session's own routing logic.

## Changes

- **`util.ts`** — adds `extractPdsEndpoint` as the new public-facing export (same implementation); marks the internal `extractPdsUrl` as `@deprecated` in favour of `extractPdsEndpoint`
- **`index.ts`** — re-exports `extractPdsEndpoint` from the package root
- **`.changeset/`** — minor bump for `@atproto/lex-password-session`

## Usage

```ts
import { extractPdsEndpoint } from '@atproto/lex-password-session'

// Snapshot at persistence time — guaranteed to match PasswordSession's own routing
const pdsUrl = extractPdsEndpoint(didDoc) ?? serviceUrl
await persistAccount({ did, pdsUrl, ... })
```

This lets callers seed the PDS endpoint at account-persistence time using exactly the same predicate the live session uses, so cold-start request routing is correct before the first refresh delivers a fresh DID doc.

<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes #5317
