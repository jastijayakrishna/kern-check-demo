# Replace TS enums with const-style enum objects and update usages

### Motivation
- Standardize enum usage across the codebase to the new `as const` object + `ValueOf` pattern and ensure GraphQL/TypeORM runtime enum values use constant objects and centralized tokens.
- Make enum string values stable and lowercase by default to match external interfaces and validation expectations.

### Description
- Replaced multiple TypeScript `enum` declarations with `as const` objects and exported `ValueOf`-based types for `authorization`, `sharing`, `billing`, `direction`, `limit-duration`, and `district` related enums (e.g. `AUTHORIZATION_ACTION_CODE`, `AUTHORIZATION_RESOURCE_CODE`, `TARGET_TYPE`, `DIRECTION`, `LIMIT_DURATION`, `DISTRICT_SYNC_ACTION`).
- Updated `registerEnumType` calls to reference `GRAPHQL_ENUM_TOKEN` entries and changed `@Field`, TypeORM `enum` options, and `@IsEnum` usages to use the constant objects instead of `enum` types.
- Propagated import/usage changes across apps and libs (resolver/service/loader updates in `mercury`, `venus`, `jupiter`, `mars`, and libs under `libs/database`) to use the new constant names and values.
- Added/updated tests and constants mapping: added assertions for district sync action casing and invalid action rejection in `sync-districts.input.spec.ts`, and added `constants/` mapping to `package.json` `moduleNameMapper`.

### Testing
- Ran unit tests with `yarn test`, and the test suite (including the updated `SyncDistrictsInput` specs) passed.
- Performed a TypeScript type-check with `tsc --noEmit`, which completed successfully.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a7fdf2e4abc8327b4213ea845a89a91)
