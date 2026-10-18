# Prevent out-of-order Stripe risk events from restoring access

### Motivation

- Stripe webhooks for refunds and disputes can arrive out of order, which may cause a delayed risk event to incorrectly restore a subscription that was suspended by a newer event.
- The intent is to apply risk-driven suspension updates atomically in timestamp order and ensure suspension wins ties when events share the same timestamp.

### Description

- The webhook handler now applies suspension changes via an RPC call to `set_subscription_suspension` instead of performing a direct `update` on `subscriptions` in `app/api/billing/webhook/route.ts`.
- Added a migration `supabase/migrations/202607270003_order_risk_events.sql` that creates `public.set_subscription_suspension(p_customer_id text, p_suspended boolean, p_event_created bigint, p_event_id text)` which updates `subscriptions` only when the incoming event is newer than the recorded `last_event_created`, or when timestamps tie and the incoming event requests suspension (so suspension wins ties).
- The migration includes a function comment and restricts execution of the function to the `service_role` for safety by revoking public access and granting execute to `service_role`.

### Testing

- Ran `npm run typecheck` and it completed successfully.
- Ran `npm run lint` and it completed successfully.
- Ran `npm test` and all tests passed (`28` tests across `7` files).
- Ran `npm run build` and the production build completed successfully.
- Ran `git diff --check` and there were no check errors.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a675ba2b70c8321b1d50e5b9a262113)
