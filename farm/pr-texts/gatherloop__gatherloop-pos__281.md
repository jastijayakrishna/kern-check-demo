# Add error state handling to auth logout usecase

## Summary
Updated the auth logout flow to properly handle and persist error states instead of auto-recovering to idle. This allows users to retry logout operations when they fail.

## Key Changes
- Added `error` state to `AuthLogoutState` type union
- Modified state transition logic to allow `LOGOUT` action from both `idle` and `error` states
- Changed error recovery behavior: `LOGOUT_ERROR` now transitions to `error` state instead of `idle`
- Added error state handling in `AuthLogoutController` to display error toast message
- Updated test expectations to verify error state persistence and retry capability

## Implementation Details
- The usecase now maintains an explicit error state, giving users visibility into logout failures
- Users can retry logout from the error state without manual intervention
- Error toast notification is displayed when logout fails, improving user feedback
- State machine now supports the flow: `idle → loading → error → loading → loaded` for retry scenarios

https://claude.ai/code/session_0124mMP8QLqRQboQf7pVjkrL
