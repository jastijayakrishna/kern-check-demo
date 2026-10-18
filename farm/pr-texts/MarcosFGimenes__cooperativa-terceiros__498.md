# Fix infinite loading on package details by skipping per-service history hydration

### Motivation

- Opening a package could stall on an indefinite server render because the page fetched full progress histories for each service, causing many Firestore queries and a single blocked request to freeze the route.  
- The package overview only needs the canonical progress stored on the service document, while full histories are only required on each service detail page.

### Description

- Removed the per-service history hydration from `src/app/(pcm)/pacotes/[id]/page.tsx` by deleting the `listUpdates` calls and the loop that fetched updates for every service.  
- Removed the `listUpdates` import and left a clarifying comment explaining why histories are no longer loaded during package rendering.  
- The page still fetches package, services and folder lists and continues to use the canonical progress fields on service documents for aggregated views.

### Testing

- Ran lint (`npm run lint`) which completed successfully with no new issues.  
- Ran typecheck (`npm run typecheck`) which reported preexisting TypeScript errors unrelated to this change and did not complete cleanly.  
- Ran unit tests (`npm test` / `vitest`) where 89 tests passed and 5 tests failed in existing suites (`serviceProgress`, `curvaS`, `servicesReferenceDate`); failures are preexisting and not caused by the removed history hydration.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a899393534c8329b0a1679ddc69b8b1)
