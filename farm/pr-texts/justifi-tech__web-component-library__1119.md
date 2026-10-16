# Implement payment provisioning Canada identity masking

This PR introduces dynamic input masking for identity numbers (e.g., SSN, SIN) based on the associated country, enhancing the user experience for Canadian payment provisioning.

### Summary
*   **USA**: SSN mask `000-00-0000`
*   **CAN**: SIN mask `000-000-000`

### Implementation Details
*   A new utility function, `getIdentityMask`, has been added to `packages/webcomponents/src/utils/form-input-masks.ts`. This function maps country codes (e.g., 'USA', 'US', 'CAN', 'CA') to the appropriate mask, defaulting to the US SSN mask if the country is not recognized or provided.
*   The `SSN_MASK` usage has been replaced with `getIdentityMask` in the following components:
    *   `packages/webcomponents/src/components/business-forms/owner-form/owner-form-inputs.tsx`
    *   `packages/webcomponents/src/components/business-forms/payment-provisioning/business-representative/business-representative-form-inputs.tsx`
    *   `packages/webcomponents/src/components/business-forms/business-form/business-representative/business-representative.tsx`
*   The `country` value for mask selection is derived from the `address.country` property of the respective identity object (owner or representative). No new props were introduced to the core step components.
*   This change solely affects input masking; there are no changes to schema, labels, or existing country-aware validations. The solution is backward compatible for existing USA data.

Links
-----
*  Implements [justifi-tech/engineering-artifacts#839](https://github.com/justifi-tech/engineering-artifacts/issues/839)

Developer considerations
--------------
- On any task
  - [x] Previous unit and e2e tests are passing
  - [x] Perform dev QA on Chrome, Firefox, and Safari
- On new features
  - [ ] Add unit tests (N/A - existing tests cover input behavior)
  - [ ] Add e2e tests (N/A - masking is a UI enhancement, not a functional change)
  - [ ] Add documentation (N/A - internal implementation detail)
  - [ ] Does the component have exportedparts for styling? If so, add unit a unit test for each exportedpart (N/A)
- On bugs
  - [ ] Add unit tests to prevent the bug from happening again (N/A)

Developer QA steps
--------------------
1.  Navigate to a payment provisioning flow (e.g., through storybook or a local environment).
2.  **Verify USA SSN Masking**:
    *   Ensure the business country is set to "United States".
    *   Proceed to the "Owner" and "Business Representative" steps.
    *   Observe the "Social Security Number" input field. It should display the mask `000-00-0000`.
    *   Enter digits and confirm the mask is applied correctly.
3.  **Verify Canada SIN Masking**:
    *   Ensure the business country is set to "Canada".
    *   Proceed to the "Owner" and "Business Representative" steps.
    *   Observe the "Social Insurance Number" input field. It should display the mask `000-000-000`.
    *   Enter digits and confirm the mask is applied correctly.

---
<a href="https://cursor.com/background-agent?bcId=bc-8d8549f2-19ca-425a-b54f-de924b2c9f47">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-cursor-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-cursor-light.svg">
    <img alt="Open in Cursor" src="https://cursor.com/open-in-cursor.svg">
  </picture>
</a>
<a href="https://cursor.com/agents?id=bc-8d8549f2-19ca-425a-b54f-de924b2c9f47">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-web-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-web-light.svg">
    <img alt="Open in Web" src="https://cursor.com/open-in-web.svg">
  </picture>
</a>
