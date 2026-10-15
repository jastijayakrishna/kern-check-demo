# Display usage for queries in automations

## Description

Adds a counter on the query edit pages (both SQL/non-REST queries and REST API endpoints) showing how many automations reference the current query. Per [PClmnt's review feedback](https://github.com/Budibase/budibase/pull/18627#issuecomment-4335712892), this is rolled into the existing **Usage** button rather than a separate button — the popover now renders both a `Screens` section (existing) and an `Automations` section (new).

The lookup runs entirely against the already-loaded `automationStore`, scanning each automation's serialised `definition` for the query's `_id`, so `EXECUTE_QUERY`, `API_REQUEST` and any other step that stores a `queryId` are all picked up.

## Addresses
- https://github.com/Budibase/budibase/issues/18513

## Screenshots

| Closed: single `Usage: N` button | Open: popover with `Automations` section |
|---|---|
| ![Usage button closed](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmctNzZmZGJjOWY3NTAxNDZmZWI5MDI3MTNkMzU4MjlmY2MiLCJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmctNzZmZGJjOWY3NTAxNDZmZWI5MDI3MTNkMzU4MjlmY2MvY2M2YjUxODAtMTBlOS00YzgxLWI1ZDctNGVkMDU1OGMzN2I2IiwiaWF0IjoxNzc3Mzg1NDUzLCJleHAiOjE3Nzc5OTAyNTMsImZpbGVuYW1lIjoic2NyZWVuc2hvdF8zMWM4MDdjYzhiZDU0NzY1YjZhOThjZTg1NmViMjNkYS5wbmcifQ.uoSCW-vqpINS4nb5ZCc0suZspTsHM7k0TDcV9KO2ND0) | ![Usage popover open](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmctNzZmZGJjOWY3NTAxNDZmZWI5MDI3MTNkMzU4MjlmY2MiLCJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmctNzZmZGJjOWY3NTAxNDZmZWI5MDI3MTNkMzU4MjlmY2MvNjAwMjUxN2MtZDM4OC00ZTAyLWIxNTItODEyY2UzYjhkNzI1IiwiaWF0IjoxNzc3Mzg1NDUzLCJleHAiOjE3Nzc5OTAyNTMsImZpbGVuYW1lIjoic2NyZWVuc2hvdF82MTIxNDBiODVkMTA0Y2QwOGM0MjBhN2U4ZmNhZjU4Yi5wbmcifQ.NAX7bzlIDhPeSGGMInrBfg8SA5fe23_BFuNm0r3csiw) |
| One consolidated `Usage: 1` button (replaces the previous separate `Usage` + `Automations` buttons) | Popover titled `Usage` showing the `Automations` section with the connected automation. Empty `Screens` section is hidden when there are no connected screens; both sections render when both are present. |

## Launchcontrol

Query editing pages now show a single `Usage: N` counter that surfaces both screens and automations referencing the query, with deep-links to each.

Link to Devin session: https://app.devin.ai/sessions/caadaade17d5426b849254a8f19f02e6
Requested by: @PClmnt
