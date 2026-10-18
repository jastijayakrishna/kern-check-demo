# Animate ping test-mode tab switching

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary
Adds a sliding selection chip to the `/ping` test-mode control (TCP / UDP / EB / Database), following the same motion pattern as the sidebar highlight.

- The active background **slides** between buttons instead of popping on/off, including the 2×2 mobile layout.
- Helper copy **cross-fades** with the selected mode.
- Database-only fields still appear with a short enter animation.
- Motion is compositor-driven (`transform` / opacity) and respects `prefers-reduced-motion`.

[ping-mode-switch-animation.mp4](https://cursor.com/agents/bc-34b3487a-e546-4bac-a6e9-4bf6f200d47a/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fping-mode-switch-animation.mp4)

## Test plan
- [x] Open `/ping` and switch TCP → UDP → EB → Database: the chip should travel, not blink.
- [x] Confirm helper text updates with a short fade and that port defaults still change with the mode.
- [x] Resize below/`sm`: switching should slide vertically/diagonally in the 2×2 grid.
- [x] Keyboard: arrow keys still move the tab selection.
- [x] `prefers-reduced-motion: reduce` should skip the slide.


<sub>To show artifacts inline, <a href="https://cursor.com/dashboard/cloud-agents#my-pull-requests">enable</a> in settings.</sub>
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-34b3487a-e546-4bac-a6e9-4bf6f200d47a?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-34b3487a-e546-4bac-a6e9-4bf6f200d47a&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>


