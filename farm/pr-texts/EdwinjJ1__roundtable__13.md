# Add contextual breakout room handoffs

## Summary
- fix Google/NextAuth routing by moving the auth handler to the Pages API route NextAuth expects
- add persisted breakout rooms, messages, and handoff proposals with contextual LLM replies and role-based responder routing
- productize the handoff flow so Send to main chat closes the breakout room and returns the user to the main chat ready to work

## Test Plan
- ./node_modules/.bin/eslint .
- ./node_modules/.bin/tsc --noEmit
- ./node_modules/.bin/vitest run tests/breakout-actions.test.ts
