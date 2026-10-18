# fix(core): Parse tagged thinking for GLM responses

## What this PR does

This PR enables tagged thinking parsing for DashScope OpenAI-compatible `glm-*` requests, so `<think>...</think>` content returned in the normal `content` field is converted into thought parts instead of being displayed as normal assistant output.

The parsing decision now follows the effective request model (`request.model || contentGeneratorConfig.model`). This matters when a caller overrides a non-GLM default config to a GLM request model, or overrides a configured GLM model to a non-GLM model.

It also keeps provider-supplied `reasoning_content` / `reasoning` when tagged parsing is enabled but the stream or response does not actually contain tagged thinking. For streaming responses, reasoning-channel text is buffered during tagged streams and emitted only if no tagged thought is found, avoiding duplicate thought output when the provider sends both channels across different chunks.

## Why it's needed

Issue #6007 reports that GLM-5.2 can return reasoning inline in `content` when the request uses a large `max_tokens` value such as 131072. In that response shape, `reasoning_content` is empty and the visible assistant output can include internal reasoning followed by a stray `</think>` tag before the final answer.

Qwen Code already has a tagged-thinking parser, but the DashScope GLM path was not opting into it for GLM requests. The resulting call chain is `OpenAI-compatible GLM response -> OpenAI response converter -> normal assistant text parts -> stream-json / TUI output`, which lets raw thinking tags reach user-visible output instead of the thought channel.

## Reviewer Test Plan

### How to verify

Reviewers can verify the unit behavior with a GLM-style response whose `content` is `<think>reasoning</think>final`: the converter should emit one thought part for `reasoning` and one normal text part for `final`.

The added coverage also verifies:

- DashScope parsing options are based on the effective request model, including request-level GLM and non-GLM overrides.
- Non-streaming `reasoning_content` is preserved when no thinking tags are present.
- Non-streaming duplicate `reasoning_content` is suppressed when tagged thinking has already been parsed from `content`.
- Streaming duplicate `reasoning_content` is suppressed when tagged thinking appears in the same chunk.
- Streaming duplicate `reasoning_content` is suppressed when the reasoning channel arrives first and tagged content arrives in a later chunk.
- Streaming reasoning-channel text is still flushed on finish when tagged parsing is enabled but no tagged thought appears in content.

### Evidence (Before & After)

Before: the response shape reported in #6007 would pass inline `<think>...</think>` content through the DashScope GLM path as normal visible assistant text. Request-level model overrides could also choose a GLM model while the parsing option stayed tied to the configured default model.

After: DashScope OpenAI-compatible requests whose effective model is `glm-*` enable tagged thinking parsing, so inline tagged reasoning is converted to thought content while the final answer remains normal text. Responses that provide reasoning through `reasoning_content` still preserve that separate reasoning channel when no tagged block is present, including streaming responses.

Targeted validation:

```powershell
npm exec vitest run packages/core/src/core/openaiContentGenerator/provider/dashscope.test.ts packages/core/src/core/openaiContentGenerator/converter.test.ts packages/core/src/core/openaiContentGenerator/pipeline.test.ts -- --coverage=false
```

Result: 3 test files passed, 297 tests passed.

Typecheck validation:

```powershell
npm run typecheck --workspace=packages/core
```

Result: passed.

Build validation from the earlier PR revision:

```powershell
npm run build --workspace=packages/core
```

Result: passed.

```powershell
npm run build
npm run bundle
```

Result: passed locally on Windows. The build completed with existing warnings ab
