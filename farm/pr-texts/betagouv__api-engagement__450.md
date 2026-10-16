# refacto: Migrate v0/view endpoint to stat-event repository

## Summary
- add a repository method that serves the v0 view stats endpoint for both Elasticsearch and PostgreSQL backends
- reuse the repository in the view controller so filters and facets work against either storage engine
- extend repository tests to cover the new search logic for both data sources
- reuse the existing `toPg` mapper to resolve PostgreSQL facet column names safely

## Testing
- npm test -- src/repositories/__tests__/stat-event.test.ts

------
https://chatgpt.com/codex/tasks/task_e_68d3dd7c2c4c83248dd813a700f0476f
