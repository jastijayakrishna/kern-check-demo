# Add checklist template support for projects and quote acceptance

### Motivation
- Allow projects to be bootstrapped from reusable checklist templates and pick a specific template when creating a project or when accepting a quote.

### Description
- Fetch `listChecklistTemplates` in the projects and client detail pages and pass `checklistTemplates` into `ProjectForm` for creation flows.
- Extend `ProjectForm` to accept a `checklistTemplates` prop, filter active templates, and render a `checklistTemplateId` select alongside the existing `seedChecklist` option for new projects.
- Add `resolveDefaultChecklistTemplateId` and `resolveChecklistTemplateIdForQuote` helpers and update `seedProjectChecklist` to accept an optional `templateId` and a `replaceExisting` option while querying `checklist_items` by `template_id` when provided.
- Wire template resolution into `acceptQuote` to seed a project checklist based on quote service items and into `upsertProject` to use the explicitly selected `checklistTemplateId` or fallback to the quote-based resolver, and add `checklistTemplateId` to the `projectSchema` validation.

### Testing
- Ran TypeScript typecheck which completed successfully.
- Performed a Next.js build with `npm run build` which succeeded without errors.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a332549f1d88332bd85ec59f34ebae5)
