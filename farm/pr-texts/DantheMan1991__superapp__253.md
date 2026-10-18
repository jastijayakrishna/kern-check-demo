# Re-land production slice 1a, with the migration applied first

Restores #251, reverted by #252. **The migrations are already applied to both databases** — that is the only thing that changed.

## What actually broke

Nothing in the deploy path runs migrations: `build` is `next build`, `prebuild` only copies the map worker, `vercel.json` is crons. So `main` auto-deployed code that queries `production_run_carcasses` and the table was never created anywhere.

The blast radius was the whole module rather than the new screen, which is worth knowing before the next read lands here: `ProductionModule` calls `listRunCarcasses` for **every** run in its summary loop, to decide whether the sheet column has earned its width. A read that exists to keep a column honest is still a read on every page load.

## Correcting the revert's diagnosis

Both of #252's theories were wrong. Checked against production directly, read-only:

| #252 said | Production says |
| --- | --- |
| `app_user` has no `SELECT` on the new table — `ALTER DEFAULT PRIVILEGES` only covers tables created by the role that set it | True in general, irrelevant here. `db:create-role` and `db:migrate` both connect as `DATABASE_URL_OWNER`, the same `neondb_owner` — the case where default privileges **do** apply. `pg_default_acl` holds `app_user=arwd/neondb_owner`, and **no** table in `public` is unreadable by `app_user`. |
| Running the migration by hand did not fix it, so a second cause is underneath | The table existed on **neither** database, so nothing was tested by running it "by hand". Replaying `0184` and `0185` against production inside a transaction and rolling back applied both cleanly. There is no second cause. |
| If `0184` reached production the orphan table must be dropped before re-applying | It did not. `to_regclass` returned null. Dropping on that advice would have been a destructive act taken on a guess. |

## Certified in the opposite order

The code is #251's, unchanged. What changed is the ordering:

1. `npm run db:migrate -- --dev` → dev branch ✅
2. `npm run db:migrate` → production ✅
3. Verified on **both** in `pg_class`/`pg_policies`: RLS enabled **and** forced, both policies (`member_all`, `superadmin_all`), 6 CHECKs, 3 FKs, `app_user` holding SELECT and INSERT **with no manual grant**, 0 rows.
4. `npm run test:isolation` — **429 tests, 25 files, all pass**.
5. `npx tsc --noEmit` clean.

Step 4 is the one that means something. The dev branch created this table by migration **long after** `app_user` existed — the ordering that would expose a grant skew. The from-zero build CI uses grants `app_user` after the schema exists and structurally cannot see one.

Because the table is already live and empty, merging this is additive: the code arrives to a table that has been sitting there unused.

## The deploy gap, which outlives this slice

[ADR 0014](docs/decisions/0014-migrations-are-applied-before-the-merge.md) plus a `migrations` CI job that fails any PR adding a `drizzle/*.sql` without `full-tests`, printing the ordering rule in its failure. This PR carries the label, so the job is self-testing.

**It checks a label, not a database.** It makes forgetting loud, not impossible. The release job that would actually close this — migrations applied before Vercel promotes a build — is recorded as still open in the ADR, along with why migrating inside `build` is worse than the problem it solves.

## Still open

`production_run_carcasses` holds zero rows on both databases. **No carcass row has ever been written by a person**, and the two screens most likely to be wrong are the ones in a state nothing else on this pack has: a sheet on a FINISHED run, and the form that changes shape when a carcass is condemned.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
