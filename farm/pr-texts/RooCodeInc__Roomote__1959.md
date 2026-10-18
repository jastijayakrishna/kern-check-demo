# [Fix] Recover Fast sessions orphaned during quiet retries

## Why this PR exists

- [x] I am a maintainer / this is internal Roomote work

## What changed

- Persist a hidden canonical retry marker as soon as Fast enters retry recovery.
- Keep short retries quiet on the user-facing surface while preserving enough durable state to recover an orphaned turn.
- Retire the marker on successful recovery and let expired-lease reconciliation turn abandoned markers into terminal closeouts.

The quiet-retry window previously suppressed both the user-facing notice and its canonical persistence. If the turn owner disappeared during that window, the Session retained its prompt and tool activity but had no durable retry marker or terminal assistant event for reconciliation to repair.

## How it was tested

- Fast service and conversation repository tests: 123 passed.
- Scheduled Session reconciliation tests: 7 passed.
- `pnpm lint:fast`, `pnpm check-types:fast`, and `pnpm knip` passed.
- Controlled smoke: forced a retryable provider outage through the real Fast/OpenCode path, hard-killed the turn owner while the retry marker was still hidden, expired the responding lease, and ran the real scheduled reconciliation function. The same marker became a visible inactive closeout, and the local Session UI showed a terminal interruption with `ready` status instead of an orphaned turn.

## Checklist

- [x] The PR title follows the repository convention.
- [x] This PR is small and scoped to one change.
- [x] Lint and type checks pass locally.
- [x] Tests and manual validation are included above.
- [x] No secrets, private data, or customer details are included.
