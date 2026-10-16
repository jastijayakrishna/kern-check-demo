# fix(runtime-core): dedupe concurrent Module.init() calls

## Description

This PR addresses the issue of `Module.init()` being called multiple times concurrently, which could lead to redundant or problematic re-initialization of remote modules.

The changes introduce a mechanism to deduplicate concurrent `Module.init()` calls by utilizing a shared in-flight promise. This ensures that the remote module's initialization logic (including `initContainer` and `beforeInitContainer` hooks) is executed only once, even when `init()` is invoked simultaneously. Proper cleanup of `initing` and `initPromise` is also ensured after the initialization completes.

A new regression test has been added to verify this behavior, asserting that concurrent `init()` calls result in a single execution of the underlying initialization logic and leave the module in a stable, initialized state.

## Related Issue

https://github.com/module-federation/core/issues/4330

## Types of changes

- [ ] Docs change / refactoring / dependency upgrade
- [x] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)

## Checklist

- [x] I have added tests to cover my changes.
- [ ] All new and existing tests passed.
- [ ] I have updated the documentation.

---
<p><a href="https://cursor.com/background-agent?bcId=bc-6e89c483-f454-44ac-a915-298b40e51de1"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/agents?id=bc-6e89c483-f454-44ac-a915-298b40e51de1"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a></p>
