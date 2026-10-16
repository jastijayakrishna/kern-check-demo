# fix: remove spammy `notification-services-controller` error logs for silent failures

## Explanation

Error logs inside the notification controllers are not needed. Our services can fail silently and can retry.
This removes the unnecessary error logs which are spamming sentry.

## References

https://github.com/MetaMask/metamask-extension/issues/39861
https://github.com/MetaMask/metamask-extension/issues/39862

## Checklist

- [x] I've updated the test suite for new or updated code as appropriate
- [ ] I've updated documentation (JSDoc, Markdown, etc.) for new or updated code as appropriate
- [x] I've communicated my changes to consumers by [updating changelogs for packages I've changed](https://github.com/MetaMask/core/tree/main/docs/processes/updating-changelogs.md)
- [ ] I've introduced [breaking changes](https://github.com/MetaMask/core/tree/main/docs/processes/breaking-changes.md) in this PR and have prepared draft pull requests for clients and consumer packages to resolve them

---
<p><a href="https://cursor.com/background-agent?bcId=bc-63bcc551-ae14-4009-be62-bd36fecc8da4"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/agents?id=bc-63bcc551-ae14-4009-be62-bd36fecc8da4"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a></p>


<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Logging-only changes (plus a minor catch/throw adjustment) in non-critical notification flows; behavior remains largely the same aside from reduced error visibility.
> 
> **Overview**
> Reduces Sentry noise by removing internal `log.error` calls from notification "silent failure" paths in `NotificationServicesController` and `NotificationServicesPushController` (e.g., enable/disable push and missing bearer token), while keeping behavior as best-effort/no-op on failure.
> 
> For on-chain trigger deletion, the controller now throws a generic `Failed to delete OnChain triggers` error without logging the underlying error, and the package changelog is updated to document these expected silent-failure adjustments.
> 
> <sup>Written by [Cursor Bugbot](https://cursor.com/dashboard?tab=bugbot) for commit b27dc2003c70477bd29090bb88f03b717b9e21b8. This will update automatically on new commits. Configure [here](https://cursor.com/dashboard?tab=bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
