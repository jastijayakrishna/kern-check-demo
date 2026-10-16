# Fix optIn in test extension and Playwright runner by using full rules

Task/Issue URL: https://app.asana.com/1/137249556945/project/1201844467387842/task/1213823263615313?focus=true

## Description:
The compact rule format intentionally omits optIn steps to save space (DuckDuckGo browsers only use optOut). This caused the test extension and Playwright runner to silently fail optIn actions — they returned true with 0 clicks since _runRulesSequentially on an empty array is vacuously true.

Fix: when autoAction is 'optIn', send the full rules from rules.json (which includes optIn steps) instead of compact rules. The compact format remains unchanged for the production optOut path.

Changes:
- addon/background.ts: load rules.json alongside compact-rules.json; when config.autoAction is 'optIn', send full rules via the autoconsent field instead of compact rules
- playwright/runner.ts: import full rules from rules.json; when autoAction is 'optIn', send full rules instead of compact rules

## Steps to test this PR:
- test with opt-in mode in test extension

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Low risk: changes are limited to test/QA paths and rule-loading logic, mainly switching the rule payload when `autoAction` is `optIn` to avoid silent no-op behavior.
> 
> **Overview**
> Fixes *opt-in* behavior in the test extension and Playwright harness by sending **full CMP rules** (from `rules.json`) when `config.autoAction === 'optIn'`, since compact rules intentionally omit opt-in steps.
> 
> The background service worker now loads and stores both `compact-rules.json` and full `rules.json`, and selects which bundle to return on `init`. The Playwright runner similarly switches between compact rules for opt-out tests and full rules for opt-in tests.
> 
> <sup>Written by [Cursor Bugbot](https://cursor.com/dashboard?tab=bugbot) for commit 81b1b48ed915b346c22d7178298800a57ba7a589. This will update automatically on new commits. Configure [here](https://cursor.com/dashboard?tab=bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
