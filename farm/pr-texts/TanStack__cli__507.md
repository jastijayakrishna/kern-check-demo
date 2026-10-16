# feat(cli): add Render and Vercel deployment targets

## Summary

Adds first-class Render and Vercel deployment targets for React and Solid TanStack Start apps. Both providers are Gold partners in the CLI deployment picker.

## Render

- Generates a `render.yaml` Blueprint with commands for the selected package manager
- Uses Nitro's `render-com` preset and the generated package `start` script
- Pins Render's supported Bun version when Bun is selected, including `--no-install` scaffolds
- Documents Render's standard **New > Blueprint** flow

## Vercel

- Generates Nitro's Vercel Build Output API deployment
- Adds explicit TanStack Start framework detection through `vercel.json`
- Uses Sentry's serverless entry setup when Sentry is also selected
- Packages Sentry dependencies inside the Vercel function instead of leaving unresolved externals

## Compatibility

- Supports React and Solid file-router apps
- Supports npm, Yarn, pnpm, and Bun
- Rejects Deno early with a clear package-manager compatibility error

## Usage

```bash
npx @tanstack/cli create my-render-app --deployment render
npx @tanstack/cli create my-vercel-app --deployment vercel
```

## Validation

- All 10 workspace projects build
- 265 `@tanstack/create` tests pass
- 101 CLI tests pass
- 7 blocking browser tests pass
- Generated React and Solid deployment scaffolds build successfully
- Render and Vercel local deployment previews return HTTP 200
- Vercel plus Sentry emits Build Output API v3 with Sentry dependencies packaged in the function

Includes a minor changeset for `@tanstack/cli` and `@tanstack/create`.
