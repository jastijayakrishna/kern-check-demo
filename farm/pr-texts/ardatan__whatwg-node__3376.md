# Fix duplicate `transfer-encoding: chunked` header when using uWebSockets.js

- [x] Investigate the issue: `transfer-encoding: chunked` being duplicated when using uWebSockets.js with streaming responses
- [x] Fix `sendResponseToUwsOpts` in `packages/server/src/uwebsockets.ts` to skip `transfer-encoding` header (uWebSockets.js adds it automatically)
- [x] Add unit tests verifying the fix (both non-streaming and streaming response cases)
- [x] Fix CI: add missing `onData` method to mock `UWSResponse` in test to satisfy TypeScript type check
- [x] Merge master and resolve conflicts (`package-lock.json`)
- [x] Add changeset (`.changeset/fix-uws-duplicate-transfer-encoding.md`)
- [x] Add integration test in `node.spec.ts` using raw `http.request` to confirm `transfer-encoding: chunked` appears exactly once in a real uWS streaming response (proving uWS adds it automatically after our filtering)
- [x] All tests pass (8/8), TypeScript check clean
