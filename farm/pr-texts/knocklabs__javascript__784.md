# feat(KNO-10076): Expo + React Native support Devices array

### Description

This PR migrates the React Native SDK's push notification handling from a simple `tokens` string array to a richer `devices` array structure that includes token, locale, and timezone information for each device.

**What changed:**
- Introduced a new `Device` interface with `token` (required), `locale` (optional), and `timezone` (optional) fields
- Updated `KnockPushNotificationProvider` to store channel data as `{ devices: Device[] }` instead of `{ tokens: string[] }`
- Modified `registerPushTokenToChannel` to automatically capture device locale and timezone using `Intl.DateTimeFormat().resolvedOptions()`
- Updated device registration logic to find and update existing devices by token (refreshing locale/timezone) rather than just checking for duplicates

---

**Link to Devin run**: https://app.devin.ai/sessions/497067a8cbeb4d16bf547c182b9e9812  
**Requested by**: andy@knock.app (@andy-knock)

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> Migrate push notifications from a `tokens` array to a `devices` array capturing locale and timezone, updating registration and deregistration logic accordingly.
> 
> - **React Native push module (`KnockPushNotificationProvider.tsx`)**:
>   - Introduce `Device` interface with `token`, optional `locale` and `timezone`.
>   - Replace channel data from `{ tokens: string[] }` to `{ devices: Device[] }` and centralize updates via `setChannelData`.
>   - Update `registerPushTokenToChannel` to upsert devices by `token`, capturing `locale`/`timezone` via `Intl.DateTimeFormat().resolvedOptions()`.
>   - Update `unregisterPushTokenFromChannel` to remove from `devices` by matching `token`; tweak log/error messages.
> - **Breaking**: channel data shape changes from `tokens` to `devices`.
> - **Changeset**: minor version bumps for `@knocklabs/react-native` and `@knocklabs/expo`.
> 
> <sup>Written by [Cursor Bugbot](https://cursor.com/dashboard?tab=bugbot) for commit e2000fe4be102d6bdb38be97ce2ba89438eb206a. This will update automatically on new commits. Configure [here](https://cursor.com/dashboard?tab=bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
