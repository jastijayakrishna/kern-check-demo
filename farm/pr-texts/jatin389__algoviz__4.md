# Add multi-branch GitHub Pages deployment with previews

## Summary

This PR implements a multi-branch deployment system for GitHub Pages, allowing every branch to deploy to the site while maintaining a single GitHub Pages instance. The main branch deploys to the site root, while all other branches deploy to preview folders that are automatically cleaned up when branches are deleted.

## Key Changes

- **New deployment scripts:**
  - `.github/scripts/pages-target.sh`: Determines the target path and base URL for each branch (main → root, others → `preview/<slug>/`)
  - `.github/scripts/publish-pages.sh`: Handles publishing to the `gh-pages` branch with retry logic to handle concurrent deployments from multiple branches

- **Updated CI/CD workflow (`.github/workflows/deploy.yml`):**
  - Changed from using `actions/upload-pages-artifact` and `actions/deploy-pages` to a custom publishing script
  - Now runs on all branches (except `gh-pages` itself) instead of just `main`
  - Concurrency group changed to per-branch (`pages-${{ github.ref }}`) so new pushes to the same branch supersede in-flight deploys without cancelling other branches
  - Passes `VITE_BASE_PATH` environment variable to build step for correct asset paths
  - Simplified permissions to just `contents: write`

- **New cleanup workflow (`.github/workflows/pages-cleanup.yml`):**
  - Automatically removes preview folders when branches are deleted
  - Can also be manually triggered to clean up stale previews

- **Build configuration (`vite.config.ts`):**
  - Made base path configurable via `VITE_BASE_PATH` environment variable for branch-specific builds
  - Maintains `/algoviz/` default for local development

- **Documentation (`README.md`):**
  - Added Deployment section explaining the multi-branch setup and URLs
  - Documents the one-time GitHub Pages source configuration requirement

## Implementation Details

- The publish script rebuilds the `gh-pages` branch from scratch on each run rather than using a worktree, allowing multiple branches to deploy concurrently without conflicts
- Includes retry logic (5 attempts with exponential backoff) to handle race conditions when multiple branches deploy simultaneously
- Preserves the `preview/` directory when deploying main, ensuring other branches' previews survive
- Branch names are normalized to URL-safe slugs (lowercase, special characters → hyphens)
- Includes `.nojekyll` file to prevent Jekyll processing of underscore-prefixed files

https://claude.ai/code/session_01Kkw8ggZGsRisRtQ7WLrufJ
