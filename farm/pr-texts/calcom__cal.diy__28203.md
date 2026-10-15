# fix: add phone mask overrides for Argentina and Finland to prevent digit truncation

## What does this PR do?

Adds custom phone mask overrides for **Argentina** and **Finland** in the booking form phone input, fixing cases where `react-phone-input-2`'s built-in masks are too short and truncate valid phone numbers.

- **Argentina (+54):** Built-in mask allows 10 national digits, but all Argentine mobile numbers require **11 digits** (the `9` prefix + area code + subscriber). Users could not enter their full mobile number.
- **Finland (+358):** Built-in mask allows 9 national digits, but some valid Finnish mobile numbers have **10 digits**. Users with these numbers were truncated.

Also extracts `CUSTOM_PHONE_MASKS` into a shared `phone-masks.ts` module (with JSDoc comments on each entry) so the component and tests import from a single source of truth.

Related issues: #15931, #23628, #22992, #26459

### How this was identified

A systematic cross-reference of `react-phone-input-2`'s built-in masks against `libphonenumber-js/max` validation was performed across all 54 countries with masks. Argentina and Finland were the only two where standard mobile numbers exceed the mask's digit limit.

### Updates since last revision

- Extracted `CUSTOM_PHONE_MASKS` into a shared `phone-masks.ts` module so both `PhoneInput.tsx` and the test file import from the same source of truth (no more duplication) — addresses review feedback from @cubic-dev-ai
- Fixed non-null assertion lint warning in the test file (`parsed!` → `parsed?.nationalNumber.length ?? 0`)
- Fixed TypeScript error: `toBeGreaterThanOrEqual` only accepts 1 argument, moved custom error message to `expect()` second parameter

## Mandatory Tasks (DO NOT REMOVE)

- [x] I have self-reviewed the code (A decent size PR without self-review might be rejected).
- [x] N/A — No developer docs update required for this fix.
- [x] I confirm automated tests are in place that prove my fix is effective or that my feature works.

## How should this be tested?

1. Run unit tests: `TZ=UTC yarn vitest run apps/web/components/phone-input/PhoneInput.test.ts`
2. Manual UI test:
   - Open any Cal.com booking page with a phone number field
   - Select **Argentina (+54)** → enter a mobile number like `9 11 1234 5678` (11 digits) → verify all digits are accepted
   - Select **Finland (+358)** → enter a 10-digit mobile number like `40 1234 5678` → verify all digits are accepted
3. Verify existing overrides still work (Ivory Coast, Benin, Austria)

## Human Review Checklist

- [ ] Verify `react-phone-input-2` correctly handles the **parentheses** in Argentina's mask format `(..) .........` — this is atypical and was not tested in a browser
- [ ] Verify Finland mask `.. ... .. ...` (10 digits) spacing looks sensible in the UI and doesn't break shorter 9-digit numbers
- [ ] Confirm the new `phone-masks.ts` module is picked up correctly by the build (new file added to `apps/web/components/phone-input/`)

## Checklist

- [x] I have read the [contributing guide](https://github.com/calcom/cal.com/blob/main/CONTRIBUTING.md)
- [x] My code follows the style guidelines of this project
- [x] I have commented my code, particularly in hard-to-understand areas
- [x] My changes generate no new warnings

---

Link to Devin run: https://app.devin.ai/sessions/9237ad31251745838ebff70e785900df
Original Devin run: https://app.devin.ai/sessions/f8bc68b8f6ca43c797a18708da373d27
Requested by: bot_apk (apk@cognition.ai)
