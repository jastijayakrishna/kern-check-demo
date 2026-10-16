# feat: Add inventory views with PatternFly data-view library PoC

Implements a proof of concept for the new PatternFly data-view library as an alternative to the existing systems table. Adds feature flag support to toggle between the current implementation and the new data-view based approach.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Summary by Sourcery

Introduce a proof-of-concept inventory view using PatternFly DataView and enable it via a feature flag fallback to the existing systems table.

New Features:
- Implement SystemsDataViewTable component using PatternFly DataView to display systems
- Add InventoryViews page component and a useInventoryViewsFeatureFlag hook to toggle between the new DataView and the existing Systems table

Build:
- Add @patternfly/react-data-view dependency to package.json
