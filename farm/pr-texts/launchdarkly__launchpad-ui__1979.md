# fix(components): cap default Modal height so tall dialogs scroll

## Summary

Reported in #cringe: the flag templates edit modal in gonfalon (Project settings → Flag settings → edit a template) renders taller than the viewport, and neither the header nor the footer (Save/Cancel) is reachable — nothing scrolls.

The cause is in `Modal.module.css`, not the consumer. `[slot='body']` already has `overflow: auto; flex: 1`, but that only produces a scroll container if the dialog's height is bounded, and the default modal variant has no height constraint — so it grows to its content height inside the vertically-centered `.overlay` and spills off both ends.

Adding `max-height` alone is not enough: with `.base` laid out as a block, the dialog's `height: 100%` resolves against an auto-height parent (max-height doesn't make it definite), so the dialog still overflows the clamped modal. So this change does three things:

```diff
 .base {
+	display: flex;
+	flex-direction: column;

 	& [role='dialog']:has([slot='body']) {
-		height: 100%;
+		flex: 1;
+		min-height: 0;
 	}

 	& [slot='body'] {
 		overflow: auto;
 		flex: 1;
+		min-height: 0;
 	}
 }

 .default {
+	max-height: calc(100% - var(--lp-size-64));
 }
```

The cap lives on `.default` rather than `.base` so the `drawer` variant — already bounded by `position: fixed; top: 0; bottom: 0` — keeps its full-height layout. Consumers that currently work around this by setting their own `max-height: 90vh` (several in gonfalon) keep working; theirs simply wins over the default cap.

## Screenshots (if appropriate):

New `Long Content` story, viewport ~990px tall.

Before — header, footer, and both ends of the body are off screen with no scroll:

![Modal before](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmdfaGVBMWRpc2owVHVLd2VVSyIsInVzZXJfaWQiOm51bGwsImJ1Y2tldF9uYW1lIjoiZGV2aW5hdHRhY2htZW50cyIsImJ1Y2tldF9rZXkiOiJhdHRhY2htZW50c19wcml2YXRlL29yZ19oZUExZGlzajBUdUt3ZVVLLzFiNjc3ODk1LTEyMGMtNDcwOC05NjhjLTMzNDQwZTE2OWY1NyIsImlhdCI6MTc4NTk1OTE1NiwiZXhwIjoxNzg2NTYzOTU2LCJmaWxlbmFtZSI6Im1vZGFsLWJlZm9yZS5wbmcifQ.FUeo14rXfRdIBHWZKGQ03U7dMRq_lnDqgEDUpupOszA)

After — modal capped to the viewport, body scrolls, header and footer stay put:

![Modal after](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmdfaGVBMWRpc2owVHVLd2VVSyIsInVzZXJfaWQiOm51bGwsImJ1Y2tldF9uYW1lIjoiZGV2aW5hdHRhY2htZW50cyIsImJ1Y2tldF9rZXkiOiJhdHRhY2htZW50c19wcml2YXRlL29yZ19oZUExZGlzajBUdUt3ZVVLLzhkYzQ2M2IzLWM2MWYtNGY1ZC04ZDA5LTZkMjEzZDM4MmRhMCIsImlhdCI6MTc4NTk1OTE1NiwiZXhwIjoxNzg2NTYzOTU2LCJmaWxlbmFtZSI6Im1vZGFsLWFmdGVyLnBuZyJ9.16mtXnzHtLJQZdW-JUaH6X4jsQJGMUIw20THFZt0_QA)

## Testing approaches

- Added the `Long Content` story (also snapshot in Chromatic's mobile mode) so this regression is covered visually going forward.
- Manually verified in Storybook that `Example`, `With Header`, and `Drawer` are unchanged, and that the drawer still fills the viewport height with its footer pinned.
- `pnpm vitest run packages/components/__tests__/Modal.spec.tsx`, `pnpm oxlint:js`, `pnpm lint:css:path`, and `pnpm fmt:check` all pass.
- Chromatic will show diffs for the modal stories — expected, since anything taller than the viewport now scrolls instead of overflowing.

Reported by @stasquatch.


Link to Devin session: https://app.devin.ai/sessions/5b24f25ecbec49129be72e26ed3b9c4e

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> CSS-only layout fix scoped to the default Modal variant; drawer behavior is explicitly preserved and the change is covered by a new visual story.
> 
> **Overview**
> Fixes tall **default** `Modal` dialogs growing past the viewport so header, footer, and body content become unreachable with no scroll.
> 
> **`Modal.module.css`** makes `.base` a flex column, caps **`.default`** with `max-height: calc(100% - var(--lp-size-64))`, and swaps dialog `height: 100%` for `flex: 1` plus `min-height: 0` on the dialog and `[slot='body']` so the body slot scrolls while header and footer st
