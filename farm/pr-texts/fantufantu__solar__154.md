# Enforce authorization and ownership checks across resolvers and services

### Motivation
- Standardize and tighten access control by replacing ad-hoc JWT guard usage with resource/action-based authorization and explicit ownership checks.
- Prevent unauthorized modifications and views of user-owned resources by validating the `createdById` against the acting user.
- Simplify resolver guards and centralize permission enforcement to support finer-grained authorization checks.

### Description
- Replaced many `@UseGuards(JwtAuthGuard)` usages with the `@Authorization` decorator and `AUTHORIZATION_ACTION_CODE` on multiple resolvers (earth, jupiter, mars, mercury, venus) to require resource/action authorizations.
- Added `assertOwnership` helper methods and calls in `ArticleService`, `ResumeService`, and `BillingService` to validate resource ownership and throw `BadRequestException` or `ForbiddenException` when appropriate.
- Updated resolver and service method signatures and call sites to pass the current user id where needed (e.g. billing update/limitation methods) and adjusted sharing deletion logic to require ownership for certain operations.
- Cleaned up unused imports and removed an obsolete mutation (`upgradeMembership`) from `UserResolver` and minor formatting tweaks across files.

### Testing
- Ran the existing automated test suite (unit and integration tests) against the modified modules, and the tests completed successfully.
- Verified that the GraphQL resolvers compile and the updated service methods pass type checks and basic request flows in local test runs.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a84537d6bdc832797c97f0fc6fb6213)
