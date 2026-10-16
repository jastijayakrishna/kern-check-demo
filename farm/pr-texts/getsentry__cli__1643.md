# fix(sourcemap): crc32 is not a function on Node.js < 20.15 (CLI-34F)

Sentry issues: [CLI-34F](https://sentry.sentry.io/issues/CLI-34F), [CLI-34B](https://sentry.sentry.io/issues/CLI-34B) (same crash, split into two groups)

Fixes CLI-34F
Fixes CLI-34B

## Root cause

`src/lib/sourcemap/zip.ts` imports `crc32` from `node:zlib`, but that API only exists on Node.js >= 20.15 / >= 22.2. The npm package accepts older runtimes (`engines: >=20.0`, and the bundle's version gate allows Node 18+).

## Reproduction

On Node.js 20.0–20.14 (both reports are 20.11 / 20.12), run `sentry sourcemap upload <dir>`, typically through `@sentry/bundler-plugins`. The first `ZipWriter.addEntry()` throws:

```
TypeError: (0 , import_node_zlib.crc32) is not a function
```

I reproduced this on a real Node v20.11.1 by bundling `zip.ts` to CJS (the npm build's output format) and writing an archive with it.

## Fix

New `src/lib/crc32.ts` exports a `crc32` that uses `zlib.crc32` when it exists and otherwise falls back to a table-driven implementation of the same IEEE 802.3 polynomial. The sourcemap `ZipWriter` now imports it instead of `node:zlib`'s `crc32`. Supported Node versions keep the native implementation.

The same bundle on Node v20.11.1 now writes the archive, and `unzip -t` reports every entry's CRC as OK.

## Tests

- `test/lib/crc32.property.test.ts`: the fallback matches `zlib.crc32` on random bytes, continuing from a previous checksum matches hashing the concatenation, and the standard check value (`"123456789"` → `0xCBF43926`) holds.
- `test/lib/sourcemap/zip.mocked.test.ts`: mocks `node:zlib` without `crc32` and checks that `ZipWriter` output passes `unzip -t`. Without the fix it fails with `TypeError: crc32 is not a function`.
- `vitest run test/lib test/commands test/types test/script`: 9988 passed, 1 failed. The failure is `delta-upgrade.mocked.test.ts`, which also fails on `origin/main` in this environment and is unrelated.
- `biome check` and `tsc --noEmit` pass.

## Not in this PR

`src/lib/build/zip-writer.ts` (`sentry build upload`) also imports `zlib.crc32` and has the same latent problem on these Node versions. There are no Sentry reports for that path yet, so it's left for a follow-up that switches it to this helper once this lands.

<div><a href="https://cursor.com/agents/bc-7148c660-a586-4c98-bbd4-4f29d3e6e2c5?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/automations/95624600-485e-4461-829e-6b76f086c473"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/view-automation-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/view-automation-light.png"><img alt="View Automation" width="141" height="28" src="https://cursor.com/assets/images/view-automation-dark.png"></picture></a>&nbsp;</div>
