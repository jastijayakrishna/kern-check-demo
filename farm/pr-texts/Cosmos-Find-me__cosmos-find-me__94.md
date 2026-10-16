# feat: Add automated test user seed for easier dev onboarding

## Summary
Simplifies developer onboarding by automating test user creation for E2E tests. New devs can now run a single SQL migration instead of manually creating test users in Supabase dashboard.

## Changes Made

### 🗄️ Database Migration
- **Added** `supabase/migrations/002_seed_test_user.sql`
  - Creates test user with default credentials (test@example.com / testpassword123)
  - Idempotent with `ON CONFLICT DO NOTHING` clauses
  - Sets up complete user profile automatically (auth user + profile + company data + preferences)

### 📝 Documentation
- **Updated** `docs/01-GETTING_STARTED.md`
  - Added optional step 5 for test user creation
  - Clear explanation that it's only needed for E2E tests
- **Updated** `docs/02-SUPABASE_SETUP.md`
  - Added Step 4.5 with detailed test user setup instructions
  - Updated verification step to include test user check
- **Updated** `.env.example`
  - Added reference to seed migration for test credentials

### ⚙️ Setup & Configuration
- **Updated** `scripts/setup-supabase.cjs`
  - Fixed migration reference (removed non-existent `002_row_level_security.sql`)
  - Now correctly references `002_seed_test_user.sql`
- **Added** `.eslintignore`
  - Excludes generated files (.next/, tests/reports/) from linting

## Benefits for New Developers

**Before:**
1. Clone repo
2. Setup Supabase
3. Run schema migration
4. 🔴 Manually create test user in Supabase dashboard
5. 🔴 Manually add test credentials to .env.local
6. Run E2E tests

**After:**
1. Clone repo
2. Setup Supabase
3. Run schema migration + test user seed
4. ✅ Run E2E tests immediately!

## Testing

- ✅ 289 unit tests passing
- ✅ All linting and type checks passing
- ✅ Build verification successful
- ✅ SQL migration syntax validated
- ✅ Migration is idempotent (safe to run multiple times)

## Migration Usage

New developers can create the test user by running in Supabase SQL Editor:
```sql
-- Run after 001_initial_schema.sql
-- Creates test@example.com / testpassword123
supabase/migrations/002_seed_test_user.sql
```

Closes #14

🤖 Generated with [Claude Code](https://claude.com/claude-code)
