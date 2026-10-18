# Remote mobile: 1:1 feed parity, real desktop chrome, voice dictation

Rebuilds the remote mobile client so the transcript is a real 1:1 of the desktop feed (properly padded/responsive), the chrome is the **actual desktop components** rather than hand-rolled knockoffs, and the composer gains **voice dictation with a tap mic button**.

Spec: `docs/superpowers/specs/2026-07-08-remote-mobile-feed-rewrite-design.md`
Plan: `docs/superpowers/plans/2026-07-08-remote-mobile-feed-rewrite.md`

## What changed (7 tasks)

1. **Responsive feed + the real "no padding" root cause.** `renderer/styles.css` only `@source`'d `src/providers`/`src/shared`, so the phone's Tailwind build **never emitted `Feed.tsx`'s own container classes** — that (not the values) is why the phone had no padding. Added `@source "../../../src/renderer"` (additive/no-op for desktop) and made `Feed.tsx:997` a container-query container (`@container` + `@min-[480/768px]` steps; the wide step equals the historical desktop classes verbatim, so wide output is unchanged and narrow desktop tiles improve too).
2. **Approvals via the real `ConditionOutlet`** — replaced the hand-rolled tap-bar with the generic `conditions-core/ConditionOutlet` + the provider `conditionViews` registry and a structured phone dispatch (`pty→replyWithPtyAction`, `custom→resolveCondition`). No wire changes.
3. **Real `PaneHeader`** title strip (provider badge + shortened cwd), cwd self-subscribed in SessionView.
4. **Real `ComposerInput` shell** driven by a thin phone controller (Enter/Shift+Enter/Esc). Slash picker + image paste inert (out of scope — need wire widening); prompt-history dropped (no arrow keys on touch).
5. **Token-gated `POST /dictate`** reusing the desktop Deepgram batch engine via an injected `transcribeAudio` dep — the API key never leaves the main process. Auth mirrors the `/ws` upgrade exactly; audio is transcribe-and-discard.
6. **Voice dictation + tap mic button.** A `MediaRecorder` capture (rolled inline — the `agent-voice-dictation` main entry re-exports a Node-only streaming client that can't bundle in a browser) POSTs to `/dictate` and appends the `<stt>`-wrapped transcript. The desktop starts dictation from the Fn hotkey, which a phone lacks, so an explicit mic button is the phone's entry point.
7. **CSS polish** — composer/mic styling, restored the iOS 16px anti-zoom floor over the mounted 12px desktop textarea, pruned dead tap-bar selectors, fixed the `PairScreen` `borderRadius` contract leak.

## Verification
- ✅ `tsc --noEmit -p tsconfig.web.json` clean, `tsc -b tsconfig.node.json` clean, `npm run client:build` succeeds on every task.
- ✅ Confirmed the container-query rules actually emit into the phone CSS (they didn't before the `@source` fix), and that the node-only STT package stays out of the browser bundle.
- ⚠️ **Not machine-verified (needs a real paired phone):** on-device feed padding/legibility, approvals resolving via the real views, and the dictation round-trip (mic permission → record → `/dictate` → transcript append). Recommend a device smoke test before merge.

## Out of scope (deferred, by design)
Slash-command picker + image paste (need wire-protocol widening), related-agent chips (no sub-agent data over v1 wire), terminal panes, streaming dictation preview.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

