# feat(families): send and manage family invites UI (NEU-349)

## Summary
- Adds a `FamilyDetail` page where family admins can send invites (by email) and revoke pending ones
- Adds the `families` API client with full CRUD + invite management endpoints
- Extends `AuthContext` to carry `family_role` so admin-only controls render correctly
- Updates `Register` to accept a `family_invite_token` query param and auto-login after registration
- Adds per-invite optimistic pending state and removes a dead back-link

## Changes
- `src/api/families.ts` — new API client (list families, get family, send/revoke invites, update/delete family)
- `src/api/families.test.ts` — 209-line test suite for all API calls
- `src/pages/FamilyDetail.tsx` — family detail page with invite form and pending/active member lists
- `src/pages/FamilyDetail.test.tsx` — 241-line test suite covering admin and non-admin views, invite flow, and revoke flow
- `src/contexts/AuthContext.tsx` / `AuthContext.test.tsx` — expose `family_role` from decoded JWT
- `src/pages/Register.tsx` / `Register.test.tsx` — handle `family_invite_token` param, auto-login
- `src/types/index.ts` — add `Family`, `FamilyMember`, `FamilyInvite` types
- `src/routes.tsx` — add `/families/:id` route

## Test plan
- [ ] `task test` passes (all existing + new tests green)
- [ ] Family admin can navigate to `/families/:id` and see the invite form
- [ ] Sending an invite posts to the API and shows the new invite in the pending list
- [ ] Revoking an invite shows per-invite pending state, then removes the row on success
- [ ] Non-admin member sees the family page without the invite form
- [ ] Registering via a family invite link auto-logs in and redirects to dashboard

🤖 Generated with [Claude Code](https://claude.com/claude-code)
