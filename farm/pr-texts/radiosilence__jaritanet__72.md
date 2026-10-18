# fix(exits): config ergonomics — auto-port, oldboy, exit-direct picker, docs

Follow-up polish on the exit nodes (#70) — makes the config sane and the picker/profile readable.

## Changes
- **Picker clarity:** `exit-select`'s "direct" option is now **`exit-direct`** (a thin alias for `entry-select`) instead of literally showing `entry-select` in the exit list. Reads as an egress choice, parallel to `exit-oldboy`. (Avoids the tag `direct` — reserved by sing-box for its bypass outbound.)
- **Auto-port:** `port` is now **optional**, deterministically derived from the exit name (djb2 → 20000–29999) and used identically everywhere (gateway bind / ss server / rathole client / client outbound). Uniqueness asserted at deploy; explicit override still works. No more hand-picking plumbing ports.
- **`home` → `oldboy`:** the name is cosmetic (picker tag + resource names); `substrate` (default `k8s` = the one home cluster) is what decides *where* it runs. Documented so it's no longer "undocumentable."
- **Bug fix:** route `final` used a hardcoded `exit-select`, which dangles when no exits are configured — now falls back to `entry-select` via `finalOutbound`.
- **Docs:** rewrote the E2E architecture diagram (the old one was wrong — showed tailnet as xray-only and entry-select wired straight to egresses). New one: gateway = hub, entry = protocol, exit = where the gateway forwards. Added a **README topology config reference** (`gateway`/`exits`/`edges`, substrate = where-it-runs) and a **commented VPS-exit example**.

## Deploy note
Renaming `home` → `oldboy` **replaces** the exit's k8s + rathole resources (`exit-home` → `exit-oldboy`) and shifts its loopback port to the derived value — a brief exit recreation + one profile update/notify on deploy. Expected, one-time.

## Verify
typecheck / lint 0-0 / tests green. `buildProfile` structure-tested with **and without** exits (correct `entry-select`/`exit-direct`/`exit-select`; no-exits falls back to `entry-select`, no dangling tags). Generated profile eyeballed for readability.

Next up (separate PRs): full architecture-diagram rewrite, then Oracle Cloud cleanup.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
