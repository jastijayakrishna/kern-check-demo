# BEL-712: add optional transactional queue send support

### Motivation
- Prevent webhook jobs from being enqueued outside of the surrounding DB transaction so that job inserts can be rolled back when the transaction fails.
- Provide a type-safe way to pass a transaction-backed `db.executeSql` adapter into `pg-boss` `send()` calls.

### Description
- Extended generated queue handler signatures to accept an optional `options?: QueueSendOptions` and forward it to `pg-boss` via `queue.send(queueName, data, options)`.
- Added `QueueDbAdapter`, `QueueSendOptions`, `buildDbAdapter(transaction)` and `queueSendOptionsFromTransaction(transaction)` helpers to create a pg-boss-compatible `db.executeSql` adapter from a wrapped transaction object.
- Updated person-tag data paths to pass `queueSendOptionsFromTransaction(tx.dbTransaction.wrappedTransaction)` into `triggerWebhook` calls so webhook enqueueing uses the active transaction for `activity.created` and `tag.person.added` (including the idempotent path).

### Testing
- Ran `npm run check` (svelte/TS type checks) which failed with pre-existing, unrelated repository-wide errors and did not introduce new failures tied to these changes.
- Ran `eslint` on the modified files and addressed issues (verified handlers compile syntactically); lint check for the changed files succeeded after a small fix.
- Verified the modified files were staged and committed successfully with a descriptive commit message.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_b_69f2a8ee184c83308376ade09f94726e)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **Refactor**
  * Webhook dispatches now run with transaction-aware delivery options and improved queue handler typing.
  * Queue processing now forwards transaction context to webhook sends for more reliable enqueueing.

* **Behavior Change**
  * Webhook failures are no longer silently caught and logged locally—errors will propagate for centralized handling.

* **Documentation**
  * Updated locale references to link “Status” and “Delivery logs” to the webhooks delivery logs page.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
