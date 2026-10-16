# Prevent header injection into anonymous session JWT tenant/project claims

### Motivation
- Close an authorization bypass where unauthenticated callers could mint anonymous JWTs scoped to arbitrary tenant/project values by supplying `x-inkeep-tenant-id` / `x-inkeep-project-id` headers for global `web_client` apps.

### Description
- Stop reading `x-inkeep-tenant-id` and `x-inkeep-project-id` from the request when creating new anonymous session tokens so `tid`/`pid` claims are only populated from the app binding or a previously validated refresh token; change applied in `agents-api/src/domains/run/routes/auth.ts`.

### Testing
- Ran targeted test attempts: `pnpm -C agents-api test --run src/__tests__/run/routes/auth.test.ts` failed due to a duplicate `--run` option from the wrapper, and `pnpm -C agents-api exec vitest --run src/__tests__/run/routes/auth.test.ts` failed due to workspace package resolution for `@inkeep/agents-core`, so automated unit tests could not complete in this environment; pre-commit checks also failed due to network/corepack issues preventing `pnpm` download.

------
[Codex Task](https://chatgpt.com/codex/tasks/task_b_69cb444f08308333ac4eeda9887fb52e)
