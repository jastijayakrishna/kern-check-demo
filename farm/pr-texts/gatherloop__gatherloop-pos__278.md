# Add native session management with AsyncStorage token persistence

## Summary
Implements React Native-specific session management that persists authentication tokens to AsyncStorage and attaches them to outgoing requests via an axios interceptor. This addresses the limitation that React Native's networking layer doesn't reliably store httpOnly session cookies (which require HTTPS), so native apps need to carry the JWT bearer token instead.

## Key Changes
- **New native auth token storage layer** (`authToken.native.ts`): Manages JWT token persistence in AsyncStorage with `getStoredAuthToken`, `setStoredAuthToken`, and `clearStoredAuthToken` functions
- **Native auth interceptor** (`registerAuthTokenInterceptor`): Registers an axios request interceptor that automatically attaches the stored bearer token to all outgoing requests, with an unregister function for cleanup
- **Native auth repository** (`auth.native.ts`): Implements `ApiAuthRepository` to persist tokens on login and clear them on logout
- **Web stub implementations** (`authToken.ts`): Provides no-op implementations for web since it uses httpOnly cookies instead
- **App initialization logic** (`App.tsx`): Added session check on cold start to determine initial route (dashboard vs login) and register the auth interceptor before any screens can make requests
- **Test coverage** (`auth.native.spec.ts`): Comprehensive end-to-end tests verifying token persistence, clearing on logout, and interceptor registration
- **Jest configuration updates**: Added transformIgnorePatterns to handle ESM dependencies and mocked AsyncStorage for tests
- **ESLint configuration**: Disabled module boundary enforcement in spec files to allow deep imports of native implementation files

## Notable Implementation Details
- Uses Metro's `.native.ts` resolution to provide platform-specific implementations without conditional imports
- Disables `withCredentials` in the axios config since native apps use bearer tokens instead of cookies
- Handles the race condition on app startup by deferring initial route selection until the stored token is checked
- Includes comprehensive comments explaining why native needs different session handling than web

https://claude.ai/code/session_01B5eCrTswyxLFDBWEZn6L6a
