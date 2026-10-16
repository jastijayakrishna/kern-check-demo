# feat: implement launchMiniappTool for Base miniapp delivery via XMTP

# feat: implement launchMiniappTool for Base miniapp delivery via XMTP

## Summary

Adds a new `launchMiniappTool` that enables Hybrid agents to launch Base miniapps by sending their URLs via XMTP messages. This addresses **HYBRID-48** and provides the foundation for agents to deliver miniapps through conversational interfaces.

**Key Changes:**
- Creates `packages/core/src/tools/miniapp.ts` with `launchMiniappTool` following existing tool patterns  
- Tool accepts `miniappUrl` (with URL validation) and optional `message` text
- Sends content via XMTP using `runtime.conversation.send()` method
- Includes comprehensive error handling, logging, and performance timing
- Exports the tool in `packages/core/src/tools/index.ts`

The implementation closely follows the `sendMessageTool` pattern for consistency with the existing codebase. Miniapp URLs are sent as regular text messages initially - Base-specific validation and custom content types can be added in future iterations.

## Review & Testing Checklist for Human

**Critical items to verify (3):**

- [ ] **End-to-end functionality**: Create a test agent that uses `launchMiniappTool` and verify miniapp URLs are actually sent via XMTP and received correctly
- [ ] **URL validation works**: Test that the tool properly validates URLs and rejects invalid inputs (empty strings, malformed URLs, etc.)
- [ ] **Message formatting**: Send a miniapp URL with optional message text and confirm the formatting looks good on the recipient side (message + double newline + URL)

### Notes

- Tool treats miniapp URLs as regular text messages (no custom XMTP content types) to keep implementation simple as requested
- No Base-specific URL validation implemented yet - accepts any valid URL format  
- All verification commands passed: `pnpm typecheck`, `pnpm lint`, and `pnpm build` completed successfully
- Requested by Ian (@ian) - Link to Devin run: https://app.devin.ai/sessions/3b445d1e7e194b11a7507e7a5b43bdcf
    
<!-- This is an auto-generated description by cubic. -->
---

## Summary by cubic
Implements launchMiniappTool to let agents deliver Base miniapps by sending their URLs over XMTP. Addresses HYBRID-48 and enables simple, validated miniapp launch from chat.

- **New Features**
  - Added launchMiniappTool in packages/core/src/tools/miniapp.ts.
  - Validates miniappUrl (zod) and supports optional message; content = message + double newline + URL.
  - Sends via XMTP using runtime.conversation.send and returns success, messageId, content, error.
  - Exported in packages/core/src/tools/index.ts with logging, timing, and error handling.

<!-- End of auto-generated description by cubic. -->
