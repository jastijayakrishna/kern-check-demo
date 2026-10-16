# mount sticky disk with noinit_itable to stop repeated lazy-init writes (release/v2)

## Summary
Same change as #123, applied to `release/v2`: mount the builder sticky disk with `-o noinit_itable` so the `ext4lazyinit` kernel thread doesn't zero the uninitialized inode tables (a non-trivial portion of the device) in the background. On copy-on-write clones of a snapshot taken before lazy init finished, that zeroing replays on every clone and is discarded with it — pure wasted Ceph write load. The zeroing is unnecessary for correctness (checksummed group descriptors track unused inodes; unallocated blocks on the thin-provisioned device read back as zeroes).

Link to Devin session: https://app.devin.ai/sessions/1054a9452e8a49ccb891391e2327a612
Requested by: @piob-io

<!-- codesmith:footer -->
---
<a href="https://app.blacksmith.sh/useblacksmith/codesmith/setup-docker-builder/pr/124"><picture><source media="(prefers-color-scheme: dark)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v2.svg"><source media="(prefers-color-scheme: light)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-light-v2.svg"><img alt="View with [code]smith" src="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v2.svg"></picture></a> <a href="https://backend.blacksmith.sh/track/enable-autofix?expires=1787954417&installation_model_id=2&pr_number=124&repository=useblacksmith%2Fsetup-docker-builder&return_to=https%3A%2F%2Fgithub.com%2Fuseblacksmith%2Fsetup-docker-builder%2Fpull%2F124&signature=5d50a198cd7b66d08493597778a7d0131925c9d225e6e8346fae898cf3b734fb"><picture><source media="(prefers-color-scheme: dark)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-light.svg"><img alt="Autofix with [code]smith" src="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-dark.svg"></picture></a>
<sup>Need help on this PR? Tag <code>@codesmith-bot</code> with what you need. Autofix is disabled.</sup>

<!-- codesmith:autofix:disabled -->
<!-- /codesmith:footer -->

<!-- codesmith:footer:staging -->
---
<a href="https://staging.blacksmith.sh/useblacksmith/codesmith/setup-docker-builder/pr/124"><picture><source media="(prefers-color-scheme: dark)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v2.svg"><source media="(prefers-color-scheme: light)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-light-v2.svg"><img alt="View with [code]smith" src="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v2.svg"></picture></a> <a href="https://stagingbackend.blacksmith.sh/track/enable-autofix?expires=1787954420&installation_model_id=8&pr_number=124&repository=useblacksmith%2Fsetup-docker-builder&return_to=https%3A%2F%2Fgithub.com%2Fuseblacksmith%2Fsetup-docker-builder%2Fpull%2F124&signature=ea85368d7b1c7ba048bd30fa27dc0b1bb32c6f2fcada945950df0c7821992866"><picture><source media="(prefers-color-scheme: dark)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-light.svg"><img alt="Autofix with [code]smith" src="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-dark.svg"></picture></a>
<sup>Need help on this PR? Tag <code>@codesmith-bot</code> with what you need. Autofix is disabled. (Staging)</sup>

<!-- codesmith:autofix:disabled -->
<!-- /codesmith:footer:staging -->
