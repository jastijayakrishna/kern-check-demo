# Fix performance issue when throwing errors with stackTraceLimit = 0 and improve @fs URL parsing

- [x] Fix performance issue with stackTraceLimit = 0 by preventing catastrophic backtracking 
- [x] Improve @fs URL parsing to handle multiple @ symbols correctly
- [x] Add comprehensive test coverage for @fs URL parsing scenarios  
- [x] Remove performance benchmarking tests as requested in code review
- [x] Remove unused parseErrorStacktrace import
- [x] Add test cases for https URLs with @fs prefix
- [x] Add comment explaining minimum length validation (3 characters) for stack trace locations

Added explanatory comments for the minimum length validation in the Firefox/Safari stack trace parsing logic. The value `3` represents the minimum valid location format: 1 character for filename + 1 colon + 1 character for line number (e.g., "a:1").

<!-- START COPILOT CODING AGENT TIPS -->
---

💬 Share your feedback on Copilot coding agent for the chance to win a $200 gift card! Click [here](https://survey3.medallia.com/?EAHeSx-AP01bZqG0Ld9QLQ) to start the survey.
