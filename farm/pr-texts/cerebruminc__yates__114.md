# fix: sanitize all hyphens in slug generation

## Summary
- sanitize every hyphen when building slugs
- expose `sanitizeSlug` for testing
- test sanitization with multiple hyphens

## Testing
- `npm run lint`
- `npx jest test/unit/sanitizeSlug.spec.ts`


------
https://chatgpt.com/codex/tasks/task_e_684feda1f074832aa6ae64e90b86286d
