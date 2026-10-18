# refactor(enums): align enum object keys with their string values

### Motivation

- Simplify backend enum definitions so each enum object's keys are identical to their persisted/API string values to reduce cognitive load and prevent mismatches. 
- Make enum access consistent across services (GraphQL, TypeORM, and service call sites) for resources like authorization actions, district levels, share targets, billing durations, directions, and COS bucket names. 

### Description

- Converted multiple `as const` enum objects to use lowercase/string-identical keys (for example `DISTRICT_LEVEL`, `DISTRICT_SYNC_ACTION`, `AUTHORIZATION_ACTION_CODE`, `AUTHORIZATION_RESOURCE_CODE`, `TARGET_TYPE`, `DIRECTION`, `LIMIT_DURATION`, `BUCKET_NAME`).
- Updated all affected call sites, resolvers, services and tests to reference the new enum keys (e.g. `DISTRICT_SYNC_ACTION.create` instead of `DISTRICT_SYNC_ACTION.CREATE`).
- Adjusted COS bucket enum to include the hyphenated name as a string key and updated its usages (access `BUCKET_NAME['cabin-cab']`).
- Kept `registerEnumType(...)` and GraphQL/type exports intact so runtime enum registration and TypeScript `ValueOf<>` types remain functional.

### Testing

- Ran `pnpm exec jest --runInBand` and all test suites passed (`3` suites, `12` tests). 
- Ran `git diff --check` which produced no new errors from these changes. 
- Ran `pnpm exec prettier --check $(git diff --name-only -- '*.ts')` which reported a formatting warning in an existing file (`apps/mars/src/resume/resume.service.ts`).
- Ran `pnpm exec eslint .` and `pnpm exec tsc --noEmit` which are blocked by repository configuration / pre-existing type issues (ESLint flat config missing and several strict property-initialization/DataLoader readonly typing errors) and are not caused by the enum key changes.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a806975f7b8832791cd2e7c95a66db1)
