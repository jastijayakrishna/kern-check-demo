# Refactor: Create common URL validation function for Git commands

# Fix CodeQL security check for URL validation

This PR enhances the URL validation in the `getRemoteRefs` function to use the `parseRemoteValue` function from `gitRemoteParse.js`, which provides robust validation for both HTTPS and SSH URLs.

## Changes
- Use `parseRemoteValue` for URL validation in `getRemoteRefs`
- Maintain existing checks for URLs starting with 'git@' or 'https://'
- Continue to throw errors for invalid URLs instead of returning empty arrays

This should resolve the CodeQL security check failure for command injection vulnerabilities.

Link to Devin run: https://app.devin.ai/sessions/633f4e7216c14ad981748f67af34901b
Requested by: Kazuki
