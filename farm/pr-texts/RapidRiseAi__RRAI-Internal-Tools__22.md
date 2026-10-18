# Add checklist template selection and seeding for projects and quotes

### Motivation

- Provide a way to select a checklist template when creating a project and to seed project checklists from templates automatically. 
- Ensure a project created from an accepted quote can inherit a checklist tied to the quote's service. 

### Description

- Added checklist template support to the project creation UI by extending `ProjectForm` with an optional `checklistTemplates` prop and a selector for `checklistTemplateId`, while preserving the existing "Add starter checklist" option. 
- Refactored checklist seeding logic in `lib/actions.ts`: introduced `resolveDefaultChecklistTemplateId`, `resolveChecklistTemplateIdForQuote`, and updated `seedProjectChecklist` to accept an optional `templateId` and `replaceExisting` option. 
- Hooked checklist seeding into workflows: `upsertProject` will seed from the explicit `checklistTemplateId` or resolve from the accepted `quoteId`, and `acceptQuote` will seed the new project from the quote's service template when available. 
- Updated pages to fetch `listChecklistTemplates()` and pass templates into the project form, added `checklistTemplateId` to `projectSchema` validation, and introduced `ChecklistTemplate` types and a lightweight `ProjectFormWithChecklist` casting wrapper where needed. 

### Testing

- Performed TypeScript type-check with `tsc --noEmit`, which completed successfully. 
- No automated unit tests were modified by this change.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a332549f1d88332bd85ec59f34ebae5)
