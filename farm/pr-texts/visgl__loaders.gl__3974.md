# chore(deps): bump js-yaml from 4.1.0 to 4.3.2 in /test/apps/typescript-test

Bumps [js-yaml](https://github.com/nodeca/js-yaml) from 4.1.0 to 4.3.2.
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/nodeca/js-yaml/blob/4.3.2/CHANGELOG.md">js-yaml's changelog</a>.</em></p>
<blockquote>
<h2>4.3.2 - 2026-08-26</h2>
<h3>Changed</h3>
<ul>
<li>[backport] Hard-limit merge sequence size to 100.</li>
</ul>
<h3>Security</h3>
<ul>
<li>[backport] Count empty mappings in merge sequences toward <code>maxTotalMergeKeys</code>
to limit CPU usage, <a href="https://redirect.github.com/nodeca/js-yaml/issues/797">#797</a>.</li>
</ul>
<h2>4.3.1 - 2026-07-31</h2>
<h3>Security</h3>
<ul>
<li>[backport] Remove quadratic complexity from <code>!!omap</code> duplicate key detection.</li>
</ul>
<h2>4.3.0 - 2026-06-27</h2>
<h3>Added</h3>
<ul>
<li>[backport] Added <code>maxTotalMergeKeys</code> (10000) loader option to limit the total number of
keys processed by YAML merge (<code>&lt;&lt;</code>) across one <code>load()</code> / <code>loadAll()</code> call.</li>
</ul>
<h3>Fixed</h3>
<ul>
<li>Restore umd builds back to es5.</li>
</ul>
<h3>Removed</h3>
<ul>
<li>[backport] <code>maxMergeSeqLength</code> replaced with <code>maxTotalMergeKeys</code> for limiting YAML merge
processing.</li>
</ul>
<h2>[4.2.0] - 2026-06-01</h2>
<h3>Added</h3>
<ul>
<li>Added <code>docs/safety.md</code> with notes about processing untrusted YAML.</li>
<li>Added <code>maxDepth</code> (100) loader option. Not a problem, but gives a better
exception instead of RangeError on stack overflow.</li>
<li>Added <code>maxMergeSeqLength</code> (20) loader option. Not a problem after <code>merge</code> fix,
but an additional restriction for safety.</li>
<li>Added sourcemaps to <code>dist/</code> builds.</li>
</ul>
<h3>Changed</h3>
<ul>
<li>Stop resolving numbers with underscores as numeric scalars, <a href="https://redirect.github.com/nodeca/js-yaml/issues/627">#627</a>.</li>
<li>Switched dev toolchains to Vite / neostandard.</li>
<li>Updated demo.</li>
<li>Reorganized tests.</li>
<li><code>dist/</code> files are no longer kept in the repository.</li>
</ul>
<h3>Fixed</h3>
<ul>
<li>Fix parsing of properties on the first implicit block mapping key, <a href="https://redirect.github.com/nodeca/js-yaml/issues/62">#62</a>.</li>
<li>Fix trailing whitespace handling when folding flow scalar lines, <a href="https://redirect.github.com/nodeca/js-yaml/issues/307">#307</a>.</li>
<li>Reject top-level block scalars without content indentation, <a href="https://redirect.github.com/nodeca/js-yaml/issues/280">#280</a>.</li>
<li>Ensure numbers survive round-trip, <a href="https://redirect.github.com/nodeca/js-yaml/issues/737">#737</a>.</li>
<li>Fix test coverage for issue <a href="https://redirect.github.com/nodeca/js-yaml/issues/221">#221</a>.</li>
<li>Fix flow scalar trailing whitespace folding, <a href="https://redirect.github.com/nodeca/js-yaml/issues/307">#307</a>.</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/nodeca/js-yaml/commit/79ca68d90f333fbe6d9e42827527e62636200191"><code>79ca68d</code></a> 4.3.2 released</li>
<li><a href="https://github.com/nodeca/js-yaml/commit/d90b6612a5a84385bdcb556c44578eac76dc0f6b"><code>d90b661</code></a> Backport merge limits from v5.4.1</li>
<li><a href="https://github.com/nodeca/js-yaml/commit/86e91b815b8794c3c73a179c1770871e37ec2df8"><code>86e91b8</code></a> 4.3.1 released</li>
<li><a href="https://github.com/nodeca/js-yaml/commit/c3cc4b0bb9ddb9af2dd9b61e0d56f5ce7983cd4a"><code>c3cc4b0</code></a> Backport quadratic complexity fix for !!omap</li>
<li><a href="https://github.com/nodeca/js-yaml/commit/33d05b5d29a8c21360f620f7e1c1706e24522eda"><code>33d05b5</code></a> 4.3.0 released</li>
<li><a href="https://github.com/nodeca/js-yaml/commit/663bfab6db2b4a146a9366fd685f069345be4ddb"><code>663bfab</code></a> Drop demo publish, to not override new v5 one.</li>
<li><a href="https://github.com/nodeca/js-yaml/commit/1cb8c7b94bf75e15116869c1c0482dcb22785986"><code>1cb8c7b</code></a> Add v4-legacy tag for publish</li>
<li><a href="https://github.com/nodeca/js-yaml/commit/02f27afad532763263cd2b6be35c24ee8e1f6157"><code>02f27af</code></a> Restore umd builds back to es5</li>
<li><a href="https://github.com/nodeca/js-yaml/commit/8be84edaf15e7c394fa3b813179d1bcc280e87fb"><code>8be84ed</code></a> Fix es5 compatibility</li>
<li><a href="https://github.com/nodeca/js-yaml/commit/59423c6f8cdc78742ac00e25a4dd39ef16b702e4"><code>59423c6</code></a> Replace <code>maxMergeSeqLength</code> option with <code>maxTotalMergeKeys</code> (more robust). Ba...</li>
<li>Additional commits viewable in <a href="https://github.com/nodeca/js-yaml/compare/4.1.0...4.3.2">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=js-yaml&package-manager=npm_and_yarn&previous-version=4.1.0&new-version=4.3.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/visgl/loaders.gl/network/alerts).

</details>
