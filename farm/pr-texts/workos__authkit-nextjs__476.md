# feat: Add optional WORKOS_ISSUER access token issuer validation

## Summary

Adds an opt-in `iss` claim check to access token verification. When `WORKOS_ISSUER` is set, it is passed to `jose.jwtVerify` as the expected issuer; when unset, behavior is unchanged (signature + expiry only, no `iss` check).

`WORKOS_ISSUER` may be a single issuer or a comma-separated list; `getExpectedIssuer()` splits on commas (trimmed, empties dropped) and forwards a plain string for one value or a `string[]` for several — `jose`'s `issuer` option accepts both.

```ts
function getExpectedIssuer(): string | string[] | undefined {
  if (!WORKOS_ISSUER) return undefined;
  const issuers = WORKOS_ISSUER.split(',').map((s) => s.trim()).filter(Boolean);
  return issuers.length <= 1 ? issuers[0] : issuers;
}
const issuer = getExpectedIssuer();
await jwtVerify(accessToken, JWKS(), issuer ? { issuer } : undefined);
```

```sh
WORKOS_ISSUER=https://api.workos.com/user_management/client_123
WORKOS_ISSUER=https://api.workos.com,https://api.workos.com/user_management/client_123
```

Opt-in rather than defaulted because the API does not mint a single issuer shape — it varies by environment (`https://api.workos.com` for legacy environments, `https://api.workos.com/user_management/<clientId>` for environments created since mid-2025, custom auth domains, and flag-gated `/sso/<clientId>` and `/convex/<clientId>` variants). A hardcoded default would reject valid tokens and force a refresh on every request for most environments. The list form covers apps that accept tokens from more than one of those issuers (e.g. during an issuer migration). Same shape as the `issuer` override in workos/authkit-react-router#85.

Link to Devin session: https://app.devin.ai/sessions/0ee38e859a9849658a7cdb2d215d89a6
Open in Devin Desktop: https://app.devin.ai/desktop/session/0ee38e859a9849658a7cdb2d215d89a6?variant=devin
Requested by: @m0tzy
