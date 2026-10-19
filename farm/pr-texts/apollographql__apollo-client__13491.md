# chore(deps): update dependency vitest to v4 [security]

> [!NOTE]
> This PR body was truncated due to platform limits.

This PR contains the following updates:

| Package | Change | [Age](https://docs.renovatebot.com/merge-confidence/) | [Adoption](https://docs.renovatebot.com/merge-confidence/) | [Passing](https://docs.renovatebot.com/merge-confidence/) | [Confidence](https://docs.renovatebot.com/merge-confidence/) |
|---|---|---|---|---|---|
| [vitest](https://vitest.dev) ([source](https://redirect.github.com/vitest-dev/vitest/tree/HEAD/packages/vitest)) | [`3.2.6` → `4.1.11`](https://renovatebot.com/diffs/npm/vitest/3.2.6/4.1.11) | ![age](https://developer.mend.io/api/mc/badges/age/npm/vitest/4.1.11?slim=true) | ![adoption](https://developer.mend.io/api/mc/badges/adoption/npm/vitest/4.1.11?slim=true) | ![passing](https://developer.mend.io/api/mc/badges/compatibility/npm/vitest/3.2.6/4.1.11?slim=true) | ![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/vitest/3.2.6/4.1.11?slim=true) |

---

> [!WARNING]
> Some dependencies could not be looked up. Check the [Dependency Dashboard](../issues/11062) for more information.

---

### Vitest: Path Traversal / Arbitrary File Read via @&#8203;vitest/mocker Redirect Mock
[CVE-2026-84373](https://nvd.nist.gov/vuln/detail/CVE-2026-84373) / [GHSA-82fw-gwwq-j7x9](https://redirect.github.com/advisories/GHSA-82fw-gwwq-j7x9)

<details>
<summary>More information</summary>

#### Details
##### Summary
`@vitest/mocker` registers a redirect mock's target path without validating it
against the dev server's file-serving allowlist. An attacker who can reach the
dev server's WebSocket can register a redirect mock pointing outside the project
root; when the mocked module is requested, the plugin's `load` hook returns
`readFile(<attacker path>)` as the module source, disclosing local files.

This is exploitable **without authentication** only through the public
`mockerPlugin` / standalone `interceptorPlugin` exports (used by third-party dev
servers), which register the handler on Vite's unauthenticated HMR socket.
Vitest's own browser mode registers mocks over a **token-authenticated** RPC and
is not remotely reachable by default (see Scope).

##### Affected code
`packages/mocker/src/node/interceptorPlugin.ts`.

The `load` hook is the file-read sink:

```ts
if (mock.type === 'redirect') {
  return readFile(mock.redirect, 'utf-8')
}
```

`mock.redirect` is derived from client input at registration time with no
boundary check:

```ts
if (event.type === 'redirect') {
  const redirectUrl = new URL(event.redirect)
  event.redirect = join(server.config.root, redirectUrl.pathname)
}
registry.register(event)
```

There is no `server.fs.allow` / `server.fs.deny` check and no assertion that the
resolved path stays within the project root.

##### Registration paths and trust boundaries
- **Public `mockerPlugin` / `interceptorPlugin` (unauthenticated).** In
  `configureServer`, the plugin registers `server.ws.on('vitest:interceptor:register', …)`
  on Vite's HMR WebSocket. That socket performs no token, Origin, or same-origin
  check, so any client that can reach it can register a redirect mock. This is
  the path the "unauthenticated" impact applies to.
- **Vitest browser mode (authenticated).** Mocks register over the browser RPC
  (`registerMock`), which sits behind a per-run token (`isValidApiRequest`, a
  random `api.token`). The interceptor's `configureServer` socket is not used for
  registration here (in v5 it does not run at all, as the plugin is injected per
  environment). The same missing boundary check exists on the authenticated RPC
  path, but reaching it requires the token, so it is not a remote-unauthenticated
  read.

##### Path handling
`new URL(redirect).pathname` combined with `join(root, pathname)` does **not**
confine reads to the root:

- Special/hierarchical schemes (`file:`, `http:`) are normalized by WHATWG URL,
  so `..` segments are collapsed and the result stays under the root. Payloads of
  the form `file:///../../etc/passwd` do **not** escape.
- A non-special (opaque) scheme preserves `..` in `pathname`, so
  `join(root, "../../…/etc/passwd")` resolves outside the root and reads an
  arbitrary file.

Even without escaping the root, the missing `server.fs` check allows reading any
in-root file the dev server would otherwise refuse to serve (for example an
in-root `.env` or source that is denied by `server.fs.deny`).

##### Scope / preconditions
- This is a **development-server** issue. The dev server binds to `localhost` by
  default and is not reachable from the network unless the developer exposes it
  (`server.host` / `0.0.0.0`, a LAN bind, or a proxy).
- A raw (non-browser) client against a reachable server bypasses browser origin
  and CORS protections entirely and can both register the mock and read the
  response.
- A browser-based drive-by against a localhost server is substantially mitigated
  by Vite defaults: the default CORS origin allowlist is limited to `localhost`
  origins, and `server.allowedHosts` blocks DNS-rebinding, so a cross-origin page
  cannot read the file contents back.

##### Impact
Disclosure of local files readable by the dev-server process (source, in-root
`.env`/secrets, and, via the opaque-scheme payload, files outside the project
root). No integrity or availability impact.

##### Affected versions
Present since `@vitest/mocker` was introduced.

- **Affected: `@vitest/mocker` >= 2.1.0** (shipped in `vitest` and
  `@vitest/browser` >= 2.1.0), through 4.1.x and the 5.0.0 pre-releases.
- **Fixed:** Vitest 4.1.11 and 5.0.0. Older majors (2.1.x, 3.x) are not
  maintained and are not planned to receive the fix.

##### Fix
Validate the resolved redirect target against Vite's file-serving allowlist
(`isFileLoadingAllowed`) before registering it, at every registration site, and
stop registering the interceptor WebSocket events in Vitest's browser mode
(mocks there flow through the authenticated RPC).

#### Severity
- CVSS Score: 5.9 / 10 (Medium)
- Vector String: `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N`

#### References
- [https://github.com/vitest-dev/vitest/security/advisories/GHSA-82fw-gwwq-j7x9](https://redirect.github.com/vitest-dev/vitest/security/advisories/GHSA-82fw-gwwq-j7x9)
- [https://nvd.nist.gov/vuln/detail/CVE-2026-84373](https://nvd.nist.gov/vuln/detail/CVE-2026-84373)
- [https://github.com/vitest-dev/vitest/pull/10972](https://redirect.github.com/vitest-dev/vitest/pull/10972)
- [https://github.com/vitest-dev/vitest/pull/10974](https://redirect.github.com/vitest-dev/vitest/pull/10974)
- [https://github.com/vitest-dev/vitest/commit/51edf2b072902aec6d30c90ebaafd8f121c6f9d8](https://redirect.github.com/vitest-dev/vitest/commit/51edf2b072902aec6d30c90ebaafd8f121c6f9d8)
- [https://github.com/vitest-dev/vitest/commit/8ff9b9a9efca7c6cfd5243569440de8d7a33aec4](https://redirect.github.com/vitest-dev/vitest/commit/8ff9b9a9efca7c6cfd5243569440de8d7a33aec4)
- [https://github.com/vitest-dev/vitest/commit/fe5a11d3ceac5ec10d6d7d21a46d4caca132c48f](https://redirect.github.com/vitest-dev/vitest/commit/fe5a11d3ceac5ec10d6d7d21a46d4caca132c48f)
- [https://github.com/vitest-dev/vitest/releases/tag/v4.1.11](https://redirect.github.com/vitest-dev/vitest/releases/tag/v4.1.11)
- [https://github.com/vitest-dev/vitest/releases/tag/v5.0.0-rc.2](https://redirect.github.com/vitest-dev/vitest/releases/tag/v5.0.0-rc.2)
- [https://github.com/advisories/GHSA-82fw-gwwq-j7x9](https://redirect.github.com/advisories/GHSA-82fw-gwwq-j7x9)

This data is provided by the [GitHub Advisory Database](https://redirect.github.com/advisories/GHSA-82fw-gwwq-j7x9) ([CC-BY 4.0](https://redirect.github.com/github/advisory-database/blob/main/LICENSE.md)).
</details>

---

### Release Notes

<details>
<summary>vitest-dev/vitest (vitest)</summary>

### [`v4.1.11`](https://redirect.github.com/vitest-dev/vitest/releases/tag/v4.1.11)

[Compare Source](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.10...v4.1.11)

#####    🐞 Bug Fixes

- Revive global concurrency limit for test lifecycle \[backport to v4]  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) and [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;10992](https://redirect.github.com/vitest-dev/vitest/issues/10992) [<samp>(5146d)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/5146df80b)
- **browser**:
  - Encode iframeId in tester iframe URL \[backport to v4]  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va), **Pduhard** and **Claude Opus 4.8** in [#&#8203;10955](https://redirect.github.com/vitest-dev/vitest/issues/10955) [<samp>(10b2c)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/10b2cd201)
  - Trigger playwright/chromium gc on lower disk availability \[backport to v4]  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa), **Hiroshi Ogawa** and **OpenCode** in [#&#8203;10951](https://redirect.github.com/vitest-dev/vitest/issues/10951) [<samp>(9851d)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/9851dbc41)
- **mocker**:
  - Restrict redirect mocks to the fs allowlist \[backport to v4]  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;10974](https://redirect.github.com/vitest-dev/vitest/issues/10974) [<samp>(fe5a1)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/fe5a11d3c)

#####     [View changes on GitHub](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.10...v4.1.11)

### [`v4.1.10`](https://redirect.github.com/vitest-dev/vitest/releases/tag/v4.1.10)

[Compare Source](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.9...v4.1.10)

#####    🐞 Bug Fixes

- **browser**: Check fs access in builtin commands \[backport to v4]  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa), **Hiroshi Ogawa** and **OpenCode (claude-opus-4-8)** in [#&#8203;10680](https://redirect.github.com/vitest-dev/vitest/issues/10680) [<samp>(5c18d)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/5c18dd267)
- **vm**: Fix external module resolve error with deps optimizer query for encoded URI \[backport to v4]  -  by [@&#8203;SveLil](https://redirect.github.com/SveLil) and [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;10661](https://redirect.github.com/vitest-dev/vitest/issues/10661) [<samp>(bae52)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/bae52b511)

#####     [View changes on GitHub](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.9...v4.1.10)

### [`v4.1.9`](https://redirect.github.com/vitest-dev/vitest/releases/tag/v4.1.9)

[Compare Source](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.8...v4.1.9)

##### 🐞 Bug Fixes

- Fix `importOriginal` with optimizer and query import \[backport to v4] - by **Hiroshi Ogawa**, **David Harris**, **Codex**and **Vladimir** in [#&#8203;10546](https://redirect.github.com/vitest-dev/vitest/issues/10546) [<samp>(a5180)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/a5180190c)
- **browser**:
  - Wait for orchestrator readiness before resolving browser sessions \[backport to v4] - by **Vladimir** and **Séamus O'Connor** in [#&#8203;10555](https://redirect.github.com/vitest-dev/vitest/issues/10555) [<samp>(7fb29)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/7fb29651a)
  - Wait for iframe tester readiness before preparing  \[backport to v4] - by **Vladimir** and **Séamus O'Connor** in [#&#8203;10497](https://redirect.github.com/vitest-dev/vitest/issues/10497) and [#&#8203;10556](https://redirect.github.com/vitest-dev/vitest/issues/10556) [<samp>(fbc62)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/fbc626c40)
- **mocker**:
  - Hoist vi.mock() for vite-plus/test imports \[backport to v4] - by **Hiroshi Ogawa**, **LongYinan**, **Claude Opus 4.8** and **Vladimir** in [#&#8203;10548](https://redirect.github.com/vitest-dev/vitest/issues/10548) [<samp>(2c955)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/2c9559c02)
- **pool**:
  - Prevent test run hang on worker crash  \[backport to v4] - by **Ari Perkkiö** and **Jattioui Ismail** in [#&#8203;10543](https://redirect.github.com/vitest-dev/vitest/issues/10543) and [#&#8203;10564](https://redirect.github.com/vitest-dev/vitest/issues/10564) [<samp>(934b0)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/934b0f587)

##### [View changes on GitHub](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.8...v4.1.9)

### [`v4.1.8`](https://redirect.github.com/vitest-dev/vitest/releases/tag/v4.1.8)

[Compare Source](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.7...v4.1.8)

#####    🐞 Bug Fixes

- **browser**:
  - Disable client `cdp` API when `allowWrite/allowExec: false` \[backport to v4]  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) and **Codex** in [#&#8203;10450](https://redirect.github.com/vitest-dev/vitest/issues/10450) [<samp>(e4067)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/e4067b3b1)
  - Remove orphaned Playwright route when same module is mocked via multiple ids \[backport to v4]  -  by [@&#8203;toxik](https://redirect.github.com/toxik) and [@&#8203;Zelys-DFKH](https://redirect.github.com/Zelys-DFKH) in [#&#8203;10474](https://redirect.github.com/vitest-dev/vitest/issues/10474) [<samp>(675b4)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/675b4343f)

#####     [View changes on GitHub](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.7...v4.1.8)

### [`v4.1.7`](https://redirect.github.com/vitest-dev/vitest/releases/tag/v4.1.7)

[Compare Source](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.6...v4.1.7)

#####    🐞 Bug Fixes

- **runner**: Limit concurrency per task branch in addition to per leaf callbacks (backport)  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;10384](https://redirect.github.com/vitest-dev/vitest/issues/10384) [<samp>(4f0f2)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/4f0f2a1ee)

#####     [View changes on GitHub](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.6...v4.1.7)

### [`v4.1.6`](https://redirect.github.com/vitest-dev/vitest/releases/tag/v4.1.6)

[Compare Source](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.5...v4.1.6)

#####    🐞 Bug Fixes

- **browser**: Provide project reference in `ToMatchScreenshotResolvePath`  -  by [@&#8203;macarie](https://redirect.github.com/macarie) and [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;10138](https://redirect.github.com/vitest-dev/vitest/issues/10138) [<samp>(31882)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/31882607c)
- Global `sequence.concurrent: true` with top-level `test(..., { concurrent: false })` + depreacte `sequential` test API and options  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa), **Codex** and [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;10196](https://redirect.github.com/vitest-dev/vitest/issues/10196) [<samp>(2847d)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/2847dfa2a)
- **browser**: Simplify orchestrator otel carrier  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;10285](https://redirect.github.com/vitest-dev/vitest/issues/10285) [<samp>(18af9)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/18af98cee)

#####    🏎 Performance

- Stringify diff objects only once  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;10276](https://redirect.github.com/vitest-dev/vitest/issues/10276) [<samp>(9f7b1)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/9f7b1528c)

#####     [View changes on GitHub](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.5...v4.1.6)

### [`v4.1.5`](https://redirect.github.com/vitest-dev/vitest/releases/tag/v4.1.5)

[Compare Source](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.4...v4.1.5)

#####    🚀 Experimental Features

- **coverage**: Istanbul to support `instrumenter` option  -  by [@&#8203;BartWaardenburg](https://redirect.github.com/BartWaardenburg) and [@&#8203;AriPerkkio](https://redirect.github.com/AriPerkkio) in [#&#8203;10119](https://redirect.github.com/vitest-dev/vitest/issues/10119) [<samp>(0e0ff)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/0e0ff41c7)

#####    🐞 Bug Fixes

- \--project negation excludes browser instances  -  by [@&#8203;felamaslen](https://redirect.github.com/felamaslen) in [#&#8203;10131](https://redirect.github.com/vitest-dev/vitest/issues/10131) [<samp>(9423d)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/9423dc084)
- Project color label on html reporter  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;10142](https://redirect.github.com/vitest-dev/vitest/issues/10142) [<samp>(596f7)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/596f73986)
- Fix `vi.defineHelper` called as object method  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;10163](https://redirect.github.com/vitest-dev/vitest/issues/10163) [<samp>(122c2)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/122c25b5b)
- Alias `agent` reporter to `minimal`  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;10157](https://redirect.github.com/vitest-dev/vitest/issues/10157) [<samp>(663b9)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/663b99fe3)
- Respect diff config options in soft assertions  -  by [@&#8203;Copilot](https://redirect.github.com/Copilot), **sheremet-va** and [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;8696](https://redirect.github.com/vitest-dev/vitest/issues/8696) [<samp>(9787d)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/9787dedad)
- Respect diff config options in soft assertions "  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;8696](https://redirect.github.com/vitest-dev/vitest/issues/8696) [<samp>(7dc6d)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/7dc6d54fd)
- **ast-collect**: Recognize \_*vi_import* prefix in static test discovery  -  by [@&#8203;Yejneshwar](https://redirect.github.com/Yejneshwar) in [#&#8203;10129](https://redirect.github.com/vitest-dev/vitest/issues/10129) [<samp>(32546)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/325463ab2)
- **coverage**: Descriptive error message when reports directory is removed during test run  -  by [@&#8203;DaveT1991](https://redirect.github.com/DaveT1991) and [@&#8203;AriPerkkio](https://redirect.github.com/AriPerkkio) in [#&#8203;10117](https://redirect.github.com/vitest-dev/vitest/issues/10117) [<samp>(14133)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/1413382e1)
- **snapshot**: Increase default snapshot max output length  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) and **Codex** in [#&#8203;10150](https://redirect.github.com/vitest-dev/vitest/issues/10150) [<samp>(21e66)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/21e66ff63)
- **ui**: Fix jsx/tsx syntax highlight  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;10152](https://redirect.github.com/vitest-dev/vitest/issues/10152) [<samp>(f1b1f)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/f1b1f6c7b)
- **web-worker**: Support MessagePort objects referenced inside postMessage data  -  by [@&#8203;whitphx](https://redirect.github.com/whitphx) and **Claude Opus 4.6 (1M context)** in [#&#8203;9927](https://redirect.github.com/vitest-dev/vitest/issues/9927) and [#&#8203;10124](https://redirect.github.com/vitest-dev/vitest/issues/10124) [<samp>(7ad7d)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/7ad7d39af)
- **api**: Make test-specification options writable  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;10154](https://redirect.github.com/vitest-dev/vitest/issues/10154) [<samp>(6abd5)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/6abd557b7)

#####     [View changes on GitHub](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.4...v4.1.5)

### [`v4.1.4`](https://redirect.github.com/vitest-dev/vitest/releases/tag/v4.1.4)

[Compare Source](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.3...v4.1.4)

#####    🚀 Experimental Features

- **coverage**:
  - Default to text reporter `skipFull` if agent detected  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;10018](https://redirect.github.com/vitest-dev/vitest/issues/10018) [<samp>(53757)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/53757804c)
- **experimental**:
  - Expose `assertion` as a public field  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;10095](https://redirect.github.com/vitest-dev/vitest/issues/10095) [<samp>(a120e)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/a120e3ab8)
  - Support aria snapshot  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa), **Claude Opus 4.6 (1M context)**, [@&#8203;AriPerkkio](https://redirect.github.com/AriPerkkio), **Codex** and [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9668](https://redirect.github.com/vitest-dev/vitest/issues/9668) [<samp>(d4fbb)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/d4fbb5cc9)
- **reporter**:
  - Add filterMeta option to json reporter  -  by [@&#8203;nami8824](https://redirect.github.com/nami8824) and [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;10078](https://redirect.github.com/vitest-dev/vitest/issues/10078) [<samp>(b77de)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/b77de968e)

#####    🐞 Bug Fixes

- Use "black" foreground for labeled terminal message to ensure contrast  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;10076](https://redirect.github.com/vitest-dev/vitest/issues/10076) [<samp>(203f0)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/203f07af7)
- Make `expect(..., message)` consistent as error message prefix  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) and **Codex** in [#&#8203;10068](https://redirect.github.com/vitest-dev/vitest/issues/10068) [<samp>(a1b5f)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/a1b5f0f4f)
- Do not hoist imports whose names match class properties .  -  by [@&#8203;SunsetFi](https://redirect.github.com/SunsetFi) in [#&#8203;10093](https://redirect.github.com/vitest-dev/vitest/issues/10093) and [#&#8203;10094](https://redirect.github.com/vitest-dev/vitest/issues/10094) [<samp>(0fc4b)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/0fc4b47e0)
- **browser**: Spread user server options into browser Vite server in project  -  by [@&#8203;GoldStrikeArch](https://redirect.github.com/GoldStrikeArch) in [#&#8203;10049](https://redirect.github.com/vitest-dev/vitest/issues/10049) [<samp>(65c9d)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/65c9d55eb)

#####     [View changes on GitHub](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.3...v4.1.4)

### [`v4.1.3`](https://redirect.github.com/vitest-dev/vitest/releases/tag/v4.1.3)

[Compare Source](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.2...v4.1.3)

#####    🚀 Experimental Features

- Add `experimental.preParse` flag  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;10070](https://redirect.github.com/vitest-dev/vitest/issues/10070) [<samp>(78273)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/7827363bd)
- Support `browser.locators.exact` option  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;10013](https://redirect.github.com/vitest-dev/vitest/issues/10013) [<samp>(48799)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/487990a19)
- Add `TestAttachment.bodyEncoding`  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;9969](https://redirect.github.com/vitest-dev/vitest/issues/9969) [<samp>(89ca0)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/89ca0e254)
- Support custom snapshot matcher  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa), **Claude Sonnet 4.6** and **Codex** in [#&#8203;9973](https://redirect.github.com/vitest-dev/vitest/issues/9973) [<samp>(59b0e)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/59b0e6411)

#####    🐞 Bug Fixes

- Advance fake timers with `expect.poll` interval  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) and **Claude Sonnet 4.6** in [#&#8203;10022](https://redirect.github.com/vitest-dev/vitest/issues/10022) [<samp>(3f5bf)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/3f5bfa365)
- Add `@vitest/coverage-v8` and `@vitest/coverage-istanbul` as optional dependency  -  by [@&#8203;alan-agius4](https://redirect.github.com/alan-agius4) in [#&#8203;10025](https://redirect.github.com/vitest-dev/vitest/issues/10025) [<samp>(146d4)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/146d4f0a0)
- Fix `defineHelper` for webkit async stack trace + update playwright 1.59.0  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;10036](https://redirect.github.com/vitest-dev/vitest/issues/10036) [<samp>(5a5fa)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/5a5fa49fe)
- Fix suite hook throwing errors for unused auto test-scoped fixture  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) and **Claude Sonnet 4.6** in [#&#8203;10035](https://redirect.github.com/vitest-dev/vitest/issues/10035) [<samp>(39865)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/398657e8d)
- **expect**:
  - Remove `JestExtendError.context` from verbose error reporting  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;9983](https://redirect.github.com/vitest-dev/vitest/issues/9983) [<samp>(66751)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/66751c9e8)
  - Don't leak "runner" types  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;10004](https://redirect.github.com/vitest-dev/vitest/issues/10004) [<samp>(ec204)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/ec2045543)
- **snapshot**:
  - Fix flagging obsolete snapshots for snapshot properties mismatch  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) and **Claude Sonnet 4.6** in [#&#8203;9986](https://redirect.github.com/vitest-dev/vitest/issues/9986) [<samp>(6b869)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/6b869156b)
  - Export custom snapshot matcher helper from `vitest`  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) and **Codex** in [#&#8203;10042](https://redirect.github.com/vitest-dev/vitest/issues/10042) [<samp>(691d3)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/691d341fd)
- **ui**:
  - Don't leak vite types  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;10005](https://redirect.github.com/vitest-dev/vitest/issues/10005) [<samp>(fdff1)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/fdff1bf9a)
- **vm**:
  - Fix external module resolve error with deps optimizer query  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) and **Claude Sonnet 4.6** in [#&#8203;10024](https://redirect.github.com/vitest-dev/vitest/issues/10024) [<samp>(9dbf4)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/9dbf47786)

#####     [View changes on GitHub](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.2...v4.1.3)

### [`v4.1.2`](https://redirect.github.com/vitest-dev/vitest/releases/tag/v4.1.2)

[Compare Source](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.1...v4.1.2)

This release bumps Vitest's `flatted` version and removes version pinning to resolve `flatted`'s CVE related issues ([#&#8203;9975](https://redirect.github.com/vitest-dev/vitest/issues/9975)).

#####    🐞 Bug Fixes

- Don't resolve `setupFiles` from parent directory  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;9960](https://redirect.github.com/vitest-dev/vitest/issues/9960) [<samp>(7aa93)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/7aa937776)
- Ensure sequential mock/unmock resolution  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) and **Claude Opus 4.6** in [#&#8203;9830](https://redirect.github.com/vitest-dev/vitest/issues/9830) [<samp>(7c065)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/7c06598db)
- **browser**: Take failure screenshot if `toMatchScreenshot` can't capture a stable screenshot  -  by [@&#8203;macarie](https://redirect.github.com/macarie) in [#&#8203;9847](https://redirect.github.com/vitest-dev/vitest/issues/9847) [<samp>(faace)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/faace1fbe)
- **coverage**: Correct `coverageConfigDefaults` values and types  -  by [@&#8203;Arthie](https://redirect.github.com/Arthie) in [#&#8203;9940](https://redirect.github.com/vitest-dev/vitest/issues/9940) [<samp>(b3c99)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/b3c992cb2)
- **pretty-format**: Fix output limit over counting  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;9965](https://redirect.github.com/vitest-dev/vitest/issues/9965) [<samp>(d3b7a)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/d3b7a40fa)
- Disable colors if agent is detected  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) and [@&#8203;AriPerkkio](https://redirect.github.com/AriPerkkio) in [#&#8203;9851](https://redirect.github.com/vitest-dev/vitest/issues/9851) [<samp>(6f97b)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/6f97b55dd)

#####     [View changes on GitHub](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.1...v4.1.2)

### [`v4.1.1`](https://redirect.github.com/vitest-dev/vitest/releases/tag/v4.1.1)

[Compare Source](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.0...v4.1.1)

#####    🚀 Features

- **experimental**:
  - Expose `matchesTags` to test if the current filter matches tags  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9913](https://redirect.github.com/vitest-dev/vitest/issues/9913) [<samp>(eec53)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/eec53d9f5)
  - Introduce `experimental.vcsProvider`  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9928](https://redirect.github.com/vitest-dev/vitest/issues/9928) [<samp>(56115)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/561150036)

#####    🐞 Bug Fixes

- Mark `TestProject.testFilesList` internal properly  -  by [@&#8203;sapphi-red](https://redirect.github.com/sapphi-red) in [#&#8203;9867](https://redirect.github.com/vitest-dev/vitest/issues/9867) [<samp>(54f26)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/54f2660f5)
- Detect fixture that returns without calling `use`  -  by [@&#8203;oilater](https://redirect.github.com/oilater) in [#&#8203;9831](https://redirect.github.com/vitest-dev/vitest/issues/9831) and [#&#8203;9861](https://redirect.github.com/vitest-dev/vitest/issues/9861) [<samp>(633ae)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/633ae2303)
- Drop vite 8.beta support  -  by [@&#8203;AriPerkkio](https://redirect.github.com/AriPerkkio) in [#&#8203;9862](https://redirect.github.com/vitest-dev/vitest/issues/9862) [<samp>(b78f5)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/b78f5389d)
- Type regression in vi.mocked() static class methods  -  by [@&#8203;purepear](https://redirect.github.com/purepear) and [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;9857](https://redirect.github.com/vitest-dev/vitest/issues/9857) [<samp>(90926)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/90926641b)
- Properly re-evaluate actual modules of mocked external  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;9898](https://redirect.github.com/vitest-dev/vitest/issues/9898) [<samp>(ae5ec)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/ae5ec03ef)
- Preserve coverage report when html reporter overlaps  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;9889](https://redirect.github.com/vitest-dev/vitest/issues/9889) [<samp>(2d81a)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/2d81ad897)
- Provide `vi.advanceTimers` to the preview provider  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9891](https://redirect.github.com/vitest-dev/vitest/issues/9891) [<samp>(1bc3e)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/1bc3e63be)
- Don't leak event listener in playwright provider  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9910](https://redirect.github.com/vitest-dev/vitest/issues/9910) [<samp>(d9355)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/d93550ff7)
- Open browser in `--standalone` mode without running tests  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9911](https://redirect.github.com/vitest-dev/vitest/issues/9911) [<samp>(e78ad)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/e78adcf97)
- Guard disposable and optional `body`  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9912](https://redirect.github.com/vitest-dev/vitest/issues/9912) [<samp>(6fdb2)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/6fdb2ba61)
- Resolve `retry.condition` RegExp serialization issue  -  by [@&#8203;nstepien](https://redirect.github.com/nstepien) and [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;9942](https://redirect.github.com/vitest-dev/vitest/issues/9942) [<samp>(7b605)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/7b6054328)
- **collect**:
  - Don't treat extra props on `test` return as tests  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9871](https://redirect.github.com/vitest-dev/vitest/issues/9871) [<samp>(141e7)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/141e72aa1)
- **coverage**:
  - Simplify provider types  -  by [@&#8203;AriPerkkio](https://redirect.github.com/AriPerkkio) in [#&#8203;9931](https://redirect.github.com/vitest-dev/vitest/issues/9931) [<samp>(aaf9f)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/aaf9f18ae)
  - Load built-in provider without module runner  -  by [@&#8203;AriPerkkio](https://redirect.github.com/AriPerkkio) in [#&#8203;9939](https://redirect.github.com/vitest-dev/vitest/issues/9939) [<samp>(bf892)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/bf8920817)
- **expect**:
  - Soft assertions continue after .resolves/.rejects promise errors  -  by [@&#8203;mixelburg](https://redirect.github.com/mixelburg), **Maks Pikov**, **Claude Opus 4.6 (1M context)** and [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;9843](https://redirect.github.com/vitest-dev/vitest/issues/9843) [<samp>(6d74b)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/6d74b4948)
  - Fix sinon-chai style API  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;9943](https://redirect.github.com/vitest-dev/vitest/issues/9943) [<samp>(0f08d)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/0f08dda2c)
- **pretty-format**:
  - Limit output for large object  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) and **Claude Opus 4.6 (1M context)** in [#&#8203;9949](https://redirect.github.com/vitest-dev/vitest/issues/9949) [<samp>(0d5f9)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/0d5f9d6ef)

#####     [View changes on GitHub](https://redirect.github.com/vitest-dev/vitest/compare/v4.1.0...v4.1.1)

### [`v4.1.0`](https://redirect.github.com/vitest-dev/vitest/releases/tag/v4.1.0)

[Compare Source](https://redirect.github.com/vitest-dev/vitest/compare/v4.0.18...v4.1.0)

Vitest 4.1 is out!

This release page lists all changes made to the project during the 4.1 beta. To get a review of all the new features, read our [blog post](https://vitest.dev/blog/vitest-4-1).

#####    🚀 Features

- Return a disposable from doMock()  -  by [@&#8203;kirkwaiblinger](https://redirect.github.com/kirkwaiblinger) in [#&#8203;9332](https://redirect.github.com/vitest-dev/vitest/issues/9332) [<samp>(e3e65)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/e3e659a96)
- Added chai style assertions  -  by [@&#8203;ronnakamoto](https://redirect.github.com/ronnakamoto) and [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;8842](https://redirect.github.com/vitest-dev/vitest/issues/8842) [<samp>(841df)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/841df9ac5)
- Update to sinon/fake-timers v15 and add `setTickMode` to timer controls  -  by [@&#8203;atscott](https://redirect.github.com/atscott) and [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;8726](https://redirect.github.com/vitest-dev/vitest/issues/8726) [<samp>(4b480)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/4b480aaed)
- Expose matcher types  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9448](https://redirect.github.com/vitest-dev/vitest/issues/9448) [<samp>(3e4b9)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/3e4b913b1)
- Add `toTestSpecification` to reported tasks  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9464](https://redirect.github.com/vitest-dev/vitest/issues/9464) [<samp>(1a470)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/1a4705da9)
- Show a warning if `vi.mock` or `vi.hoisted` are declared outside of top level of the module  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9387](https://redirect.github.com/vitest-dev/vitest/issues/9387) [<samp>(5db54)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/5db54a468)
- Track and display expectedly failed tests (.fails) in UI and CLI  -  by [@&#8203;Copilot](https://redirect.github.com/Copilot), **sheremet-va** and [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9476](https://redirect.github.com/vitest-dev/vitest/issues/9476) [<samp>(77d75)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/77d75fd34)
- Support tags  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9478](https://redirect.github.com/vitest-dev/vitest/issues/9478) [<samp>(de7c8)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/de7c8a521)
- Implement `aroundEach` and `aroundAll` hooks  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9450](https://redirect.github.com/vitest-dev/vitest/issues/9450) [<samp>(2a8cb)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/2a8cb9dc2)
- Stabilize experimental features  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9529](https://redirect.github.com/vitest-dev/vitest/issues/9529) [<samp>(b5fd2)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/b5fd2a16a)
- Accept `new` or `all` in `--update` flag  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9543](https://redirect.github.com/vitest-dev/vitest/issues/9543) [<samp>(a5acf)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/a5acf28a5)
- Support `meta` in test options  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9535](https://redirect.github.com/vitest-dev/vitest/issues/9535) [<samp>(7d622)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/7d622e3d1)
- Support type inference with a new `test.extend` syntax  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9550](https://redirect.github.com/vitest-dev/vitest/issues/9550) [<samp>(e5385)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/e53854fcc)
- Support vite 8 beta, fix type issues in the config with different vite versions  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9587](https://redirect.github.com/vitest-dev/vitest/issues/9587) [<samp>(99028)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/990281dfd)
- Add assertion helper to hide internal stack traces  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) and **Claude Opus 4.6** in [#&#8203;9594](https://redirect.github.com/vitest-dev/vitest/issues/9594) [<samp>(eeb0a)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/eeb0ae2f8)
- Store failure screenshots using artifacts API  -  by [@&#8203;macarie](https://redirect.github.com/macarie) in [#&#8203;9588](https://redirect.github.com/vitest-dev/vitest/issues/9588) [<samp>(24603)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/24603e3c4)
- Allow `vitest list` to statically collect tests instead of running files to collect them  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9630](https://redirect.github.com/vitest-dev/vitest/issues/9630) [<samp>(7a8e7)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/7a8e7fc20)
- Add `--detect-async-leaks`  -  by [@&#8203;AriPerkkio](https://redirect.github.com/AriPerkkio) in [#&#8203;9528](https://redirect.github.com/vitest-dev/vitest/issues/9528) [<samp>(c594d)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/c594d4af3)
- Implement `mockThrow` and `mockThrowOnce`  -  by [@&#8203;thor-juhasz](https://redirect.github.com/thor-juhasz) and [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9512](https://redirect.github.com/vitest-dev/vitest/issues/9512) [<samp>(61917)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/619179fb7)
- Support `update: "none"` and add docs about snapshots behavior on CI  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;9700](https://redirect.github.com/vitest-dev/vitest/issues/9700) [<samp>(05f18)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/05f1854e2)
- Support playwright `launchOptions` with `connectOptions`  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;9702](https://redirect.github.com/vitest-dev/vitest/issues/9702) [<samp>(f0ff1)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/f0ff1b2a0)
- Add `page/locator.mark` API to enhance playwright trace  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;9652](https://redirect.github.com/vitest-dev/vitest/issues/9652) [<samp>(d0ee5)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/d0ee546fe)
- **api**:
  - Support tests starting or ending with `test` in `experimental_parseSpecification`  -  by [@&#8203;jgillick](https://redirect.github.com/jgillick) and **Jeremy Gillick** in [#&#8203;9235](https://redirect.github.com/vitest-dev/vitest/issues/9235) [<samp>(2f367)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/2f367fad3)
  - Add filters to `createSpecification`  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9336](https://redirect.github.com/vitest-dev/vitest/issues/9336) [<samp>(c8e6c)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/c8e6c7fbf)
  - Expose `runTestFiles` as alternative to `runTestSpecifications`  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9443](https://redirect.github.com/vitest-dev/vitest/issues/9443) [<samp>(43d76)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/43d761821)
  - Add `allowWrite` and `allowExec` options to `api`  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9350](https://redirect.github.com/vitest-dev/vitest/issues/9350) [<samp>(20e00)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/20e00ef78)
  - Allow passing down test cases to `toTestSpecification`  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9627](https://redirect.github.com/vitest-dev/vitest/issues/9627) [<samp>(6f17d)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/6f17d5ddf)
- **browser**:
  - Add `userEvent.wheel` API  -  by [@&#8203;macarie](https://redirect.github.com/macarie) in [#&#8203;9188](https://redirect.github.com/vitest-dev/vitest/issues/9188) [<samp>(66080)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/660801979)
  - Add `filterNode` option to prettyDOM for filtering browser assertion error output  -  by [@&#8203;Copilot](https://redirect.github.com/Copilot), **sheremet-va** and [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9475](https://redirect.github.com/vitest-dev/vitest/issues/9475) [<samp>(d3220)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/d3220fcd8)
  - Support playwright persistent context  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa), **Claude Opus 4.6** and [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9229](https://redirect.github.com/vitest-dev/vitest/issues/9229) [<samp>(f865d)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/f865d2ba4)
  - Added `detailsPanelPosition` option and button  -  by [@&#8203;shairez](https://redirect.github.com/shairez) in [#&#8203;9525](https://redirect.github.com/vitest-dev/vitest/issues/9525) [<samp>(c8a31)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/c8a31147c)
  - Use BlazeDiff instead of pixelmatch  -  by [@&#8203;macarie](https://redirect.github.com/macarie) in [#&#8203;9514](https://redirect.github.com/vitest-dev/vitest/issues/9514) [<samp>(30936)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/309362089)
  - Add `findElement` and enable strict mode in webdriverio and preview  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9677](https://redirect.github.com/vitest-dev/vitest/issues/9677) [<samp>(c3f37)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/c3f37721c)
- **cli**:
  - Add [@&#8203;bomb](https://redirect.github.com/bomb).sh/tab completions  -  by [@&#8203;AmirSa12](https://redirect.github.com/AmirSa12) and [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;8639](https://redirect.github.com/vitest-dev/vitest/issues/8639) [<samp>(200f3)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/200f31704)
- **coverage**:
  - Support `ignore start/stop` ignore hints  -  by [@&#8203;AriPerkkio](https://redirect.github.com/AriPerkkio) in [#&#8203;9204](https://redirect.github.com/vitest-dev/vitest/issues/9204) [<samp>(e59c9)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/e59c94ba6)
  - Add `coverage.changed` option to report only changed files  -  by [@&#8203;kykim00](https://redirect.github.com/kykim00) and [@&#8203;AriPerkkio](https://redirect.github.com/AriPerkkio) in [#&#8203;9521](https://redirect.github.com/vitest-dev/vitest/issues/9521) [<samp>(1d939)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/1d9392c67)
- **experimental**:
  - Add `onModuleRunner` hook to `worker.init`  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9286](https://redirect.github.com/vitest-dev/vitest/issues/9286) [<samp>(e977f)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/e977f3deb)
  - Option to disable the module runner  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) and [@&#8203;AriPerkkio](https://redirect.github.com/AriPerkkio) in [#&#8203;9210](https://redirect.github.com/vitest-dev/vitest/issues/9210) [<samp>(9be61)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/9be6121ee)
  - Add `importDurations: { limit, print }` options  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa), **Claude Opus 4.6** and [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9401](https://redirect.github.com/vitest-dev/vitest/issues/9401) [<samp>(7e10f)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/7e10fb356)
  - Add print and fail thresholds for `importDurations`  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) and **Claude Opus 4.6** in [#&#8203;9533](https://redirect.github.com/vitest-dev/vitest/issues/9533) [<samp>(3f7a5)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/3f7a5f8f8)
- **fixtures**:
  - Pass down file context to `beforeAll`/`afterAll`  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9572](https://redirect.github.com/vitest-dev/vitest/issues/9572) [<samp>(c8339)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/c83395f2c)
- **reporters**:
  - Add `agent` reporter to reduce ai agent token usage  -  by [@&#8203;cpojer](https://redirect.github.com/cpojer) in [#&#8203;9779](https://redirect.github.com/vitest-dev/vitest/issues/9779) [<samp>(3e9e0)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/3e9e096a2)
- **runner**:
  - Enhance `retry` options  -  by [@&#8203;MazenSamehR](https://redirect.github.com/MazenSamehR), **Matan Shavit**, [@&#8203;AriPerkkio](https://redirect.github.com/AriPerkkio) and [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9370](https://redirect.github.com/vitest-dev/vitest/issues/9370) [<samp>(9e4cf)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/9e4cfd295)
- **ui**:
  - Allow run individual test/suites  -  by [@&#8203;userquin](https://redirect.github.com/userquin) in [#&#8203;9465](https://redirect.github.com/vitest-dev/vitest/issues/9465) [<samp>(73b10)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/73b10f1b9)
  - Add project filter/sort support  -  by [@&#8203;userquin](https://redirect.github.com/userquin) in [#&#8203;8689](https://redirect.github.com/vitest-dev/vitest/issues/8689) [<samp>(0c7ea)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/0c7eaac16)
  - Add duration sorting to explorer  -  by [@&#8203;julianhahn](https://redirect.github.com/julianhahn) and [@&#8203;cursoragent](https://redirect.github.com/cursoragent) in [#&#8203;9603](https://redirect.github.com/vitest-dev/vitest/issues/9603) [<samp>(209b1)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/209b1b0e1)
  - Implement filter for slow tests  -  by [@&#8203;DerYeger](https://redirect.github.com/DerYeger) and [@&#8203;userquin](https://redirect.github.com/userquin) in [#&#8203;9705](https://redirect.github.com/vitest-dev/vitest/issues/9705) [<samp>(8880c)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/8880c907a)
- **vitest**:
  - Add run summary in GitHub Actions Reporter  -  by [@&#8203;macarie](https://redirect.github.com/macarie) and **jhnance** in [#&#8203;9579](https://redirect.github.com/vitest-dev/vitest/issues/9579) [<samp>(96bfc)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/96bfc8345)

#####    🐞 Bug Fixes

- Deprecate several vitest/\* entry points  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9347](https://redirect.github.com/vitest-dev/vitest/issues/9347) [<samp>(fd459)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/fd45928be)
- Use `meta.url` in `createRequire`  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9441](https://redirect.github.com/vitest-dev/vitest/issues/9441) [<samp>(e3422)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/e34225563)
- Preact browser mode init example of render function not async  -  by [@&#8203;WuMingDao](https://redirect.github.com/WuMingDao) in [#&#8203;9375](https://redirect.github.com/vitest-dev/vitest/issues/9375) [<samp>(2bea5)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/2bea549c7)
- Deprecate unused types in matcher context  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9449](https://redirect.github.com/vitest-dev/vitest/issues/9449) [<samp>(20f87)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/20f8753a2)
- Handle `external/noExternal` during `configEnvironment` hook  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) and **Claude Opus 4.6** in [#&#8203;9508](https://redirect.github.com/vitest-dev/vitest/issues/9508) [<samp>(59ea2)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/59ea27c1c)
- Replace default ssr environment runner with Vitest server module runner  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) and **Claude Opus 4.6** in [#&#8203;9506](https://redirect.github.com/vitest-dev/vitest/issues/9506) [<samp>(cd5db)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/cd5db660c)
- Propagate experimental CLI options to child projects  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) and **Claude Opus 4.6** in [#&#8203;9531](https://redirect.github.com/vitest-dev/vitest/issues/9531) [<samp>(b624f)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/b624fae53)
- Show a warning when `browser.isolate` is used  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9410](https://redirect.github.com/vitest-dev/vitest/issues/9410) [<samp>(3d48e)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/3d48ebcb9)
- Fix `vi.mock({ spy: true })` node v8 coverage  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa), **hi-ogawa** and **Claude Opus 4.6** in [#&#8203;9541](https://redirect.github.com/vitest-dev/vitest/issues/9541) [<samp>(687b6)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/687b633c1)
- Don't show internal ssr handler in errors  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9547](https://redirect.github.com/vitest-dev/vitest/issues/9547) [<samp>(76c43)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/76c4397b5)
- Close vitest if it failed to start  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9573](https://redirect.github.com/vitest-dev/vitest/issues/9573) [<samp>(728ba)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/728ba617f)
- Fix ssr environment runner in project  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;9584](https://redirect.github.com/vitest-dev/vitest/issues/9584) [<samp>(09006)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/090064f97)
- Trim trailing white spaces in code block  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;9591](https://redirect.github.com/vitest-dev/vitest/issues/9591) [<samp>(f78be)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/f78bea992)
- Support inline snapshot inside test.for/each  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;9590](https://redirect.github.com/vitest-dev/vitest/issues/9590) [<samp>(615fd)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/615fd521e)
- Apply source maps for external module stack trace  -  by [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) in [#&#8203;9152](https://redirect.github.com/vitest-dev/vitest/issues/9152) [<samp>(79e20)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/79e20d5a3)
- Remove the `.name` from statically collected test  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9596](https://redirect.github.com/vitest-dev/vitest/issues/9596) [<samp>(b66ff)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/b66ff691a)
- Don't suppress warnings on pnp  -  by [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9602](https://redirect.github.com/vitest-dev/vitest/issues/9602) [<samp>(89cbd)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/89cbdaea3)
- Support snapshot with `expect.soft`  -  by [@&#8203;iumehara](https://redirect.github.com/iumehara), [@&#8203;hi-ogawa](https://redirect.github.com/hi-ogawa) and **Claude Opus 4.6** in [#&#8203;9231](https://redirect.github.com/vitest-dev/vitest/issues/9231) [<samp>(3eb2c)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/3eb2cd541)
- Log seed when only `sequence.shuffle.tests` is enabled  -  by [@&#8203;kaigritun](https://redirect.github.com/kaigritun), **Kai Gritun** and [@&#8203;sheremet-va](https://redirect.github.com/sheremet-va) in [#&#8203;9576](https://redirect.github.com/vitest-dev/vitest/issues/9576) [<samp>(8182b)</samp>](https://redirect.github.com/vitest-dev/vitest/commit/8182b77ad)
- Externalize `expect/src/utils` from `

> [!IMPORTANT]
> ✂ PR body was truncated to here.


</details>

---

### Configuration

📅 **Schedule**: (in timezone America/Los_Angeles)

- Branch creation
  - At any time (no schedule defined)
- Automerge
  - At any time (no schedule defined)

🚦 **Automerge**: Disabled by config. Please merge this manually once you are satisfied.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

---

 - [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job log](https://developer.mend.io/github/apollographql/apollo-client).
<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0NC4xNTYuMyIsInVwZGF0ZWRJblZlciI6IjQ0LjE1Ni4zIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6WyI6Y2hyaXN0bWFzX3RyZWU6IGRlcGVuZGVuY2llcyJdfQ==-->

