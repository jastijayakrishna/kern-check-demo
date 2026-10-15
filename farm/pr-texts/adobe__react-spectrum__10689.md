# fix: preserve tree focus when items arrive

Closes #10660

A focused empty Tree should remain keyboard-navigable when its rows arrive. Keep the collection's focus handlers attached while empty, while allowing normal Tab navigation and text selection in empty-state content. This keeps focus tracking intact without moving focus back after the user has left the collection; ListBox behavior is unchanged.

Added Tree and GridList regressions and a `PopulateFocusedEmptyTree` story that adds rows without moving focus. AI-assisted; repository guidance was followed and the diff was reviewed.

## ✅ Pull Request Checklist:

- [x] Included link to corresponding [React Spectrum GitHub Issue](https://github.com/adobe/react-spectrum/issues/10660).
- [x] Added/updated unit tests and storybook for this change (for new code or code which already has tests).
- [x] Filled out test instructions.
- [x] ~~Updated documentation (if it already exists for this component).~~ No public API or documented behavior changes; added a reproduction story.
- [x] Looked at the Accessibility Practices for this feature - [Treegrid pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treegrid/).
- [x] I understand every change in this PR and can explain why it's there.
- [x] If AI-assisted, I followed our [AI contribution guidance](https://github.com/adobe/react-spectrum/blob/main/CONTRIBUTING.md#ai-assisted-contributions) and pointed my assistant at [AGENTS.md](https://github.com/adobe/react-spectrum/blob/main/AGENTS.md).

## 📝 Test Instructions:

Open the new Tree story, Tab into the empty tree, press Enter to populate it, and use ArrowDown to navigate both rows. In a loading example, moving focus out before items arrive should leave focus outside the tree. Empty-state links should work in both Tab directions, and text inputs should retain their native select-all shortcut.

- Full unit suite: 383 suites, 8,376 tests and 262 snapshots passed (16 tests skipped), using one worker with a memory limit.
- Full SSR suite: 60 suites / 74 tests passed.
- Removed the duplicate browser regression following review; the Tree unit test covers the reported bug.
- Formatting, types, oxlint, package checks and constraints passed, run sequentially.
- Previously verified the new Storybook example: Tab into the empty tree, Enter to add rows, then ArrowDown to One and Two.

Local runner notes: SSR used `BROWSERSLIST_IGNORE_OLD_DATA=true` for an outdated data warning. Storybook needed a temporary PostCSS path-decoding workaround for a non-ASCII checkout path; it was restored after verification and is not part of this PR.

## 🧢 Your Project:

Independent open-source contribution.
