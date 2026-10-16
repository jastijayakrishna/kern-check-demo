# [eng-2057] Send structured output schema as json_schema

## Summary
`generateObject` / `Output.object` never sent the schema to Requesty, so Claude (e.g. `anthropic/claude-fable-5.1`) answered in prose and the SDK threw `AI_NoObjectGeneratedError`.

Before:
- No tools: `response_format` was overwritten to `{type: "json_object"}` and the schema was dropped. The router only maps `json_schema` to Anthropic `output_config`, so Claude got no constraint at all.
- With tools: the AI SDK's internal `{type: "json", schema}` was passed through as-is. That's not a valid OpenAI `response_format`, so it was ignored too.

After (`adaptResponseFormat`, same mapping as `@ai-sdk/openai-compatible`):
```
{type:'json', schema, name, description} -> {type:'json_schema', json_schema:{name: name ?? 'response', description, schema}}
{type:'json'} (no schema)                -> {type:'json_object'}
text / undefined                         -> omitted
```

Tested live against prod with our own key: `generateObject` and `Output.object` with tools now return valid objects on `anthropic/claude-fable-5.1` and `openai/gpt-4.1-mini`. Both failed before the fix. Added mock-fetch tests in `src/integration/response-format.test.ts`.

Patch bump to 3.6.4.

Link to Devin session: https://app.devin.ai/sessions/7c1c9bd910b94cc7a9126525815aaa6f
Open in Devin Desktop: https://app.devin.ai/desktop/session/7c1c9bd910b94cc7a9126525815aaa6f?variant=devin
Requested by: @requesty-JohnCosta27
