# fix(accounts): vertically align row arrows on account details page

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## **Description**

On the account details page, the `>` arrow at the end of each row sat slightly higher than the text next to it. This PR centres the arrows so they line up with the text in every row, including Account name, Networks, Private keys, Smart Account, Wallet, Secret Recovery Phrase and Remove account.

## **Changelog**

CHANGELOG entry: Fixed the vertical alignment of the arrow icons on the account details page.

<!--
## **Related issues**

Fixes:
-->

## **Manual testing steps**

1. Run the extension and unlock a wallet.
2. Open the account menu and go to an account's details page.
3. Verify the `>` arrow in each row is vertically centred with the row's text.


## **Screenshots/Recordings**

### **Before**
<img width="364" height="488" alt="Screenshot 2026-09-30 at 1 42 40 PM" src="https://github.com/user-attachments/assets/e640beed-82dd-4038-8021-57a566f2839a" />
<img width="361" height="316" alt="Screenshot 2026-09-30 at 1 56 34 PM" src="https://github.com/user-attachments/assets/c8bcde64-43ff-4a50-88f4-18edbfdde3e1" />

### **After**

<img width="362" height="503" alt="Screenshot 2026-09-30 at 2 30 13 PM" src="https://github.com/user-attachments/assets/6e304abc-e441-48b4-b41a-d071e2449b03" />
<img width="371" height="287" alt="Screenshot 2026-09-30 at 2 30 21 PM" src="https://github.com/user-attachments/assets/5bc7b4c6-7039-488b-9126-c19cca0aa139" />

## **Pre-merge author checklist**

- [x] I've followed [MetaMask Contributor Docs](https://github.com/MetaMask/contributor-docs) and [MetaMask Extension Coding Standards](https://github.com/MetaMask/metamask-extension/blob/main/.github/guidelines/CODING_GUIDELINES.md).
- [x] I've completed the PR template to the best of my ability
- [x] I’ve included tests if applicable
- [x] I’ve documented my code using [JSDoc](https://jsdoc.app/) format if applicable
- [ ] I’ve applied the right labels on the PR (see [labeling guidelines](https://github.com/MetaMask/metamask-extension/blob/main/.github/guidelines/LABELING_GUIDELINES.md)). Not required for external contributors.

## **Pre-merge reviewer checklist**

- [ ] I've manually tested the PR (e.g. pull and build branch, run the app, test code being changed).
- [ ] I confirm that this PR addresses all acceptance criteria described in the ticket it closes and includes the necessary testing evidence such as recordings and or screenshots.

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-996df5dd-08aa-463e-9f57-398f2be10247?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-996df5dd-08aa-463e-9f57-398f2be10247&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
