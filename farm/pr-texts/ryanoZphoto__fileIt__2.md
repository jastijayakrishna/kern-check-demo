# feat: support multiple alternative scenarios

## Summary
- expand default scenarios to include Alt B–D
- build suggestions to populate multiple alternatives and compare all scenarios
- make scenario names editable

## Testing
- `npm run lint`
- `npm test`


------
https://chatgpt.com/codex/tasks/task_e_68c6060aa050832fb6ae7c9f4885bb46

## Summary by Sourcery

Add support for multiple alternative scenarios (Alt B–D) with generic cloning and suggestion features, make scenario names editable, and refactor UI and summary logic to handle dynamic scenario counts

New Features:
- Introduce Alt B, Alt C, and Alt D scenarios in default state
- Provide a generic cloneScenario function and buildScenarioSuggestions to generate alternative scenario suggestions
- Enable editing scenario names directly in the UI

Enhancements:
- Refactor summary calculation to compute metrics for all scenarios via a unified summaries object
- Dynamically render ScenarioCard components and comparison grid based on the scenarios list instead of hardcoded pairs
