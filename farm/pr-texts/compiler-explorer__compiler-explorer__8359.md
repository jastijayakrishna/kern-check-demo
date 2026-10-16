# Fix externalparser properties not surviving prediscovery serialization

## Summary
- Fix externalparser not working with prediscovered compilers (e.g., MicroPython)
- The `externalparser.props` function was lost during JSON serialization, causing `exe` path to be undefined
- Now stores `exe` and `args` directly on the externalparser object
- Removes the unused `props` function pattern from externalparser
- Adds proper TypeScript typing for externalparser
- Improves error messages to include compiler ID
- Adds delay before process.exit to allow Loki logs to flush

## Test plan
- [x] TypeScript type check passes
- [x] Linter passes  
- [x] Unit tests pass
- [ ] Deploy to staging and verify MicroPython compilers work

🤖 Generated with [Claude Code](https://claude.com/claude-code)
