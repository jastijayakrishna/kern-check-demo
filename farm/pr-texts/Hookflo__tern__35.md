# Isolate new-platform verification changes without altering existing algorithm behavior

### Motivation
- Add first-class support for Sentry, Grafana, Doppler and Sanity webhooks while avoiding broad changes to shared algorithm parsing behavior. 
- Keep existing platform algorithms and behavior intact so other providers continue to work without regressions. 
- Fix failing tests/fixtures (Polar secret handling and fal.ai signing inputs) introduced by earlier edits.

### Description
- Registered new platforms (`sentry`, `grafana`, `doppler`, `sanity`) in `src/types.ts` and added platform configurations in `src/platforms/algorithms.ts` while keeping the global algorithm surface unchanged. 
- Removed the new global `stripe-compatible` headerFormat and instead used the existing `comma-separated` parsing for Sanity signatures so no generic parser expansion was required. 
- Extended `src/verifiers/algorithms.ts` in targeted places only: added `json-stringified` payload formatting, Sentry-specific fallback payload candidate resolution, and Doppler synthetic dedupe id generation, and limited timestamp extraction-from-signature to the `comma-separated` format. 
- Restored Polar `secretEncoding` to `base64` usage for Standard Webhooks secrets and fixed the fal.ai test fixture to canonicalize the payload with newlines and produce a hex ED25519 signature and correct header names. 
- Added platform auto-detection entries in `src/index.ts` for the four new providers and added test helpers and fixtures in `src/test.ts` for Sentry/Grafana/Doppler/Sanity signatures.

### Testing
- Ran `npm run build` and TypeScript compilation completed successfully. 
- Ran `npm run lint` and lint completed (existing repository warnings remain but no new lint errors were introduced). 
- Ran the test harness via `npm test` and the full suite completed with all test checks printed as `PASSED`, including the newly added Sentry/Grafana/Doppler/Sanity tests and the adjusted Polar and fal.ai checks.

------
[Codex Task](https://chatgpt.com/codex/tasks/task_e_699ddef8b0a88324ab18fab63a49c51d)
