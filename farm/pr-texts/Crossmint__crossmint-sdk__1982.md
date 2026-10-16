# fix(react-native-ui): keep signer OTP actions above the keyboard

## Description

The React Native signer OTP dialogs render a fixed, vertically-centered modal (`justifyContent: "center"`, `maxHeight: "80%"`) with no keyboard handling. When the OTP keyboard opens on mobile, it overlaps the bottom of the modal and hides the **Submit** and **Re-send code** controls — leaving users unable to complete OTP, with no visible cue to dismiss the keyboard. Reported via a customer support ticket with repros on both iOS and Android.

Since the numeric one-time-code keyboard has no submit affordance, the hidden buttons are a hard block on the flow. The only customization surface (`appearance`/`UIConfig`) exposes colors/spacing/fonts but nothing to control layout, so integrators can't work around it without building a fully custom signer UI.

Fix, applied once in the shared path so both dialogs benefit:
- Wrap the modal overlay in a `KeyboardAvoidingView` (`behavior="padding"` on iOS, `"height"` on Android) in both `PhoneSignersDialog` and `EmailSignersDialog`, so the modal shifts up when the keyboard appears.
- Make the shared `BaseCodeInput` content a `ScrollView` (`keyboardShouldPersistTaps="handled"`) so the input and actions stay reachable on smaller screens.

Affected files:
- `packages/client/ui/react-native/src/components/signers/PhoneSignersDialog.tsx`
- `packages/client/ui/react-native/src/components/signers/EmailSignersDialog.tsx`
- `packages/client/ui/react-native/src/components/signers/BaseCodeInput.tsx`

## Test plan

- `pnpm --filter @crossmint/client-sdk-react-native-ui... build` — passes (type-checks the changes).
- `biome check` on the three changed files — clean.
- Manual verification recommended on a physical device / simulator: open the phone and email signer OTP prompts, confirm that with the keyboard open the OTP input, Submit, and Re-send controls all remain visible and tappable on both iOS and Android. Layout/behavior is unchanged when the keyboard is closed.

## Package updates

- `@crossmint/client-sdk-react-native-ui` — patch. Changeset added at `.changeset/otp-keyboard-avoidance.md`.


Link to Devin session: https://crossmint.devinenterprise.com/sessions/32f1fce091994095838a55cd48a116d2
Requested by: @jorge2393
