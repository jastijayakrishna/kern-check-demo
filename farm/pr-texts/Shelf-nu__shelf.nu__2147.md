# feat: add CSV export loaders for note activity

## Summary
- add Remix loaders for `/assets/:assetId/activity.csv` and `/bookings/:bookingId/activity.csv` that stream note activity as CSV with sanitized filenames
- extend CSV utilities to export asset and booking notes with escaped content and localized timestamps
- render CSV export buttons in asset and booking note components and cover the new loaders and UI with Vitest specs

## Testing
- CI=1 npm run test -- --run --reporter=basic

------
https://chatgpt.com/codex/tasks/task_b_68ff5026eca483269b9372f46a9184f1

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Added CSV export functionality for asset and booking activity logs. Users can now download timestamped activity reports containing notes and history for assets and bookings with a single click.

* **Tests**
  * Added test coverage for the new CSV export functionality and related UI components.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
