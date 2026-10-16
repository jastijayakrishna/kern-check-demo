# fix: replace randombytes usage in @near-js/crypto

## Summary
- swap the randombytes dependency for `randomBytes` from `@noble/hashes/utils`
- update ed25519 and secp256k1 keypair generators to use the new random byte source
- adjust the crypto package dependencies to include `@noble/hashes`

## Testing
- pnpm --filter @near-js/crypto test *(fails: `TS2307: Cannot find module '@near-js/utils'` during ts-jest compilation)*

------
https://chatgpt.com/codex/tasks/task_e_68f27257156c83299229ec1e1f8b724a
