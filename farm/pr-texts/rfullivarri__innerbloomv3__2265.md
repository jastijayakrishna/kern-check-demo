# Fix iOS Google sign-up return to onboarding

## Root cause
`Crear cuenta` started Google OAuth through Clerk's `SignUp` resource. When the selected Google identity already existed, Clerk transitioned internally to sign-in and did not complete the native handoff consistently. The browser therefore remained on the web flow instead of invoking the app callback.

## Change
- Keep the native transaction as `mode=sign-up` with `redirect_path=/intro-journey2`.
- Start Google OAuth through Clerk's `SignIn` resource for the mobile auth page, matching the working native login path.
- Keep the visible label and native callback intent as **Crear cuenta**. Clerk social OAuth creates a user when no account exists and signs in when it does.

Expected result: after Google, the browser opens `innerbloom://localhost/callback`, closes, and `NativeMobileBridge` sends the app to `/intro-journey2`.

## Validation
- `pnpm --filter web build` passed.
- No iOS/Xcode, Android, dependency, or web-login changes.
