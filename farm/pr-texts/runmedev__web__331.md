# Update WebMCP registration to current spec

## Summary

- register tools through the current `document.modelContext` WebMCP API
- retain `navigator.modelContext` as a compatibility fallback for earlier implementations
- observe asynchronous `registerTool` failures and update the design documentation

## Verification

- `pnpm -C app exec vitest run src/components/WebMcp/WebMcpToolRegistrationHost.test.tsx`
- `runme run build test`
- opened `http://localhost:5173` in the ChatGPT in-app browser
- verified all nine Runme WebMCP tools were registered
- successfully invoked the read-only `listDocumentation` tool through WebMCP
