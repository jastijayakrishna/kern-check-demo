# Update S3 connection fields

## Summary
- update connection config generator to make `endpoint_url` and `layout` optional for S3
- drop deprecated fields `bucket_name` and `path_to_file`

## Testing
- `npm run lint` *(fails: ESLint couldn't find a configuration file)*
- `npm run compile` *(fails: cannot find type definitions)*

------
https://chatgpt.com/codex/tasks/task_e_6853f3641f088322932defe828f50dbe
