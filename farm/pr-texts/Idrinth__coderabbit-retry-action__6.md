# Send pause/review/resume commands in 3 phases with 1-min separation

CodeRabbit requires a specific sequence of commands to properly retry
a review: pause, review, resume - each separated by ~1 minute. This
restructures the action to:

1. First identify all PRs needing retry
2. Send @coderabbitai pause to all eligible PRs
3. Wait 60 seconds
4. Send @coderabbitai review to all eligible PRs
5. Wait 60 seconds
6. Send @coderabbitai resume to all eligible PRs

Different PRs are progressed within each phase, so the wait time is
shared across all PRs rather than per-PR.

https://claude.ai/code/session_01LvmP5BsbKCZwYJVSFP9KQ8

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Refactor**
  * Restructured PR retry logic with a three-phase workflow including pauses and resume commands between phases, with 60-second delays for better coordination.
  * Improved retry threshold evaluation for enhanced cooldown and rate-limit handling.

* **Chores**
  * Removed emoji prefixes from log messages for cleaner output.

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
