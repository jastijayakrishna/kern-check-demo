# Chore: fix eslint suppressions — require-no-margin in EmailSharingConfiguration.tsx

**What is this feature?**

Removes the 2 `@grafana/require-no-margin` ESLint suppressions in `public/app/features/dashboard/components/ShareModal/SharePublicDashboard/ConfigPublicDashboard/EmailSharingConfiguration.tsx`, eliminating all suppressions for that file.

Both flagged `<Field>` elements used `className={styles.field}`, where `field` was purely `css({ label: 'field-noMargin', marginBottom: 0 })` — a manual margin-reset workaround. This is replaced with the built-in `noMargin` prop, and the now-unused `field` style key is removed. The `noMargin` prop sets the Field's `marginBottom` to `0`, so the rendered result is identical. Vertical spacing between the fields is already provided by the parent `FieldSet`'s `gap: theme.spacing(3)`, so there is no visual change.

**Why do we need this feature?**

Reduces bulk ESLint suppression tech debt by fixing the underlying violations rather than suppressing them.

**Which issue(s) does this PR fix?**:

N/A

**Special notes for your reviewer:**

- Suppressions removed: 2 (`@grafana/require-no-margin`), regenerated via `yarn lint:prune` — only the target entry was pruned; no new suppressions introduced.
- This is a pure CSS-equivalence change (no runtime behavior change), so no new tests were added.
- Validation: `yarn typecheck` (14 projects) clean, `yarn lint:ts` clean, and the existing `SharePublicDashboard.test.tsx` suite passes (25/25).

---

_This PR was opened by the ESLint tech-debt automation. Anyone should feel free to review and merge it if they're confident in the change. Any questions should be directed to the Grafana Frontend Platform team._

<div><a href="https://cursor.com/agents/bc-b45b2d91-82ed-4796-b458-3bd2511ac4fd?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/automations/99b7f98c-76c7-11f1-ba66-0e7d0216e441"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/view-automation-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/view-automation-light.png"><img alt="View Automation" width="141" height="28" src="https://cursor.com/assets/images/view-automation-dark.png"></picture></a>&nbsp;</div>
