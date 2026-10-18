# fix(auth): don't clear profile when the fetch fails offline

## Summary
- Reopening the installed PWA offline restores the cached Supabase session fine (decoding a stored JWT needs no network), but the profile row fetch is a real network call that fails offline. `loadProfile` treated that failure the same as "no profile exists", so `profileComplete` flipped to `false` and the route guard sent already-onboarded students back to `/setup-profile` on every offline open.
- `loadProfile` now checks the fetch `error` explicitly. On success it caches the profile to `localStorage` (`arete-profile-cache`, same dual-sync pattern `useProgress` already uses); on a failed fetch it falls back to that cached copy instead of clearing the profile.

Reported by a beta tester (Prosper Dan) testing offline mode: signed in, went offline, and got kicked to the name/details setup screen despite already having a profile.

## Test plan
- [x] Added regression test `falls back to the cached profile when the fetch fails offline` in `src/__tests__/authContext.test.jsx`
- [x] `npm test` — 310/310 passing
- [x] `npm run lint` — no new warnings/errors

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **Bug Fixes**
  - Improved session reliability when profile data cannot be fetched, such as during offline use.
  - Cached profile information is now restored when reopening the app with an existing session.
  - Prevented temporary profile-fetch errors from incorrectly making a signed-in user appear to have no profile.
  - Updated profile caching so current data is saved and outdated data is removed when appropriate.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
