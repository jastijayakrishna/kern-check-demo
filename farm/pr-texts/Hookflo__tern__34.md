# Follow-up: restore custom token defaults and document token-auth compatibility

### Motivation

- Ensure `platform: 'custom'` continues to behave as a token-style provider by default so custom/token-based integrations keep working.
- Preserve backward compatibility for token-auth helpers by keeping a clear modern API while not breaking existing callers.
- Clarify README so users understand the `verifyTokenAuth` API and the default custom-platform token config.

### Description

- Restored the `custom` platform default `signatureConfig.customConfig` to include `type: 'token-based'` and `idHeader: 'x-webhook-id'` in `src/platforms/algorithms.ts` so token-style behavior is the default for `platform: 'custom'`.
- Kept the clearer helper `verifyTokenAuth(...)` and retained `verifyTokenBased(...)` as a backward-compatible alias that delegates to `verifyTokenAuth` in `src/index.ts`, and ensured token verification returns a canonical `eventId` when applicable.
- Updated `README.md` to explicitly document that `verifyTokenBased(...)` remains supported and that `platform: 'custom'` has a token-compatible default via `signatureConfig.customConfig`.
- Expanded tests in `src/test.ts` to assert both `verifyTokenAuth` and the `verifyTokenBased` alias paths and to validate canonical `eventId` behavior remains intact.

### Testing

- Ran `npm run build` and the TypeScript build completed successfully.
- Ran `npm test` which executed the test script; most verification tests passed but existing Polar and fal.ai verification checks still report failures in the test output (these failures pre-existed and were not introduced by this follow-up fix).

------
[Codex Task](https://chatgpt.com/codex/tasks/task_e_699dcd5306c48324a2b363a98dca39a6)
