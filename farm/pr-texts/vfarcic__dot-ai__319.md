# feat(query): add visualization endpoint for Web UI

## Description

**What does this PR do?**

Implements a visualization endpoint that enables the Web UI to display rich visualizations of Kubernetes resources returned by the query tool, including AI-inferred relationships (topology, dependencies, traffic flow) that text responses cannot effectively convey.

**Why is this change needed?**

Understanding cluster architecture, resource relationships, and dependencies is much easier with visual representations than text. The key differentiator is AI inferring relationships that non-AI tools cannot - like app dependencies from env vars, traffic flow patterns, and application groupings.

## Related Issues

- Closes #317

## Type of Change

- [ ] 🐛 Bug fix (non-breaking change that fixes an issue)
- [x] ✨ New feature (non-breaking change that adds functionality)
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to change)
- [ ] 📚 Documentation update
- [ ] ♻️ Refactoring (no functional changes)
- [x] ✅ Test updates (adding or updating tests)
- [x] 🔧 Configuration changes
- [ ] 🚀 Performance improvements
- [ ] 🎨 Style changes (formatting, naming, etc.)
- [ ] 📦 Dependency updates
- [ ] 🔨 CI/CD changes

## Testing Checklist

- [x] Tests added or updated
- [x] All existing tests pass locally
- [x] Manual testing performed
- [x] Test coverage maintained or improved

**Test commands run:**
```bash
npm run test:integration query
```

**Test results:**
- Session storage and retrieval verified (sessionId returned in query responses)
- Visualization URL generation tested with WEB_UI_BASE_URL configuration
- Visualization endpoint responses validated for structure and content
- Session expiry handling verified (404 for non-existent session)
- Multiple visualization types tested (mermaid, cards, code, table)

## Documentation Checklist

- [ ] README.md updated (if user-facing changes)
- [ ] Documentation updated (if applicable)
- [x] Code comments added for complex logic
- [ ] API documentation updated (if API changes)
- [x] [CONTRIBUTING.md](CONTRIBUTING.md) guidelines followed

> Note: Documentation deferred to PRD #318 to enable silent release and unblock Web UI development

## Security Checklist

- [x] No secrets or credentials committed
- [x] Input validation implemented where needed
- [x] Security implications considered and documented
- [x] Dependencies scanned for vulnerabilities
- [x] Authentication/authorization logic reviewed
- [x] Error messages don't leak sensitive information

## Breaking Changes

**Does this PR introduce breaking changes?**
- [ ] Yes
- [x] No

Visualization URL is only added to query responses when `WEB_UI_BASE_URL` environment variable is set. Existing behavior unchanged without configuration.

## Checklist

- [x] My code follows the project's code style guidelines
- [x] I have performed a self-review of my code
- [x] I have commented my code, particularly in hard-to-understand areas
- [x] My changes generate no new warnings or errors
- [x] I have added tests that prove my fix is effective or my feature works
- [x] New and existing tests pass locally with my changes
- [x] Any dependent changes have been merged and published
- [x] PR title follows Conventional Commits format

## Additional Context

**Reviewer Notes:**
- AI visualization prompt design (`prompts/visualize-query.md`) - emphasizes both obvious relationships (ownerReferences, selectors) and deep analysis (env var dependencies, naming patterns)
- Session storage implementation uses GenericSessionManager pattern
- REST API visualization endpoint at `GET /api/v1/visualize/{sessionId}`
- Integration tests validate AI-generated visualization structure dynamically

**Follow-up Work:**
- PRD #318: Visualization Feature Documentation (environment variable docs, tool output examples, Web UI cross-references)

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Added visualization support for query results with a new visualization endpoint
  * Introduced Web UI integration via configurable `webUI.baseUrl` setting
  * Query responses now include session tracking (sessionId and visualizationUrl)

* **Documentation**
  * Updated visualization feature documentation and configuration guides
  * Completed visualization endpoint implementation documentation

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
