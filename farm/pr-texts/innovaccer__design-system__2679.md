# fix: rename select option key identifier to id

## Summary
- rename the optional OptionType identifier from `key` to `id`
- update the select utilities to respect the new `id` field when comparing options
- adjust the select utility tests to cover `id`-based duplicate label handling

## Testing
- npm test -- --runTestsByPath core/components/organisms/select/__test__/utils.test.tsx

------
https://chatgpt.com/codex/tasks/task_b_690b1d756190832d8816103bf9e255d8
