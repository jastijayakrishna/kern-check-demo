# Smoother mobile page transitions

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
Mobile route changes previously popped: the old page vanished immediately, the enter animation often played *behind* the closing nav sheet, and there was no exit motion.

This coordinates the two motions and uses a calmer fade-and-lift:

- **Nav sheet:** after a tap, the selection highlight can register, then the drawer eases closed over an already-painted destination (the sheet close *is* the transition).
- **Other mobile navigations:** View Transitions crossfade the outgoing page out and the incoming page in, with a slightly longer fluid curve and a bit more travel than desktop. Sidebar and the mobile top bar stay still.
- Browsers without View Transitions keep the CSS enter animation. `prefers-reduced-motion` still disables the motion.

Unmount cleanup now also removes `data-page-reveal` from `<html>`. Clearing only the 720ms timer would have left that flag in place and permanently suppressed later page transitions.

No API or routing changes.
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-217968e4-d173-4d7e-9e44-d13927ce5291?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-217968e4-d173-4d7e-9e44-d13927ce5291&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>


