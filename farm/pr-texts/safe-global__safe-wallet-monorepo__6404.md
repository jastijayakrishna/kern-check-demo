# Fix(web): Tenderly simulation links to respect custom configuration

Resolves #6403

## Summary
- update Tenderly simulation link builder to derive organization and project from a custom API URL
- wire the custom Tenderly settings into the web and mobile simulation link usage
- add unit tests covering the new simulation link logic

## Testing
* Set https://api.tenderly.co/api/vl/account/floki-devs/project/contracts/simulate as a custom Tenderly URL in the environment variable settings
* Simulate a tx, click on the generated Tenderly link

------
https://chatgpt.com/codex/tasks/task_b_68df7fa95e60832fa1520d234eaed147
