# chore(deps): bump vitest from 4.1.0 to 4.1.11

Bumps [vitest](https://github.com/vitest-dev/vitest/tree/HEAD/packages/vitest) from 4.1.0 to 4.1.11.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vitest-dev/vitest/releases">vitest's releases</a>.</em></p>
<blockquote>
<h2>v4.1.11</h2>
<h3>   🐞 Bug Fixes</h3>
<ul>
<li>Revive global concurrency limit for test lifecycle [backport to v4]  -  by <a href="https://github.com/sheremet-va"><code>@​sheremet-va</code></a> and <a href="https://github.com/hi-ogawa"><code>@​hi-ogawa</code></a> in <a href="https://redirect.github.com/vitest-dev/vitest/issues/10992">vitest-dev/vitest#10992</a> <a href="https://github.com/vitest-dev/vitest/commit/5146df80b"><!-- raw HTML omitted -->(5146d)<!-- raw HTML omitted --></a></li>
<li><strong>browser</strong>:
<ul>
<li>Encode iframeId in tester iframe URL [backport to v4]  -  by <a href="https://github.com/sheremet-va"><code>@​sheremet-va</code></a>, <strong>Pduhard</strong> and <strong>Claude Opus 4.8</strong> in <a href="https://redirect.github.com/vitest-dev/vitest/issues/10955">vitest-dev/vitest#10955</a> <a href="https://github.com/vitest-dev/vitest/commit/10b2cd201"><!-- raw HTML omitted -->(10b2c)<!-- raw HTML omitted --></a></li>
<li>Trigger playwright/chromium gc on lower disk availability [backport to v4]  -  by <a href="https://github.com/hi-ogawa"><code>@​hi-ogawa</code></a>, <strong>Hiroshi Ogawa</strong> and <strong>OpenCode</strong> in <a href="https://redirect.github.com/vitest-dev/vitest/issues/10951">vitest-dev/vitest#10951</a> <a href="https://github.com/vitest-dev/vitest/commit/9851dbc41"><!-- raw HTML omitted -->(9851d)<!-- raw HTML omitted --></a></li>
</ul>
</li>
<li><strong>mocker</strong>:
<ul>
<li>Restrict redirect mocks to the fs allowlist [backport to v4]  -  by <a href="https://github.com/sheremet-va"><code>@​sheremet-va</code></a> in <a href="https://redirect.github.com/vitest-dev/vitest/issues/10974">vitest-dev/vitest#10974</a> <a href="https://github.com/vitest-dev/vitest/commit/fe5a11d3c"><!-- raw HTML omitted -->(fe5a1)<!-- raw HTML omitted --></a></li>
</ul>
</li>
</ul>
<h5>    <a href="https://github.com/vitest-dev/vitest/compare/v4.1.10...v4.1.11">View changes on GitHub</a></h5>
<h2>v4.1.10</h2>
<h3>   🐞 Bug Fixes</h3>
<ul>
<li><strong>browser</strong>: Check fs access in builtin commands [backport to v4]  -  by <a href="https://github.com/hi-ogawa"><code>@​hi-ogawa</code></a>, <strong>Hiroshi Ogawa</strong> and <strong>OpenCode (claude-opus-4-8)</strong> in <a href="https://redirect.github.com/vitest-dev/vitest/issues/10680">vitest-dev/vitest#10680</a> <a href="https://github.com/vitest-dev/vitest/commit/5c18dd267"><!-- raw HTML omitted -->(5c18d)<!-- raw HTML omitted --></a></li>
<li><strong>vm</strong>: Fix external module resolve error with deps optimizer query for encoded URI [backport to v4]  -  by <a href="https://github.com/SveLil"><code>@​SveLil</code></a> and <a href="https://github.com/hi-ogawa"><code>@​hi-ogawa</code></a> in <a href="https://redirect.github.com/vitest-dev/vitest/issues/10661">vitest-dev/vitest#10661</a> <a href="https://github.com/vitest-dev/vitest/commit/bae52b511"><!-- raw HTML omitted -->(bae52)<!-- raw HTML omitted --></a></li>
</ul>
<h5>    <a href="https://github.com/vitest-dev/vitest/compare/v4.1.9...v4.1.10">View changes on GitHub</a></h5>
<h2>v4.1.9</h2>
<h3>🐞 Bug Fixes</h3>
<ul>
<li>Fix <code>importOriginal</code> with optimizer and query import [backport to v4] - by <strong>Hiroshi Ogawa</strong>, <strong>David Harris</strong>, <strong>Codex</strong>and <strong>Vladimir</strong> in <a href="https://redirect.github.com/vitest-dev/vitest/issues/10546">vitest-dev/vitest#10546</a> <a href="https://github.com/vitest-dev/vitest/commit/a5180190c"><!-- raw HTML omitted -->(a5180)<!-- raw HTML omitted --></a></li>
<li><strong>browser</strong>:
<ul>
<li>Wait for orchestrator readiness before resolving browser sessions [backport to v4] - by <strong>Vladimir</strong> and <strong>Séamus O'Connor</strong> in <a href="https://redirect.github.com/vitest-dev/vitest/issues/10555">vitest-dev/vitest#10555</a> <a href="https://github.com/vitest-dev/vitest/commit/7fb29651a"><!-- raw HTML omitted -->(7fb29)<!-- raw HTML omitted --></a></li>
<li>Wait for iframe tester readiness before preparing  [backport to v4] - by <strong>Vladimir</strong> and <strong>Séamus O'Connor</strong> in <a href="https://redirect.github.com/vitest-dev/vitest/issues/10497">vitest-dev/vitest#10497</a> and <a href="https://redirect.github.com/vitest-dev/vitest/issues/10556">vitest-dev/vitest#10556</a> <a href="https://github.com/vitest-dev/vitest/commit/fbc626c40"><!-- raw HTML omitted -->(fbc62)<!-- raw HTML omitted --></a></li>
</ul>
</li>
<li><strong>mocker</strong>:
<ul>
<li>Hoist vi.mock() for vite-plus/test imports [backport to v4] - by <strong>Hiroshi Ogawa</strong>, <strong>LongYinan</strong>, <strong>Claude Opus 4.8</strong> and <strong>Vladimir</strong> in <a href="https://redirect.github.com/vitest-dev/vitest/issues/10548">vitest-dev/vitest#10548</a> <a href="https://github.com/vitest-dev/vitest/commit/2c9559c02"><!-- raw HTML omitted -->(2c955)<!-- raw HTML omitted --></a></li>
</ul>
</li>
<li><strong>pool</strong>:
<ul>
<li>Prevent test run hang on worker crash  [backport to v4] - by <strong>Ari Perkkiö</strong> and <strong>Jattioui Ismail</strong> in <a href="https://redirect.github.com/vitest-dev/vitest/issues/10543">vitest-dev/vitest#10543</a> and <a href="https://redirect.github.com/vitest-dev/vitest/issues/10564">vitest-dev/vitest#10564</a> <a href="https://github.com/vitest-dev/vitest/commit/934b0f587"><!-- raw HTML omitted -->(934b0)<!-- raw HTML omitted --></a></li>
</ul>
</li>
</ul>
<h5><a href="https://github.com/vitest-dev/vitest/compare/v4.1.8...v4.1.9">View changes on GitHub</a></h5>
<h2>v4.1.8</h2>
<h3>   🐞 Bug Fixes</h3>
<ul>
<li><strong>browser</strong>:
<ul>
<li>Disable client <code>cdp</code> API when <code>allowWrite/allowExec: false</code> [backport to v4]  -  by <a href="https://github.com/hi-ogawa"><code>@​hi-ogawa</code></a> and <strong>Codex</strong> in <a href="https://redirect.github.com/vitest-dev/vitest/issues/10450">vitest-dev/vitest#10450</a> <a href="https://github.com/vitest-dev/vitest/commit/e4067b3b1"><!-- raw HTML omitted -->(e4067)<!-- raw HTML omitted --></a></li>
<li>Remove orphaned Playwright route when same module is mocked via multiple ids [backport to v4]  -  by <a href="https://github.com/toxik"><code>@​toxik</code></a> and <a href="https://github.com/Zelys-DFKH"><code>@​Zelys-DFKH</code></a> in <a href="https://redirect.github.com/vitest-dev/vitest/issues/10474">vitest-dev/vitest#10474</a> <a href="https://github.com/vitest-dev/vitest/commit/675b4343f"><!-- raw HTML omitted -->(675b4)<!-- raw HTML omitted --></a></li>
</ul>
</li>
</ul>
<h5>    <a href="https://github.com/vitest-dev/vitest/compare/v4.1.7...v4.1.8">View changes on GitHub</a></h5>
<h2>v4.1.7</h2>
<h3>   🐞 Bug Fixes</h3>
<ul>
<li><strong>runner</strong>: Limit concurrency per task branch in addition to per leaf callbacks (backport)  -  by <a href="https://github.com/hi-ogawa"><code>@​hi-ogawa</code></a> in <a href="https://redirect.github.com/vitest-dev/vitest/issues/10384">vitest-dev/vitest#10384</a> <a href="https://github.com/vitest-dev/vitest/commit/4f0f2a1ee"><!-- raw HTML omitted -->(4f0f2)<!-- raw HTML omitted --></a></li>
</ul>
<h5>    <a href="https://github.com/vitest-dev/vitest/compare/v4.1.6...v4.1.7">View changes on GitHub</a></h5>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vitest-dev/vitest/commit/9bd8d464e6328c567c2dbcd8fdd977d57a9425c2"><code>9bd8d46</code></a> chore: release v4.1.11 (<a href="https://github.com/vitest-dev/vitest/tree/HEAD/packages/vitest/issues/10995">#10995</a>)</li>
<li><a href="https://github.com/vitest-dev/vitest/commit/9851dbc41c286a30abfb6b29cce65f3e5b7b40a1"><code>9851dbc</code></a> fix(browser): trigger playwright/chromium gc on lower disk availability [back...</li>
<li><a href="https://github.com/vitest-dev/vitest/commit/db616d227b6e0cb07a94f5d1bba262ee95db7e46"><code>db616d2</code></a> chore: release v4.1.10 (<a href="https://github.com/vitest-dev/vitest/tree/HEAD/packages/vitest/issues/10718">#10718</a>)</li>
<li><a href="https://github.com/vitest-dev/vitest/commit/bae52b5112a6fd8200101b88bf8af9685d077295"><code>bae52b5</code></a> fix(vm): fix external module resolve error with deps optimizer query for enco...</li>
<li><a href="https://github.com/vitest-dev/vitest/commit/a7a61e78c7d0718f00173cff6800a91a344457d4"><code>a7a61e7</code></a> chore: release v4.1.9 (<a href="https://github.com/vitest-dev/vitest/tree/HEAD/packages/vitest/issues/10598">#10598</a>)</li>
<li><a href="https://github.com/vitest-dev/vitest/commit/934b0f587cb61d8338d83f525295322692a2db40"><code>934b0f5</code></a> fix(pool): prevent test run hang on worker crash (<a href="https://github.com/vitest-dev/vitest/tree/HEAD/packages/vitest/issues/10543">#10543</a>) [backport to v4] (#...</li>
<li><a href="https://github.com/vitest-dev/vitest/commit/7fb29651afbae2a9b0cefe6c031a9308f168ac60"><code>7fb2965</code></a> fix(browser): wait for orchestrator readiness before resolving browser sessio...</li>
<li><a href="https://github.com/vitest-dev/vitest/commit/a5180190c1be7089e3705e3dd9e84fea118d09d3"><code>a518019</code></a> fix: fix <code>importOriginal</code> with optimizer and query import [backport to v4] (#...</li>
<li><a href="https://github.com/vitest-dev/vitest/commit/e61f2dd2a0ba0a266c1c5e0334aad3799fee527f"><code>e61f2dd</code></a> chore: release v4.1.8</li>
<li><a href="https://github.com/vitest-dev/vitest/commit/e4067b3b150005fd42cf75f994300119245806b9"><code>e4067b3</code></a> fix(browser): disable client <code>cdp</code> API when <code>allowWrite/allowExec: false</code> [ba...</li>
<li>Additional commits viewable in <a href="https://github.com/vitest-dev/vitest/commits/v4.1.11/packages/vitest">compare view</a></li>
</ul>
</details>
<br />

