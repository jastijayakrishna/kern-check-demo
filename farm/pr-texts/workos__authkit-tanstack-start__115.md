# fix: source client access tokens from the session

## Summary

The client `TokenStore` (`src/client/tokenStore.ts`) read a JavaScript-readable `workos-access-token` cookie and adopted it as the session bearer token. This change removes that client-readable cookie channel and sources the token from the server-side session.

_Please review before merging._
