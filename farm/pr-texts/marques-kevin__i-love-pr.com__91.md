# feat: add joyful customize FAB pinned to dashboard window

## Summary

Implements the UX lock from #86: replaces the in-flow subtitle and Customize/Done/Add chart toolbar with a floating action button pinned to the dashboard window.

## Changes

- Remove subtitle and in-flow Customize / Done / Add chart buttons from `custom_dashboard.tsx`
- Add `CustomizeFab` pinned inside `.dashboard-window` (absolute, bottom-right, z-20)
- Idle: round primary FAB with Edit02 icon → enters edit mode
- Edit: morphs into horizontal speed-dial (Add + Done) with motion/react spring animations
- Scroll body gets `pb-20` / `scroll-pb-20` so last card clears the FAB
- Empty state keeps in-flow Add chart CTA; FAB visible on empty dashboards too
- `useReducedMotion`: instant show/hide and icon swap
- Remove unused `dashboard.subtitle*` i18n keys

## Test plan

- [x] `npm run check` passes locally
- [x] FAB stays pinned while scrolling
- [x] Customize → edit morph (Add + Done)
- [x] Add opens picker modal
- [x] Done exits edit mode
- [x] Empty state Add chart still works

Closes #86

<div><a href="https://cursor.com/agents/bc-6ab9a67d-48ac-4964-aa0e-be46eac12660?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/automations/09f675ba-942a-11f1-ba66-0e7d0216e441"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/view-automation-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/view-automation-light.png"><img alt="View Automation" width="141" height="28" src="https://cursor.com/assets/images/view-automation-dark.png"></picture></a>&nbsp;</div>


