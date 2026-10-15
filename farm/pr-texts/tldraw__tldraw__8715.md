# feat(examples): add native flex layout shape example

Partially inspired by customer request, partially to showcase new framelike behavior, this example adds a drag-and-droppable container that uses native css flexbox as the layout engine. 

https://github.com/user-attachments/assets/508d8f8e-bb33-45f1-b9e9-87c1d18d5b63


### Change type

- [ ] `bugfix`
- [ ] `improvement`
- [x] `feature`
- [ ] `api`
- [ ] `other`

### Test plan

1. Open the flex layout example.
2. Select the frame background and use the contextual toolbar to toggle horizontal/vertical layout.
3. Drag the outside green rectangle into the layout and verify the hint/drop line, pointer-up reparenting, and growth.
4. Drag a child out and verify it deparents and the layout shrinks during mouse move before pointer-up.

- [ ] Unit tests
- [ ] End to end tests

### Release notes

- Added a flex layout custom shape example.

<sub>To show artifacts inline, <a href="https://cursor.com/dashboard/cloud-agents#team-pull-requests">enable</a> in settings.</sub>
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-d6af83b5-a09f-4f7a-abc7-0a597d9d6e13"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-d6af83b5-a09f-4f7a-abc7-0a597d9d6e13"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
