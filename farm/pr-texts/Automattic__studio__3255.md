# Add Spotlight keywords for improved discoverability

## Related issues

- Related to [user feedback on X](https://x.com/ddryo_loos/status/2048696454567579980?s=46) that the installed app is hard to find when searching for "WordPress" because the app name is just "Studio".

## How AI was used in this PR

Codex was used to inspect the Electron Forge packaging configuration, test how macOS Spotlight reads app bundle metadata, and apply the focused metadata change. The resulting diff was reviewed and validated locally.

## Proposed Changes

- Add macOS `MDItemKeywords` metadata to the packaged app via Electron Forge `packagerConfig.extendInfo`. This is scoped to macOS app-bundle metadata and does not change Windows or Linux package metadata.
- Include `WordPress`, `WordPress Studio`, `WP`, and `local WordPress development` as Spotlight keywords so the app can be discovered by WordPress-related searches without renaming the app bundle.

## Testing Instructions

1. Build a packaged macOS app:

```sh
npm run make:macos-arm64
```

2. Replace the installed app with the packaged app, or copy it to `/Applications/Studio.app`.

3. Confirm the packaged plist contains the metadata as a comma-separated string:

```sh
/usr/libexec/PlistBuddy -c 'Print :MDItemKeywords' /Applications/Studio.app/Contents/Info.plist
```

Expected output:

```text
WordPress, WordPress Studio, WP, local WordPress development
```

4. Force Spotlight to re-import the app bundle and inspect the indexed metadata:

```sh
mdimport -i /Applications/Studio.app
mdls -name kMDItemKeywords /Applications/Studio.app
```

Expected output should include `WordPress` in `kMDItemKeywords`.

5. Verify the app can be found through a WordPress keyword query:

```sh
mdfind "kMDItemKeywords == '*WordPress*' && kMDItemContentType == 'com.apple.application-bundle'"
```

Expected output should include:

```text
/Applications/Studio.app
```

6. Optional manual check: open Spotlight and search for `WordPress`; Studio should be discoverable.

Local validation run on this branch:

```sh
npm run typecheck
npx prettier --check apps/studio/forge.config.ts
npx ts-node -e "import config from './apps/studio/forge.config'; const keywords = (config.packagerConfig as any).extendInfo?.MDItemKeywords; if (typeof keywords !== 'string' || !keywords.includes('WordPress')) process.exit(1); console.log(keywords);"
```

Note: `npx eslint --fix apps/studio/forge.config.ts` currently fails because `apps/studio/forge.config.ts` is outside the repo's ESLint TypeScript project service configuration.

## Pre-merge Checklist

- [x] Have you checked for TypeScript, React or other console errors?
