# fix: keep the PKCE verifier out of OAuth state

## Summary

The PKCE code verifier was serialized into the OAuth `state` parameter, so it round-tripped through the authorization response URL. This change keeps the verifier in the cookie only and reconstructs it on callback, so it no longer travels in the URL.

_Please review before merging._

## Deployment compatibility

This security fix intentionally rejects the previous shared state/cookie format. Old-format callbacks reaching updated instances and new-format callbacks reaching old instances both fail during a mixed-version rollout. Accepting legacy URL state would retain the callback-replay vulnerability.

Deploy sign-in and callback handlers together with a coordinated cutover. In-flight sign-ins using the old format must restart afterward. Existing authenticated sessions are unaffected. The README now documents this upgrade requirement.
