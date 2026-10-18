# Purchases: migrate PlanBillingPeriod to raw Purchase

Related to [SHILL-2256](https://linear.app/a8c/issue/SHILL-2256/remove-the-purchases-assembler-read-the-raw-purchase-object-directly)

## Proposed Changes

Fixes a crash on the classic manage-purchase detail page by finishing the raw-`Purchase` migration for `PlanBillingPeriod`, which the plan-details subtree had been left passing a raw purchase into.

* Migrate `PlanBillingPeriod` (`plan-details/billing-period.tsx`) off the camelCase data-stores `Purchase` onto the raw snake_case `Purchase` from `@automattic/api-core`.
* Read raw fields directly (`product_slug`, `renew_date`, `expiry_date`, `is_locked`, `is_attached_to_holding_site`) and source `isExpiring`/`isRenewingBeforeExpiration`/`isExpiredOrRemoved`/`showCreditCardExpiringWarning` from the local `raw-purchase-helpers` module instead of `calypso/lib/purchases`.
* Add an `isExpiring` port to `raw-purchase-helpers`, which the component needs.
* Update the `billing-period` unit-test fixtures to the raw snake_case shape.

## Why are these changes being made?

Commit #112808 migrated the manage-purchase subtree onto the raw snake_case `Purchase` from `@automattic/api-core`. `plan-details/index.tsx` was migrated and now hands its child `<PlanBillingPeriod>` the raw purchase, but the child was still typed against the camelCase data-stores shape and still called the `calypso/lib/purchases` helpers.

The raw purchase has no nested `payment` object (it uses flat `payment_type`, `payment_card_*` fields), so `isPaidWithCreditCard` read `purchase.payment.type` on an `undefined` value, throwing `TypeError: Cannot read properties of undefined (reading 'type')` and rendering the manage-purchase error boundary ("Sorry, there was an error loading this page"). Rather than re-wrap the purchase in a temporary `createPurchaseObject` bridge, this migrates the component to the raw shape — the end-state SHILL-2256 is driving toward.

## Testing Instructions

TC:
```
yarn test-client client/me/purchases/manage-purchase/plan-details/test/billing-period.jsx
```

Manual testing:
* On Jetpack Cloud staging, open a subscription's manage-purchase page (e.g. `/purchases/subscriptions/<site>/<id>`).
* Confirm the page loads with the "Billing period" section rendered instead of the error boundary, for both a monthly plan (shows "Billed monthly" + "Upgrade to yearly billing") and a yearly plan (shows "Billed yearly").
* Check the browser console — the `Cannot read properties of undefined (reading 'type')` TypeError should be gone.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
