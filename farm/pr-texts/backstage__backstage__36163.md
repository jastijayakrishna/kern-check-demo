# fix(kubernetes-backend): remove duplicate permissions registration

## Hey, I just made a Pull Request!

Fixes `yarn tsc` on master. #35313 and #33832 both added the `kubernetesPermissions` import and registration in `plugin.ts`, resulting in a duplicate identifier error. This keeps the registration from #33832, which only happens when `kubernetes` config is present, matching how permissions were exposed before through the router.

#### :heavy_check_mark: Checklist

<!--- Please include the following in your Pull Request when applicable: -->

- [ ] A changeset describing the change and affected packages. ([more info](https://github.com/backstage/backstage/blob/master/CONTRIBUTING.md#creating-changesets))
- [ ] Added or updated documentation
- [ ] Tests for new functionality and regression tests for bug fixes
- [ ] Screenshots attached (for UI changes)
- [x] All your commits have a `Signed-off-by` line in the message. ([more info](https://github.com/backstage/backstage/blob/master/CONTRIBUTING.md#developer-certificate-of-origin))

🤖 Generated with [Claude Code](https://claude.com/claude-code)
