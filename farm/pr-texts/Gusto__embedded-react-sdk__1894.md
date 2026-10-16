# test(e2e): fail tests when ZodError appears in browser console

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Today an e2e shard can pass green while the SDK is silently crashing into an error boundary mid-flow. The most common cause is a `ZodError` thrown out of `@gusto/embedded-api`'s response parsing — the API client validates every response against the published Zod schema, and when the backend ships a shape the schema disagrees with, the parse throws and React catches it at the nearest error boundary. Example of what this looks like in the browser console:

```
Caused by: ZodError: [
  {
    "received": "Payroll",
    "code": "invalid_enum_value",
    "options": ["payroll", "ContractorPaymentGroup"],
    "path": ["Wire-In-Request-List", 0, "payment_type"],
    "message": "Invalid enum value. Expected 'payroll' | 'ContractorPaymentGroup', received 'Payroll'"
  }
]
    at safeParseResponse (chunk-WPXFCYAE.js?...)
    at async $do (@gusto_embedded-api-...wireInRequestsList.js?...)
The above error occurred in the <Root> component.
```

When this happens the SDK renders an error boundary instead of the expected screen, but unless the test happens to assert on something that's now missing it passes anyway. We want the shard to fail loudly so we catch schema drift between `zenpayroll` / `gws-flows` and the published `@gusto/embedded-api` Zod schemas.

## Changes

- In the shared Playwright `page` fixture (`e2e/utils/localTestFixture.ts`), subscribe to the `console` and `pageerror` events for every test.
- Capture any message whose text contains `ZodError` (covers both uncaught throws and React's error-boundary `console.error` logs).
- At the end of the test:
  - Attach the captured text as `zod-errors.txt` on the Playwright report so the HTML report / artifacts show exactly what was logged.
  - If the test would otherwise pass, throw to fail it. If the test already failed for another reason, the existing failure is preserved (the attachment still surfaces the Zod text).

This fixture wraps every test in every config (`playwright.config.ts`, `playwright.demo.config.ts`, `playwright.local.config.ts`), so the check is on by default for MSW-mode runs, demo runs, and local-backend runs.

## Testing

- `npm run test:scenarios` — passes (scenario module tests).
- `npx tsc --noEmit ... e2e/utils/localTestFixture.ts` — passes.
- `npx prettier --check e2e/utils/localTestFixture.ts` — passes.
- Behavioral check (manual): the listener fires before `await use(page)` returns, so it sees console output for the entire test lifetime, including renders triggered by `page.goto` and any subsequent interactions. If a `ZodError` shows up at any point the test fails with a message that includes the full captured text plus a `zod-errors.txt` attachment.

## Related

- Affects every e2e shard (MSW mode default config + demo + local).

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-b0ab4b94-8e4b-450d-a96e-27540289306c"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-b0ab4b94-8e4b-450d-a96e-27540289306c"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
