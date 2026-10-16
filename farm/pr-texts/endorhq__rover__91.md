# chore: improve UX by instructing users how to initialize an uninitialized repository

## Summary
- Add preAction hook to check for rover.json before executing commands
- Provide clear guidance when users try to run commands in uninitialized directories
- Display helpful tip about running `rover init` to set up the project

## Changes
- **packages/cli/src/index.ts**: Added preAction hook that:
  - Checks if `rover.json` exists in current directory
  - Skips check for `init` command (which is used to create the config)
  - Shows friendly error message with project status
  - Displays tip about running `rover init` to initialize
  - Exits with code 1 to prevent command execution

## User Experience Improvement
Before this change, users running Rover commands in uninitialized directories would encounter confusing errors later in the command execution. Now they get immediate, actionable feedback explaining what they need to do.

🤖 Generated with [Claude Code](https://claude.ai/code)
