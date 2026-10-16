# Fix server credentials

## Summary
- load API keys and credentials from environment variables
- clean up Wigle imports

## Testing
- `npm test` *(fails: jest not found)*

------
https://chatgpt.com/codex/tasks/task_e_685f590db030832b9811c0fd1deb4e43

## Summary by Sourcery

Load Shodan and Wigle credentials from environment variables, replacing hard-coded values and removing unused imports

Enhancements:
- Retrieve Shodan API key and Wigle username/password from environment variables

Chores:
- Remove hard-coded WIGLE_API_KEY constant and basic-auth dependency import
