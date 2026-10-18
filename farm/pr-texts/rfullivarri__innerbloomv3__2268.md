# fix web google oauth onboarding redirect

## What changed

- Adds an explicit `oauthMode` to the shared Google OAuth button so the displayed auth intent can differ from the Clerk resource used to start OAuth.
- Routes web Google sign-up and the onboarding auth gate through Clerk's `signIn` OAuth resource while preserving the sign-up/onboarding redirect target.
- Enables Clerk cross-mode completion for web Google sign-up, matching the safer mobile OAuth pattern already used in the app.

## Why

The web onboarding flow could get stuck on `/sso-callback` after Google OAuth. The browser console showed Clerk failing `POST /v1/client/sign_ups` with `400 Bad Request`, which happens before the app can create a session or redirect to onboarding.

Using Clerk's sign-in OAuth resource for Google avoids forcing the callback through the failing `sign_ups` endpoint when the selected Google account already exists, while still allowing Clerk to complete sign-up when needed.

## Impact

- Web Google sign-up should complete and redirect to `/intro-journey` or the requested onboarding target.
- Existing Google users entering from a sign-up CTA should no longer get stranded on `/sso-callback`.
- Native Android/iOS files are untouched in this hotfix branch.

## Validation

- Confirmed the hotfix branch diff contains only 3 web auth files.
- Ran `pnpm install --offline` in the clean worktree to install local dependencies.
- Ran `pnpm --filter @innerbloom/web typecheck`; it still fails on existing `origin/main` TypeScript errors unrelated to this change, including `src/auth/runtimeAuth.tsx`, dashboard/demo test types, `replaceAll` lib target issues, avatar profile test fixtures, Clerk localization typing, and mobile premium lab types.
