# Domain-only flow: skip site-or-domain for logged-out users too

Part of DOTPROD-122

## Proposed Changes

* Makes the domain-only checkout simplification skip the "Choose how to use your domain" (`site-or-domain`) step for **logged-out** users too, not only logged-in users.
* In the `domain-only` step's `onContinue`, after auto-submitting `site-or-domain`, `site-picker`, and `plans-site-selected`, navigate from the last auto-submitted step in a login-aware way (via `getNextStepName`) instead of relying on `goToNextStep()`.
* Widens the `goToStep` prop type to accept a target step name.
* Tests: the logged-out case now asserts navigation to the account step; adds a logged-in case asserting it proceeds to checkout.

❌ User should not see the `site-or-domain` step (check the testing instructions)
<img width="1840" height="1140" alt="Screenshot 2026-07-22 at 20 26 11" src="https://github.com/user-attachments/assets/3b13b38f-c17c-4c5d-b810-48c045721e74" />

## Why are these changes being made?

The `calypso_signup_domain_only_checkout_simplification_v1` treatment (shipped as the default in #112218) only skipped `site-or-domain` for logged-in users. For logged-out users, the still-pending account step left the flow "not every step submitted", so the framework's `goToNextStep()` advanced by array index from `domain-only` straight back onto the just-skipped `site-or-domain` step. This makes the skip behave consistently across both auth states.

## Testing Instructions

Use the **Calypso Live** link from the auto-generated comment on this PR (the build tag changes as new commits are pushed). The direct link for the current build is:
[`https://calypso.live/start/domain/domain-only?image=registry.a8c.com/calypso/app:build-189712`](https://calypso.live/start/domain/domain-only?image=registry.a8c.com/calypso/app:build-189712)

**Logged out**

1. Make sure you are logged out.
2. Go to `/start/domain/domain-only`.
3. Add a domain to the cart and press continue.
4. Check that the next step is the sign-up (account creation) step, not "Choose how to use your domain".
5. After logging in / creating the account, check that the next step is checkout.

**Logged in**

1. While logged in, add a domain to the cart and press continue.
2. Check that the next step is checkout.

You can also run the unit tests: `yarn test-client client/signup/steps/domains`.

## Pre-merge Checklist

- [ ] Has the general commit checklist been followed? (PCYsg-hS-p2)
- [x] [Have you written new tests](https://github.com/Automattic/wp-calypso/blob/trunk/docs/testing/index.md) for your changes?
- [ ] Have you tested the feature in Simple (P9HQHe-k8-p2), Atomic (P9HQHe-jW-p2), and self-hosted Jetpack sites (PCYsg-g6b-p2)?
- [ ] Have you checked for TypeScript, React or other console errors?
- [ ] For UI changes, have you tested the affected components in [dark mode](https://github.com/Automattic/wp-calypso/blob/trunk/docs/dark-mode.md)?
- [ ] Have you tested accessibility for your changes? Ensure the feature remains usable with various user agents (e.g., browsers), interfaces (e.g., keyboard navigation), and assistive technologies (e.g., screen readers) (PCYsg-S3g-p2).
- [ ] Have you used memoizing on expensive computations?
- [ ] Have we added the "[Status] String Freeze" label as soon as any new strings were ready for translation (p4TIVU-5Jq-p2)?
- [ ] For changes affecting Jetpack: Have we added the "[Status] Needs Privacy Updates" label if this pull request changes what data or activity we track or use (p4TIVU-aUh-p2)?

🤖 Generated with [Claude Code](https://claude.com/claude-code)

