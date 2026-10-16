# refactor(dunning): migrate request overdue payment form to TanStack Form

## Context

Part of the Formik → TanStack Form migration ([LAGO-1148](https://linear.app/getlago/issue/LAGO-1148/initiative-form-migration-strategy)). The customer "request overdue payment" page was still on Formik + yup, and its `no-restricted-imports` lint warnings are two of the remaining ones.

This page was picked because it is one of the smallest and most isolated forms left: two fields (`emails`, `paymentMethod`), one sub-component, no drawer/dialog machinery, and no shared form state with anything else.

## Description

**`validationSchema.ts` (new)** — holds the zod schema, the inferred `CustomerRequestOverduePaymentForm` type (previously hand-written in `RequestPaymentForm.tsx`) and the default values.

Validation parity with the previous yup schema:

| Field | Before (yup) | After (zod) |
| --- | --- | --- |
| `emails` | `.required('')` | `.min(1, 'text_620bc4d4269a55014d493f3d')` — yup's empty message could never render, and Zod v4 substitutes a raw "Invalid input" for `message: ''`, so the existing "Email is required" key is used |
| `emails` | `.emails('text_66b258f62100490d0eb5ca8b')` | `.refine(isMultipleEmailsValid, 'text_66b258f62100490d0eb5ca8b')` — same semantics, same message key, and it still short-circuits on an empty value so the field never shows two messages at once |
| `paymentMethod` | not validated | `z.object` mirroring `PaymentMethodReferenceInput`, both members optional |

**`zodCustoms.ts`** — the comma-separated email check is extracted out of `zodMultipleEmails` as `isMultipleEmailsValid`, so this schema reuses the shared implementation instead of duplicating the split-and-regex logic. `zodMultipleEmails` itself is unchanged for its existing callers; this field only differs in its message, whose copy is written for a list of recipients rather than a single address.

**`RequestPaymentForm.tsx`** — becomes a `withForm` section instead of taking a `formikProps` prop, so the form is handed down through the mechanism already used everywhere else in the app. `TextInputField` becomes `form.AppField` + `field.TextInputField` (keeping `beforeChangeFormatter={['lowercase']}`), and the manually-driven `PaymentMethodComboBox` is bound to a `form.AppField name="paymentMethod"` calling `field.handleChange(value)`, so its whole-object value stays in form state exactly as before.

**`index.tsx`** — `useFormik` → `useAppForm` with `revalidateLogic()`. The page body is wrapped in a real `<form>`, which also brings the native browser behaviours the Formik version lacked: pressing Enter in the recipient input now submits. No extra classes were needed on the wrapper — the header is `sticky`, `main` carries its own viewport heights and the footer is `fixed`, none of which the added block node disturbs. The footer button becomes `form.SubmitButton`, keeping the genuinely external `!hasDunningIntegration || totalAmount === 0` gate and dropping the `!isValid` gate that `canSubmit` now owns. `onSubmitInvalid` wires `scrollToFirstInputError`. `enableReinitialize` is replaced by a `form.reset` effect on the customer email, which lands after the query resolves.

### Behaviour change to know about

Formik used `validateOnMount`, so an invalid form disabled the submit button immediately and never showed the "required" message. With `revalidateLogic()` the button stays enabled and the error surfaces on the first submit attempt, then live — same rules, different moment. This is the convention across every migrated form.

## Tests

- `__tests__/validationSchema.test.ts` — single/multiple emails, the required message on an empty value (asserting a single issue), and the invalid-emails message including a trailing separator
- `components/__tests__/RequestPaymentForm.test.tsx` — lowercasing on submit, Enter-to-submit, payment-method select-then-submit (the BIL-410 shape-mismatch guard), and both error messages blocking submit
- the existing `__tests__/index.test.tsx` passes unchanged, minus its now-unused `initializeYup()` call

`pnpm code:style` and `pnpm test` are green.

<!-- Linear link -->
Fixes LAGO-1172

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01AdirPHN4tyNn5CYuHYNuhf
