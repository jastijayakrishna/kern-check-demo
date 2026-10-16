# refactor: capitalize GitHub in action names and error codes

Capitalize GitHub in action names and error codes

This PR updates all instances of lowercase "github" to "GitHub" in our action names, error codes, and configuration types for consistency.

Changes:
- Update action types to use 'GitHub' instead of 'github'
- Update error types and codes to use 'GitHub'
- Update configuration types to use 'GitHub'
- Ensure consistent capitalization across all GitHub-related actions

Testing:
- No runtime changes, only string constant updates
- CI will verify type checking and linting

Link to Devin run: https://app.devin.ai/sessions/e99c9f57799f470f9d95adbfb561cc91
Requested by: henry@dust.tt
