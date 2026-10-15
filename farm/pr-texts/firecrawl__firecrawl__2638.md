# Add debug logging for 402 credit check failures

## Summary

Adds comprehensive debug logging to help diagnose 402 errors where the system incorrectly thinks users don't have enough credits.

**Changes:**
**`credit_billing.ts`**: Added detailed logging when credit check fails, capturing all ACUC fields and computed values (price_credits, coupon_credits, total_credits_sum, adjusted_credits_used, remaining_credits, etc.) plus the derived values used in the comparison (creditsWillBeUsed, totalPriceCredits)

## Review & Testing Checklist for Human

- [ ] Verify no sensitive data is being logged (API keys, tokens, user content, URLs) - I removed `req.body` but please double-check the logged fields
- [ ] Confirm the logged fields will actually help diagnose the 402 issue - may want to cross-reference with what data you need to debug the specific case
- [ ] Test by triggering a 402 error and verifying the log output contains the expected fields

**Test plan:** Deploy to staging, trigger a credit check failure (e.g., with a team that has low/no credits), and verify the logs contain all the expected debugging information.

### Notes

- Link to Devin run: https://app.devin.ai/sessions/144689b51c8844a59bd8d77e63a1371d
- Requested by: Micah Stairs (@micahstairs)

<!-- This is an auto-generated description by cubic. -->
---
## Summary by cubic
Added debug logging to credit checks to diagnose 402 “insufficient credits” errors. Captures key fields and computed values used to compare credits used vs allowed.

- **New Features**
  - Log key values on failure (teamId, creditsRequested, price_credits, coupon_credits, total_credits_sum, adjusted_credits_used, remaining_credits, computed_creditsWillBeUsed, computed_totalPriceCredits, creditUsagePercentage, isAutoRechargeEnabled, autoRechargeThreshold).

<sup>Written for commit 3554c28a80628f6a2b2d355f59e39b5b4701c99c. Summary will update on new commits.</sup>

<!-- End of auto-generated description by cubic. -->
