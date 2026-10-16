# fix(storage): re-read unreconciled buckets, TTL from load, converge bucket CORS, no message-text error swallowing

## Summary

Devnet data-room uploads kept failing with `STORAGE_BUCKET_NOT_RECONCILED` long after the reconciler had recorded `physical_name`. Locally (MinIO/RustFS) it worked. Four fixes in the storage path, each with a repro test:

1. **`getBucketConfig` no longer caches an unreconciled row** (`graphile-presigned-url-plugin/src/storage-module-cache.ts`). Before this, the first upload attempt (before the reconciler finished) cached the row with `physical_name: null` for the whole TTL (1h in prod). Every retry got the same not-reconciled answer. Now a row without a `physical_name` is never cached, so retries re-read it until the name lands. Reconciled rows are still cached.
2. **The TTL now counts from the load, not the last read** (`updateAgeOnGet: true` removed from `bucketCache` and `storageModuleCache`). With `updateAgeOnGet`, each cache hit reset the entry's age. Under steady traffic an entry never expired, so a changed bucket or module row (mime types, size limits, a renamed `physical_name`) was never picked up. Now a change shows up within one TTL. Nothing invalidates these caches when a bucket row changes: no LISTEN/NOTIFY, and the exported `clearBucketCache` has no caller in the server. The TTL is the only refresh path.
3. **`BucketProvisioner.provision` converges CORS.** With no effective origins it used to skip CORS entirely, so a rule written by an earlier provision stayed on the bucket for good. It now calls `DeleteBucketCors` (new `clearCors`; `NoSuchCORSConfiguration` counts as already cleared). This matters because constructive-db will re-run provisioning when `allowed_origins` changes (companion PR). Removing an origin now removes the S3 rule.
4. **Stop ignoring S3 errors because of words in the message.** `setPublicAccessBlock`, `setBucketPolicy`, `setCors`, `enableVersioning`, `setLifecycleRules` and `deleteBucketPolicy` used to treat an error as "backend doesn't support this" if its message merely contained text like `'policy'`, `'CORSConfiguration'`, `'PublicAccessBlockConfiguration'` or `'not well-formed'`. An AWS AccessDenied for `s3:PutBucketPolicy` reads `"... because no identity-based policy allows the s3:PutBucketPolicy action"`, so it was **silently skipped**: a public bucket was reported as provisioned while its public-read policy was never applied. Unsupported-API tolerance now goes only by error code (`XmlParseException`, `NotImplemented`, plus `MissingContentMD5` for lifecycle), and everything else throws `ProvisionerError` with the AWS message.

```ts
// before: error ignored when the message contains 'policy'
if (... || err.message?.includes('policy')) return;
// after: only an explicit "not implemented" code is ignored
if (isUnsupportedOperation(err)) return;
```

## Reproduce-first evidence

Each test was run against `main`'s `src/` (`git stash` of the source change only) and then against the fix. Jest runs these suites from `src` via ts-jest, so no dist rebuild is involved.

`graphile-presigned-url-plugin/__tests__/bucket-config-cache.test.ts`

| test | main | fix |
|---|---|---|
| sees the physical name the reconciler records after a pre-reconcile read | ✕ `Expected "cnst-app-documents-0001", Received null` | ✓ |
| serves a reconciled bucket from the cache | ✓ | ✓ |
| re-reads a changed bucket row once its TTL passes, even under steady traffic | ✕ `Expected 200, Received 100` | ✓ |

`packages/bucket-provisioner` (`provisioner.test.ts` + `provisioner.integration.test.ts` against RustFS `1.0.0-rc.5`, CI's image): **main 10 failed / 64 passed → fix 74 passed**. The ones that failed on main:

- integration: clears the CORS rule set once the bucket records no origin (real RustFS: rule still present on main)
- clears any CORS rule set for a bucket nothing browses; removes the rule set an earlier provision wrote once the origins are gone
- setBucketPolicy throws an AWS AccessDenied whose message mentions a policy (resolved silently on main)
- setPublicAccessBlock throws a MalformedXML that names the configuration; setCors throws an AccessDenied that names the configuration
- enableVersioning / setLifecycleRules throw when only the message names the configuration
- clearCors treats a missing CORS configuration as cleared / throws on genuine errors (new method)

Full local runs: presigned-url-plugin 97/97, bucket-provisioner 131/131 (RustFS), graphile-bucket-provisioner-plugin 11/11.

## Rollout

constructive-db's reconciler pins `@constructive-io/bucket-provisioner` `0.30.0`. Items 3 and 4 reach devnet after this is published and the pin is bumped. Items 1 and 2 reach devnet with the next GraphQL server image that includes `graphile-presigned-url-plugin`.


Link to Devin session: https://app.devin.ai/sessions/287c7006762a425dbcc8ef94a69812af
Open in Devin Desktop: https://app.devin.ai/desktop/session/287c7006762a425dbcc8ef94a69812af?variant=devin
Requested by: @pyramation
