# Add optional issuer config for access token validation

## Summary

Adds an opt-in `iss` claim check to access token verification via a new `issuer` config key (`configure({ issuer })` or `WORKOS_ISSUER`, resolved by the existing generic `getConfig` env-var mapping). When set, it is passed to `jose.jwtVerify`; when unset, behavior is unchanged (no `iss` check).

```ts
const issuer = getConfig('issuer');
await jwtVerify(accessToken, JWKS, issuer ? { issuer } : undefined);
```

`issuer` is `string | string[]` so an app can accept tokens from more than one issuer (e.g. during an issuer migration); `jose`'s `issuer` option already accepts both. `WORKOS_ISSUER` is split on commas in `Configuration.getValue` (trimmed, empties dropped; a single value stays a string):

```ts
configure({ issuer: 'https://api.workos.com/user_management/client_123' });
configure({ issuer: ['https://api.workos.com', 'https://api.workos.com/user_management/client_123'] });
// WORKOS_ISSUER=https://api.workos.com,https://api.workos.com/user_management/client_123
```

Opt-in rather than defaulted because the API does not mint a single issuer shape — it varies by environment (`https://api.workos.com` for legacy environments, `https://api.workos.com/user_management/<clientId>` for environments created since mid-2025, custom auth domains, and flag-gated path variants). Mirrors workos/authkit-nextjs#476.

Link to Devin session: https://app.devin.ai/sessions/0ee38e859a9849658a7cdb2d215d89a6
Open in Devin Desktop: https://app.devin.ai/desktop/session/0ee38e859a9849658a7cdb2d215d89a6?variant=devin
Requested by: @m0tzy
