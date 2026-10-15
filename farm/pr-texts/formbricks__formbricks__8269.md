# fix: redact webhook signing secrets from management API responses

## Summary

- Webhook **list, detail, update, and delete** responses in both the v1 and v2 management APIs returned the raw webhook record including the stored signing `secret`. Since read-only API keys are allowed to perform GET requests, a lower-privileged key holder could obtain reusable webhook signing material and forge signed webhook deliveries to downstream consumers (ENG-1319 sibling report: ENG-921).
- The signing secret is now **only exposed once, in the POST create response** — matching the existing app UI behavior (`WebhookCreatedModal` shows the secret once with a copy warning) and the audit-log redaction policy.
- Added `removeSecretFromWebhook` helpers (separate copies for v1 and v2 to keep the API versions decoupled) applied at the route layer; the lib layer is unchanged because `testEndpointAction` legitimately needs the stored secret server-side.
- OpenAPI schemas updated: new `webhookWithoutSecret` component used for GET/PUT/DELETE responses; create response keeps the full `webhook` schema.

Fixes [ENG-921](https://linear.app/formbricks/issue/ENG-921/security-report-read-only-api-keys-can-retrieve-webhook-signing)

## Test plan

- [x] Unit tests for `removeSecretFromWebhook` (v1 + v2): secret removed, all other fields preserved
- [x] Existing webhook test suites pass (45 tests)
- [x] Typecheck clean for all touched files
- [ ] Manual: create webhook via v2 API → secret present in 201 response; GET list/detail → no `secret` field; PUT/DELETE → no `secret` field
- [ ] Manual: same checks against v1 endpoints
- [ ] Verify webhook settings UI still shows secret in the created modal and test-endpoint flow still works

🤖 Generated with [Claude Code](https://claude.com/claude-code)
