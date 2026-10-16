# Add color argument to IconButton component

## Type

- [ ] Bugfix 🐛
- [x] New feature 🌈
- [ ] Change request 🤓
- [ ] Documentation 📚
- [ ] Tech debt 👩‍💻

## Changes proposed ✔️

- Added an optional `color` prop to the `IconButton` component, defaulting to `neutral-textHigh`, which is forwarded to the inner `Icon`.
- Included new tests to verify the `color` prop's default and custom values.
- Added new Storybook stories to showcase the `color` prop, including an `ai-generative` gradient example.
- Updated relevant `CHANGELOG.md` files.

---
[Slack Thread](https://nuvemshop.slack.com/archives/C093SRT6GBT/p1755785262265859?thread_ts=1755785262.265859&cid=C093SRT6GBT)

<a href="https://cursor.com/background-agent?bcId=bc-1cca343a-f3ee-4b2e-81e8-e4d383cced52">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-cursor-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-cursor-light.svg">
    <img alt="Open in Cursor" src="https://cursor.com/open-in-cursor.svg">
  </picture>
</a>
<a href="https://cursor.com/agents?id=bc-1cca343a-f3ee-4b2e-81e8-e4d383cced52">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-web-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-web-light.svg">
    <img alt="Open in Web" src="https://cursor.com/open-in-web.svg">
  </picture>
</a>



<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * IconButton accepts an optional color prop to customize the inner icon color (defaults to neutral-textHigh).
* **Documentation**
  * Top-level and component changelogs updated with the new version and feature note.
* **Storybook**
  * New stories demonstrating primary-textHigh and ai-generative colors.
* **Tests**
  * Unit test added to verify the icon reflects the provided color.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
