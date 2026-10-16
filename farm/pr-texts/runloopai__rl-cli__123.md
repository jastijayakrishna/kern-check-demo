# feat: network policy create flags

## Description

This PR updates the `rl-cli` to support the newly introduced `allow AI gateway` and `allow MCP gateway` flags for network policy creation, aligning the CLI with recent backend controller changes.

**Note:** PR titles should follow [Conventional Commits](https://www.conventionalcommits.org/) format (e.g., `feat(devbox): add support for custom env vars` or `fix(snapshot): resolve pagination issue`) as they are used for automatic release notes generation.

## Type of Change

<!-- Mark the relevant option with an 'x' -->

- [ ] Bug fix (non-breaking change which fixes an issue)
- [x] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement
- [ ] Test updates

## Related Issues

<!-- Link to related issues using #issue-number -->
Closes #

## Changes Made

-   **CLI Command:** Added `--allow-ai-gateway` and `--allow-mcp-gateway` flags to the `rl network-policy create` command.
-   **Type Definitions & Interfaces:** Updated `CreateOptions`, `CreateNetworkPolicyParams`, `UpdateNetworkPolicyParams`, and `ExtendedEgress` to include the new `allowAiGateway` and `allowMcpGateway` fields.
-   **Service Layer:** Modified `createNetworkPolicy`, `updateNetworkPolicy`, `getNetworkPolicy`, and `listNetworkPolicies` functions in `networkPolicyService` to handle the new gateway fields.
-   **UI Components:** Integrated form fields for `allowAiGateway` and `allowMcpGateway` into the `NetworkPolicyCreatePage` and added display for these settings in the `NetworkPolicyDetailScreen`.

## Testing

<!-- Describe how you tested your changes -->

- [x] I have tested locally
- [ ] I have added/updated tests
- [x] All existing tests pass

Verified:
-   CLI help output for `network-policy create` displays the new flags.
-   TypeScript compilation is successful with no errors.
-   Functional testing of creating and viewing network policies via the CLI and UI, confirming the new gateway settings are correctly applied and displayed.

## Checklist

- [x] My code follows the code style of this project
- [x] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [x] I have updated the documentation accordingly (CLI help output)
- [x] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [x] New and existing unit tests pass locally with my changes
- [x] Any dependent changes have been merged and published

## Screenshots (if applicable)

<!-- Add screenshots to help explain your changes -->

## Additional Notes

The new `allow AI gateway` and `allow MCP gateway` flags default to "No" in the UI.

---
[Slack Thread](https://runloophq.slack.com/archives/C079G6098BH/p1772056925156089?thread_ts=1772056925.156089&cid=C079G6098BH)

<p><a href="https://cursor.com/agents/bc-c2e84086-a2bf-5e94-9875-8f69a1de7263"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-c2e84086-a2bf-5e94-9875-8f69a1de7263"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</p>
