# Route lapsed staff/employer sessions to their own sign-in doors

## Summary
- Add `signInDoorFor(pathname)` so a signed-out visitor hitting a protected `/employer/*` or `/ops/*` route is redirected to that console's own branded sign-in page instead of the generic `/sign-in`, which carries invite-only "Create an account" copy that doesn't apply to staff/employer users.
- `/app` and everything else still fall back to the generic `/sign-in` door.
- Auth form's "full name" field now shows generic copy ("Full name") instead of "As shown in your passport" for non-traveller audiences.

## Test plan
- [ ] `signInDoorFor` unit tests cover `/employer`, `/ops`, and fallback cases
- [ ] Manually verify a lapsed session on `/employer/*` redirects to `/employer/sign-in`
- [ ] Manually verify a lapsed session on `/ops/*` redirects to `/ops/sign-in`
- [ ] Manually verify `/app/*` still redirects to `/sign-in`

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01D6sviXri3zJ7JFp55bbYeh
