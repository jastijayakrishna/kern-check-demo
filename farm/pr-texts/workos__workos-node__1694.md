# feat: Add optional issuer option for session token validation

## Description

Adds an opt-in `iss` claim check when verifying session access tokens (`authenticateWithSessionCookie` and `loadSealedSession(...).authenticate()`). A new `WorkOSOptions.issuer?: string | string[]` is threaded through `UserManagement.issuer` to both `isValidJwt` implementations and passed straight to `jose.jwtVerify`, which natively accepts a single issuer or a list:

```ts
await jwtVerify(accessToken, jwks, issuer ? { issuer } : undefined);
```

When `issuer` is not set, behavior is unchanged (no `iss` validation). Opt-in rather than defaulted because the API does not mint a single issuer shape — it varies by environment (`https://api.workos.com` for legacy environments, `https://api.workos.com/user_management/<clientId>` for environments created since mid-2025, custom auth domains, and flag-gated path variants). No env var is added here; the core SDK only reads `WORKOS_API_KEY`/`WORKOS_CLIENT_ID` from the environment and this option is passed programmatically like the rest of `WorkOSOptions`.

All edits are within `@oagen-ignore` blocks / ignore-marked files. Companion PRs: workos/authkit-nextjs#476, workos/authkit-remix#90, workos/authkit-react-router#85.

## Documentation

Does this require changes to the WorkOS Docs? E.g. the [API Reference](https://workos.com/docs/reference) or code snippets need updates.

```
[ ] Yes
```

README updated in this PR; no docs-site change required.

Link to Devin session: https://app.devin.ai/sessions/0ee38e859a9849658a7cdb2d215d89a6
Open in Devin Desktop: https://app.devin.ai/desktop/session/0ee38e859a9849658a7cdb2d215d89a6?variant=devin
Requested by: @m0tzy
