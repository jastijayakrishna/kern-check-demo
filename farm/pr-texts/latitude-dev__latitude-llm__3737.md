# feat(web): replace Annotations tab with Scores tab in trace/session drawers

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Fixes #3692 by replacing the Annotations tab in trace and session detail drawers with a **Scores** tab that lists every score source (`annotation`, `custom`, `evaluation`).

- Adds `listTraceScores` / `listScoresBySession` domain + web server functions (no `source` filter)
- Annotation scores keep full create/edit UX via existing `AnnotationCard`
- Custom/evaluation scores render as read-only cards with source badge, verdict, feedback, and linked signal
- Legacy URL params `detailTab=annotations` / `sessionTab=annotations` normalize to `scores`

## Test plan

- [ ] Open a trace with API-ingested custom/evaluation scores and confirm they appear under Scores
- [ ] Create/edit an annotation from the Scores tab and verify it still works
- [ ] Open a multi-trace session and confirm scores from all traces are listed with trace labels
- [ ] Verify clicking an annotation score still navigates to the conversation anchor
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-873dc96f-e266-4600-a9dd-7b2f77dc5f1f"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-873dc96f-e266-4600-a9dd-7b2f77dc5f1f"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
