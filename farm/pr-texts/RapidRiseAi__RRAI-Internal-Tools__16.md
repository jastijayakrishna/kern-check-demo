# Refactor project checklist seeding

### Motivation

- Ensure new projects receive a coherent, relevant checklist rather than always using the hardcoded starter items.  
- Allow project creators to choose a checklist template when creating a project so seeded items match the project type.  
- Use quote/service information where available to pick a sensible template automatically.  

### Description

- Load active checklist templates in `ProjectForm` and expose a `Checklist template` select for new projects by importing `listChecklistTemplates()` and making the form `async` (`components/forms.tsx`).  
- Extend `projectSchema` to accept an optional `checklistTemplateId` (`lib/validation.ts`).  
- Refactor checklist seeding to accept an optional `templateId?: string`, query `checklist_items` with `.eq("template_id", selectedTemplateId)` when provided, and keep the existing hardcoded fallback if no template items are found (`lib/actions.ts`).  
- Add helper resolution functions to pick a sensible default template (`resolveDefaultChecklistTemplateId`) and to derive a service-specific template from a quote (`resolveChecklistTemplateIdForQuote`) and wire them into `seedProjectChecklist`.  
- Update project creation flows so `upsertProject` and `acceptQuote` pass the selected or derived template id when seeding (`lib/actions.ts`).  

### Testing

- Ran `npm test` (Vitest) and the test suite passed.  
- Ran `npm run typecheck` (`tsc --noEmit`) and type checking succeeded.  
- Ran `npm run lint` (ESLint) and linter completed with no errors.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a332549f1d88332bd85ec59f34ebae5)
