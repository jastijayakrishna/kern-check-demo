# fix(react): composed ref stability

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary
- add a memoized `useComposedRefs` hook for React ref composition
- replace inline `composeRefs(...)` render calls across React components and the factory `asChild` path
- add regression coverage for stable callback refs in the utility, Field.Textarea, and factory asChild paths

## Tests
- `bun run react test:ci src/utils/compose-refs.test.tsx src/components/field/field.test.tsx src/components/factory.test.tsx`
- `bun run react typecheck`
- `bun run react lint`
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-6f454c92-cb6a-4c96-baa2-1b57b03086ec"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-6f454c92-cb6a-4c96-baa2-1b57b03086ec"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
