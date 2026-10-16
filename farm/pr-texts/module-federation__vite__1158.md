# fix: Keep React DOM Sharing Client-Safe

## Summary

  Prevents `react-dom/server*` from being automatically added to client share sets through `COMMON_SHARED_SUBPATHS`.

  Browser-safe subpaths remain automatically shared:

  - `react-dom/client`
  - `react-dom/profiling`

  During SSR, server subpaths resolve normally or can be configured as explicit shared keys.

  No public API changes.
