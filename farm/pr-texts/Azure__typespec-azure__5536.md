# Preserve TypeScript client logging options when defaulting the logger

Generated Azure TypeScript clients replaced caller-provided `loggingOptions` with a logger-only object, dropping allow-listed headers, query parameters, and other `LogPolicyOptions` fields.

- **Generation**
  - Spread existing logging options before applying the package logger fallback.
  - Preserve explicit caller-provided loggers.

```ts
loggingOptions: {
  ...options.loggingOptions,
  logger: options.loggingOptions?.logger ?? logger.info,
},
```

- **Coverage**
  - Add focused coverage for allowed header and query parameter forwarding.
  - Update affected modular scenario baselines.

- **Release**
  - Add a patch change entry for `@azure-tools/typespec-ts`.

<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes #5535
