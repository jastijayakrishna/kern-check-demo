# fix(core): preserve shared request context identity

## Description

This PR https://github.com/mastra-ai/mastra/pull/13094 introduced a side-effect of making `RequestContext` immutable inside tools: tool reads work, but writes go to the clone, so caller-side dynamic state is lost.

So there is no way to communicate any new state "outside" from the tool.

## Type of change

- [x] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement
- [ ] Test update

## Checklist

- [x] I have linked the related issue(s) in the description above
- [x] I have made corresponding changes to the documentation (if applicable)
- [x] I have added tests that prove my fix is effective or that my feature works
- [ ] I have addressed all Coderabbit comments on this PR


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## ELI5
This PR makes tools and their caller share the same “note pad” for a request, instead of tools working on a copy. So if a tool updates request data, the caller can see those updates.

### What changed
- Updated `mergeRequestContexts` to detect when the builder-time and execution-time `RequestContext` are the *exact same instance*, and in that case return it directly (no cloned/merged copy).
- Added/extended a tool-builder test to verify the tool receives the same `RequestContext` identity and that mutations to `ctx.requestContext` are visible to the caller.
- Added a patch-level changeset for `@mastra/core` describing the user-facing “lost write” bug fix.

### Impact
- Fixes lost dynamic state where tool writes were previously applied to a cloned `RequestContext`.
- Non-breaking bug fix; workflow serialization/deserialization for distinct contexts remains unchanged.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
