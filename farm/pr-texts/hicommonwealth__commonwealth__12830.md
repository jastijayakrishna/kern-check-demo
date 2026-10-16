# feat: restrict SMS login to US and Canada

## Summary
- add ticket for limiting SMS login to US and CA
- restrict phone input to US/CA numbers
- show SMS login only for US/CA IPs

## Testing
- `pnpm lint-branch-warnings` *(fails: Proxy response (403) !== 200 when HTTP Tunneling)*
- `pnpm -r check-types` *(fails: Proxy response (403) !== 200 when HTTP Tunneling)*

------
https://chatgpt.com/codex/tasks/task_e_68a4e8bbbf2c832f8309ab4eff801341
