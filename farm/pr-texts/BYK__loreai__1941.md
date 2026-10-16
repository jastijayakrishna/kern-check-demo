# feat(gateway): per-provider budgets in USD, tokens or quota percent

## Summary

Per-provider budgets on top of #1931/#1938 (stacked on the #1938 branch). A budget is keyed by `(provider, auth_kind | null, account | null)` and has a `unit` (`usd` | `tokens` | `percent`) and a `window` (`daily` | `5h` | `7d`):

- **daily / usd, daily / tokens** — evaluated against the persisted `provider_costs` ledger for the current UTC day (new core query `getProviderDayUsage(day, provider, authKind|null, account|null)`, `null` = wildcard); `resets_at` = next UTC midnight.
- **5h / 7d / percent** — evaluated against the latest persisted quota snapshot for that window; `resets_at` is the provider's own `resets_at`. When `now >= resets_at` the window has rolled since we last observed it, so `used` is reported as 0 and the status is `stale: true` (we don't invent the next boundary). Missing snapshot → `used: null, stale: true`.
- Windows shorter than a day cannot be measured in USD/tokens from a daily ledger, so `5h`/`7d` require `unit: "percent"`; conversely `daily` requires `usd`/`tokens` (percent has no denominator there). Both mismatches are 400s with that explanation.

**Enforcement** (`pipeline.ts`, existing throttle block only): when any provider budgets exist, the request's pre-upstream attribution (last upstream route + `resolveAuth`) is matched against them and `computeProviderBudgetPressure` (same 50 %-floor ramp as the daily/quota throttles, max over matching budgets) is combined as `max(quotaPressure, providerPressure)` into the existing `getDailyThrottleDelay`. The global daily budget / `LORE_DAILY_BUDGET` path is untouched and remains the legacy fallback; a DB failure while evaluating is caught and never affects the request.

**API** (additive, same route):
- `GET /api/v1/costs` → `provider_budgets: ProviderBudgetStatus[]` (`budget + { used, fraction, resets_at, stale }`).
- `PATCH /api/v1/costs/budget` accepts `{ amount }` (unchanged validation, byte-identical `{ amount, disabled }` response), `{ provider_budgets: [...] }`, or both. `LORE_DAILY_BUDGET` still 409s any body containing `amount` (before anything is persisted) but does not govern provider budgets. Limits: ≤50 entries, only the six fields, provider `^[a-z0-9._-]{1,64}$`, account `^[A-Za-z0-9._:-]{1,128}$`, amount in `(0, 1e9]` (`(0, 100]` for percent), no duplicate `(provider, auth_kind, account, unit, window)`.
- Storage: replace-all JSON in `kv_meta.provider_budgets`; corrupt data parses to `[]`.

**UI** (read-only): provider cards show matching budgets under a "Budgets" divider as `used / amount` (money, count or `%`), red at ≥100 %, `(stale)` when stale. The card editor from the issue is not in this PR (see open question).

## How tested

```
pnpm run typecheck && pnpm run lint && pnpm run format:check
pnpm --filter @loreai/core test -- provider-costs
pnpm --filter @loreai/gateway test -- provider-budgets operations-api cost-tracker   # 73 passed
pnpm --filter @loreai/ui test                                                         # 524/524
pnpm --filter @loreai/core build && pnpm --filter @loreai/ui build && pnpm --filter @loreai/gateway run bundle
node scripts/ui-deep-link-smoke.mjs
pnpm --filter @loreai/ui test:e2e e2e/provider-costs.spec.ts                          # seeds a 7d/80% budget, asserts "41% / 80%"
```
`packages/gateway/test/provider-budgets.test.ts` covers the validation matrix, daily USD/token evaluation with auth-kind/account wildcards, quota-window evaluation (normal, rolled-over reset boundary, missing snapshot, limit/remaining-derived percent), `resets_at` alignment, pressure ramp/wildcards/max-wins with mixed units, and corrupt-KV tolerance. `operations-api.test.ts` covers the legacy body, provider body, malformed bodies, and the env-override precedence cases (`{amount}` → 409, `{provider_budgets}` → 200, mixed → 409 with nothing persisted).

## Definition of done

- [x] Budgets per provider (and optionally auth kind / account) in USD, tokens or percent-of-quota
- [x] Daily and 5h/7d windows aligned to the provider's `resets_at`
- [x] Enforcement in the existing throttle path; `LORE_DAILY_BUDGET` legacy fallback preserved
- [x] `PATCH /api/v1/costs/budget` additive; old body byte-compatible
- [x] Tests: reset boundary, mixed units, env-override precedence

## Open questions

- USD/token budgets on 5h/7d windows would need a sub-day usage ledger (e.g. hourly buckets in `provider_costs`). I rejected them with a clear 400 instead of adding that storage — say if you want the hourly ledger.
- The issue mentions a budget editor on the provider cards; this PR ships the API + read-only display. I can add the editor as a follow-up on top of #1938 if wanted.

Closes #1927

Link to Devin session: https://app.devin.ai/sessions/46f05418a7614e8d9028a3b21174d343
Open in Devin Desktop: https://app.devin.ai/desktop/session/46f05418a7614e8d9028a3b21174d343?variant=devin
Requested by: @BYK
