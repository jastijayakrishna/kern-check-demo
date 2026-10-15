# Name the exported PDF after the site and reporting period

## Summary

<!-- Please reference the issue this PR addresses in the following list. -->
Related issue(s):

- Resolves #13216

## Relevant technical choices

- This is the first use of `Intl.DateTimeFormat.prototype.formatRange` in the codebase, so `pdf-utils.ts` adds `/// <reference lib="es2021.intl" />` — `tsconfig` targets `es5`, which leaves it untyped. All `@wordpress/browserslist-config` targets support it.
- `getSiteHost` gained an optional `fallback` parameter, so the filename can fall back to `report` for an unparseable URL while the header keeps showing the raw value as before.
- Per AC8, reserved characters are removed from the localized date too, so locales that write dates with `/` lose the separators, e.g. zh-CN `2026/3/1 – 2026/3/7` becomes `202631 – 202637`.

## PR Author Checklist

- [x] My code is tested and passes existing unit tests.
- [x] My code has an appropriate set of unit tests which all pass.
- [x] My code is backward-compatible with WordPress 5.2 and PHP 7.4.
- [x] My code follows the [WordPress](https://make.wordpress.org/core/handbook/best-practices/coding-standards/) coding standards.
- [x] My code has proper inline documentation.
- [x] I have added a QA Brief on the issue linked above.
- [x] I have signed the Contributor License Agreement (see <https://cla.developers.google.com/>).

---------------

_Do not alter or remove anything below. The following sections will be managed by moderators only._

## Code Reviewer Checklist

- [ ] Run the code.
- [ ] Ensure the acceptance criteria are satisfied.
- [ ] Reassess the implementation with the IB.
- [ ] Ensure no unrelated changes are included.
- [ ] Ensure CI checks pass.
- [ ] Check Storybook where applicable.
- [ ] Ensure there is a QA Brief.
- [ ] Ensure there are no unexpected significant changes to file sizes.

## Merge Reviewer Checklist

- [ ] Ensure the PR has the correct target branch.
- [ ] Double-check that the PR is okay to be merged.
- [ ] Ensure the corresponding issue has a ZenHub release assigned.
- [ ] Add a changelog message to the issue.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
