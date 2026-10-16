# feat(transaction-footer): linhas do Footer/Summary usam a Transaction List Read Only (MR-908)

## Description

This is a follow-up to MR-908 (#1277). In Figma, each main item and detail row of `Transaction Summary / Footer` and `Transaction Summary / Aside` is an instance of **Transaction List Read Only**. The main item uses `Density=Default`, the details use `Density=Compact`, and every row has no icon and no divider. The code drew these rows by hand, with only a label, a value and `info`. That left out the strikethrough, the amount types and the tag from Content List Amount.

- `TransactionSummaryContent` now draws each row with `TransactionListReadOnly`: `content` and `amount` at size `sm`, `inverted: false` by default, `showDivider={false}`, and density `default` for the main item and `compact` for the details.
- New type `TransactionSummaryItem = { content, amount }`, with the Content List Default and Content List Amount props (without `size`). Rows now accept every amount type (`default`, `positive`, `negative`, `inactive`, `strikethrough`, `strikethrough-neutral`), `strikethroughValue`, `tag` and `info`.
- `TransactionRow` (`label`/`value`/`info`) still works and is `@deprecated`. It is converted to `{ content: { title }, amount: { value, info } }`. `label`/`value`/`info` changed from `ReactNode` to `string`. No consumer uses 1.147 yet.
- The Total keeps its current rendering. It gets its own type, `TransactionTotal`.
- The hand-built row CSS was removed from `_transaction-footer.scss`.
- In Storybook, the fixtures and snippets use the new format. `Visual tests / Transaction Summary` has a combination with every type, the tag and a content with description. The pt/en texts now say that each row is a Transaction List Read Only.

Fixes # (MR-908)

## Types of changes

- [ ] Bug fix (non-breaking change which fixes an issue)
- [x] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [x] This change requires a documentation update

## How Has This Been Tested?

- Jest `TransactionFooter.test.tsx` and `TransactionSummary.test.tsx` (19 tests): the legacy row, the strikethrough types, positive/negative/inactive, the tag, compact vs default density, and no divider inside the rows.
- ESLint, Stylelint, the locale lint, the library build and the Storybook build pass.
- `tsc -b` only fails on errors already on master, in `CrossSellCard.stories.tsx`.
- Before/after comparison of Footer Default, Footer Highlight and Aside: the rows look the same.

## Screenshots (if appropriate):

![Footer Default](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmdfWndQZUNIY3E5aGpjcmhzRC81OTY5N2VkNi0zNzI5LTRiYjktYjFiYS0xNTVkNzVmNmM5ZjQiLCJpYXQiOjE3OTE5OTg2NTUsIm9yZ19pZCI6Im9yZ19ad1BlQ0hjcTloamNyaHNEIiwiZmlsZW5hbWUiOiJzc19kOTdiMWQwZi5wbmcifQ.XV4D3w3WbeXpGQBW3dQe5hjzF55gw6YGWa3q5PoVEJo)
![Visual tests Footer](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmdfWndQZUNIY3E5aGpjcmhzRC9hNmU2NjExNS1mYjhlLTRjNDQtYTY0MC0wMDUxZjhkYzUxNWQiLCJpYXQiOjE3OTE5OTg2NTUsIm9yZ19pZCI6Im9yZ19ad1BlQ0hjcTloamNyaHNEIiwiZmlsZW5hbWUiOiJzc18xYTMwOTY3OC5wbmcifQ.Lih7ZIOU8pEqwtsggxVH3ce3B-pXgsSO9unjCDCASmo)

## Checklist:

- [ ] I have read the [CONTRIBUTING](CONTRIBUTING.md) document
- [x] I have performed a self-review of my own code
- [x] My changes generate no new warnings
- [ ] My changes work in Chrome, Edge, and Firefox
- [x] I have made corresponding changes to the documentation (if appropriate)
- [x] I have added tests that prove my fix is effective or that my feature works
- [x] All new and existing tests passed

Link to Devin session: https://app.devin.ai/sessions/2636f28b4ca74a92b7a508a441684539
Open in Devin Desktop: https://app.devin.ai/desktop/session/2636f28b4ca74a92b7a508a441684539?variant=devin
Requested by: @igor-monteiro-almeida
