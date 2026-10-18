# fix(trust-center): gate the public download on scan status and lifecycle

## The defect

`/api/trust/download/[token]/route.ts` is the **only unauthenticated file-serving path in the repo** — no session, no tenant context, just a single-use token. It selected `{ pathKey, originalName }` and passed the pathKey straight to `createSignedDownloadUrl`.

It therefore could not gate on anything. A valid token served:

- a file scanned **INFECTED**
- a file whose scan had not finished (**PENDING** — the state every file is in between storage and the async scan)
- a **soft-deleted** file
- a file that never reached **STORED** (a `PENDING`/`FAILED` upload)

Every internal path already ran the three-part check (`audit-pack-sharepoint-export`, `downloadEvidenceFile`, `downloadFile`, the access-review route, `vendor-doc-text`). The public one didn't. A column you never load is a gate you cannot apply.

**404, not 403.** The caller is anonymous, so a distinguishable status confirms a document exists behind a token that was guessed or replayed. A test asserts the blocked and missing responses are byte-identical.

## Two adjacent fail-open paths in the same predicate

**`bundle-attachments` guarded the gate with `scanStatus !== undefined &&`** — so an *absent* status skipped it entirely, while the client mirror (`isScanPending`) treats a falsy status as PENDING, i.e. not servable. A fail-open wrapper around a fail-closed predicate. `undefined` is now in `isDownloadAllowed`'s signature (the body always handled it) so no call site is pushed into writing that again.

**`isDownloadAllowed` returned `true` for INFECTED whenever `AV_SCAN_MODE=disabled`**, because the mode check sat above the INFECTED check — while its own comment claimed INFECTED was refused *"regardless of mode"*. Scanning being off explains why *new* files are unscanned; it cannot un-know a verdict already recorded on an old one, and `av-webhook/route.ts` writes INFECTED with **no mode check**, so such rows genuinely exist. Order reversed so the comment is true.

> ⚠️ **Behaviour change, flagged deliberately.** `tests/unit/av-scan.test.ts` asserted `isDownloadAllowed('INFECTED') === true` under `disabled`. That assertion is **updated, not deleted**, with the reasoning in place. Confirmed with the repo owner before changing.

## The guard could never have caught this

`tests/guards/evidence-download-authz.test.ts` claims at line 11: *"Every serving path runs through the ONE isDownloadAllowed predicate."* Its assertions enumerated four files by hand. The trust route was added later and simply wasn't on the list — so the guard stayed green for the entire life of the bug.

Replaced with a **discovery scan**: walk `src/`, find every caller of a storage read primitive (`readStream` / `createSignedDownloadUrl`), and require each to gate or appear in `NON_SERVING_READS` with a written reason. It found **14 call sites**, not 4.

The five declared non-serving reads each have a narrow justification — hashing for integrity (`audit-hardening`), reading back bytes this process just wrote (`import-snapshot`, `risk-report`), pre-scan staging (`evidence-import`), and avatars (not FileRecord-backed). A `no stale entries` test keeps the list honest; it caught one bogus entry of mine during development.

## The strict gate had never run

`tests/mocks/env.ts` returned `undefined` for `AV_SCAN_MODE`, so `isDownloadAllowed` took its **permissive** branch in every test in the repo — meaning the strict gate that blocks a mid-scan file was never once exercised. My PENDING test failed against it, which is how it surfaced. Now mirrors the real `.default("strict")`.

This is the same defect class as `NOTIFICATIONS_TZ` on the Calendar round: a mock that answers differently from production makes its suites green without testing the shipped configuration.

## Tests

`tests/unit/trust-download-route.test.ts` — new, the route's first executing tests. Drives the real export with prisma, the token consumer and the provider mocked. Every case uses a **valid, correctly-consumed token**, be
