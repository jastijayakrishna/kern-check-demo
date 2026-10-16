# Add listAll/getAll pagination helpers to monitors, imports, and events

## Summary

Adds missing pagination convenience helpers (`list_all`/`get_all` in Python, `listAll`/`getAll` in JS) to the monitors, imports, and events clients. These helpers automatically iterate through paginated `list()` responses until all items are collected.

Previously only websets, items, and webhooks had these helpers. Now all resources with paginated list endpoints have consistent helper methods.

**Note:** `monitors.runs` was intentionally not given helpers because API testing confirmed that endpoint doesn't support pagination (returns all results at once with `hasMore=false`).

## Review & Testing Checklist for Human

- [ ] Verify the pagination logic matches existing helpers in websets/items/webhooks clients
- [ ] Test `monitors.list_all()` / `monitors.listAll()` with an account that has multiple monitors
- [ ] Test `imports.list_all()` / `imports.listAll()` with an account that has multiple imports  
- [ ] Test `events.list_all()` / `events.listAll()` with an account that has events

**Recommended test:** Run the SDK test scripts from the session to verify helpers work:
```python
from exa_py import Exa
client = Exa(api_key="...")
for monitor in client.websets.monitors.list_all():
    print(monitor.id)
```

### Notes

- There's a separate bug where `MonitorRunStatus` enum is missing `'failed'` value causing validation errors - will be addressed in a separate PR
- Some docstring cleanup happened in the events client as part of the rewrite

Link to Devin run: https://app.devin.ai/sessions/92241ad92562428c91cf01b8f93aaf81
Requested by: ishan@exa.ai
