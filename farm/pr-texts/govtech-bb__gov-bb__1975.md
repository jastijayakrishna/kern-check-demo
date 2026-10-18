# feat(chat): rate-limit the public /api/chat endpoint (#1972)

## What
Adds a per-IP request limiter to the public `POST /api/chat` endpoint. Requests
beyond `CHAT_RATE_LIMIT` (default 20) per 60-second window per client IP get a
`429` + `Retry-After` **before** any body parse, RAG lookup, or Bedrock call.

Closes #1972.

## Why
The endpoint is public and unauthenticated, and every request triggers a RAG
retrieval + a **paid Bedrock inference**. With no app-level limit, a simple
script could run up cost or exhaust the service — protection depended entirely
on a WAF rule that may not exist in every environment.

## How
- In-process, per-IP **fixed-window** limiter — reproduces the convention already
  used by `apps/form_builder_api` (`express-rate-limit`) and `apps/api`
  (`@nestjs/throttler`). Those libraries are framework-coupled (Express / Nest)
  and can't run in the chat app's TanStack Start web-standard handler, so the
  *policy* is reused, not the literal library.
- Defense-in-depth **alongside** the WAF, not a replacement. Per-process buckets
  (same as the existing limiters); documented per-instance caveat + Redis upgrade
  path.
- Client IP is best-effort from `x-forwarded-for`; **not logged** (PII).
- Tunable via `CHAT_RATE_LIMIT` (documented in `apps/chat/.env.example`); default
  20/min — tighter than the builder API's 120 because chat is public and each
  call costs a model inference.

## Verification
- New unit tests **6/6** (`node:test`); full chat suite **166 pass / 0 fail**
  (7 pre-existing skips); `chat:build` succeeds.
- Pure in-process logic, so no live-URL check — the unit tests are the
  verification.

## Files
- `apps/chat/src/lib/chat/rate-limit.ts` (+ `.test.ts`)
- `apps/chat/src/routes/api.chat.ts`, `config/env.ts`, `.env.example`

🤖 Generated with [Claude Code](https://claude.com/claude-code)
