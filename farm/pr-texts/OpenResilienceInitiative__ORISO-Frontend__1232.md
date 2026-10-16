# fix(registration): show the locale-aware title for a preselected topic

## Summary
- Part of #1154 (slice 2 of 3). Stacked on the Weblate-bundle-wins PR.
- `TopicSelection` already used `getRegistrationTopicDisplay()`. `PreselectedTopic` still rendered the German API `titles.long`, so a direct registration link stayed German after a language switch.

## Test plan
- [ ] `npx vitest run --project unit src/components/registration/preselectionBox/PreselectedTopic.test.tsx`
- [ ] Open a registration URL with a preselected topic, switch to French, confirm the summary title is French not German

Verified: local only.


Made with [Cursor](https://cursor.com)
