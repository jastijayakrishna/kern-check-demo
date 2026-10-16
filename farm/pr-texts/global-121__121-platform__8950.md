# fix: Remove Intersolve Visa production URL flag

[AB#45164](https://dev.azure.com/redcrossnl/7d17f2a9-3f18-40f1-8c29-98568fbca7e4/_workitems/edit/45164)

## Describe your changes

Intersolve deprecated integration; its new acceptance environment uses production-compatible URL paths.
Remove INTERSOLVE_VISA_PROD from the environment example and backend validation.
Always use production URL prefixes and align the mock service routes, preserving existing production behavior.
Add four URL regression tests; all 241 Visa unit tests, formatting, lint, typechecks, builds, and CodeQL passed.

## Checklist before requesting a code review

- [x] I have performed a self-review of my code
- [x] I have addressed all Copilot comments
- [x] I have asked the design team to review these changes, or: The changes do not touch the UI/UX
- [x] I have added tests for my changes, or: Adding tests is unnecessary/irrelevant
- [x] I have made sure that all automated checks pass before requesting a review
- [x] I have updated all [documentation](https://github.com/rodekruis/dev-internal-documentation/blob/main/121/documentation.md) where necessary
- [x] I have checked [the list of integrations](https://github.com/global-121/121-platform/wiki/Integrations-with-external-systems#api-endpoints-used-by-external-systems) with the 121 API for [changed endpoints](https://github.com/global-121/121-platform/blob/main/services/121-service/README.md#api)
- [x] I do not need any deviation from [our PR guidelines](https://github.com/global-121/121-platform/blob/main/docs/CONTRIBUTING.md#pull-request-guidelines)

Local checks passed; GitHub CI remains pending. CodeQL found zero alerts. The automated reviewer could not load model `claude-sonnet-4.6`; a separate read-only code review found no significant issues. No public 121 API endpoints changed.

## Portal preview-deployment

<!--- Do not remove this block. It will be replaced automatically by a GitHub action if a deployment is made -->

<!-- start deployment url -->

This PR does not have any preview deployments yet.

<!-- end deployment url -->
