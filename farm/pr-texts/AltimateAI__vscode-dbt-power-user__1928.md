# feat: surface `error.name`/`message`/`code` on telemetry errors

## Why

`TelemetryService.sendTelemetryError` previously forwarded only `error.stack`. That single property runs through VS Code's `TelemetryLogger.cleanData` PII redactor before reaching App Insights, which can collapse the entire stack into the URL replacement marker `<REDACTED: URL>` when the original stack is a single URL-shaped string. When that happens, the resulting App Insights event has empty `customDimensions.message` and an opaque stack — no error class, no message, no system error code — making field triage impossible.

0.60.7 telemetry surfaced two cohorts where this bites:

| Event | Volume (24h) | Symptom |
|---|---|---|
| `extensionActivationError` | 19 / 15 machines | `stack: "<REDACTED: URL>"`, all on win32 + VS Code 1.117 |
| `CommandProcessExecutionError` | 24 / 18 machines | child_process spawn failure carries `error.code` (ENOENT, EACCES, EPERM) — never reaches telemetry |

## Fix

`sendTelemetryError` now also extracts `error.name`, `error.message`, and `error.code` (when present) as their own top-level properties, via a small helper:

```ts
private extractErrorFields(error: unknown): { [key: string]: string } {
  if (!(error instanceof Error)) return {};
  const fields: { [key: string]: string } = {
    error_name: error.name,
    error_message: error.message,
  };
  const code = (error as { code?: unknown }).code;
  if (typeof code === "string" || typeof code === "number") {
    fields.error_code = String(code);
  }
  return fields;
}
```

These individual short string fields don't trigger the URL/path regexes the way a multi-line stack does, so they survive redaction and group cleanly in App Insights.

## Pre/post evidence

New `src/test/suite/telemetryService.test.ts` (7 tests) replaces the live TelemetryReporter on the service instance with a spy and asserts the exact properties dictionary handed to App Insights.

**Pre-fix on `origin/master` HEAD (4d067e04, fix not applied):**

```
      82 |   });
      83 |
      84 |   it("forwards error.message as a top-level property (survives URL redaction)", () => {

      at Object.<anonymous> (src/test/suite/telemetryService.test.ts:81:44)

  ● TelemetryService.sendTelemetryError surfaces diagnostic fields › forwards error.message as a top-level property (survives URL redaction)

    expect(received).toBe(expected) // Object.is equality

    Expected: "Channel closed"
    Received: undefined

      85 |     const err = new Error("Channel closed");
      86 |     telemetry.sendTelemetryError("unhandlederror", err);
    > 87 |     expect(captureProperties().error_message).toBe("Channel closed");
         |                                               ^
      88 |   });
      89 |
      90 |   it("forwards error.code for system errors (ENOENT, EACCES, etc.)", () => {

      at Object.<anonymous> (src/test/suite/telemetryService.test.ts:87:47)

  ● TelemetryService.sendTelemetryError surfaces diagnostic fields › forwards error.code for system errors (ENOENT, EACCES, etc.)

    expect(received).toBe(expected) // Object.is equality

    Expected: "ENOENT"
    Received: undefined

       98 |     );
       99 |     const props = captureProperties();
    > 100 |     expect(props.error_code).toBe("ENOENT");
          |                              ^
      101 |     expect(props.error_message).toBe("spawn /usr/local/bin/python ENOENT");
      102 |     expect(props.error_name).toBe("Error");
      103 |   });

      at Object.<anonymous> (src/test/suite/telemetryService.test.ts:100:30)

Test Suites: 1 failed, 1 total
Tests:       3 failed, 4 passed, 7 total
Snapshots:   0 total
Time:        2.367 s, estimated 3 s
Ran all test suites matching /src\/test\/suite\/telemetryService.test.ts/i.
```

**Post-fix on this branch:**

```
PASS src/test/suite/telemetryService.test.ts
  TelemetryService.sendTelemetryError surfaces diagnostic fields
    ✓ forwards error.name as a top-level property (3 ms)
    ✓ forwards error.message as a top-level property (survives URL redaction) (1 ms)
    ✓ forwards error.code for system errors (ENOENT, EACCES, etc.) (1 ms)
    ✓ does not regress the existing stack property (1 ms)
    ✓ preserves caller-supplied custom properties (3 ms)
    ✓ tolerates non-Error error values without surfacing diagnostic fields
    ✓ tolerates undefined error (1 ms)

Test Suites: 1 passed, 1 total
Tests:       7 passed, 7 total
Snapshots:   0 total
Time:        4.276 s
Ran all test suites matching /src\/test\/suite\/telemetryService.test.ts/i.
```

Full jest suite: 463 pass, 1 pre-existing skipped (28 suites total).

## Secondary code paths considered

- `sendTelemetryEvent` (the non-error variant) is unchanged — it never received error objects to begin with.
- All call sites of `sendTelemetryError` get the new fields automatically; they're additive and never override caller-supplied properties of the same name (`...properties` spreads first). I did not audit every individual call site because the change is purely additive and the new fields are documented as optional in the type.
- The `stack` property and `removeGenericSecretsFromStackTrace` masking are unchanged — `error.message` and `error.code` get their own fields, but the stack continues to flow through the existing redactor, so secret-pattern masking still applies to it.
- Caller-supplied `properties` (e.g., `message` from `vscodeTerminal.error`) continue to win over the new defaults because of the spread order.

## Downstream impact

Once a 0.60.8 lands with this PR, the dashboards in `monitoring/app.py` and the App Insights queries in earlier triage tickets (#1890, #1913, #1926) can pivot on `error_name` / `error_code` — no more guessing what `<REDACTED: URL>` means.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Improvements**
  * Telemetry error reporting now captures error name, message, and code as distinct fields for better diagnostics

* **Tests**
  * Added comprehensive test suite for error telemetry handling, including edge case scenarios

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
