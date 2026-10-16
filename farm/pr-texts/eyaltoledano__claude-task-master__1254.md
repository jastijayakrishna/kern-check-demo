# fix: handle subtasks in getTask method

Fixes issue where 'tm show' command could not find subtasks by their dotted notation ID (e.g., '8.1').

The getTask method now checks if the task ID contains a dot and properly searches within parent task subtasks, returning a Task-like object with the full dotted ID.

This mirrors the fix already implemented in updateTaskStatus method for consistent subtask handling across the codebase.

Fixes #1253

Generated with [Claude Code](https://claude.ai/code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- New Features
  - Subtasks can be accessed via dotted IDs (e.g., "parent.subtask") and are shown as full task entries with sensible defaults, resolved dependencies, parent context, and inherited metadata.
  - Regular task lookup for non-dotted IDs remains unchanged.

- Bug Fixes
  - "tm show" correctly locates and displays subtasks when using dotted notation.
  - Retrieving non-existent subtasks now returns no result without affecting top-level task retrieval.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
