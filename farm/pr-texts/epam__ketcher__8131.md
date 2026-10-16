# Refactor: #8130 - Fix for many sonar issues

## Summary
- throw a proper `Error` for invalid SRU cross-bond counts and simplify the cis/trans stereochemistry check
- guard against null UI state, await the file saver promise, and streamline polymer bond selection changes
- replace the unused `reduce` call in the rotate controller with an explicit iteration
- add accessible labels, semantic tab buttons, and Sonar spacing fixes across the demo, react, and SSR packages

## Testing
- not run (not requested)

------
https://chatgpt.com/codex/tasks/task_e_68e822eecebc832999e44b13b3f31d70
