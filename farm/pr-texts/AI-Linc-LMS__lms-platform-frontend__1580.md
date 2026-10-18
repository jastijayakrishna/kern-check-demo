# perf(auth): one user-profile request per boot, not two

From the perf RCA. A confirmed cost on **every authenticated page load**, which is the "navigation feels slow" complaint rather than a login-page one.

## The duplication

`AuthProvider` (`lib/auth/auth-context.tsx:158`) and `ProfileGateProvider` (`lib/contexts/ProfileGateContext.tsx:65`) are both mounted in the root layout. Each fetches the user profile through a different service:

```ts
// accounts.service.ts:202   AND   profile.service.ts:181
`/accounts/clients/${config.clientId}/user-profile/`
```

Identical URL, neither aware of the other. At the measured backend latency of **120–340 ms**, that's ~250 ms added to every hard navigation, on every route, for a byte-identical second copy.

## Two things this had to get right

**Callers get their own shallow copy.** `auth-context` does `userProfile.role = roleFromCookie` when the API omits a role. Handing both callers the same object would leak that write into ProfileGate's copy — and *only* for users whose profile has no role, which is the exact case that code path exists for. A test fails if the copy is removed:

```
× a caller mutating its copy cannot corrupt the other's
```

**The fetcher is generic.** The two services each declare their own `UserProfile` for this one endpoint and the shapes differ (accounts' carries `id`/`user_name`/`phone`). Picking either would force a cast on the other caller, so each states the shape it expects — exactly as it did when it made the request itself.

## Scope

5-second window, deliberately **not** a data cache. It collapses the concurrent boot fan-out; a later navigation re-fetches, so nothing goes stale in the UI. A failed request is not cached and does not wedge the next caller — also tested.

## Verification

- 5 tests, revert-proofed (removing the copy guard fails the mutation test).
- `npx vitest run` — **863 passed** (61 files, 30s).
- `npx tsc --noEmit` — clean apart from the two pre-existing `tutorAutoContinue.test.ts` errors.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
