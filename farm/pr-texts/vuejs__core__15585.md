# chore(deps): update all non-major dependencies

> ℹ️ **Note**
> 
> This PR body was truncated due to platform limits.

This PR contains the following updates:

| Package | Change | [Age](https://docs.renovatebot.com/merge-confidence/) | [Confidence](https://docs.renovatebot.com/merge-confidence/) | Type | Update |
|---|---|---|---|---|---|
| [@types/node](https://redirect.github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/node) ([source](https://redirect.github.com/DefinitelyTyped/DefinitelyTyped/tree/HEAD/types/node)) | [`^24.13.5` → `^24.19.2`](https://renovatebot.com/diffs/npm/@types%2fnode/24.13.5/24.19.2) | ![age](https://developer.mend.io/api/mc/badges/age/npm/@types%2fnode/24.19.2?slim=true) | ![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@types%2fnode/24.13.5/24.19.2?slim=true) | devDependencies | minor |
| [actions/setup-node](https://redirect.github.com/actions/setup-node) | `v7.0.0` → `v7.1.0` | ![age](https://developer.mend.io/api/mc/badges/age/github-tags/actions%2fsetup-node/v7.1.0?slim=true) | ![confidence](https://developer.mend.io/api/mc/badges/confidence/github-tags/actions%2fsetup-node/v7.0.0/v7.1.0?slim=true) | action | minor |
| [actions/upload-artifact](https://redirect.github.com/actions/upload-artifact) | `v7.0.1` → `v7.0.2` | ![age](https://developer.mend.io/api/mc/badges/age/github-tags/actions%2fupload-artifact/v7.0.2?slim=true) | ![confidence](https://developer.mend.io/api/mc/badges/confidence/github-tags/actions%2fupload-artifact/v7.0.1/v7.0.2?slim=true) | action | patch |
| [playwright](https://playwright.dev) ([source](https://redirect.github.com/microsoft/playwright)) | [`^1.63.0` → `^1.64.0`](https://renovatebot.com/diffs/npm/playwright/1.63.0/1.64.0) | ![age](https://developer.mend.io/api/mc/badges/age/npm/playwright/1.64.0?slim=true) | ![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/playwright/1.63.0/1.64.0?slim=true) | devDependencies | minor |
| [pnpm](https://pnpm.io) ([source](https://redirect.github.com/pnpm/pnpm/tree/HEAD/pnpm/npm/pnpm)) | [`12.4.2` → `12.11.2`](https://renovatebot.com/diffs/npm/pnpm/12.4.2/12.11.2) | ![age](https://developer.mend.io/api/mc/badges/age/npm/pnpm/12.11.2?slim=true) | ![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/pnpm/12.4.2/12.11.2?slim=true) | packageManager | minor |
| [pretty-bytes](https://redirect.github.com/sindresorhus/pretty-bytes) | [`^7.1.3` → `^7.2.0`](https://renovatebot.com/diffs/npm/pretty-bytes/7.1.3/7.2.0) | ![age](https://developer.mend.io/api/mc/badges/age/npm/pretty-bytes/7.2.0?slim=true) | ![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/pretty-bytes/7.1.3/7.2.0?slim=true) | devDependencies | minor |
| [sass](https://redirect.github.com/sass/dart-sass) | [`^1.104.1` → `^1.105.1`](https://renovatebot.com/diffs/npm/sass/1.104.1/1.105.1) | ![age](https://developer.mend.io/api/mc/badges/age/npm/sass/1.105.1?slim=true) | ![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/sass/1.104.1/1.105.1?slim=true) | devDependencies | minor |
| [source-map-js](https://redirect.github.com/7rulnik/source-map-js) | [`^1.2.1` → `^1.2.2`](https://renovatebot.com/diffs/npm/source-map-js/1.2.1/1.2.2) | ![age](https://developer.mend.io/api/mc/badges/age/npm/source-map-js/1.2.2?slim=true) | ![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/source-map-js/1.2.1/1.2.2?slim=true) | pnpm.catalog.default | patch |

---

### Release Notes

<details>
<summary>actions/setup-node (actions/setup-node)</summary>

### [`v7.1.0`](https://redirect.github.com/actions/setup-node/releases/tag/v7.1.0)

[Compare Source](https://redirect.github.com/actions/setup-node/compare/v7.0.0...v7.1.0)

##### What's Changed

##### Enhancements:

- Add support for mise.toml file by [@&#8203;gperdomor](https://redirect.github.com/gperdomor) in [#&#8203;1421](https://redirect.github.com/actions/setup-node/pull/1421)
- Support absolute paths in node-version-file by [@&#8203;v-mahabaleshwars](https://redirect.github.com/v-mahabaleshwars) in [#&#8203;1633](https://redirect.github.com/actions/setup-node/pull/1633)

##### Bug fixes:

- Add Node version validation and manifest fetch retry by [@&#8203;v-jitenderpalsingh](https://redirect.github.com/v-jitenderpalsingh) in [#&#8203;1580](https://redirect.github.com/actions/setup-node/pull/1580)

##### Documentation updates:

- README.md: bump actions/checkout to latest version 7 by [@&#8203;deining](https://redirect.github.com/deining) in [#&#8203;1578](https://redirect.github.com/actions/setup-node/pull/1578)
- docs: add V7 ESM migration and NODE_AUTH_TOKEN behavior change by [@&#8203;v-gowridurgad](https://redirect.github.com/v-gowridurgad) in [#&#8203;1593](https://redirect.github.com/actions/setup-node/pull/1593)
- Fixed cache recommendation syntax by [@&#8203;SubJunk](https://redirect.github.com/SubJunk) in [#&#8203;1603](https://redirect.github.com/actions/setup-node/pull/1603)

##### Dependency updates:

- Update workflow pins and migrate Node matrices to modern versions by [@&#8203;v-HarithaVattikuti](https://redirect.github.com/v-HarithaVattikuti) in [#&#8203;1583](https://redirect.github.com/actions/setup-node/pull/1583)
- Upgrade  [@&#8203;actions/cache](https://redirect.github.com/actions/cache) to 6.2.0 by [@&#8203;philip-gai](https://redirect.github.com/philip-gai) in [#&#8203;1584](https://redirect.github.com/actions/setup-node/pull/1584)
- Pin [@&#8203;types/node](https://redirect.github.com/types/node) to v24 by [@&#8203;v-priyagupta108](https://redirect.github.com/v-priyagupta108) in [#&#8203;1585](https://redirect.github.com/actions/setup-node/pull/1585)
- Override brace-expansion to 5.0.8 by [@&#8203;v-priyagupta108](https://redirect.github.com/v-priyagupta108) with [@&#8203;Copilot](https://redirect.github.com/Copilot) in [#&#8203;1599](https://redirect.github.com/actions/setup-node/pull/1599)
- Upgrade  actions/checkout from 7.0.0 to 7.0.1 by [@&#8203;dependabot](https://redirect.github.com/dependabot) in [#&#8203;1598](https://redirect.github.com/actions/setup-node/pull/1598)
- Upgrade  prettier from 3.8.4 to 3.9.6 by [@&#8203;dependabot](https://redirect.github.com/dependabot) in [#&#8203;1590](https://redirect.github.com/actions/setup-node/pull/1590)
- Upgrade  [@&#8203;vercel/ncc](https://redirect.github.com/vercel/ncc) from 0.44.0 to 0.45.0 by [@&#8203;dependabot](https://redirect.github.com/dependabot) in [#&#8203;1610](https://redirect.github.com/actions/setup-node/pull/1610)
- Upgrade  pnpm/action-setup from 6.0.9 to 6.0.10 by [@&#8203;dependabot](https://redirect.github.com/dependabot) in [#&#8203;1602](https://redirect.github.com/actions/setup-node/pull/1602)
- Upgrade  baseline-browser-mapping from 2.10.38 to 2.11.22 by [@&#8203;dependabot](https://redirect.github.com/dependabot) in [#&#8203;1629](https://redirect.github.com/actions/setup-node/pull/1629)
- Upgrade [@&#8203;types/semver](https://redirect.github.com/types/semver) from 7.7.1 to 7.8.0 by [@&#8203;dependabot](https://redirect.github.com/dependabot) in [#&#8203;1616](https://redirect.github.com/actions/setup-node/pull/1616)
- Upgrade [@&#8203;typescript-eslint/parser](https://redirect.github.com/typescript-eslint/parser) from 8.62.0 to 8.70.0 by [@&#8203;dependabot](https://redirect.github.com/dependabot) in [#&#8203;1615](https://redirect.github.com/actions/setup-node/pull/1615)
- Upgrade pnpm/action-setup from 6.0.10 to 6.1.0 by [@&#8203;dependabot](https://redirect.github.com/dependabot) in [#&#8203;1631](https://redirect.github.com/actions/setup-node/pull/1631)
- Upgrade jest-each from 30.4.1 to 30.5.2 by [@&#8203;dependabot](https://redirect.github.com/dependabot) in [#&#8203;1636](https://redirect.github.com/actions/setup-node/pull/1636)
- Upgrade eslint-plugin-n from 18.1.0 to 18.3.0 by [@&#8203;dependabot](https://redirect.github.com/dependabot) in [#&#8203;1638](https://redirect.github.com/actions/setup-node/pull/1638)
- Update dependencies and add license files by [@&#8203;v-HarithaVattikuti](https://redirect.github.com/v-HarithaVattikuti) in [#&#8203;1642](https://redirect.github.com/actions/setup-node/pull/1642)
- Upgrade eslint from 10.5.0 to 10.11.0 and package.json from 7.0.0 to 7.1.0 by [@&#8203;dependabot](https://redirect.github.com/dependabot) in [#&#8203;1635](https://redirect.github.com/actions/setup-node/pull/1635)

##### New Contributors

- [@&#8203;v-jitenderpalsingh](https://redirect.github.com/v-jitenderpalsingh) made their first contribution in [#&#8203;1580](https://redirect.github.com/actions/setup-node/pull/1580)
- [@&#8203;philip-gai](https://redirect.github.com/philip-gai) made their first contribution in [#&#8203;1584](https://redirect.github.com/actions/setup-node/pull/1584)
- [@&#8203;gperdomor](https://redirect.github.com/gperdomor) made their first contribution in [#&#8203;1421](https://redirect.github.com/actions/setup-node/pull/1421)
- [@&#8203;SubJunk](https://redirect.github.com/SubJunk) made their first contribution in [#&#8203;1603](https://redirect.github.com/actions/setup-node/pull/1603)

**Full Changelog**: <https://github.com/actions/setup-node/compare/v7.0.0...v7.1.0>

</details>

<details>
<summary>actions/upload-artifact (actions/upload-artifact)</summary>

### [`v7.0.2`](https://redirect.github.com/actions/upload-artifact/releases/tag/v7.0.2)

[Compare Source](https://redirect.github.com/actions/upload-artifact/compare/v7.0.1...v7.0.2)

#### What's Changed

- Improves artifact download retries when the service returns HTTP 429 (rate limiting), including honoring valid Retry-After headers.
- Updates [@&#8203;actions/artifact](https://redirect.github.com/actions/artifact) to v6.3.1.

#### New Contributors

- [@&#8203;tunc-d](https://redirect.github.com/tunc-d) made their first contribution in [#&#8203;821](https://redirect.github.com/actions/upload-artifact/pull/821)

**Full Changelog**: <https://github.com/actions/upload-artifact/compare/v7.0.1...v7.0.2>

</details>

<details>
<summary>microsoft/playwright (playwright)</summary>

### [`v1.64.0`](https://redirect.github.com/microsoft/playwright/releases/tag/v1.64.0)

[Compare Source](https://redirect.github.com/microsoft/playwright/compare/v1.63.0...v1.64.0)

#### 🧰 WebMCP

New [page.webmcp](https://playwright.dev/docs/api/class-page#page-webmcp) and [frame.webmcp](https://playwright.dev/docs/api/class-frame#frame-webmcp) give access to the tools that a page registers through the experimental [WebMCP](https://playwright.dev/docs/api/class-webmcp) browser API, so you can test them like any other part of your app:

```js
const browser = await chromium.launch({ args: ['--enable-features=WebMCP'] });
const page = await browser.newPage();
await page.goto('https://example.com');

for (const tool of await page.webmcp.tools())
  console.log(tool.name, tool.description);

const result = await page.webmcp.callTool('add', { a: 2, b: 40 });
console.log(result.content[0].text); // "42"
```

[Playwright MCP](https://playwright.dev/docs/getting-started-mcp) also supports WebMCP by default, with page-defined tools offered to the agent as `webmcp_<tool>`. Pass `--no-webmcp` to opt out.

[`playwright-cli`](https://playwright.dev/docs/getting-started-cli) exposes them as well:

```bash
playwright-cli webmcp-list
playwright-cli webmcp-call search_catalog --params '{"query":"cats"}'
```

#### 🎬 Better videos

Videos can now be recorded at a custom frame rate, and the decorations for actions are styled with plain CSS:

```js
// playwright.config.ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    video: {
      mode: 'on',
      size: { width: 1920, height: 1080 },
      fps: 60,
      show: {
        actions: {
          style: {
            point: 'width: 20px; height: 20px; border-radius: 50%; background: red',
            highlight: 'outline: 2px solid #&#8203;333; background: rgba(0, 128, 255, .15)',
            title: 'font-size: 16px',
          },
        },
      },
    },
  },
});
```

- New `fps` option in [testOptions.video](https://playwright.dev/docs/api/class-testoptions#test-options-video), [`recordVideo`](https://playwright.dev/docs/api/class-browser#browser-new-context-option-record-video) and
  [screencast.start()](https://playwright.dev/docs/api/class-screencast#screencast-start). Firefox and WebKit currently capture up to 25 frames per second.
- New [`style`](https://playwright.dev/docs/api/class-screencast#screencast-show-actions-option-style) option takes CSS declarations for the `point` marker, the target
  `highlight` and the action `title`. It replaces the `fontSize` option, which is now deprecated.
- The cursor stays visible at the last action point, survives navigations and travels along a natural, eased path.
- Videos are encoded with VP9 instead of VP8, which takes less CPU and produces smaller files of the same or better
  quality.
- All video options are also available in [Playwright MCP](https://playwright.dev/docs/getting-started-mcp) and [`playwright-cli`](https://playwright.dev/docs/getting-started-cli).

#### 🎯 Test runner

- New [testProject.default](https://playwright.dev/docs/api/class-testproject#test-project-default) option keeps a project in the config without running it by default. You can configure every browser you care about, and let a plain `npx playwright test` run just your favourite one:

  ```js
  // playwright.config.ts
  import { defineConfig, devices } from '@playwright/test';

  export default defineConfig({
    projects: [
      { name: 'chromium', use: devices['Desktop Chrome'] },
      { name: 'firefox', use: devices['Desktop Firefox'], default: false },
      { name: 'webkit', use: devices['Desktop Safari'], default: false },
    ],
  });
  ```

  ```bash
  npx playwright test                     # runs chromium only
  npx playwright test --project=firefox   # runs firefox
  npx playwright test --project="*"       # runs all three, for example on CI
  ```

- New `--shuffle` command line option schedules tests in a random order, which helps to find tests that accidentally depend on each other.

  ```bash
  npx playwright test --shuffle
  # Running 42 tests using 4 workers, shuffle seed 271828182
  # ...

  # Pass the seed to reproduce the same order.
  npx playwright test --shuffle 271828182
  ```

- New `lock` option in [test.describe.configure()](https://playwright.dev/docs/api/class-test#test-describe-configure) adds [test locks](https://playwright.dev/docs/test-parallel#test-locks) to all tests in a file or a group:

  ```js
  test.describe.configure({ lock: 'user-settings' });
  ```

- New `type` option of `toHaveScreenshot` in [testConfig.expect](https://playwright.dev/docs/api/class-testconfig#test-config-expect) stores all unnamed screenshots as WebP:

  ```js
  // playwright.config.ts
  export default defineConfig({
    expect: {
      toHaveScreenshot: { type: 'webp' },
    },
  });
  ```

#### 🪆 Locator.within()

New [locator.within()](https://playwright.dev/docs/api/class-locator#locator-within) combines two locators that you already have, reading in the natural order —
"this button, within that dialog":

```js
const saveButton = page.getByRole('button', { name: 'Save' });
const dialog = page.getByTestId('settings-dialog');

await saveButton.within(dialog).click();
```

Relative locators such as [locator.nth()](https://playwright.dev/docs/api/class-locator#locator-nth) or [locator.first()](https://playwright.dev/docs/api/class-locator#locator-first) are resolved inside each parent
separately, which makes column-like queries straightforward:

```js
// The third cell of every row, not the third cell in the table.
const thirdColumn = page.getByRole('cell').nth(2).within(page.getByRole('row'));
await expect(thirdColumn).toHaveText(['Apple', 'Banana', 'Cherry']);
```

#### New APIs

- New [page.getByRef()](https://playwright.dev/docs/api/class-page#page-get-by-ref) locates an element by its aria ref, such as `e2`, reported by [page.ariaSnapshot()](https://playwright.dev/docs/api/class-page#page-aria-snapshot) in the `'ai'` mode.
- New option [`includeShadow`](https://playwright.dev/docs/api/class-page#page-content-option-include-shadow) in [page.content()](https://playwright.dev/docs/api/class-page#page-content) and [frame.content()](https://playwright.dev/docs/api/class-frame#frame-content) serializes open shadow roots as [declarative shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM#declaratively_with_html).
- New option [`signCount`](https://playwright.dev/docs/api/class-credentials#credentials-create-option-sign-count) sets the initial signature counter of a virtual credential. [credentials.create()](https://playwright.dev/docs/api/class-credentials#credentials-create) and [credentials.get()](https://playwright.dev/docs/api/class-credentials#credentials-get) return the current `signCount`, and it is saved and restored together with the credentials in the storage state.
- New [fullConfig.filteredProjects](https://playwright.dev/docs/api/class-fullconfig#full-config-filtered-projects) lists the projects that were selected to run after applying the `--project` filter. It is available in global setup and reporters.
- New [apiRequestContext.addCookies()](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-add-cookies), [apiRequestContext.cookies()](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-cookies) and [apiRequestContext.clearCookies()](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-clear-cookies) manage cookies of a request context, mirroring the [BrowserContext](https://playwright.dev/docs/api/class-browsercontext) methods:

  ```js
  await request.addCookies([{ name: 'session-id', value: '42', url: 'https://example.com' }]);
  console.log(await request.cookies('https://example.com'));
  await request.clearCookies({ name: 'session-id' });
  ```

#### Breaking changes ⚠️

- `screen` property is now forwarded from the [device descriptors](https://playwright.dev/docs/emulation#devices). If you use `...devices['Desktop Chrome']` and alike, `window.screen` and media queries now see the emulated screen size. You can opt-out by explicitly setting `screen` to `undefined`:

  ```js
  // playwright.config.ts
  export default defineConfig({
    use: {
      ...devices['Desktop Chrome'],
      screen: undefined,
    },
  });
  ```

- JSX in your test files now follows your `tsconfig.json`. Playwright compiles JSX in test files according to the `jsx`, `jsxFactory`, `jsxFragmentFactory` and `jsxImportSource` [tsconfig options](https://playwright.dev/docs/test-typescript#tsconfig-jsx-options), and defaults to the automatic runtime from `react/jsx-runtime`.

- `--update-snapshots=missing` now passes the test run. Tests that only create missing snapshots now pass in the `'missing'` mode of [testConfig.updateSnapshots](https://playwright.dev/docs/api/class-testconfig#test-config-update-snapshots), so that CI can generate new snapshots and verify the existing ones in a single run. The mode used when the option is not specified is now called `'default'` and behaves as before: missing snapshots are written and the test fails.

- Elements inside hidden iframes are considered hidden. Elements inside an iframe that is not visible, for example with `visibility: hidden`, are now considered hidden by actions, [locator.isVisible()](https://playwright.dev/docs/api/class-locator#locator-is-visible) and [expect(locator).toBeVisible()](https://playwright.dev/docs/api/class-locatorassertions#locator-assertions-to-be-visible).

#### Browser Versions

- Chromium 156.0.8078.4
- Mozilla Firefox 157.0
- WebKit 27.2

This version was also tested against the following stable channels:

- Google Chrome 155
- Microsoft Edge 155

</details>

<details>
<summary>pnpm/pnpm (pnpm)</summary>

### [`v12.11.2`](https://redirect.github.com/pnpm/pnpm/releases/tag/v12.11.2): pnpm 12.11.2

[Compare Source](https://redirect.github.com/pnpm/pnpm/compare/v12.11.1...v12.11.2)

This release fixes `--workspace-concurrency=Infinity`, filters set by an `updateConfig` hook, and store fetches with `enable-modules-dir=false`.

##### Patch Changes

- `--workspace-concurrency=Infinity` now runs workspace projects with no concurrency limit. It used to fail with `invalid digit found in string` [#&#8203;16793](https://redirect.github.com/pnpm/pnpm/issues/16793).

- `pnpm install` and other recursive commands now apply the `filter` and `filterProd` that an `updateConfig` hook sets. They used to run on every workspace project [#&#8203;16792](https://redirect.github.com/pnpm/pnpm/issues/16792).

- `enable-modules-dir=false` now also fetches the packages an install reuses from an existing lockfile, so the store holds every package the lockfile lists.

<!-- sponsors -->

#### Platinum Sponsors

<table>
  <tbody>
    <tr>
      <td align="center" valign="middle">
        <a href="https://bit.cloud/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer"><img src="https://pnpm.io/img/users/bit.svg" width="80" alt="Bit"></a>
      </td>
      <td align="center" valign="middle">
        <a href="https://openai.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/openai_dark.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/openai_light.svg" />
            <img src="https://pnpm.io/img/users/openai_dark.svg" width="160" alt="OpenAI" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://notion.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer"><img src="https://pnpm.io/img/users/notion.svg" width="80" alt="Notion"></a>
      </td>
    </tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://coderabbit.ai/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/coderabbit.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/coderabbit_light.svg" />
            <img src="https://pnpm.io/img/users/coderabbit.svg" width="220" alt="CodeRabbit" />
          </picture>
        </a>
      </td>
    </tr>
  </tbody>
</table>

#### Gold Sponsors

<table>
  <tbody>
    <tr>
      <td align="center" valign="middle">
        <a href="https://sanity.io/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/sanity.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/sanity_light.svg" />
            <img src="https://pnpm.io/img/users/sanity.svg" width="120" alt="Sanity" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://discord.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/discord.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/discord_light.svg" />
            <img src="https://pnpm.io/img/users/discord.svg" width="220" alt="Discord" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://vite.dev/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer"><img src="https://pnpm.io/img/users/vitejs.svg" width="42" alt="Vite"></a>
      </td>
    </tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://serpapi.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/serpapi_dark.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/serpapi_light.svg" />
            <img src="https://pnpm.io/img/users/serpapi_dark.svg" width="160" alt="SerpApi" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://stackblitz.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/stackblitz.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/stackblitz_light.svg" />
            <img src="https://pnpm.io/img/users/stackblitz.svg" width="190" alt="Stackblitz" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://workleap.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/workleap.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/workleap_light.svg" />
            <img src="https://pnpm.io/img/users/workleap.svg" width="190" alt="Workleap" />
          </picture>
        </a>
      </td>
    </tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://nx.dev/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/nx.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/nx_light.svg" />
            <img src="https://pnpm.io/img/users/nx.svg" width="50" alt="Nx" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://latitude.so/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer"><img src="https://pnpm.io/img/users/latitude.svg" width="160" alt="Latitude"></a>
      </td>
    </tr>
  </tbody>
</table>

<!-- sponsors end -->

### [`v12.11.1`](https://redirect.github.com/pnpm/pnpm/releases/tag/v12.11.1): pnpm 12.11.1

[Compare Source](https://redirect.github.com/pnpm/pnpm/compare/v12.11.0...v12.11.1)

This release fixes two ways `pnpm install` could fail, runs tools of any Rust release through `pnx`, and treats `registry.npmjs.com` as an alias of the npm registry.

##### Patch Changes

- `pnpm install` no longer fails when `packageManager` pins the pnpm version that is already running and the registry does not publish that version. pnpm warns and continues. A registry mirror that has not synced a release no longer blocks the commands of a project pinned to it.

- `pnpm install` no longer fails with `ERR_PNPM_CMD_SHIM_CHMOD` when `node_modules/.bin` holds a shim that another user created, if everyone can already execute it and it is not world-writable. This happens when several users share one checkout.

- `enable-modules-dir=false` (`enableModulesDir: false` through the Node.js addon) fetches the registry packages the host can install into the store again, as pnpm v10 did, while still writing nothing under `node_modules`. The setting exists for a `node_modules` that something else mounts from the store, such as a FUSE daemon, and that consumer no longer has to download each package on first access. A plain `--lockfile-only` run still fetches nothing.

- `pnpm pack` and `pnpm publish` no longer put `.npmignore` and `.gitignore` files in the tarball. A `files` entry that names one still ships it.

- pnpm now treats `https://registry.npmjs.com/` as an alias of `https://registry.npmjs.org/`. Registry requests, credentials, and trusted publishing use the canonical hostname.

- `pnx --package=rust@<channel> <tool>` runs a tool of that Rust release, for example `pnx --package=rust@nightly-2026-01-01 cargo build`. pnpm installs the release with the components and targets from `rust-toolchain.toml` and the target of each `--target` argument.

- `pnpm install` now links agent skills for more coding agents. It detects the agent from `ANTIGRAVITY_AGENT`, `COPILOT_AGENT`, `COPILOT_CLI`, `CODEX_THREAD_ID`, `CODEX_SANDBOX`, `AI_AGENT`, and `CLAUDE_CODE` [pnpm/tasks#116](https://redirect.github.com/pnpm/tasks/issues/116).

- When the registry rejects `pnpm stage publish`, the error message now starts with "Failed to stage package".

<!-- sponsors -->

#### Platinum Sponsors

<table>
  <tbody>
    <tr>
      <td align="center" valign="middle">
        <a href="https://bit.cloud/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer"><img src="https://pnpm.io/img/users/bit.svg" width="80" alt="Bit"></a>
      </td>
      <td align="center" valign="middle">
        <a href="https://openai.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/openai_dark.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/openai_light.svg" />
            <img src="https://pnpm.io/img/users/openai_dark.svg" width="160" alt="OpenAI" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://notion.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer"><img src="https://pnpm.io/img/users/notion.svg" width="80" alt="Notion"></a>
      </td>
    </tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://coderabbit.ai/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/coderabbit.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/coderabbit_light.svg" />
            <img src="https://pnpm.io/img/users/coderabbit.svg" width="220" alt="CodeRabbit" />
          </picture>
        </a>
      </td>
    </tr>
  </tbody>
</table>

#### Gold Sponsors

<table>
  <tbody>
    <tr>
      <td align="center" valign="middle">
        <a href="https://sanity.io/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/sanity.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/sanity_light.svg" />
            <img src="https://pnpm.io/img/users/sanity.svg" width="120" alt="Sanity" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://discord.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/discord.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/discord_light.svg" />
            <img src="https://pnpm.io/img/users/discord.svg" width="220" alt="Discord" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://vite.dev/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer"><img src="https://pnpm.io/img/users/vitejs.svg" width="42" alt="Vite"></a>
      </td>
    </tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://serpapi.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/serpapi_dark.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/serpapi_light.svg" />
            <img src="https://pnpm.io/img/users/serpapi_dark.svg" width="160" alt="SerpApi" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://stackblitz.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/stackblitz.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/stackblitz_light.svg" />
            <img src="https://pnpm.io/img/users/stackblitz.svg" width="190" alt="Stackblitz" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://workleap.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/workleap.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/workleap_light.svg" />
            <img src="https://pnpm.io/img/users/workleap.svg" width="190" alt="Workleap" />
          </picture>
        </a>
      </td>
    </tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://nx.dev/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/nx.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/nx_light.svg" />
            <img src="https://pnpm.io/img/users/nx.svg" width="50" alt="Nx" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://latitude.so/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer"><img src="https://pnpm.io/img/users/latitude.svg" width="160" alt="Latitude"></a>
      </td>
    </tr>
  </tbody>
</table>

<!-- sponsors end -->

### [`v12.11.0`](https://redirect.github.com/pnpm/pnpm/releases/tag/v12.11.0): pnpm 12.11.0

[Compare Source](https://redirect.github.com/pnpm/pnpm/compare/v12.10.1...v12.11.0)

This release adds Rust toolchain management, links the agent skills that dependencies ship, adds the `permissions` setting, and keeps the colors of streamed script output.

##### Minor Changes

- `pnpm install` now links the agent skills that direct dependencies ship under `skills/<name>/SKILL.md` into the project's agent skill directories, such as `.claude/skills`. A package's skills are linked only after you approve them with `pnpm approve`. The `skills.dirs` setting chooses the directories [pnpm/rfcs#35](https://redirect.github.com/pnpm/rfcs/pull/35).

  Added the `permissions` setting, which records what each dependency may do. Its `build` capability works like `allowBuilds` and takes precedence over it. `pnpm approve-builds` writes to `permissions` when `pnpm-workspace.yaml` already has it, and to `allowBuilds` otherwise.

  Added `pnpm permissions`, which lists the granted and denied permissions and the packages awaiting approval. `pnpm approve` reviews build scripts and agent skills in one prompt [pnpm/rfcs#36](https://redirect.github.com/pnpm/rfcs/pull/36).

- pnpm now installs and runs Rust toolchains.

  - With `cargo.enabled`, `pnpm install` installs the toolchain named in `rust-toolchain.toml`. pnpm verifies the release signature, stores the toolchain once per machine, and links it into `.pnpm/rust`. `pnpm run` and `pnpm exec` put its `cargo` and `rustc` on the `PATH`.
  - `pnpm add -g rust@<channel>` installs a toolchain globally. The `cargo` and `rustc` commands run it outside projects that pin their own. `pnpm update -g`, `pnpm ls -g`, and `pnpm remove -g` manage it like any global package.
  - In a project, `pnpm add rust@<channel>` pins the toolchain in `rust-toolchain.toml`.
  - `pnpm shim add rust` adds project-aware shims for `cargo`, `rustc`, and the other Rust tools. In a project with a `rust-toolchain.toml`, they run the toolchain the file names and install it on first use. Elsewhere, the next command of the same name on `PATH` runs, such as rustup's.

- `pnpm run` and `pnpm exec` now keep the colors of script output that they print under the project's name, such as with `--stream`. pnpm sets `FORCE_COLOR=1` for these scripts when its own output is in color, unless `FORCE_COLOR` is already set.

  Script output is also rendered more cleanly:

  - A line that a progress bar redraws with `\r` shows only its last state.
  - Escape codes that move the cursor or clear the screen are dropped.
  - Long colored lines are cut at the terminal width.
  - `pnpm -r run` no longer garbles its live output when a script fails while other scripts are still running.

##### Patch Changes

##### Installing packages

- pnpm no longer panics with "unexpected error when polling the I/O driver" when it runs under QEMU user-mode emulation, such as a `linux/amd64` container on an Apple Silicon Mac [#&#8203;16696](https://redirect.github.com/pnpm/pnpm/issues/16696).

- `pnpm view`, `pnpm update`, and other commands that read registry metadata now work behind proxies that end a response by closing the connection without a TLS `close_notify` alert [#&#8203;16704](https://redirect.github.com/pnpm/pnpm/issues/16704).

- pnpm now switches to the version a project pins in `packageManager` or `devEngines.packageManager` even when `pnpm-workspace.yaml` has a setting the running pnpm cannot read, such as a `lockfile.includeResolutionSettings` section. If pnpm does not switch, it still reports that setting [#&#8203;16675](https://redirect.github.com/pnpm/pnpm/issues/16675).

- When the `pnpm` package has to download its native binary on first run, it now uses the registry and credentials from `.npmrc` and from the `npm_config_registry` and `pnpm_config_registry` environment variables. `COREPACK_NPM_REGISTRY` still takes precedence. A project `.npmrc` is not read when `COREPACK_INTEGRITY_KEYS` turns off the signature check [#&#8203;16655](https://redirect.github.com/pnpm/pnpm/issues/16655).

- `pnpm install` and `pnpm add --config` now apply `minimumReleaseAge` when they resolve a config dependency. A config dependency range resolves to the newest version that is old enough, so a later clean `pnpm install --frozen-lockfile` accepts the lockfile [#&#8203;16660](https://redirect.github.com/pnpm/pnpm/issues/16660).

- `pnpm remove` with `catalogPrune` no longer removes catalog entries that `pnpm-lock.yaml` still records for workspace projects missing from disk. Before, a following frozen install failed with `ERR_PNPM_LOCKFILE_CONFIG_MISMATCH` [#&#8203;16679](https://redirect.github.com/pnpm/pnpm/issues/16679).

- With `cargo.enabled`, `pnpm install` now writes the source replacement for vendored crates into `.pnpm/crates/config.toml` and includes it as optional from `.cargo/config.toml`. A checkout without `.pnpm` builds with plain Cargo [#&#8203;16659](https://redirect.github.com/pnpm/pnpm/issues/16659).

- With `nodeLinker.type` set to `loaded`, Node.js now stops with `ERR_PNPM_LOADER_UNSUPPORTED_NODE` when it preloads the store loader on a version the loader cannot serve. The supported versions are `^24.18.0 || >=26.2.0`. On other versions, CommonJS packages imported from ESM failed with `Cannot find module` on their first relative `require()`.

- On Windows, `pnpm install` no longer fails with "The filename, directory name, or volume label syntax is incorrect" when a package contains a file whose name is invalid on Windows, such as `icon.svg?as=metadata.d.ts`. pnpm removes the invalid characters from the name and prints a warning that lists the renamed files.

- On Windows, hoisting no longer fails intermittently with link errors when a junction is created or replaced concurrently [pnpm/tasks#53](https://redirect.github.com/pnpm/tasks/issues/53).

##### Resolving dependencies

- `pnpm install --no-optional` now installs the peer dependencies a project declares when `autoInstallPeers` is on. The lockfile marked such a peer `optional: true` when another dependency had it as an optional peer.

- `pnpm install` and `pnpm dedupe` now link an optional peer to the workspace package that the workspace root depends on when the picked version matches it. They installed the registry package with the same name and version [#&#8203;16706](https://redirect.github.com/pnpm/pnpm/issues/16706).

- Removal overrides such as `"debug>supports-color": "-"` now also apply to an optional peer that a package declares only in `peerDependenciesMeta` [#&#8203;16681](https://redirect.github.com/pnpm/pnpm/issues/16681).

- `pnpm add` and other installs that re-resolve dependencies now keep the locked `devEngines.runtime` version while it still satisfies the declared range [#&#8203;16764](https://redirect.github.com/pnpm/pnpm/issues/16764).

- `pnpm audit --fix update` now updates only the dependencies whose locked version is vulnerable [#&#8203;14928](https://redirect.github.com/pnpm/pnpm/issues/14928).

- `pnpm outdated` and `pnpm update --interactive` now apply `overrides` before they look up the latest version. Before, a dependency overridden to an npm alias was compared with the latest version of the package the override replaces [#&#8203;16719](https://redirect.github.com/pnpm/pnpm/issues/16719).

##### Patched dependencies

- Patches saved with CRLF line endings now apply, including a patch that creates or deletes a file. pnpm rejected the git headers of such a patch with `ERR_PNPM_INVALID_PATCH` and the message `invalid file mode: 100644` [#&#8203;16641](https://redirect.github.com/pnpm/pnpm/issues/16641).

- A patch that changes a file's mode, such as adding or removing the executable bit, now applies the new mode on Unix [pnpm/tasks#110](https://redirect.github.com/pnpm/tasks/issues/110).

##### Injected dependencies and deploy

- With `sharedWorkspaceLockfile: false`, an injected workspace package installed in the same run as its dependent now holds only the files its `files` field selects. The copy also held other files of the project, such as `tsconfig.json` [#&#8203;16683](https://redirect.github.com/pnpm/pnpm/issues/16683).

- A script listed in `syncInjectedDepsAfterScripts` no longer fails when it rewrites `package.json` while pnpm is copying its edits into the injected copies. The sync after the script now replaces a half-copied manifest.

- `pnpm deploy` with a shared lockfile no longer fails with `ERR_PNPM_LOCKFILE_CONFIG_MISMATCH` for `settings.dedupeInjectedDeps` or `settings.dedupePeerDependents` when `lockfile.includeResolutionSettings` is enabled. The deployed lockfile now records both settings as `false`, the values the deploy installs with.

- `pnpm deploy` now writes the dependencies in the deployed `package.json` sorted by name. It also sorts the `allowBuilds` entries in the deployed `pnpm-workspace.yaml`. Repeated deploys of the same lockfile now produce identical files [#&#8203;16687](https://redirect.github.com/pnpm/pnpm/issues/16687).

##### Packing and publishing

- `pnpm pack` and `pnpm publish` now match `.npmignore` and `.gitignore` rules the way npm does. A negation such as `!lib/**` or `!lib/**/!(*.map)` re-includes files under a directory that an earlier `*` rule excluded [#&#8203;16743](https://redirect.github.com/pnpm/pnpm/issues/16743).

- `pnpm pack` and `pnpm publish` no longer always include root files that merely start with `README`, `LICENSE`, or `LICENCE`, such as `README_INTERNAL.md`. Only `README`, `LICENSE`, `LICENCE`, and `COPYING`, with or without an extension, ship regardless of `files` and `.npmignore`, as in npm [#&#8203;16753](https://redirect.github.com/pnpm/pnpm/issues/16753).

- `pnpm publish --provenance=false` and `--no-provenance` now turn off provenance under trusted publishing, so a package can be published from a self-hosted runner. Setting `provenance: false` in `pnpm-workspace.yaml` does the same [#&#8203;16721](https://redirect.github.com/pnpm/pnpm/issues/16721).

##### Speed and resource use

- `pnpm install` hardlinks files from a group-writable or world-writable store again. pnpm copied every file from such a store into `node_modules` [#&#8203;16677](https://redirect.github.com/pnpm/pnpm/issues/16677).

- A repeat `pnpm install` no longer imports patched packages and packages with build scripts again when nothing changed. Their builds no longer run again either. This happened when `recursiveInstall` was `false` or the project had a `file:` dependency [#&#8203;16705](https://redirect.github.com/pnpm/pnpm/issues/16705).

- Verifying the lockfile against `trustPolicy` and `minimumReleaseAge` uses less memory. pnpm no longer keeps every published version's manifest of each checked package in memory until the install ends [#&#8203;16656](https://redirect.github.com/pnpm/pnpm/issues/16656).

- `pnpm rebuild <pkg>` and `pnpm rebuild --pending` no longer read the manifest of every installed package to find build scripts. Only the selected packages are inspected and built. On a large `node_modules` served lazily, such as over a network or FUSE mount, this turned a rebuild of a few packages into a fetch of every package.

- `pnpm rebuild` no longer removes and recreates `node_modules` when the settings recorded in `node_modules/.modules.yaml` differ from the current configuration. The rebuild runs the build scripts against the installed packages as they are.

- `pnpm store prune` now compacts the store's `index.db` after removing package entries, so the file shrinks again [#&#8203;16717](https://redirect.github.com/pnpm/pnpm/issues/16717).

##### Registry commands

- `pnpm whoami`, `pnpm bugs`, `pnpm docs`, `pnpm repo`, `pnpm star`, `pnpm unstar`, and `pnpm stars` now honor the `--registry` option.

- `--registry` now takes precedence over a scope's configured registry for scoped packages in `pnpm access`, `pnpm view`, `pnpm repo`, `pnpm star`, `pnpm unstar`, `pnpm owner`, `pnpm deprecate`, `pnpm undeprecate`, `pnpm unpublish`, `pnpm dist-tag`, `pnpm team`, and `pnpm stage`. Without `--registry`, `pnpm access` now sends a scoped package or scope to the registry configured for that scope.

- Registry commands now keep the path of a registry URL such as `https://example.com/npm/` when they build request URLs. This applies to `pnpm access`, `pnpm owner`, `pnpm ping`, `pnpm search`, `pnpm star`, `pnpm stars`, `pnpm team`, `pnpm unstar`, and `pnpm whoami`.

- `pnpm view` now honors the network retry settings.

- `pnpm repo` now fetches the repository URLs of several packages in parallel.

<!-- sponsors -->

#### Platinum Sponsors

<table>
  <tbody>
    <tr>
      <td align="center" valign="middle">
        <a href="https://bit.cloud/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer"><img src="https://pnpm.io/img/users/bit.svg" width="80" alt="Bit"></a>
      </td>
      <td align="center" valign="middle">
        <a href="https://openai.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/openai_dark.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/openai_light.svg" />
            <img src="https://pnpm.io/img/users/openai_dark.svg" width="160" alt="OpenAI" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://notion.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer"><img src="https://pnpm.io/img/users/notion.svg" width="80" alt="Notion"></a>
      </td>
    </tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://coderabbit.ai/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/coderabbit.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/coderabbit_light.svg" />
            <img src="https://pnpm.io/img/users/coderabbit.svg" width="220" alt="CodeRabbit" />
          </picture>
        </a>
      </td>
    </tr>
  </tbody>
</table>

#### Gold Sponsors

<table>
  <tbody>
    <tr>
      <td align="center" valign="middle">
        <a href="https://sanity.io/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/sanity.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/sanity_light.svg" />
            <img src="https://pnpm.io/img/users/sanity.svg" width="120" alt="Sanity" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://discord.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/discord.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/discord_light.svg" />
            <img src="https://pnpm.io/img/users/discord.svg" width="220" alt="Discord" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://vite.dev/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer"><img src="https://pnpm.io/img/users/vitejs.svg" width="42" alt="Vite"></a>
      </td>
    </tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://serpapi.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/serpapi_dark.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/serpapi_light.svg" />
            <img src="https://pnpm.io/img/users/serpapi_dark.svg" width="160" alt="SerpApi" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://stackblitz.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/stackblitz.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/stackblitz_light.svg" />
            <img src="https://pnpm.io/img/users/stackblitz.svg" width="190" alt="Stackblitz" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://workleap.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/workleap.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/workleap_light.svg" />
            <img src="https://pnpm.io/img/users/workleap.svg" width="190" alt="Workleap" />
          </picture>
        </a>
      </td>
    </tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://nx.dev/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/nx.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/nx_light.svg" />
            <img src="https://pnpm.io/img/users/nx.svg" width="50" alt="Nx" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://latitude.so/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer"><img src="https://pnpm.io/img/users/latitude.svg" width="160" alt="Latitude"></a>
      </td>
    </tr>
  </tbody>
</table>

<!-- sponsors end -->

### [`v12.10.1`](https://redirect.github.com/pnpm/pnpm/releases/tag/v12.10.1): pnpm 12.10.1

[Compare Source](https://redirect.github.com/pnpm/pnpm/compare/v12.10.0...v12.10.1)

This release fixes `pnpm install` failures after an `overrides` change and on a filtered frozen install with `catalogPrune`. It also fixes several bugs in the experimental `nodeLinker.type: loaded`, which now keeps its generated files in `node_modules`.

##### Patch Changes

- With `nodeLinker.type: loaded`, pnpm now writes its generated files to `node_modules`, which projects already ignore in git. The store manifest and loader are `node_modules/.pnpm/.store-manifest.json` and `node_modules/.pnpm/.store-loader.mjs`. Bin shims are in `node_modules/.bin`.

  Earlier versions wrote `.pnpm-store.json` and `.pnpm-store-loader.mjs` to the project root, and a `.pnpm` directory to the root and to each workspace package. Delete them after reinstalling.

- With `nodeLinker.type: loaded`, packages that ship their own `node_modules` directory, such as `npm` with its bundled dependencies, now load from the store. Before, one such package in the install stopped every Node.js process from starting.

- With `nodeLinker.type: loaded`, scripts can now run a Node.js runtime installed through `devEngines.runtime`. Before, every script that called `node` re-ran its own shim until it failed with "Argument list too long".

- With `nodeLinker.type: loaded`, Node.js processes start faster. In a project with 13,000 stored files, the startup overhead per process dropped from 67 ms to 18 ms.

- `pnpm install` no longer fails with `ERR_PNPM_NO_MATCHING_VERSION` after a change to `overrides` when the lockfile resolves an optional peer dependency to an npm alias of another package [#&#8203;16654](https://redirect.github.com/pnpm/pnpm/issues/16654).

- A frozen install with `catalogPrune` no longer removes catalog entries that `pnpm-lock.yaml` still records. Before, `pnpm install --frozen-lockfile --filter` failed with `ERR_PNPM_LOCKFILE_CONFIG_MISMATCH` when some workspace projects were missing from disk [#&#8203;16638](https://redirect.github.com/pnpm/pnpm/issues/16638).

- `pnpm install --fix-lockfile` no longer removes the `deprecated` and `hasBin` fields from lockfile entries [#&#8203;6600](https://redirect.github.com/pnpm/pnpm/issues/6600).

- With `enableGlobalVirtualStore`, an install that updates `node_modules` now repairs a package in the global virtual store that an interrupted install left without some of its dependency links or package files. Before, such an install kept the incomplete package if the project's `node_modules` already recorded it [#&#8203;16642](https://redirect.github.com/pnpm/pnpm/issues/16642).

- `pnpm install` now skips the Cargo and Python projects inside a nested directory that has its own `pnpm-workspace.yaml` or `.git` directory, such as a git worktree of the same workspace or a separate clone.

- The `Request took` warning for package metadata now starts timing when pnpm sends the request. Before, it also counted the time the request waited for a free request slot, so large installs printed it for requests the registry answered quickly.

<!-- sponsors -->

#### Platinum Sponsors

<table>
  <tbody>
    <tr>
      <td align="center" valign="middle">
        <a href="https://bit.cloud/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer"><img src="https://pnpm.io/img/users/bit.svg" width="80" alt="Bit"></a>
      </td>
      <td align="center" valign="middle">
        <a href="https://openai.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/openai_dark.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/openai_light.svg" />
            <img src="https://pnpm.io/img/users/openai_dark.svg" width="160" alt="OpenAI" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://notion.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank" rel="noopener noreferrer"><img src="https://pnpm.io/img/users/notion.svg" width="80" alt="Notion"></a>
      </td>
    </tr>
    <tr>
      <td align="center" valign="middle">
      

> ❗ **Important**
> 
> ✂ PR body was truncated to here.


</details>

---

### Configuration

📅 **Schedule**: (UTC)

- Branch creation
  - Between 12:00 AM and 03:59 AM, only on Monday (`* 0-3 * * 1`)
- Automerge
  - At any time (no schedule defined)

🚦 **Automerge**: Disabled by config. Please merge this manually once you are satisfied.

♻ **Rebasing**: Whenever PR becomes conflicted, or you tick the rebase/retry checkbox.

👻 **Immortal**: This PR will be recreated if closed unmerged. Get [config help](https://redirect.github.com/renovatebot/renovate/discussions) if that's undesired.

---

 - [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job log](https://developer.mend.io/github/vuejs/core).
<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0NC4xMDMuMCIsInVwZGF0ZWRJblZlciI6IjQ0LjEzNC4xIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6WyJkZXBlbmRlbmNpZXMiXX0=-->

