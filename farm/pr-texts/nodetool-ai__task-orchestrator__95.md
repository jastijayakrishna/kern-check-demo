# Auto-name chats with deterministic fallback and model upgrade

## Summary
Implement intelligent auto-naming for chats with a two-tier approach: a fast deterministic fallback that always works, plus an optional model-generated upgrade for better titles.

## Key Changes
- **New module `lib/chat-title.ts`**: Provides two complementary titling functions:
  - `deriveTitle()`: Deterministic, always-available title generation that strips markdown, collapses whitespace, and truncates intelligently on word boundaries
  - `generateChatTitle()`: Best-effort model-based title generation using a fast model (Claude Haiku by default) with graceful degradation to null when credentials are unavailable or requests fail
  
- **Updated `lib/chat.ts`**: Refactored chat auto-naming logic to:
  - Set the derived title synchronously so the UI updates immediately
  - Spawn a background title upgrade task that overlaps the chat turn (no added latency)
  - Await the upgrade before the generator returns to ensure it survives the request lifetime
  - Only overwrite the derived title if it hasn't been manually changed by the user mid-turn
  
- **New test suite `__tests__/chat-title.test.ts`**: Comprehensive tests for:
  - `deriveTitle()` behavior with various markdown, whitespace, and length edge cases
  - `generateChatTitle()` graceful degradation when credentials are missing

## Notable Implementation Details
- The model-based title generation uses a separate, lightweight model (Claude Haiku) rather than the chat's own model to keep latency sub-second and costs minimal
- Title generation is wrapped in a try-finally block to ensure the upgrade completes within the request lifetime, preventing serverless teardown from interrupting it
- The upgrade only overwrites the title if the stored value still matches the derived title, protecting against clobbering user-initiated renames
- All title generation is best-effort and never throws—failures silently fall back to the deterministic derived title

https://claude.ai/code/session_019A4ELskn887chi1NGfLe5J
