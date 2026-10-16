# fix(core): return agent icon in agent schema responses

### Motivation
- Add explicit `icon` support to agent responses so clients can receive a resolved icon URL alongside `image` wherever the agent schema is returned.

### Description
- Add `icon` to the shared `agentSchema`, add `getAgentIcon()` in `apps/core/src/helpers/agent.ts`, and populate `icon` in both `apps/core/src/routes/v1/agents/get.ts` and `apps/core/src/routes/v1/agents/[id]/get.ts` before parsing/returning the schema.

### Testing
- Ran `pnpm core:lint` and `pnpm core:test`, and the lint step completed and all tests passed (`378` tests passed).

------
[Codex Task](https://chatgpt.com/codex/tasks/task_e_69a20084aa48832d88680a8a0b22f522)
