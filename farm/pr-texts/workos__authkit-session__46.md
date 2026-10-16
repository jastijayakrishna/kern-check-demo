# fix: Improve PKCE cookie missing error message

## Summary

Replaces the technical `PKCECookieMissingError` message with a user-friendly, solution-oriented alternative.

**Before:** `"PKCE verifier cookie missing — cannot verify OAuth state. Ensure Set-Cookie headers are propagated on redirects."`

**After:** `"Sign-in session could not be verified. Please try signing in again."`

The old message exposed internal implementation details (PKCE, OAuth state, Set-Cookie headers) that aren't actionable for end users. The new message covers all failure scenarios (session expiry, proxy stripping cookies, etc.) and directs the user toward the correct resolution without leaking technical specifics.

Link to Devin session: https://app.devin.ai/sessions/a078971ce8c94657a457d1a099232333
