# chore(deps): bump moment from 2.30.1 to 2.31.0

Bumps [moment](https://github.com/moment/moment) from 2.30.1 to 2.31.0.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/moment/moment/releases">moment's releases</a>.</em></p>
<blockquote>
<h2>2.31.0</h2>
<p><em>Released Sep 14, 2026</em></p>
<h4>Security fixes</h4>
<ul>
<li>Fix <a href="https://www.cve.org/CVERecord?id=CVE-2026-17495">CVE-2026-17495</a> (<a href="https://github.com/moment/moment/security/advisories/GHSA-4p3w-j4w9-5jqw">GHSA-4p3w-j4w9-5jqw</a>)</li>
</ul>
<h4>Bug fixes</h4>
<ul>
<li><a href="https://redirect.github.com/moment/moment/pull/6376">#6376</a> Prevent object prototype properties from being used as format tokens</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6386">#6386</a> Normalize lazy-loaded locale names</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6404">#6404</a> Fix parsing issue with <code>eHHmm</code> format</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6433">#6433</a> Ignore non-Moment arguments in min and max</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6434">#6434</a> Fix inherited lowercase long date formats</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6436">#6436</a> Reset locale parsing caches after updates</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6437">#6437</a> Fix weekday mismatch when the format only has part of a date</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6442">#6442</a> Fix <code>locale('__proto__')</code> corrupting the global locale</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6443">#6443</a> Avoid <code>Object.assign</code> in <code>duration.humanize</code></li>
<li><a href="https://redirect.github.com/moment/moment/pull/6446">#6446</a> Validate range when parsing a time zone offset</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6447">#6447</a> Include metadata in all-locales bundle</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6448">#6448</a> Apply postformat to locale relative time methods</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6450">#6450</a> Add stack traces to conditional deprecation warnings</li>
</ul>
<h4>New features</h4>
<ul>
<li><a href="https://redirect.github.com/moment/moment/pull/6451">#6451</a> Add internal date-default hook for Moment Timezone</li>
</ul>
<h5>New locales</h5>
<ul>
<li><a href="https://redirect.github.com/moment/moment/pull/6000">#6000</a>: Pashto ('ps')</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6278">#6278</a>, <a href="https://redirect.github.com/moment/moment/pull/6379">#6379</a>: Amharic (Ethiopia) ('am-et')</li>
</ul>
<h4>Updates to existing locales</h4>
<ul>
<li><a href="https://redirect.github.com/moment/moment/pull/5404">#5404</a> Portuguese (Brazil) ('pt-br'): Fix wrong plural usage for time</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6197">#6197</a> Indonesian ('id'): Correct the abbreviation for August</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6217">#6217</a> Georgian ('ka') and Dutch (Belgium) ('nl-be'): Correct <code>L</code> date formats</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6289">#6289</a> Swedish ('sv'): Correct the abbreviation for Thursday</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6306">#6306</a> Catalan ('ca'): Use typographic apostrophes in relative time</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6347">#6347</a> Swahili ('sw'): Correct the spelling of hour in calendar output</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6360">#6360</a> Ukrainian ('uk'): Use ISO week numbering</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6370">#6370</a> Ukrainian ('uk'): Use U+02BC apostrophes in Friday names</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6371">#6371</a> Hungarian ('hu'): Preserve numeric values in relative seconds</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6391">#6391</a> Swahili ('sw'): Fix weekday and relative-time grammar</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6396">#6396</a> German ('de', 'de-at', 'de-ch'): Parse short months without trailing dots</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6409">#6409</a> Uzbek ('uz', 'uz-latn'): Fix past relative-time formatting</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6410">#6410</a> Polish ('pl'): Use genitive month names in dotted day formats</li>
</ul>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/moment/moment/blob/develop/CHANGELOG.md">moment's changelog</a>.</em></p>
<blockquote>
<h3>2.31.0</h3>
<p><em>Released Sep 14, 2026</em></p>
<h4>Security fixes</h4>
<ul>
<li>Fix <a href="https://www.cve.org/CVERecord?id=CVE-2026-17495">CVE-2026-17495</a> (<a href="https://github.com/moment/moment/security/advisories/GHSA-4p3w-j4w9-5jqw">GHSA-4p3w-j4w9-5jqw</a>)</li>
</ul>
<h4>Bug fixes</h4>
<ul>
<li><a href="https://redirect.github.com/moment/moment/pull/6376">#6376</a> Prevent object prototype properties from being used as format tokens</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6386">#6386</a> Normalize lazy-loaded locale names</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6404">#6404</a> Fix parsing issue with <code>eHHmm</code> format</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6433">#6433</a> Ignore non-Moment arguments in min and max</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6434">#6434</a> Fix inherited lowercase long date formats</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6436">#6436</a> Reset locale parsing caches after updates</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6437">#6437</a> Fix weekday mismatch when the format only has part of a date</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6442">#6442</a> Fix <code>locale('__proto__')</code> corrupting the global locale</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6443">#6443</a> Avoid <code>Object.assign</code> in <code>duration.humanize</code></li>
<li><a href="https://redirect.github.com/moment/moment/pull/6446">#6446</a> Validate range when parsing a time zone offset</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6447">#6447</a> Include metadata in all-locales bundle</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6448">#6448</a> Apply postformat to locale relative time methods</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6450">#6450</a> Add stack traces to conditional deprecation warnings</li>
</ul>
<h4>New features</h4>
<ul>
<li><a href="https://redirect.github.com/moment/moment/pull/6451">#6451</a> Add internal date-default hook for Moment Timezone</li>
</ul>
<h5>New locales</h5>
<ul>
<li><a href="https://redirect.github.com/moment/moment/pull/6000">#6000</a>: Pashto ('ps')</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6278">#6278</a>, <a href="https://redirect.github.com/moment/moment/pull/6379">#6379</a>: Amharic (Ethiopia) ('am-et')</li>
</ul>
<h4>Updates to existing locales</h4>
<ul>
<li><a href="https://redirect.github.com/moment/moment/pull/5404">#5404</a> Portuguese (Brazil) ('pt-br'): Fix wrong plural usage for time</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6197">#6197</a> Indonesian ('id'): Correct the abbreviation for August</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6217">#6217</a> Georgian ('ka') and Dutch (Belgium) ('nl-be'): Correct <code>L</code> date formats</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6289">#6289</a> Swedish ('sv'): Correct the abbreviation for Thursday</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6306">#6306</a> Catalan ('ca'): Use typographic apostrophes in relative time</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6347">#6347</a> Swahili ('sw'): Correct the spelling of hour in calendar output</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6360">#6360</a> Ukrainian ('uk'): Use ISO week numbering</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6370">#6370</a> Ukrainian ('uk'): Use U+02BC apostrophes in Friday names</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6371">#6371</a> Hungarian ('hu'): Preserve numeric values in relative seconds</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6391">#6391</a> Swahili ('sw'): Fix weekday and relative-time grammar</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6396">#6396</a> German ('de', 'de-at', 'de-ch'): Parse short months without trailing dots</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6409">#6409</a> Uzbek ('uz', 'uz-latn'): Fix past relative-time formatting</li>
<li><a href="https://redirect.github.com/moment/moment/pull/6410">#6410</a> Polish ('pl'): Use genitive month names in dotted day formats</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/moment/moment/commit/15b45d48a176312e8f34143c5a800090abf4787f"><code>15b45d4</code></a> [pkg] Build 2.31.0 (<a href="https://redirect.github.com/moment/moment/issues/6452">#6452</a>)</li>
<li><a href="https://github.com/moment/moment/commit/631cd81454ee001e1f508e21270eae0b6bb62974"><code>631cd81</code></a> [pkg] Update changelog for upcoming release (<a href="https://redirect.github.com/moment/moment/issues/6394">#6394</a>)</li>
<li><a href="https://github.com/moment/moment/commit/6caff9e0d54e85a63a6eb97d7361f1da35bc58f4"><code>6caff9e</code></a> Merge commit from fork</li>
<li><a href="https://github.com/moment/moment/commit/710703b7eac93535ad125cbf4feb3d42afed6fb3"><code>710703b</code></a> [feature] Add internal date-default hook for Moment Timezone (<a href="https://redirect.github.com/moment/moment/issues/6451">#6451</a>)</li>
<li><a href="https://github.com/moment/moment/commit/863ed940556e6e63c43de23981a4853036a003ac"><code>863ed94</code></a> [bugfix] Add stack traces to conditional deprecation warnings (<a href="https://redirect.github.com/moment/moment/issues/6450">#6450</a>)</li>
<li><a href="https://github.com/moment/moment/commit/2c7abe1c42ee15445d30c2c5d536750a1e43a09a"><code>2c7abe1</code></a> [bugfix] Apply postformat to locale relative time methods (<a href="https://redirect.github.com/moment/moment/issues/6448">#6448</a>)</li>
<li><a href="https://github.com/moment/moment/commit/9c45ac38690c649c95e19923276b63da5fe2be26"><code>9c45ac3</code></a> [bugfix] Include metadata in all-locales bundle (<a href="https://redirect.github.com/moment/moment/issues/6447">#6447</a>)</li>
<li><a href="https://github.com/moment/moment/commit/f6eefc5fc7b44ceccbd007aeffc48ebc5eac30fa"><code>f6eefc5</code></a> [bugfix] Validate timezone offset range (<a href="https://redirect.github.com/moment/moment/issues/6446">#6446</a>)</li>
<li><a href="https://github.com/moment/moment/commit/136b441794a3bb207d593add3b59e9de0e062523"><code>136b441</code></a> [bugfix] Avoid Object.assign in duration.humanize (<a href="https://redirect.github.com/moment/moment/issues/6443">#6443</a>)</li>
<li><a href="https://github.com/moment/moment/commit/0d1050437b40f66ac47e14b285bb3d09676cf2e0"><code>0d10504</code></a> [bugfix] Fix locale('<strong>proto</strong>') corrupting the global locale (<a href="https://redirect.github.com/moment/moment/issues/6442">#6442</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/moment/moment/compare/2.30.1...2.31.0">compare view</a></li>
</ul>
</details>
<details>
<summary>Maintainer changes</summary>
<p>This version was pushed to npm by <a href="https://www.npmjs.com/~GitHub%20Actions">GitHub Actions</a>, a new releaser for moment since your current version.</p>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=moment&package-manager=npm_and_yarn&previous-version=2.30.1&new-version=2.31.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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
