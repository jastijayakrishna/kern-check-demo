# fix: resolve locked blueprint divergences

## Summary

Resolves the locked blueprint/code divergences selected in the 13-item audit.

- Remove Basic Attack auto-facing/soft-target behavior.
- Allow movement during Basic Attack startup and recovery; lock movement only during the active-hit window.
- Move World Chat persistence and delivery to Supabase using RLS, RPC, and Realtime.
- Make the server authoritative for sender identity and timestamps.
- Add message validation and a 10-messages-per-minute throttle.
- Keep Monkey King S3 and sprite-direction handling as documented mock/deferred work.
- Synchronize Blueprint, Agent Blueprint, TASKS, MEMORY, and SECURITY documentation.

## Why

The shipped runtime contradicted the locked control and authority decisions: Basic Attack could rotate toward enemies automatically, combo movement was locked for the full action, and World Chat was client-only through localStorage/BroadcastChannel.

## Validation

- Full CI passed.
- 86 test files passed.
- 698/698 tests passed.
- Typecheck passed.
- Lint passed.
- Production build passed.
- Bundle-size gate passed.
- Remote compare confirms this branch is exactly 1 commit ahead of master and 0 commits behind.

## Deployment note

The Supabase migration `20260808180354_world_chat_server_authority.sql` is included but has not been applied to production automatically. Apply it through the normal migration deployment flow after review/merge.
