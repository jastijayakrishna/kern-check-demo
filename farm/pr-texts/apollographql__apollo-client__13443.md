# Bump fast-uri from 3.1.5 to 3.1.8

Bumps [fast-uri](https://github.com/fastify/fast-uri) from 3.1.5 to 3.1.8.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/fastify/fast-uri/releases">fast-uri's releases</a>.</em></p>
<blockquote>
<h2>v3.1.8</h2>
<h2>⚠️ Security Warning</h2>
<p>This security release fixes the following medium-severity security advisory:</p>
<ul>
<li><a href="https://github.com/fastify/fast-uri/security/advisories/GHSA-hrr3-gc8f-f4qj">GHSA-hrr3-gc8f-f4qj</a> — inconsistent host case normalization via percent-encoded octets</li>
</ul>
<p>Users of the v3.x release line should upgrade to v3.1.8.</p>
<p><strong>Full Changelog</strong>: <a href="https://github.com/fastify/fast-uri/compare/v3.1.7...v3.1.8">https://github.com/fastify/fast-uri/compare/v3.1.7...v3.1.8</a></p>
<h2>v3.1.7</h2>
<h2>⚠️ Security Warning</h2>
<p>This is a security release that fixes the following high-severity security advisories:</p>
<ul>
<li><a href="https://github.com/fastify/fast-uri/security/advisories/GHSA-qw65-cvwx-89v3">GHSA-qw65-cvwx-89v3</a> — authority injection via an unvalidated port in <code>serialize()</code></li>
<li><a href="https://github.com/fastify/fast-uri/security/advisories/GHSA-58mr-gqgx-xq4g">GHSA-58mr-gqgx-xq4g</a> — host confusion via unbalanced or misplaced IP-literal brackets</li>
</ul>
<p>Users of the v3.x release line should upgrade to v3.1.7.</p>
<p><strong>Full Changelog</strong>: <a href="https://github.com/fastify/fast-uri/compare/v3.1.6...v3.1.7">https://github.com/fastify/fast-uri/compare/v3.1.6...v3.1.7</a></p>
<h2>v3.1.6</h2>
<h2>⚠️ Security Warning</h2>
<p>This release addresses the following high-severity security advisories:</p>
<ul>
<li><a href="https://github.com/fastify/fast-uri/security/advisories/GHSA-5jgf-p345-68v8">GHSA-5jgf-p345-68v8</a> — host confusion via skipped IDN canonicalization on scheme-relative references</li>
<li><a href="https://github.com/fastify/fast-uri/security/advisories/GHSA-fph4-wmhf-6fwf">GHSA-fph4-wmhf-6fwf</a> — server-side request forgery via repeated hostname percent-decoding</li>
<li><a href="https://github.com/fastify/fast-uri/security/advisories/GHSA-f65p-4m7j-42xc">GHSA-f65p-4m7j-42xc</a> — server-side request forgery via malformed IPv6 normalization</li>
<li><a href="https://github.com/fastify/fast-uri/security/advisories/GHSA-jqff-g426-hqxp">GHSA-jqff-g426-hqxp</a> — host confusion via percent-encoded scheme normalization</li>
</ul>
<p>Users of the v3.x release line should upgrade to v3.1.6.</p>
<p><strong>Full Changelog</strong>: <a href="https://github.com/fastify/fast-uri/compare/v3.1.5...v3.1.6">https://github.com/fastify/fast-uri/compare/v3.1.5...v3.1.6</a></p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/fastify/fast-uri/commit/ead3ab7bb134c989e972c8174632d0670023f269"><code>ead3ab7</code></a> Bumped v3.1.8</li>
<li><a href="https://github.com/fastify/fast-uri/commit/c88b59e3e3a20af1d5d6e499f48908d0fb12a66d"><code>c88b59e</code></a> fix: normalize decoded reg-name case</li>
<li><a href="https://github.com/fastify/fast-uri/commit/412e40abd4eb8beabfb952d80abf949a2baf27a3"><code>412e40a</code></a> Bumped v3.1.7</li>
<li><a href="https://github.com/fastify/fast-uri/commit/9f4c943e4d2133e8d78e0941203879216255bb01"><code>9f4c943</code></a> fix: backport port and IP-literal validation to v3.x (<a href="https://redirect.github.com/fastify/fast-uri/issues/216">#216</a>)</li>
<li><a href="https://github.com/fastify/fast-uri/commit/1eb3ce436fe050807caba79f886ab894f485a588"><code>1eb3ce4</code></a> fix: treat unterminated bracket hosts as reg-names again (<a href="https://redirect.github.com/fastify/fast-uri/issues/214">#214</a>)</li>
<li><a href="https://github.com/fastify/fast-uri/commit/6f970b2951fd896aa0f3a7ff28eeb6640c137d33"><code>6f970b2</code></a> Bumped v3.1.6</li>
<li><a href="https://github.com/fastify/fast-uri/commit/d941579a84273ec7e96bde596b1f7a8be447df2a"><code>d941579</code></a> fix: never run IDN canonicalization on bracketed IP literals</li>
<li><a href="https://github.com/fastify/fast-uri/commit/c0f0279cf370cb89ee56b04bbcde2a7afbe81aba"><code>c0f0279</code></a> test: adapt decoded-scheme handler assertion to 3.x (no mailto scheme)</li>
<li><a href="https://github.com/fastify/fast-uri/commit/37f3417c82994279656854f83ce938acd81c3862"><code>37f3417</code></a> Merge commit from fork</li>
<li><a href="https://github.com/fastify/fast-uri/commit/607bfbe953f28a14c2e06ae64aff38c81ca2937f"><code>607bfbe</code></a> Merge commit from fork</li>
<li>Additional commits viewable in <a href="https://github.com/fastify/fast-uri/compare/v3.1.5...v3.1.8">compare view</a></li>
</ul>
</details>
<br />

