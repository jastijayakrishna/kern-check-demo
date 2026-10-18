# Aadhaar HMAC hashing, migration, merchant bulk-payout feature flag, and related env/tests

## **User description**
### Motivation
- Replace legacy SHA-256 Aadhaar hashes with keyed HMAC-SHA-256 to support secret rotation and stronger key separation for duplicate-account prevention. 
- Gate merchant bulk-payout endpoints behind a feature flag to allow controlled rollout and UI exposure. 
- Add runtime and test-time environment validation so the app fails fast when Aadhaar HMAC secret is missing. 

### Description
- Added `backend/domains/identity/aadhaarHash.util.js` implementing normalized Aadhaar handling, HMAC-SHA-256 hashing, and candidate generation for secret rotation via `hashAadhaar` and `hashAadhaarCandidates`. 
- Replaced plaintext/legacy Aadhaar handling across KYC and recovery flows: `user.routes` normalizes Aadhaar/name on KYC submit and stores normalized values, `account-recovery.routes` now uses `hashAadhaarCandidates` to locate users across secret rotations and stores HMAC hashes via `hashAadhaar`. 
- Added `aadhaarHash` field to `User` model (`aadhaarHash: { type: String, unique: true, sparse: true, select: false }`) to store keyed hashes instead of plaintext. 
- New migration script `backend/scripts/migrate-aadhaar-hashes.js` to convert existing KYC Aadhaar values into HMAC hashes (guarded by env checks and index collision handling). 
- Updated environment handling: added `AADHAAR_HMAC_SECRET` to `.env.example` and to the required list in `startup/validateEnv.js`, and set a test default in `backend/tests/setup.js`. 
- Added unit tests `backend/tests/unit/aadhaarHash.test.js` for hashing/rotation behavior and updated `validateEnv` test to include the new required var. 
- Introduced a feature flag `MERCHANT_BULK_PAYOUTS` in `backend/services/featureFlags.service.js` with default `false`, added `requireBulkPayoutsEnabled` middleware to `merchant.routes.js`, and applied the gate to `/bulk-payouts`, `/bulk-payouts/export`, and `/bulk-payouts/mark-paid`. 
- Small server change to serve app assets with stored `contentType` in `backend/server.js` to avoid relying on filename extensions. 
- Added `migrate:aadhaar-hashes` script to `package.json`. 

### Testing
- Ran unit tests with `vitest` (`npm test` / `vitest run`) which include `backend/tests/unit/aadhaarHash.test.js` and the updated `validateEnv` unit test, and they passed. 
- Verified test environment boot by setting `AADHAAR_HMAC_SECRET` in `backend/tests/setup.js` so test imports that require env validation succeed. 
- The migration script `node backend/scripts/migrate-aadhaar-hashes.js` is included but not executed as part of automated tests and must be run manually in production after deploying the unique index and configuring `AADHAAR_HMAC_SECRET`.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a5a17b23bbc832b8cf0e9acd5017354)


___

## **CodeAnt-AI Description**
Tighten Aadhaar handling, hide bulk payout actions behind a flag, and serve app assets with the right file type

### What Changed
- Aadhaar KYC data is now normalized before saving, and Aadhaar lookups use keyed hashes with support for secret rotation
- Existing Aadhaar records can be migrated to the new hashing scheme with a one-time migration script
- Recovery and admin duplicate-check flows now reject matching Aadhaar numbers across current and retained secrets
- Merchant bulk payout pages and actions are blocked unless the bulk payout feature flag is enabled
- App asset files now return their stored content type instead of relying on the file name extension

### Impact
`✅ Fewer duplicate-account mismatches after Aadhaar secret rotation`
`✅ Safer Aadhaar storage`
`✅ No accidental access to bulk payout actions before rollout`


[🔄 Retrigger CodeAnt AI Review](https://api.codeant.ai/pr/retrigger_review?id=iwhjAIJiuQzPV82t01D72veDeVs8yp-4U9rW8Rs69zg&org=tezerports-dot)<details><summary><strong>💡 Usage Guide</strong></summary>

### Checking Your Pull Request
Every time you make a pull request, our system automatically looks through it. We check for security issues, mist
