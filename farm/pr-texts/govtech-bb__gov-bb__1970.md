# Per-form webhook destinations: fail-loud + guardrails (#1920, phase 1)

Groundwork for **per-form webhook destinations** (#1920): each form that syncs to a case-management system delivers to its own URL + secret, and misconfiguration fails loud instead of silently not-syncing. This is **phase 1 + the Session 2 guardrails**; the bulk youth-opportunity recipe migration is a separate follow-up (see below).

## What's in this PR

**Fail-loud dispatch** (`2df44b68`)
- `WebhookProcessor` throws instead of silent-skipping: `WebhookConfigError` (unset endpoint/secret env, or neither `endpoint` nor `url`) and `WebhookDeliveryError` (non-2xx/timeout/network). Both route to SQS retry → DLQ, so a misconfigured form is visible.
- Migrates science-camp off the shared `WEBHOOK_URL`/`WEBHOOK_SECRET` to its own `WEBHOOK_URL_SCIENCE_CAMP` / `WEBHOOK_SECRET_SCIENCE_CAMP`.

**Validation spine (loud & early)**
- **CI lint** (`a36d2ef0`, `1fcc6c3c`): `validate-recipes` enforces the `WEBHOOK_URL_<TOKEN>`/`WEBHOOK_SECRET_<TOKEN>` convention, requires the URL and secret **tokens to match** (blocks cross-wired secrets), and checks `mapping.applicant` paths resolve to real recipe steps. Shared convention helper in `form-types`.
- **Startup audit** (`ed51f105`): the recipe loader WARNs at boot about unprovisioned webhook env vars (surfaces a gap at deploy, not at first submission); `missingWebhookEnv()` for `/health`. Non-fatal.

**Deterministic identity** (`65aeec86`)
- Application codes are now a pure function of `(service, submissionId, submittedAt)` — stable across SQS retries (the old CSPRNG minted a new code per retry). Format unchanged (`SERVICE-DDMM-XXXXXXX`).
- Adds explicit `mapping.codeService`; unknown value throws (fail loud). `application-code.ts` relocated into `processors/`.

Docs: `docs/webhook-destinations.md` (convention, fail-loud contract, provisioning table).

## Verified
- `nx run-many -t build` green; api + form-types tests pass; `pnpm validate-recipes` OK (positive + negative). Every commit is self-contained and green.

## Deploy / provisioning (hand-off, provision-first)
Ops must set, in sandbox/staging/prod **before this deploys**, or science-camp submissions fail-loud into the DLQ:
- `WEBHOOK_URL_SCIENCE_CAMP` / `WEBHOOK_SECRET_SCIENCE_CAMP` (same values as today's shared pair).

## Follow-up (separate session — not in this PR)
- Migrate the ~18 youth-opportunity forms onto the `webhook` processor (per-form env + `mapping.codeService` + applicant paths), then delete the hardcoded `webhooks/` dispatch path. Entry criteria in `docs/plans/per-form-webhook-destinations.md` (confirm `yes`/`yar` formIds; per-form applicant field paths; ship recipes + deletion together).

Part of #1920.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
