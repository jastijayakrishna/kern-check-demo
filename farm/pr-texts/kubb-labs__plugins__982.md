# fix(examples): preserve generated client base URLs

### Motivation
- Restore the generated example runtimes' configured `baseURL` so checked-in client runtimes remain aligned with the plugins' `baseURL` configuration.

### Description
- Add `client.setConfig({ baseURL: 'https://petstore3.swagger.io/api/v3' })` to `examples/advanced/src/gen/.kubb/client.ts` and `client.setConfig({ baseURL: 'https://petstore.swagger.io/v2' })` to `examples/mcp/src/gen/.kubb/client.ts` to preserve the originally generated base URLs.

### Testing
- Ran `git diff --check` which passed.
- Attempted `pnpm --filter advanced-pet-store generate:ts && pnpm --filter mcp-pet-store generate` but generation could not be executed because Corepack could not download `pnpm@12.4.2` from the npm registry.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6ab781b2a2f88323a40886603f5a54df)
