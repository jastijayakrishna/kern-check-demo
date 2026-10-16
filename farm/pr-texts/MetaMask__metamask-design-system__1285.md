# feat: align Modal stories with extension legacy modal stories

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## **Description**

Corrects the earlier misunderstanding: [metamask-extension#43815](https://github.com/MetaMask/metamask-extension/pull/43815) removed extra Storybook stories from the **deprecated component-library** Modal, not from `@metamask/design-system-react`. Those removed stories should live in the design system instead.

This PR:

- **Restores** all Modal sub-component story files (`ModalBody`, `ModalContent`, `ModalFocus`, `ModalFooter`, `ModalHeader`, `ModalOverlay`) that were mistakenly simplified
- **Expands** `Modal.stories.tsx` to match the legacy extension Modal stories, composing the full modal stack
- **Updates** `Modal/README.mdx` with a concise usage example that mirrors the Default story and shows all sub-components (`ModalOverlay`, `ModalContent`, `ModalHeader`, `ModalBody`, `ModalFooter`)
- Adds the extension story set: `Default`, `Usage`, `IsClosedOnOutsideClick`, `IsClosedOnEscapeKey`, `InitialFocusRef`, `FinalFocusRef`, `RestoreFocus`, and `AutoFocus`

## **Related issues**

Fixes:

## **Manual testing steps**

1. Run `yarn storybook`
2. Open **React Components / Modal** and verify all 8 stories render with the full modal composition
3. Confirm sub-component pages still show their full story sets
4. Check Modal docs render without broken Canvas references

## *Screen recordings**

### Before

https://github.com/user-attachments/assets/4d58cbf0-8ce2-4f94-82e2-0a59833a487f

### After

https://github.com/user-attachments/assets/08912799-0a64-4aee-9411-c342a38699ed

## **Pre-merge author checklist**

- [x] I've followed [MetaMask Contributor Docs](https://github.com/MetaMask/contributor-docs)
- [x] I've completed the PR template to the best of my ability
- [x] I've included tests if applicable
- [x] I've documented my code using [JSDoc](https://jsdoc.app/) format if applicable
- [x] I've applied the right labels on the PR (see [labeling guidelines](https://github.com/MetaMask/metamask-extension/blob/develop/.github/guidelines/LABELING_GUIDELINES.md)). Not required for external contributors.

## **Pre-merge reviewer checklist**

- [ ] I've manually tested the PR (e.g. pull and build branch, run the app, test code being changed).
- [ ] I confirm that this PR addresses all acceptance criteria described in the ticket it closes and includes the necessary testing evidence such as recordings and or screenshots.
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-1ccd2efb-2a25-40b3-b950-81370dc6eebd"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-1ccd2efb-2a25-40b3-b950-81370dc6eebd"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
