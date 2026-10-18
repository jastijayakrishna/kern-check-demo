# fix(core): retry malformed streamed responses

## What this PR does

This PR retries malformed streamed responses before corrupted protocol text can be accepted as the assistant's final answer.

It covers two concrete failure shapes from #6666 and the follow-up traces:

1. A streamed tool call reaches the end of the stream without ever providing a function name. While the tool call is still nameless, accompanying response parts are held. If the stream finishes nameless, the held attempt is discarded through the existing invalid-stream retry path.
2. A stream has already produced structured reasoning (`reasoning_content` / thought), but visible content also contains raw `<think>` / `</think>` tag fragments. That means the reasoning and visible-content channels were mixed, so the attempt is discarded and retried instead of displaying those tags to the user.

Both malformed response shapes use the existing invalid-stream retry budget: up to four retries after the initial call, for five total attempts. Protocol-tag leaks retain a distinct telemetry classification while using the same retry budget.

Literal `<think>...</think>` text is still preserved and streamed immediately when there is no structured reasoning signal and no malformed nameless tool call. Provider-specific tagged-thinking parsing remains opt-in through provider response parsing options.

## Why it's needed

The original production case was not just "Qwen3 content may contain a complete `<think>...</think>` block." The stronger evidence is that the model/provider stream mixed channels: it returned a separate reasoning/thought channel, then left raw thinking-tag fragments and reasoning text inside visible content. One recorded case also included a tool call with an ID and arguments but no function name, which the old converter silently dropped before accepting the remaining corrupted visible text as successful output.

The safe boundary is therefore protocol-level, not model-name-level: when structured reasoning has appeared, a leading raw opening thinking tag or an unmatched raw closing thinking tag in visible content is treated as a malformed stream and retried. This avoids globally stripping user-visible literal tags and avoids enabling tagged-thinking parsing for every Qwen3-compatible endpoint.

## Reviewer Test Plan

### How to verify

1. Stream text, reasoning, and a tool call that never provides a function name. Confirm the first attempt is discarded and a healthy second response is shown.
2. Stream normal reasoning followed by visible content. Confirm reasoning/final content still works without retry.
3. Return literal `<think>example</think>` content without structured reasoning and without a malformed tool call. Confirm it remains visible.
4. Return structured reasoning first, then visible content containing `</think>` / `<think>` fragments. Confirm the bad attempt is retried and the leaked tags never appear in the TUI or chat record.
5. Return structured reasoning and visible `<think>...</think>` content in the same chunk. Confirm the bad attempt is retried and the leaked tags never appear in the TUI or chat record.

### Evidence (Before & After)

Before: malformed streams could be accepted as final output, so raw `<think>` / `</think>` fragments reached the UI and chat record.

After: malformed attempts with nameless tool calls or structured-reasoning tag leaks produce no bad TUI/chat-record output, drop their content and tool calls, withhold the finish signal, and are retried through the existing invalid-stream retry path.

Focused core tests pass **476/476**. A five-attempt integration test confirmed that four malformed attempts are discarded and only the clean fifth response reaches history. Repository `build`, `typecheck`, `lint`, and `bundle` pass locally. Fresh interactive tmux validation covered healthy structured reasoning, literal tag content, the exact recorded cross-channel leak, and a terminal incomplete tag prefix. Strict assertions confirmed that leaked tag payloads did not appear in t
