# fix(util/git): use non-empty passwords for token credentials on more platforms

## Changes

Follow-up to #47077: `getTokenCredentials` gives token-only credentials a non-empty password on more platforms, so git with Ubuntu's current curl keeps sending them on the `git-upload-pack` request.

- Azure DevOps: `x-access-token:<token>` (any non-empty username, [docs](https://learn.microsoft.com/en-us/azure/devops/repos/git/auth-overview))
- Bitbucket Cloud: `x-token-auth:<token>` ([docs](https://support.atlassian.com/bitbucket-cloud/docs/using-access-tokens/)); git-url-parse's own `x-token-auth:` prefix for `bitbucket.org` is skipped so it isn't doubled, which also stops it from being added to `username:password` credentials
- Bitbucket Server / Data Center: `x-token-auth:<token>` for project and repository HTTP access tokens ([docs](https://confluence.atlassian.com/bitbucketserver/http-access-tokens-939515499.html))
- SCM-Manager: `x-access-token:<token>` (the username is ignored for API keys, [`ApiKeyRealm`](https://github.com/scm-manager/scm-manager/blob/develop/scm-webapp/src/main/java/sonia/scm/security/ApiKeyRealm.java))
- Unknown hosts are unchanged; the docs now recommend `username` and `password` for them, and the gomod `insteadOf` example shows the `x-access-token:` form.

## Context

Please select one of the following:

- [ ] This closes an existing Issue, Closes: # <!-- NOTE that this should NOT be a Discussion -->
- [x] This doesn't close an Issue, but I accept the risk that this PR may be closed if maintainers disagree with its opening or implementation. Because this does not close an Issue, I will add a minimal reproduction repository as part of this PR.

Discussion: #47071

## AI assistance disclosure

Did you use AI tools to create any part of this pull request?

Please select one option and, if yes, briefly describe how AI was used (e.g., code, tests, docs) and which tool(s) you used.

- [ ] No — I did not use AI for this contribution.
- [ ] Yes — minimal assistance (e.g., IDE autocomplete, small code completions, grammar fixes).
- [x] Yes — substantive assistance (AI-generated non‑trivial portions of code, tests, or documentation).
- [ ] Yes — other (please describe):

Research, code, tests, docs and PR description written with Claude Code (Claude Opus 5.5 and Claude Sonnet 5.5), reviewed by @viceice.

### Use of AI in replying to PR comments

Who answers review comments:

- [x] @viceice will read and reply directly. **Name the account.**
- [ ] An agent will draft replies and @username will read them before they are posted. **Name the account.**
- [ ] An agent will draft replies and reply autonomously. **This is heavily discouraged, and we prefer that there are humans in the loop**
- [ ] Nobody has explicitly committed to replying.

## Documentation (please check one with an [x])

- [x] I have updated the documentation, or
- [ ] No documentation update is required

## How I've tested my work (please select one)

I have verified these changes via:

- [ ] Code inspection only, or
- [x] Newly added/modified unit tests, or
- [ ] No unit tests, but ran on a real repository, or
- [ ] Both unit tests + ran on a real repository

The public repository: n/a

A reproduction is compulsory for PRs that do not close an Issue: link a public repository above that reproduces the bug or shows the new behavior.
If this PR closes an Issue, confirm the fix against the Issue's reproduction.
If you are not adding a reproduction, state your reason here:

```markdown
The failure needs private repositories and tokens on each platform, so a public reproduction repository can't show it. The curl behaviour is reproduced in #47071.
```

PRs without a reproduction or a stated reason will not be reviewed and may be closed.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
