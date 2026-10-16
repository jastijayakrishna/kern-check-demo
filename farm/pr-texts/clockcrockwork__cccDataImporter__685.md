# Add URL safety/sanitization, refactor HTTP calls, and improve error handling in aliceBlogChecker

### Motivation
- Harden feed processing by preventing SSRF/private-host requests and removing raw `fetch` usage for Discord and external APIs. 
- Improve error sanitization so sensitive data (URLs, UUIDs) are redacted from logs and notifications. 
- Make the module testable and reusable by exporting main functions and moving HTTP helpers into a shared wrapper. 

### Description
- Added URL safety checks and sanitization utilities: `sanitizeText`, `toErrorMessage`, `isPrivateOrLocalAddress`, and `assertSafeUrl`, and new constant `DISCORD_MAX_CONTENT_LENGTH`.
- Replaced raw `fetch` calls with shared helpers `fetchWithRetry` and `postDiscordOrThrow` imported via a new `packages/common/httpClient.cjs` lazy wrapper, and added safe posting in `handleError`, `postToDiscord`, and `postRandomImageToDiscord`.
- Improved date parsing with a reusable `parseFeedDate` function using `luxon` and centralized feed-processing error handling; removed fragile inline date parsing logic.
- Added `net` import to detect IP addresses, removed unused `fs`, adjusted HTML-to-text call to `htmlToText.convert`, and made `aliceBlogChecker` export its functions with a `require.main === module` guard for CLI invocation.
- Strengthened feed processing: validate feed and webhook URLs with `assertSafeUrl`, skip invalid/unsafe entries, and ensure feeds with no entries raise handled errors.

### Testing
- Unit tests updated and run with `jest` covering `parseFeedDate`, use of http client helpers, resilient feed processing when one feed fails, handling of unsafe feed URLs, and error webhook content including redacted feed URL; all tests passed.
- Tests mock `feedparser-promised`, Supabase client, and `../../common/httpClient.cjs` helpers to assert behavior without real network requests, and the suite completed successfully.

------
[Codex Task](https://chatgpt.com/codex/tasks/task_e_69bb5ee494c883248121af1ae9e36ae2)
