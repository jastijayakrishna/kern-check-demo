# fix: escape injection metacharacters in Kotlin/Ruby/Rust emitters

## Summary

Spec-derived metadata (enum wire values, non-simple field names, discriminator keys) flowed into generated SDK source without being fully neutralized in the target language's string-literal syntax, allowing **code injection into the generated Kotlin/Ruby/Rust SDKs**. An attacker who can influence OpenAPI spec metadata can execute code in smoke-test CI and in downstream customers' builds/runtimes. Validated for SEC-1431; each vector was reproduced end-to-end through the real `@workos/oagen` parse→IR→emit pipeline (Ruby + Rust executed injected code; Kotlin produced a live `${...}` template), and each is now inert after this change.

The escaping helpers dropped language-specific metacharacters:

- **Kotlin** — `ktStringLiteral` escaped `\ " \n \r` but not `$`, so a wire value like `${System.getenv()}` became a live string template.
  ```diff
    "${value
      .replace(/\\/g, '\\\\')
  +   .replace(/\$/g, '\\$')
      .replace(/"/g, '\\"') ...}"
  ```
- **Ruby** — `rubyHashAccessor` / `rubyHashLiteralKey` and the union discriminator `when` clause emitted double-quoted strings/symbols escaping only `"`, leaving `#{...}` interpolation live (RCE on model load); single-quoted enum values escaped `'` but not `\`, enabling quote breakout. Adds a shared `rubyDoubleQuotedInner` (escapes `\ " #`) and doubles `\` in the single-quoted enum literal.
  ```diff
  - return `when ${JSON.stringify(value)} then ...`   // JSON escaping ≠ Ruby-safe
  + return `when "${rubyDoubleQuotedInner(value)}" then ...`
  ```
- **Rust** — `#[serde(rename = "...")]` interpolated the raw field name, so a `"` closed the attribute string and injected arbitrary Rust items. Now uses `JSON.stringify(rename)` (Rust and JSON string-escape rules coincide here).

Existing behavior for legitimate wire names is unchanged (all 664 prior tests pass); `test/injection-escaping.test.ts` adds regression coverage for each vector.

> Automated first-pass security fix. Requires human security review before merge — please confirm the Ruby/Rust escaping rules are complete for your full metacharacter set and that no legitimate spec produces different output.


Link to Devin session: https://app.devin.ai/sessions/b6955da300ef43b29ede97f199a9f3cc
