# Repository cleanup (Part 3): remove compare variant and artifacts, move refunds UI into module

## Summary

Part 3: strip the repository down to the app. Deletions, file moves, and import updates only — no component or behaviour changes. Companion to #9 (security/correctness); the two PRs are independent.

- **3.1 A/B variant removed** — `src/app/(app)/refunds/compare/` (4 files) deleted along with its four references: `REFUNDS_COMPARE_PATH` in `params.ts`, the import + `revalidatePath(REFUNDS_COMPARE_PATH)` in `actions.ts`, the "Variant A / Switch to variant B" banner (and the now-unused `Link`, `buildRefundsHref` imports) in `refunds/page.tsx`, and the `refunds workflow (variant B)` e2e describe block (removed, not repointed). `/refunds/compare` no longer appears in the build route list.
- **3.2 Design artifacts removed** — `prototypes/finops-control-center.html`, `assets/*.png` (4), `design-directions.md`. Verified nothing in `src`, `e2e`, README, or config referenced them.
- **3.3 Agent tooling removed** — `.agents/skills/verify-fintech-tool/` deleted; the two references (`AGENTS.md:69`, `README.md:72`) dropped. `AGENTS.md` itself stays as the contributor contract.
- **3.4 Refunds module self-contained** — the eight presentational components moved with `git mv` from `src/app/(app)/refunds/*` to `src/modules/refunds/ui/*`; the only diff inside them is the import path rewrite `@/app/(app)/refunds/… → @/modules/refunds/ui/…`. `page.tsx` and `loading.tsx` stay in the route directory.
- **3.5 `pnpm-workspace.yaml`** — the local uncommitted change added `packages: ["."]`. Not needed: the file exists only to carry `allowBuilds` for pnpm ≥10, and `pnpm install --frozen-lockfile` and the whole toolchain work without a `packages` list (the repo is a single package, not a workspace). Declaring it would make pnpm treat the root as a workspace member for no benefit. **Recommendation: revert it locally; nothing to commit.** The file in this PR is unchanged from `main`.

### Verification (separate local DB, migrated + seeded, `DEMO_MODE=true`)
`pnpm lint` ✔ · `pnpm typecheck` ✔ · `pnpm test` ✔ (149) · `pnpm build` ✔ · `pnpm test:e2e` ✔ 61 passed, 1 skipped (pre-existing narrow-viewport skip in `kyc.spec.ts`; the count is lower than main only because the variant-B tests are gone).


Link to Devin session: https://app.devin.ai/sessions/443802f814954c098a0825916cf012b4
Open in Devin Desktop: https://app.devin.ai/desktop/session/443802f814954c098a0825916cf012b4?variant=devin
Requested by: @kert114
