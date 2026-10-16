# fix(auth): refresh the OAuth access token before each agent run

Wizard OAuth access tokens live 1 hour. `wizard self-driving` on an uninstrumented repo runs two agent phases on one login: initialize PostHog in the project, then set up Self-driving. The second phase inherits the first phase's aging token. If it then waits on a user prompt, the token dies mid-run and the run ends in a 401 retry storm (PHW_AUTH_INVALID_OR_EXPIRED). That chained flow is specifically what this PR fixes. The login already returns a refresh token; it was parsed and never used. Now each phase starts with a fresh token.

```
login -> credentials { accessToken, refreshToken, expiresAt }

each agent -> stale? refresh + swap : keep -> spawn agent (token frozen at spawn)
```

Limit: a single phase blocked longer than the full TTL still outlives its token — that needs longer-lived tokens server-side (`is_first_party` on the wizard OAuth app). Naming follows products/desktop. Verified live against prod: refresh fired post-login, gateway v2 mint + agent + task-stream all accepted the refreshed token, zero 401s.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
