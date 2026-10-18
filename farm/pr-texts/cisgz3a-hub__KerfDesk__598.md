# fix(ui): geometry fields refresh after a canvas resize rescales the shape

See commit 5527dffa: canvas drag-resize scales the transform, never the spec; the debounced draft reconciled only on spec changes, freezing W/H/radius at pre-drag numbers. Fix keys the input on display scale (remount on rescale; typing unaffected). Failing test first (red '20' vs '40' on main), 24/24 green with fix; tsc/eslint/prettier clean. Sync-audit finding 1.
