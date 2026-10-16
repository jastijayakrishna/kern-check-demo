# fix: inquirer.prompt is not a function with inquirer v12

Closes #412 

This was a dep change made last year, but recent manual testing has found this bug, during interactive prompt for log forwarding set.

In inquirer v12, the CJS entry point no longer exposes `prompt` directly — it exports `{ createPromptModule, default }`, with the classic API living on `default`. This caused `aio rt namespace log-forwarding set` to crash immediately with `TypeError: inquirer.prompt is not a function`.

## Changes

- **`src/commands/runtime/namespace/log-forwarding/set.js`** — destructure `default` on import so `inquirer.prompt` resolves correctly:
  ```js
  // before
  const inquirer = require('inquirer')
  // after
  const { default: inquirer } = require('inquirer')
  ```

- **`test/commands/runtime/namespace/log-forwarding/set.test.js`** — update mock assignment to target the same property the source now reads from:
  ```js
  // before
  inquirer.prompt = prompt
  // after
  inquirer.default.prompt = prompt
  ```
