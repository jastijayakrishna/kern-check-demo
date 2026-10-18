# feat: floating always-on-top agent status overlay

## What

A **floating agent-status overlay**: a small frameless, always-on-top window that stays visible over other apps (Chrome, editors, fullscreen Spaces) and shows what your agents are doing at a glance.

- **Collapsed pill** (default): activity-dot counts — amber pulsing = waiting on you (permission/trust prompt), green = actively working, gray = idle, red = exited. Shows `no agents` when empty.
- **Expanded list** (click the pill): one row per agent with activity dot, title, ★ for pinned, a project chip when agents span multiple projects, and the most-actionable right-side text (attention label → provider verb like `running Bash` → activity word).
- **Click a row** → raises Agent Code and focuses that agent's pane (same focus path as the Agent Activity modal).
- Toggled via the command palette: **Floating Agent Status**. Enabled state, window position, and pill/list mode persist across restarts (`~/.config/<app>/agent-overlay.json`).
- **Auto-hides while Agent Code is focused** (the app already shows richer status everywhere); reappears when focus leaves the app. Never steals key focus (`focusable: false`, `showInactive`).

## How

The overlay deliberately does **not** consume session IPC. The main renderer — which already owns all status derivation (`dispatchActivity`, `dispatchAttentionLabelFromConditions`, `sessionTitle`, `buildVisibleDispatchRows`) — publishes a precomputed snapshot (throttled 200ms, deduped on content) over new `agent-overlay:*` channels; main caches and forwards it to the overlay window. Consequences:

- `sendToMainWindow` / the session forwarder / mainWindow.ts's single-window assumption are all untouched — no fan-out refactor.
- The overlay renderer is a dumb display: its whole bundle is **8.5 kB** (second Vite renderer entry, `overlay.html`), sharing `styles.css`, the preload bundle, and the theme via `applyTheme` on an opaque settings pass-through.
- `dispatchActivity` + palette helpers moved from `DispatchAgentList.tsx` into `workspace/dispatch/dispatchActivity.ts` (re-exported for existing importers) so all three surfaces — Dispatch list, mini-list, overlay — share one activity vocabulary.

## Verification

- `tsc -b tsconfig.node.json` and `tsc -b tsconfig.web.json` both clean
- `electron-vite build` passes; `out/renderer/overlay.html` + chunks emitted
- `vitest run`: 481 tests pass. One failing suite (`agent-voice-dictation` submodule `hotkeyBinding.test.ts`, "No test suite found" — it's a `node:test` file) fails identically on `main` at the same submodule SHA; pre-existing and unrelated.
- Not yet runtime-smoked in a live `npm run dev` session (didn't want to fight the state process lock with a running instance); worth a quick manual pass: toggle the command, drag the pill, expand, click a row from Chrome.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
