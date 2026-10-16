# Fix resize handle position during resize interactions

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
### Context
The PR fixes #12670 and the follow-up drag-timer regression in manual row and column resize. After double-click auto-size, the handle is recalculated from the resized header. During a single active drag, the 500 ms double-click timer no longer resets the handle from the header while the guide remains at the dragged offset.

### How has this been tested?
- `pnpm --filter handsontable run test:unit --testPathPattern=manualColumnResize/__tests__/utils.unit`
- `pnpm --filter handsontable run build`
- `pnpm --filter handsontable run test:e2e --testPathPattern='manual(Column|Row)Resize'`
- `pnpm --filter handsontable run eslint -- "src/plugins/manualResize/utils.ts" "src/plugins/manualColumnResize/utils.ts" "src/plugins/manualColumnResize/manualColumnResize.ts" "src/plugins/manualRowResize/manualRowResize.ts" "src/plugins/manualColumnResize/__tests__/utils.unit.js" "src/plugins/manualColumnResize/__tests__/manualColumnResize.spec.js" "src/plugins/manualRowResize/__tests__/manualRowResize.spec.js"`

### Types of changes
- [x] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature or improvement (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality not to work as expected)
- [ ] Additional language file or change to the existing one (translations)

### Related issue(s):
1. #12670

### Affected project(s):
- [x] `handsontable`
- [ ] `@handsontable/angular-wrapper`
- [ ] `@handsontable/react-wrapper`
- [ ] `@handsontable/vue3`

### Checklist:
- [x] I have reviewed the guidelines about [Contributing to Handsontable](https://github.com/handsontable/handsontable/blob/master/CONTRIBUTING.md) and I confirm that my code follows the code style of this project.
- [x] I have signed the [Contributor License Agreement](https://docs.google.com/forms/d/e/1FAIpQLScpMq4swMelvw3-onxC8Jl29m0fVp5hpf7d1yQVklqVjGjWGA/viewform?c=0&w=1)
- [ ] My change requires a change to the documentation.
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-1779b8e1-1de9-4b1a-879a-218e78b75392"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-1779b8e1-1de9-4b1a-879a-218e78b75392"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
