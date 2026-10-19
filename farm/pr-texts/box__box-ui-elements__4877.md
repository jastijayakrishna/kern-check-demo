# chore(deps-dev): bump axios from 0.33.0 to 0.34.0

Bumps [axios](https://github.com/axios/axios) from 0.33.0 to 0.34.0.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/axios/axios/releases">axios's releases</a>.</em></p>
<blockquote>
<h2>v0.34.0 — September 13, 2026</h2>
<p>This release hardens request configuration and proxy handling, adds caller diagnostics and cancellation context, and tightens TypeScript header types.</p>
<h2>⚠️ Breaking Changes &amp; Deprecations</h2>
<ul>
<li>Header Types: TypeScript now rejects header values that are Promises, functions, or objects with custom toString() methods. Resolve promises, call functions, or explicitly convert objects before assigning header values. Supported scalar, array, and grouped headers remain available. (<a href="https://redirect.github.com/axios/axios/issues/11209">#11209</a>)</li>
<li>Proxy Routing: NO_PROXY / no_proxy entries now support IPv4 and IPv6 CIDR ranges. Previously ineffective ranges now cause matching IP destinations to bypass the proxy; review existing ranges when upgrading. (<a href="https://redirect.github.com/axios/axios/issues/11172">#11172</a>)</li>
</ul>
<h2>🔒 Security Fixes</h2>
<ul>
<li>Request Configuration: Prevent inherited properties from influencing form serializer options, default request methods, headers on interceptor-returned configs, and HTTP redirect hooks. Applications relying on inherited options must define those values as own properties. (<a href="https://redirect.github.com/axios/axios/issues/11172">#11172</a>)</li>
<li>Hostname Processing: Replace quadratic regular-expression backtracking in proxy bypass hostname normalization with a linear scan, preventing excessive processing of crafted redirect hostnames. (<a href="https://redirect.github.com/axios/axios/issues/11172">#11172</a>)</li>
</ul>
<h2>🚀 New Features</h2>
<ul>
<li>Caller Diagnostics: Enable captureCallerStack: true on a request or instance to append original caller frames to asynchronous error stacks. Disabled by default. (<a href="https://redirect.github.com/axios/axios/issues/11209">#11209</a>)</li>
<li>Cancellation Context: Preserve AbortSignal.reason as CanceledError.reason, including objects and falsy values. Native and structural signals retain their identity and live getters through config merging. (<a href="https://redirect.github.com/axios/axios/issues/11209">#11209</a>)</li>
</ul>
<h2>🐛 Bug Fixes</h2>
<ul>
<li>Proxy Protocols: Accept HTTP(S) proxy schemes with or without a trailing colon, including casing and surrounding whitespace variations. Invalid nonempty strings now fail before connecting with ERR_BAD_OPTION_VALUE; redirect failures retain ERR_FR_REDIRECTION_FAILURE wrapping. Omitted protocols continue to inherit the target protocol. (<a href="https://redirect.github.com/axios/axios/issues/11182">#11182</a>)</li>
<li>Request Interceptors: Route synchronous interceptor and dispatch failures through response interceptors. Await recovery promises before dispatch; rejected recovery prevents sending the request, while successful recovery retains the last request config and ignores recovery return values. (<a href="https://redirect.github.com/axios/axios/issues/11209">#11209</a>)</li>
<li>Error Compatibility: Allow Axios to load alongside a read-only Error.prototype.toJSON, while preserving supplied own property descriptors and setters. (<a href="https://redirect.github.com/axios/axios/issues/11209">#11209</a>)</li>
</ul>
<h2>🔧 Maintenance &amp; Chores</h2>
<ul>
<li>Publishing and Tests: Use npm bundled with Node in the v0 publishing workflow and replace the FormData browser test’s external HTTP request with a Jasmine-Ajax stub. (<a href="https://redirect.github.com/axios/axios/issues/11084">#11084</a>)</li>
<li>Repository Cleanup: Add .codex/ to .gitignore. (<a href="https://redirect.github.com/axios/axios/issues/11033">#11033</a>)</li>
<li>Release Preparation: Update package and runtime version metadata to 0.34.0. (<a href="https://redirect.github.com/axios/axios/issues/11217">#11217</a>)</li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/axios/axios/compare/v0.33.0...v0.34.0">https://github.com/axios/axios/compare/v0.33.0...v0.34.0</a></p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/axios/axios/commit/ee1aa2654766c70215c5ef40991dc1079aa261da"><code>ee1aa26</code></a> chore: release v0.34.0 (<a href="https://redirect.github.com/axios/axios/issues/11217">#11217</a>)</li>
<li><a href="https://github.com/axios/axios/commit/3d25f0e3f3b0a0b764cdcbc3871d5ba866711beb"><code>3d25f0e</code></a> fix(v0)!: address error handling, cancellation and header typing (<a href="https://redirect.github.com/axios/axios/issues/11209">#11209</a>)</li>
<li><a href="https://github.com/axios/axios/commit/5268576d814a46d573e1182281a570172cee4507"><code>5268576</code></a> fix(http): normalize the configured proxy protocol (<a href="https://redirect.github.com/axios/axios/issues/11182">#11182</a>)</li>
<li><a href="https://github.com/axios/axios/commit/d29be181f85f6fe93397a07b1f69606d9622637b"><code>d29be18</code></a> fix: harden request option resolution and no_proxy matching (<a href="https://redirect.github.com/axios/axios/issues/11172">#11172</a>)</li>
<li><a href="https://github.com/axios/axios/commit/a930f390d8ecd262bb91c25bf22840f6ed6ec204"><code>a930f39</code></a> ci: use bundled npm for v0 publish (<a href="https://redirect.github.com/axios/axios/issues/11084">#11084</a>)</li>
<li><a href="https://github.com/axios/axios/commit/5233f59788308f7175287a6345b050f233a2098a"><code>5233f59</code></a> chore: runtime cleanup (<a href="https://redirect.github.com/axios/axios/issues/11033">#11033</a>)</li>
<li>See full diff in <a href="https://github.com/axios/axios/compare/v0.33.0...v0.34.0">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=axios&package-manager=npm_and_yarn&previous-version=0.33.0&new-version=0.34.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

<details>
<summary>Dependabot commands and options</summary>
<br />

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/box/box-ui-elements/network/alerts).

</details>
