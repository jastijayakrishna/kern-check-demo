# feat(mobile): Integrate RevenueCat for in-app purchases

# Use Convex User ID for RevenueCat and Integrate Real Paywall

## Summary
This PR completes the RevenueCat integration by:
- **Using Convex user IDs as RevenueCat app user IDs** instead of Clerk IDs (per user request)
- **Replacing the fake paywall UI** with real RevenueCat offerings from the dashboard
- **Adding automatic user linking** in the webhook handler when purchases are made
- **Implementing actual purchase flow** that updates subscription tiers in the database

The mobile app now shows real subscription offerings from RevenueCat, handles purchases through the RevenueCat SDK, and the backend webhook syncs subscription status to update user tiers and usage limits.

## Review & Testing Checklist for Human

**⚠️ CRITICAL - END-TO-END TESTING REQUIRED:**

This PR has NOT been tested with real purchases. The following must be verified before merging:

- [ ] **Purchase flow works end-to-end (BLOCKER)**:
  1. Open app and trigger paywall (Settings → Manage Subscription or when hitting usage limit)
  2. Select a subscription plan
  3. Complete purchase in sandbox mode
  4. Verify webhook is called and logged in backend
  5. Verify user's subscription tier is updated in Convex database
  6. Verify usage limits reflect new tier

- [ ] **Webhook event structure matches reality**: Check backend logs when test purchase is made to ensure the event structure matches what the handler expects (`event.event.app_user_id`, `event.event.product_id`, etc.)

- [ ] **Product IDs match**: Verify these product IDs in `packages/backend/convex/revenueCatBilling.ts` exactly match what's in your RevenueCat dashboard:
  - `eveokee_premium_weekly` → weekly tier
  - `eveokee_premium_monthly` → monthly tier  
  - `eveokee_premium_annual` → yearly tier

- [ ] **User linking works correctly**: The webhook handler assumes the RevenueCat app_user_id IS the Convex user ID. Verify this works by checking backend logs during first purchase.

- [ ] **Restore purchases works**: Test the "Restore Purchases" button in the paywall to ensure it correctly restores previous subscriptions.

### Notes
- User confirmed webhook is set up in RevenueCat dashboard for sandbox mode ✅
- The paywall now loads real offerings from RevenueCat instead of hardcoded fake plans
- User IDs are now Convex database IDs (not Clerk IDs) as requested
- The backend automatically links users on first purchase if not already linked

**Link to Devin run**: https://app.devin.ai/sessions/df9303def714401a9fd28c7cce286bb8  
**Requested by**: Sam He (sam@eveoky.com) / @NanHeSam

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Mobile app adds RevenueCat-based in-app purchases and subscription sync (webhook support).

* **Improvements**
  * Paywall now uses RevenueCat UI for purchase flow; theming validated with a new test component.
  * Free tier increased to 10 generations per 30-day period; alpha and weekly tiers removed.
  * Diary music generation now surfaces clear usage codes to trigger paywall/alerts.

* **Documentation**
  * Added a comprehensive RevenueCat billing & integration guide.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
