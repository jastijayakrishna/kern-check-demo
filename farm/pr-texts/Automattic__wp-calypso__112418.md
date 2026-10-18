# Checkout: fix unbalanced mobile header icons (CHE-494)

Part of CHE-494

## Proposed Changes

Makes the checkout masterbar reuse the shared **StepContainerV2 `Step.TopBar`** as its header, so the checkout header is the same component everywhere instead of a bespoke masterbar layout.

- `client/layout/masterbar/checkout.tsx` — renders `Step.TopBar` with `Step.BackButton` (left) and, on the right, an **optional** `Step.StepCounter` plus the help link (`Step.LinkButton`). The back button, help link and logo are now literally the same components used by the stepper flows.
- The **step counter** ("N of N") is optional: it appears only when the redirecting flow passes `steps_current` / `steps_total` query params, and only on mobile — matching the onboarding checkout. A direct checkout (no params) shows no stepper.
- `client/layout/masterbar/style.scss` — defines the `--step-container-v2-top-bar-padding` / `--step-container-v2-top-bar-content-height` custom properties on the masterbar. `Step.TopBar` reads these for its spacing; they are normally provided by the `.step-container-v2` root, which isn't an ancestor of the masterbar. Removes the old bespoke header styles (divider, custom back/need-help buttons).

The original scope (CHE-494) was the mobile header looking unbalanced and inconsistent; reusing `Step.TopBar` addresses that at the root by unifying on one header component.

### Before / After

<img width="953" height="964" alt="Screenshot 2026-07-08 at 17 24 38" src="https://github.com/user-attachments/assets/bd22a6b2-c90a-4c5d-ab87-95ca54337346" />



### Follow-up (not in this PR)

Having the onboarding/StepContainerV2 checkout use this masterbar too (dropping its hidden-masterbar + in-content `Step.TopBar`) so it is genuinely one header everywhere. Deferred until the reused masterbar header is validated.

## Why are these changes being made?

The checkout mobile header had inconsistent, unbalanced icons because it was a bespoke masterbar layout separate from the `Step.TopBar` used by the stepper flows. Reusing the same component removes the divergence and keeps the header consistent, with the step indicator as an optional element.

## Testing Instructions

- Open a direct checkout on mobile, e.g. `/checkout/<site>/personal-bundle`. The header should show the WordPress logo, a Back button, and the "Need help?" link — matching the onboarding checkout's top bar — with **no** step indicator.
- Open a checkout that passes `steps_current` / `steps_total` (e.g. the onboarding flow) on mobile and confirm the "N of N" step indicator appears in the header.
- Confirm spacing/padding matches the `Step.TopBar` used inside the stepper flows (no collapsed padding).
- Verify RTL renders the header correctly.

## Pre-merge Checklist

- [ ] Has the general commit checklist been followed? (PCYsg-hS-p2)
- [ ] [Have you written new tests](https://github.com/Automattic/wp-calypso/blob/trunk/docs/testing/index.md) for your changes?
- [ ] Have you tested the feature in Simple (P9HQHe-k8-p2), Atomic (P9HQHe-jW-p2), and self-hosted Jetpack sites (PCYsg-g6b-p2)?
- [x] Have you checked for TypeScript, React or other console errors?
- [ ] For UI changes, have you tested the affected components in [dark mode](https://github.com/Automattic/wp-calypso/blob/trunk/docs/dark-mode.md)?
- [ ] Have you tested accessibility for your changes? Ensure the feature remains usable with various user agents (e.g., browsers), interfaces (e.g., keyboard navigation), and assistive technologies (e.g., screen readers) (PCYsg-S3g-p2).
- [ ] Have you used memoizing on expensive computations?
- [ ] Have we added the "[Status] String Freeze" label as soon as any new strings were ready for translation (p4TIVU-5Jq-p2)?
    - [ ] For UI changes, have we tested the change in various languages (for example, ES, PT, FR, or DE)?
- [ ] For changes affecting Jetpack: Have we added the "[Status] Needs Privacy Updates" label if this pull request changes what data or activity we track or use (p4TIVU-aUh
