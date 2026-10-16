# Fix resource leaks and security issues in channel flow components

Several channel components had timeout leaks, stale closure bugs, and an insufficient URL scheme check that only blocked `javascript:` rather than using an allowlist.

## MessageInput
- **Stale transport closure**: `handleTyping` was capturing `transport` from the render scope. The 3-second debounce callback could fire with a stale (or missing) transport. Now reads `transportRef.current?.presence` at invocation time; `transport` removed from `useCallback` deps.
- **Object URL leak on unmount**: The cleanup effect used `[]` deps, so `pendingAttachments` was always the empty initial value. Added `pendingAttachmentsRef` kept in sync each render; cleanup reads from the ref.

## MessageList
- **setState after unmount**: Both `scrollToMessage` and the `scroll-to-message` event handler scheduled `setTimeout(() => setHighlightedMessageId(null), 2000)` with no cleanup. Added `highlightTimeoutRef` to track and cancel both the scroll delay and the highlight clear on unmount/channel change.

## ChannelView
- **Typing timeout leak**: The 5-second auto-remove `setTimeout` per typing user was fire-and-forget. Added `typingTimeoutsRef: Map<string, number>` — existing timeouts for the same user are cancelled before rescheduling, and all are cleared in the effect cleanup on unmount or channel switch.

## MarkdownRenderer
- **Scheme allowlist**: Replaced the single `javascript:` block with an `isSafeUrl()` helper using `ALLOWED_URL_SCHEMES = ["http:", "https:", "mailto:"]`. Applied to both `<a href>` clicks and `<img src>` — blocked images render `null` rather than loading a non-allowlisted resource.

```ts
const ALLOWED_URL_SCHEMES = ["http:", "https:", "mailto:"];

function isSafeUrl(url: string | undefined): boolean {
  if (!url) return false;
  try {
    return ALLOWED_URL_SCHEMES.includes(new URL(url).protocol);
  } catch {
    return false;
  }
}
```

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> Create a pull request against `main` in `Leveq/Nodes` to address high-risk issues found in the channel flow components.
> 
> ## Scope
> Update the following files (only as needed to implement the items below):
> - `apps/desktop/src/components/channel/ChannelView.tsx`
> - `apps/desktop/src/components/channel/MessageInput.tsx`
> - `apps/desktop/src/components/channel/MessageList.tsx`
> - `apps/desktop/src/components/channel/MarkdownRenderer.tsx`
> - (Optional/perf) `apps/desktop/src/components/channel/MessageGroup.tsx`
> 
> ## Required fixes
> 
> ### 1) MessageInput typing safety + cleanup correctness
> File: `apps/desktop/src/components/channel/MessageInput.tsx`
> - Fix `handleTyping` to avoid assuming `transport` is nullable/truthy and avoid accessing `transport.presence` when undefined.
>   - Use `transportRef.current?.presence` (or equivalent) for `setTyping` calls.
>   - Ensure the timeout callback also uses the ref, not a stale closure.
> - Fix the “cleanup preview URLs on unmount” effect so it correctly revokes object URLs for the *latest* `pendingAttachments`.
>   - Use a ref to track pending attachments, or include `pendingAttachments` in dependencies with careful revocation logic.
> 
> ### 2) MessageList timeouts: avoid setState-after-unmount
> File: `apps/desktop/src/components/channel/MessageList.tsx`
> - Track and clear `setTimeout` handles used for message highlighting and the search scroll event handler.
>   - Ensure no `setHighlightedMessageId` occurs after unmount.
> 
> ### 3) ChannelView typing timeouts: prevent leaks
> File: `apps/desktop/src/components/channel/ChannelView.tsx`
> - Track the 5-second auto-remove typing timeouts so they can be cleared on unmount/channel switch.
>   - Use a ref of timeout IDs (per typingPublicKey) and clear them in cleanup.
> 
> ### 4) MarkdownRenderer scheme allowlist (desktop hardening)
> File: `apps/desktop/src/components/channel/MarkdownRenderer.tsx`
> - Replace the single `javascript:` block with an allowlist for safe URL schemes.
>   - Allow `http:` and `https:`.
>   - Optionally allow `mailto:` (only if you think it's safe/desired); otherwise block everything else.
> - Apply the same scheme policy to markdown images (`img`) so `src` is also restricted.
>   - For blocked image sources, render nothing or a small placeholder.
> 
> ## Optional perf improvement (nice-to-have)
> File: `apps/desktop/src/components/channel/MessageGroup.tsx`
> - Avoid creating new per-message handler closures on every render if it is straightforward.
>   - If not straightforward without API changes to MessageItem, skip.
> 
> ## Constraints
> - Keep public props/signatures unchanged.
> - No cosmetic refactors beyond what is required for the fixes.
> - Ensure TypeScript types remain correct.
> 
> ## Acceptance criteria
> - No React warnings for state updates after unmount for these components.
> - No runtime errors when transport/presence is temporarily unavailable.
> - Typing-related timeouts are cleared on cleanup.
> - Markdown links/images cannot open non-allowlisted schemes.
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

*This pull request was created from Copilot chat.*
>

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/Leveq/Nodes/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.
