# fix(clusters): clarify Static IP description for outbound traffic

## Summary

**Issue**: N/A

Improved the description text for the Scaleway Static IP / Nat Gateways feature to more accurately convey that the static IPs apply to outbound traffic from the cluster, rather than inbound visibility.

**Changes**:
- Updated the description from "Your cluster will only be visible from a fixed number of public IP" to "Your cluster's outbound traffic will originate from a fixed number of public IPs"
- This clarifies that the static IPs are used for outbound connections, not for making the cluster visible

## Testing

- [ ] Changes tested locally in the relevant Console's pages and Storybooks
- [ ] `yarn format`
- [ ] `yarn lint`

## PR Checklist

- [ ] I followed naming, styling, and TypeScript rules
- [ ] I performed a self-review (diff inspected)
- [ ] I titled the PR using Conventional Commits with a scope
- [ ] I only kept necessary comments, written in English
- [ ] CI is green

https://claude.ai/code/session_012bzFagdfgnDQPDj1GigDCe

<!-- This is an auto-generated description by cubic. -->
---
## Summary by cubic
Clarifies the Scaleway Static IP toggle description so it accurately states that outbound cluster traffic uses fixed public IPs, instead of implying the cluster is only visible from those IPs.

<sup>Written for commit b033501a73c35fb92ca909055c065b34b7e1ee8a. Summary will update on new commits.</sup>

<a href="https://cubic.dev/pr/Qovery/console/pull/2917?utm_source=github" target="_blank" rel="noopener noreferrer" data-no-image-dialog="true"><picture><source media="(prefers-color-scheme: dark)" srcset="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://www.cubic.dev/buttons/review-in-cubic-light.svg"><img alt="Review in cubic" src="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"></picture></a>

<!-- End of auto-generated description by cubic. -->
