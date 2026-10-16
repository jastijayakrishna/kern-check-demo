# Fix guest post-payment form submission races

## Summary
- allow post-payment guest form links to resolve for guest checkouts by accepting a Stripe payment reference when no logged-in user ID exists
- serialize guest form writes with a row lock inside a transaction so concurrent submissions cannot overwrite each other
- add focused regression tests for payment-reference lookup and the locked append path

## Bug and impact
Recent post-payment form changes introduced two high-severity issues in the guest registration flow:
1. Guest checkouts without a logged-in payer generated form links that could never be verified, so affected guests could not submit required event forms.
2. Two guests submitting their forms at nearly the same time could overwrite each other because both requests read the same JSON payload and wrote back divergent copies, dropping one guest's answers.

## Root cause
- Access verification only supported `userId`, but guest purchases persist `userId = null` and only have a Stripe payment identifier available.
- Form submissions appended to `Payment.formResponses` with a read-modify-write sequence outside a transaction, so concurrent requests had a lost-update race.

## Validation
- `npm test -- lib/actions/payment/postPaymentForm.test.ts`
- `./node_modules/.bin/tsc --noEmit`

<div><a href="https://cursor.com/agents/bc-5bd4edf1-8126-46dc-bd0f-642961c4acea"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/automations/696a4f5a-f9f4-4e65-8dca-8b9225225cff"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/view-automation-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/view-automation-light.png"><img alt="View Automation" width="141" height="28" src="https://cursor.com/assets/images/view-automation-dark.png"></picture></a>&nbsp;</div>
