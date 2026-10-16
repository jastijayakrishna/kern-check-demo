# Add testcontainer-based database support and integration tests

# Add testcontainer-based database support and integration tests

## Summary

This PR adds infrastructure for running integration tests with a real PostgreSQL database using Testcontainers. The setup spins up a PostgreSQL container, runs Prisma migrations, and exposes a `global.testPrisma` client for tests to use.

Key changes:
- Added `@testcontainers/postgresql` and `testcontainers` dependencies to `apps/web`
- Created separate Jest config (`jest.integration.config.cjs`) for integration tests with 60s timeout
- Created setup file that starts PostgreSQL container and runs migrations
- Added `integrationTest` script and Turbo task with `db:generate` dependency
- Updated CI workflow to run integration tests after unit tests
- Added sample integration test for ClerkUser model demonstrating CRUD and constraint testing
- Updated ESLint config to recognize `__integrationTests__` directories
- Updated README with testing documentation

## Review & Testing Checklist for Human

- [ ] **Check the relative path in setup**: The `cwd: '../../packages/database'` path in `jest.integration.setup.ts` assumes tests run from `apps/web` - verify this works in all scenarios
- [ ] **Review ESLint warnings**: There are lint warnings about `PrismaClient` not found in `@repo/database` - these appear to be false positives from the import resolver not understanding the monorepo, but worth confirming
- [ ] **Verify the testing pattern**: Functions that need database testing must accept a Prisma client as an argument since `global.testPrisma` doesn't override the singleton in `packages/database`

**Recommended test plan:**
1. Run `yarn integrationTest` locally from `apps/web` directory with Docker running
2. Verify all 3 sample tests pass (create/retrieve, email constraint, user_id constraint)
3. Confirm CI pipeline passes with the new integration test step

## Updates since last revision

- Changed `@repo/database` dependency from `workspace:^` to `*` per reviewer feedback
- All CI checks now pass including Vercel deployment

### Notes

- Link to Devin run: https://app.devin.ai/sessions/4d5ea2d2f1cb440e92b93a5cce8069be
- Requested by: T (liren@starfish.sh) / @tuliren
- The generated Prisma files were added to `.prettierignore` to fix a formatting error during pre-commit hooks
