# Coordinate backend mTLS/Caddy, rate-limit & ledger fixes, secure-bet idempotency, UI/accessibility and env validation

### Motivation
- Prevent mismatched backend and Caddy mTLS settings from creating unsafe startup states and preserve plaintext operation when mTLS is not fully configured. 
- Ensure authenticated bettors are not penalized by anonymous IP quota ordering and avoid expensive full-map scans in the in-memory behavioral limiter. 
- Fix ledger migration/backfill and make secure bet placement idempotent when a prior operational outbox entry exists. 
- Improve production origin validation, UI shell navigation/accessibility, GameContext update purity, and document privacy-safe PAN recovery in the product blueprint. 

### Description
- Coordinated backend/Caddy mTLS startup checks and added guards to `backend/server.js` so enabling `BACKEND_MTLS_*` requires the corresponding Caddy upstream vars or rejects startup. 
- Reordered bet placement middleware in `backend/domains/markets/bet.routes.js` to run `authenticate` before anonymous IP limiting and removed the `unauthenticatedBetIpLimiter` import for this route. 
- Replaced the per-invocation full-map memory cleanup in `backend/middleware/behavioralRateLimit.js` with a bounded periodic sweep (`sweepExpiredBuckets`) to avoid scanning every bucket on each call while preserving TTL expiry and LRU eviction. 
- Removed `isfinite` constraints and changed ledger currency backfill in `backend/postgres/schema.sql` to copy missing `currency` from the referenced `user_wallets` row instead of hardcoding `USD`, keeping other numeric constraints intact. 
- Added idempotency handling to `backend/postgres/secureBetPlacement.js` by checking `operational_bet_outbox` for an existing `reference_id` and, if found, resuming only the operational-write path instead of creating duplicate ledger/debits. 
- Tightened origin validation in `backend/startup/validateEnv.js` so `isOrigin` accepts only `http:`/`https:` and requires `https:` in production checks. 
- Refactored `user-panel/src/services/GameContext.tsx` so accepted bet updates are determined before `setCycles`, updated `liveStatsRef` and subscribers first, and kept `setCycles` updater pure. 
- UI/UX changes: lowercased unquoted font tokens in `src/frontend/design-system/variables.css`, wired accessible navigation and mobile controls in the Admin/Merchant/User shells, made market buttons expose `aria-pressed`, and made bet CTAs preview-only/validated in `src/frontend/views/user/MainBazaarStage.jsx`. 
- Document updates in `design/BettingBazaar_UIUX_Product_Blueprint.md` to require privacy-safe, unauthenticated PAN check behavior, clarify app-assets upload route contract, and tighten the frame checklist exemption rules. 

### Testing
- Ran `npm run build:user` which completed successfully and produced the user-panel build artifacts. 
- Performed static checks with `node --check` on modified backend JS files which succeeded with no syntax errors. 
- Ran the test suite with `npm test` (Vitest) and all tests passed (`25 files, 198 tests`). 
- Attempted `npx vite build` at repository root which failed because this mono-repo root has no `index.html` entry (expected given repository layout), and does not block the validated `user-panel` build or unit tests.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a59e9194e78832d9f2411850b36381d)
