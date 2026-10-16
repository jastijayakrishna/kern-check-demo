# Refactor playground AI flow to Vercel AI SDK with Skill/CLI mode tool assembly and token usage visibility

Playground AI generation was migrated from a custom OpenAI-compatible loop to Vercel AI SDK patterns while preserving the existing layout. The refactor centralizes tool orchestration, enables proper multi-turn context handling, and surfaces tool-call progress plus token consumption in chat UI.

- **Backend: Vercel AI SDK-first generation path**
  - Replaced custom `callAI` + `AgentLoop` flow with `streamText` + `convertToModelMessages`.
  - Added structured tool registration via `ai` `tool(...)` + `zod` schemas.
  - Added per-response metadata (provider/model/mode/usage) to stream output for UI consumption.
  - Removed legacy adapter: `playground/src/libs/ai-sdk.ts`.

- **Provider/model architecture**
  - Added `resolveProviderModel(...)` and `createLanguageModel(...)` in `provider-registry.ts`.
  - Standardized model creation through `@ai-sdk/openai` for configured providers.

- **Mode-specific retrieval architecture (renamed modes)**
  - Modes are now **`skill`** and **`cli`** (replacing `tool-call` / `bm25` naming in API/UI).
  - **CLI mode** uses one tool:
    - `retrieve` (backed by retrieve API for document recall)
  - **Skill mode** uses a 3-step tool chain:
    - `load_skill` (load main `SKILL.md`)
    - `list_references` (enumerate reference metadata)
    - `read_file` (read selected reference files by path)
  - Updated generation flow to bind different tool sets and step limits by mode (`skill` vs `cli`).

- **Tool organization update**
  - Unified all concrete tool implementations under `playground/src/libs/tools`.
  - Mode entry files are placed one level above `tools` and assemble tools per mode:
    - `playground/src/libs/skill-mode.ts`
    - `playground/src/libs/cli-mode.ts`

- **Tool/skill management hardening**
  - Kept and strengthened path/category guards for safe `.md` reads under allowed skill directories.
  - Added explicit schema limits/constants for tool input bounds (retrieve/read limits).
  - Hardened library directory resolution and file existence checks used by tools.

- **Frontend chat refactor (`@ai-sdk/react`)**
  - Migrated chat state to `useChat` with transport to `/api/generate`.
  - Preserved sidebar/main layout, editor, preview, mode controls.
  - Added message-level tool call/result trace rendering.
  - Added token usage display per assistant turn and cumulative multi-turn total.
  - Updated UI mode labels to **Skill / CLI**.

- **Example (updated server generation pattern)**
```ts
const result = streamText({
  model: languageModel,
  system,
  messages: await convertToModelMessages(messages),
  tools: mode === 'skill' ? createSkillModeTools(library) : createCliModeTools(library),
  stopWhen: stepCountIs(
    mode === 'skill' ? SKILL_MODE_MAX_STEPS : CLI_MODE_MAX_STEPS
  ),
  temperature: 0.3,
  maxOutputTokens: 4000
});

return result.toUIMessageStreamResponse({
  originalMessages: messages,
  messageMetadata: ({ part }) =>
    part.type === 'finish' ? { provider, model, mode, usage: part.totalUsage } : undefined
});
```

### Screenshot
<img src="https://github.com/user-attachments/assets/381fbf62-7039-4399-addd-c155fb00d840">

<!-- START COPILOT CODING AGENT SUFFIX -->



<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 基于 vercel 的 ai-sdk 改写 playground 中的 ai 相关代码，要求：
> 
> 1.不要大量修改 ui 布局，和 ai 对话相关可以修改
> 2.通过 ai sdk 大量简化代码，删除现有的 ai-sdk 文件，用最规范的方式管理 tool，skill，以及多轮对话上下文
> 3.前端使用 @aisdk/react，ai 对话的 ui 上，显示 tool call 调用过程，以及多轮对话的 token 消耗
> 4.扫描 playground 现有代码，可以大规模重构，修改不合理的代码组织，架构设计，让他符合一个 nextjs 的 AI Agent 最佳实践
> 5.保持 ui 功能可用


</details>
