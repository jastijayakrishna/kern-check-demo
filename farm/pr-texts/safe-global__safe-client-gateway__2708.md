# Fix tests for multisig transaction notes

## Summary
- avoid Intl.NumberFormat RangeError on Node 20 by lowering maximum fraction digits
- update transaction tests to use Safe Transaction Service v2 endpoints

## Testing
- `npm test -- src/routes/transactions/transactions-history.controller.spec.ts src/routes/transactions/__tests__/controllers/list-multisig-transactions-by-safe.transactions.controller.spec.ts`

------
https://chatgpt.com/codex/tasks/task_b_68c2d3d2ea80832f95d55b41310864c7
