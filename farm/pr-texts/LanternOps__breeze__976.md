# fix: ensure UTF-8 in terminal and process output

## Fix mojibake (`�`) in terminal and process output

### Problem

Accented characters (`é è à ç …`) and other non-ASCII bytes render as `�`
in the web UI — in the remote terminal (xterm.js), and also in script
execution history and user-context command results. Most visible on
French/Windows hosts and on Linux services running with `LANG=C`.

### Root cause

Two independent failures stack on every process-output path:

1. **Source not UTF-8.** Spawned processes inherit a non-UTF-8 locale:
   `LANG=C` on minimal/systemd environments, an OEM code page (CP850/CP1252,
   etc.) on Windows — e.g. `é` = `0x82`.
2. **JSON transport corruption.** Raw bytes were converted via `string(...)`
   before `json.Marshal`. Go's JSON encoder replaces every invalid-UTF-8
   byte with `U+FFFD`, so even a later locale fix can't recover bytes already
   mangled in transit.

Both layers are needed: UTF-8 at the source for correct text, byte-safe
handling so JSON never corrupts non-UTF-8 sequences.

### Fix

A shared `agent/internal/procoutput` package centralizes both layers and is
reused everywhere a process is spawned and its output captured:

- **`ApplyEnv`** — forces `LANG/LC_ALL/LC_CTYPE=C.UTF-8` when the locale is
  not already UTF-8 (no-op for `*.UTF-8` locales).
- **`BytesToUTF8`** — passthrough when bytes are already valid UTF-8;
  otherwise, on Windows, transcodes from the **actual active code page**
  (queried at runtime via `GetConsoleOutputCP`, falling back to `GetOEMCP`)
  mapped to the matching `charmap` decoder. Unmapped pages fall back
  gracefully. Unix path is a pure passthrough.
- **`WindowsScriptCommand`** — UTF-8 console bootstrap (`chcp 65001` /
  PowerShell encoding) for shell-wrapped commands.

**Terminal flow (PTY → xterm).** Because xterm consumes raw bytes (ANSI,
binary), terminal output is sent base64-encoded — but **negotiated**, not
unconditional, to avoid any deploy-order regression. The API advertises a
`capabilities` array in the existing `connected` handshake
(`terminal_output_base64`); the agent only emits base64 if that capability
was advertised, otherwise falls back to plain text. The flag resets on
(re)connect.

**Non-terminal flows (script history, winget / user-context exec, software
install).** These are plain text displayed in the UI, so no base64 and no
negotiation: the agent simply guarantees valid UTF-8 via `procoutput` before
JSON. No API schema change, no deploy-order coupling.

### Compatibility

Terminal base64 negotiation:

| Scenario              | Behavior                                          |
|-----------------------|---------------------------------------------------|
| old agent + new API   | no base64 sent → passthrough (unchanged)          |
| new agent + old API   | no capability advertised → plain text, no garbage |
| new agent + new API   | base64 round-trip                                 |
| reconnect             | flag reset until next `connected`                 |

Deployment order between agent and API no longer matters. The non-terminal
paths carry no compatibility concern (plain UTF-8 strings throughout).

### Note for reviewers

Previously the agent silently dropped the `connected` message in `readPump`
(no `id` field). It now parses it to read `capabilities`. Behavioral change,
but no risk — nothing relied on the message being discarded.

### Files

| File | Change |
|------|--------|
| `agent/internal/procoutput/*` | New package: `ApplyEnv`, `BytesToUTF8` (runtime code-page detection), `WindowsScriptCommand` |
| `agent/internal/terminal/terminal_env.go` | Delegates to `procoutput.ApplyEnv` (terminal behavior unchanged) |
| `agent/internal/terminal/pty_{unix,darwin,darwin_nocgo,windows}.go` | env + shell bootstrap |
| `agent/internal/websocket/client.go` | base64 transport + capability gating + reset |
| `agent/internal/executor/executor.go` | env + Windows bootstrap + safe capture |
| `agent/internal/userhelper/client.go` | exec/winget: env + safe capture |
| `agent/internal/scripts/runner.go` | env + Windows bootstrap + safe capture |
| `agent/internal/remote/tools/software_install.go` | env + safe capture on installer output |
| `apps/api/src/routes/agentWs.ts` | advertise capability, decode base64 |

### Tests

- `procoutput`: valid-UTF-8 passthrough; CP850/CP1252/CP866 → correct UTF-8
  (proves it's not hardcoded to Western pages); unmapped code page falls back
  gracefully; `ApplyEnv`.
- Per-site accented-output capture tests (`executor`, `scripts`,
  `userhelper`).
- Terminal: capability parsed → base64; capability absent → plain text;
  handshake parsing; capability reset on reconnect.
- API: `connected` advertises `terminal_output_base64`; base64 decode path.
- `go test ./internal/...`, `vitest agentWs.test.ts`, API lint — all green.

---

*Draft:* opening for early feedback on the capability/handshake approach
before finalizing.
