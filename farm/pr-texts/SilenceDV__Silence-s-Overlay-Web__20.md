# Fix project ID generation for Supabase UUID columns

## Root cause

`defaultProject()` used the generic prefixed identifier helper:

`createId("project") -> project_<uuid>`

The project creation API then inserted that value directly into `projects.id`, whose Supabase/Postgres type is native `uuid`. Postgres correctly rejected it with `invalid input syntax for type uuid`.

## Fix

- generate project IDs with plain `crypto.randomUUID()`
- retain prefixed IDs only for non-database layer/slide identifiers
- centralize strict project-ID normalization
- accept an exact legacy `project_<uuid>` value by safely stripping the prefix and validating the UUID
- normalize project IDs at create, load, update/autosave, rename, duplicate, delete, editor URL, publish, and legacy-adapter boundaries
- ensure duplicated projects receive new native UUIDs
- keep Supabase columns as `uuid`

Before: `project_d9282c82-2569-4136-b255-d88e938b94c8`

After: `d9282c82-2569-4136-b255-d88e938b94c8`

## Regression coverage

- new project IDs match a UUID pattern and never start with `project_`
- duplicated project IDs are new valid UUIDs
- exact legacy prefixed IDs normalize safely
- malformed/arbitrarily-prefixed IDs are rejected
- imported/current projects normalize safely
- legacy compatibility projections normalize safely
- publish validation accepts the normalized UUID

## Validation

- typecheck passed
- ESLint passed
- Vitest: 9 files, 41 tests passed
- production Next.js build passed
- `git diff --check` passed
- static search found no remaining `createId("project")` or `project_${crypto.randomUUID()}` producer

## Production verification limitation

The exact authenticated Vercel → real Supabase flow was not reproducible from this environment because production credentials/session access were unavailable. The fix targets the exact rejected insert boundary and preserves the database UUID type, but this PR should be deployed to preview/production and verified with Create Project → Open → autosave → publish before claiming production acceptance.

Do not merge automatically.
