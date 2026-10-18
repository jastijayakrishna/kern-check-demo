# Harden page-level authorization flow

### Motivation
- Make middleware explicitly a lightweight UX guard for login redirects and not the sole authority for authorization.
- Ensure every protected page performs a server-side permission check before loading sensitive data.
- Provide a consistent experience for authenticated users who lack required permissions by redirecting them to an unauthorized page.
- Prevent accidental exposure of sensitive data by moving permission checks to page-level server code.

### Description
- Added explanatory comments to `middleware.ts` clarifying it is a non-authoritative login redirect guard and noting JWT verification is optional if edge secret handling is compatible. 
- Enforced server-side checks by calling `await requirePagePermission(permissions.<...>)` at the top of `app/dashboard/page.tsx`, `app/knowledge-base/page.tsx`, `app/reports/page.tsx`, and `app/services/page.tsx`. 
- Changed `requirePermission()` to redirect to `/unauthorized` for authenticated users who lack permissions, and added a new authenticated `app/unauthorized/page.tsx` that uses `requireUser()` and shows a helpful message with a return action. 
- Added required imports (`requirePagePermission` and `permissions`) to the modified pages so permission checks run before any data-loading helpers. 

### Testing
- Ran type checking with `npm run typecheck` and it succeeded. 
- Ran linting with `npm run lint` and it succeeded. 
- Ran unit tests with `npm test` (Vitest) which completed successfully and reported `1 passed` test file with `6 passed` tests.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a342b0793d88332a582381fc2547535)
