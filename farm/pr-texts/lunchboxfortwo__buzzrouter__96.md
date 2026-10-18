# Address the channel handoff to the channel Buzz actually created

## Root cause

`createDedicatedChannel` reached `created` and stopped on all three live runs. **The roster was never the problem.** The kind-13534 event lists owner `5253698c…` and admin `9527ffa5…`, and `resolveChannelOwner` picked the owner correctly — it is on all three journaled rows.

The `h` tag was. Buzz parses it with `val.parse::<Uuid>()` (`buzz-relay/src/handlers/ingest.rs`, `extract_channel_id`) and silently drops anything that is not a UUID. `deriveChannelId` emitted a slug — `channel-15ffe2aa-…-c42c73b3` — so:

- **kind 9007** tolerates a missing `h` (it is excluded from `requires_h_channel_scope`), so the create was accepted and the relay minted its own `gen_random_uuid()`. The channel was created under an id we never learned.
- **kind 9000** *is* in `requires_h_channel_scope`, so it was refused `invalid: channel-scoped events must include an h tag`.

### Evidence

| Source | What it shows |
|---|---|
| `channels` on the relay | `a7c48ca2-…` and `992916c4-…`, `nip29_group_id` **NULL**. Our slug appears nowhere on the relay. |
| `channel_members` | Only the bridge `b2e4ab88…`, role `owner`. The promote never landed. |
| Relay log | 9007 `NIP-29 CREATE_GROUP processed` + `Event ingested`; **no 9000 line at all**. |
| Handoff journal | created→error in **77 ms** — an immediate OK:false, not a timeout. |
| kind 13534 | `["member","5253698c…","owner"]`, `["member","9527ffa5…","admin"]` — roster healthy, and community-wide (no `d`/`h` scope tag). |

## A second, silent bug this would have exposed

Fixing only the `h` tag would have traded a loud failure for a silent one. Buzz reads the role from a dedicated `["role", …]` tag, **not** NIP-29's `["p", pubkey, role]` third slot (`validate_admin_event` and `handle_put_user` both call `extract_tag_value(event, "role")`). An absent `role` tag means "no role change", which lands a *new* member at `member`. The promote would have OK'd, the bridge would have demoted itself, and **the channel would have been left with no owner.** Both tags are now sent.

## Why it shipped

The test double accepted anything, and the assertions encoded the broken shape. It now enforces both relay rules and records the roles the relay would really have stored. Reverting either fix fails it — verified:

- revert the UUID → 3 tests fail with the exact production string `invalid: channel-scoped events must include an h tag`
- revert the `role` tag → the owner is recorded as `member` instead of `owner`

## Second reported bug: `Unexpected token '<'`

The client called `response.json()` before checking `response.ok`, so a Cloudflare HTML error page surfaced as a JSON parser complaint instead of the real failure. It now reads the body defensively and names the actual HTTP status (with specific wording for 504/524).

I took the "make the client tolerate a non-JSON response" option rather than restructuring the handoff into a background job — it is the surgical change, and the stalls were in fact fast failures (77 ms), not long-running requests.

## Verification

- `npm run typecheck` — clean
- `npm test` — 620 passed (run against a scratch Postgres so the 5 DB-backed integration files actually execute rather than silently skipping)
- `npm run build`, then `e2e/shared-channel-signer-free.spec.ts` — passed

## Not done deliberately

The three stalled production rows were **not** retried — resuming may well succeed now and would have masked the defect. They still need cleanup: the two orphaned relay channels (`a7c48ca2-…`, `992916c4-…`) are bridge-owned under ids BuzzRouter has no record of, so they cannot be resumed through the journal and should be deleted relay-side before the job re-provisions.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01GMAEvM5zBNvpw7KywwqTe7

