# feat: migrate THINKING_* events to REASONING_* in LangGraph

## Changes

Migrates event types from `THINKING_*` to `REASONING_*` across LangGraph Python and TypeScript integrations to align with updated ag-ui protocol.

### Key Updates

**Event Type Migrations:**
- `ThinkingStartEvent` → `ReasoningStartEvent`
- `ThinkingTextMessageStartEvent` → `ReasoningMessageStartEvent`
- `ThinkingTextMessageContentEvent` → `ReasoningMessageContentEvent`
- `ThinkingTextMessageEndEvent` → `ReasoningMessageEndEvent`
- `ThinkingEndEvent` → `ReasoningEndEvent`
- Added `ReasoningEncryptedValueEvent` for encrypted reasoning content

**Reasoning Content Resolution:**
- Updated `resolve_reasoning_content()` to support multiple reasoning formats:
  - Old Anthropic format: `{ type: "thinking", thinking: "..." }`
  - New standardized format: `{ type: "reasoning", reasoning: "..." }`
  - OpenAI Responses API: `{ type: "reasoning", summary: [{text: "..."}] }`
  - Extracts `signature` field from Anthropic extended thinking
- Added `resolve_encrypted_reasoning_content()` for handling `redacted_thinking` blocks

**Event Payload Enhancements:**
- Added `messageId` to reasoning events for proper tracking
- Added `role` field to `ReasoningMessageStartEvent`
- Added `signature` accumulation during reasoning processing

**Agent Configuration:**
- Updated example agents to use ChatOpenAI with reasoning configuration
- Added model support for `gpt-5.2` with reasoning settings

**Dependencies:**
- Updated ag-ui-protocol to 0.0.45 with new event definitions
- Updated @copilotkitnext versions to support new reasoning events
