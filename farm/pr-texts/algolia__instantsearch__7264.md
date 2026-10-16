# feat(result-card): minimize instead of dismiss

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
**Summary**

Follow-up to #7243 ([review comment](https://github.com/algolia/instantsearch/pull/7243#discussion_r4123051313)): the Result Card close button becomes a minimize/maximize toggle, like the Chat header. Generation keeps running while minimized, and the state persists across queries. `dismiss()` is removed from `connectResultCard`.

**Result**

Result Card unit and common tests pass; `yarn type-check` and lint pass.

[Result Card expanded and minimized](https://cursor.com/agents/bc-c0a83a6c-9c5f-46e7-a790-626716df1ef0/artifacts?path=%2Fcursor%2Fstores%2Fbc-c0a83a6c-9c5f-46e7-a790-626716df1ef0%2Fmedia%2Fresult-card-minimize.png)

<sub>To show artifacts inline, <a href="https://cursor.com/dashboard/cloud-agents#team-pull-requests">enable</a> in settings.</sub>
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-e87ac8b0-203f-5ae7-9077-be93e228bd8d?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-e87ac8b0-203f-5ae7-9077-be93e228bd8d&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
