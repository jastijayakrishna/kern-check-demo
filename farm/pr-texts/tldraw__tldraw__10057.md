# chore(deps): bump the npm_and_yarn group across 4 directories with 14 updates

Bumps the npm_and_yarn group with 13 updates in the / directory:

| Package | From | To |
| --- | --- | --- |
| [svgo](https://github.com/svg/svgo) | `3.3.3` | `3.3.4` |
| [adm-zip](https://github.com/cthackers/adm-zip) | `0.5.16` | `0.6.0` |
| [mermaid](https://github.com/mermaid-js/mermaid) | `11.15.0` | `11.16.1` |
| [postcss](https://github.com/postcss/postcss) | `8.5.10` | `8.5.23` |
| [sharp](https://github.com/lovell/sharp) | `0.33.5` | `0.35.0` |
| [@hono/node-server](https://github.com/honojs/node-server) | `1.19.13` | `1.19.17` |
| [body-parser](https://github.com/expressjs/body-parser) | `2.2.2` | `2.3.0` |
| [brace-expansion](https://github.com/juliangruber/brace-expansion) | `1.1.15` | `1.1.18` |
| [engine.io](https://github.com/socketio/socket.io) | `6.6.4` | `6.6.9` |
| [find-my-way](https://github.com/delvedor/find-my-way) | `9.2.0` | `9.7.0` |
| [form-data](https://github.com/form-data/form-data) | `4.0.5` | `4.0.6` |
| [js-yaml](https://github.com/nodeca/js-yaml) | `3.14.2` | `3.15.1` |
| [socket.io-parser](https://github.com/socketio/socket.io) | `4.2.6` | `4.2.7` |

Bumps the npm_and_yarn group with 1 update in the /apps/docs directory: [sharp](https://github.com/lovell/sharp).
Bumps the npm_and_yarn group with 1 update in the /apps/examples directory: [mermaid](https://github.com/mermaid-js/mermaid).
Bumps the npm_and_yarn group with 1 update in the /packages/mermaid directory: [mermaid](https://github.com/mermaid-js/mermaid).

Updates `svgo` from 3.3.3 to 3.3.4
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/svg/svgo/releases">svgo's releases</a>.</em></p>
<blockquote>
<h2>v3.3.4</h2>
<h2>What's Changed</h2>
<h3>Security</h3>
<ul>
<li><a href="https://svgo.dev/docs/plugins/removeScripts/">removeScriptElement</a>, remove JavaScript URIs case-insensitively and make <code>&lt;script&gt;</code> handling namespace aware. By <a href="https://github.com/SethFalco"><code>@​SethFalco</code></a></li>
</ul>
<h2>Support</h2>
<p>SVGO v3 is not officially supported, please consider upgrading to SVGO v4 instead. We've backported this fix as there are security implications, but there is no commitment to do this for more complex changes in future.</p>
<p>Consider reading our <a href="https://svgo.dev/docs/migrations/migration-from-v3-to-v4/">Migration Guide from v3 to v4</a> which should ease the process.</p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/svg/svgo/commit/72a23886b4698b27624b936f3a15a80afd36d75f"><code>72a2388</code></a> Merge commit from fork</li>
<li>See full diff in <a href="https://github.com/svg/svgo/compare/v3.3.3...v3.3.4">compare view</a></li>
</ul>
</details>
<br />

Updates `adm-zip` from 0.5.16 to 0.6.0
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/cthackers/adm-zip/releases">adm-zip's releases</a>.</em></p>
<blockquote>
<h2>v0.6.0</h2>
<p><strong>Full Changelog</strong>: <a href="https://github.com/cthackers/adm-zip/compare/v0.5.18...v0.6.0">https://github.com/cthackers/adm-zip/compare/v0.5.18...v0.6.0</a></p>
<p>This release fixes a security vulnerability (CVE-2026-39244), resolves several long-standing bugs, ships built-in TypeScript types, and includes two behavior changes worth reading before you upgrade.</p>
<ul>
<li>extractEntryTo(dirEntry, target, maintainEntryPath = false) now preserves subdirectories instead of flattening files into the target folder by basename (which also silently overwrote same-named files). (<a href="https://redirect.github.com/cthackers/adm-zip/issues/306">#306</a>)</li>
<li>Extraction no longer fails when the modification time can't be set — utimes is now best-effort. (<a href="https://redirect.github.com/cthackers/adm-zip/issues/379">#379</a>)</li>
<li>Minimum Node.js is now 14 (the code already required it; engines was incorrectly &gt;=12).</li>
<li>CVE-2026-39244 — a crafted archive declaring a huge uncompressed size could force an unbounded Buffer.alloc and OOM the process; allocation is now bounded by the data actually present. Reported by Daniel Púa (devploit), Anh Hong, and José Antonio Zamudio Amaya. (<a href="https://redirect.github.com/cthackers/adm-zip/issues/568">#568</a>)</li>
<li>Hardened entry-name lookup against object injection (<strong>proto</strong> names). Prototype-less table.</li>
<li>Data-descriptor regression rejecting valid archives (<a href="https://redirect.github.com/cthackers/adm-zip/issues/548">#548</a>, <a href="https://redirect.github.com/cthackers/adm-zip/issues/533">#533</a>, <a href="https://redirect.github.com/cthackers/adm-zip/issues/554">#554</a>)</li>
<li>Directory permissions not restored on extract (<a href="https://redirect.github.com/cthackers/adm-zip/issues/530">#530</a>)</li>
<li>Infinite recursion on symlink loops in addLocalFolder (<a href="https://redirect.github.com/cthackers/adm-zip/issues/541">#541</a>)</li>
<li>Uncaught process crash in writeFileToAsync on write failure (<a href="https://redirect.github.com/cthackers/adm-zip/issues/470">#470</a>, <a href="https://redirect.github.com/cthackers/adm-zip/issues/459">#459</a>, <a href="https://redirect.github.com/cthackers/adm-zip/issues/402">#402</a>)</li>
<li>Empty name on directory entries (<a href="https://redirect.github.com/cthackers/adm-zip/issues/466">#466</a>)</li>
<li>test() always returned false for archives with files</li>
<li>~6× faster entry sorting for large archives</li>
<li>Built-in TypeScript definitions (types.d.ts) — you can drop <code>@​types/adm-zip</code></li>
</ul>
<h2>v0.5.18</h2>
<h2>What's Changed</h2>
<ul>
<li>Bump js-yaml from 4.1.1 to 4.3.0 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/cthackers/adm-zip/pull/566">cthackers/adm-zip#566</a></li>
<li>Fix corrupted zip when round-tripping entries with a data descriptor (<a href="https://redirect.github.com/cthackers/adm-zip/issues/555">#555</a>) by <a href="https://github.com/JohnJunior"><code>@​JohnJunior</code></a> in <a href="https://redirect.github.com/cthackers/adm-zip/pull/564">cthackers/adm-zip#564</a></li>
<li>prevent crashes when process.versions is an empty object by <a href="https://github.com/matt-fidd"><code>@​matt-fidd</code></a> in <a href="https://redirect.github.com/cthackers/adm-zip/pull/551">cthackers/adm-zip#551</a></li>
<li>support for writing zip64 by <a href="https://github.com/mielverkerken"><code>@​mielverkerken</code></a> in <a href="https://redirect.github.com/cthackers/adm-zip/pull/562">cthackers/adm-zip#562</a></li>
<li>Fix Archive Utility failure on zips with empty directories (<a href="https://redirect.github.com/cthackers/adm-zip/issues/558">#558</a>) by <a href="https://github.com/JohnJunior"><code>@​JohnJunior</code></a> in <a href="https://redirect.github.com/cthackers/adm-zip/pull/563">cthackers/adm-zip#563</a></li>
</ul>
<h2>New Contributors</h2>
<ul>
<li><a href="https://github.com/JohnJunior"><code>@​JohnJunior</code></a> made their first contribution in <a href="https://redirect.github.com/cthackers/adm-zip/pull/564">cthackers/adm-zip#564</a></li>
<li><a href="https://github.com/matt-fidd"><code>@​matt-fidd</code></a> made their first contribution in <a href="https://redirect.github.com/cthackers/adm-zip/pull/551">cthackers/adm-zip#551</a></li>
<li><a href="https://github.com/mielverkerken"><code>@​mielverkerken</code></a> made their first contribution in <a href="https://redirect.github.com/cthackers/adm-zip/pull/562">cthackers/adm-zip#562</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/cthackers/adm-zip/compare/v0.5.17...v0.5.18">https://github.com/cthackers/adm-zip/compare/v0.5.17...v0.5.18</a></p>
<h2>v0.5.17</h2>
<h2>What's Changed</h2>
<ul>
<li>entryHeader time setter more tolerant by <a href="https://github.com/thomasheritage"><code>@​thomasheritage</code></a> in <a href="https://redirect.github.com/cthackers/adm-zip/pull/540">cthackers/adm-zip#540</a></li>
<li>Add check for local desc flag in crc check by <a href="https://github.com/issacgerges"><code>@​issacgerges</code></a> in <a href="https://redirect.github.com/cthackers/adm-zip/pull/543">cthackers/adm-zip#543</a></li>
<li>Create only if the directory does not exist by <a href="https://github.com/DennisHill"><code>@​DennisHill</code></a> in <a href="https://redirect.github.com/cthackers/adm-zip/pull/557">cthackers/adm-zip#557</a></li>
<li>Fix issue with absolute paths by <a href="https://github.com/kwolfy"><code>@​kwolfy</code></a> in <a href="https://redirect.github.com/cthackers/adm-zip/pull/559">cthackers/adm-zip#559</a></li>
</ul>
<h2>New Contributors</h2>
<ul>
<li><a href="https://github.com/thomasheritage"><code>@​thomasheritage</code></a> made their first contribution in <a href="https://redirect.github.com/cthackers/adm-zip/pull/540">cthackers/adm-zip#540</a></li>
<li><a href="https://github.com/issacgerges"><code>@​issacgerges</code></a> made their first contribution in <a href="https://redirect.github.com/cthackers/adm-zip/pull/543">cthackers/adm-zip#543</a></li>
<li><a href="https://github.com/DennisHill"><code>@​DennisHill</code></a> made their first contribution in <a href="https://redirect.github.com/cthackers/adm-zip/pull/557">cthackers/adm-zip#557</a></li>
<li><a href="https://github.com/kwolfy"><code>@​kwolfy</code></a> made their first contribution in <a href="https://redirect.github.com/cthackers/adm-zip/pull/559">cthackers/adm-zip#559</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/cthackers/adm-zip/compare/v0.5.16...v0.5.17">https://github.com/cthackers/adm-zip/compare/v0.5.16...v0.5.17</a></p>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/cthackers/adm-zip/blob/master/history.md">adm-zip's changelog</a>.</em></p>
<blockquote>
<h1>0.6.0 / 2026-07-10</h1>
<p>Security</p>
<ul>
<li>Fixed CVE-2026-39244: a crafted archive declaring a huge uncompressed size could force an unbounded <code>Buffer.alloc</code> (memory exhaustion / DoS) before any validation. Allocation is now bounded by the data actually present — STORED output is sized from the real bytes, DEFLATED output is grown by the inflater and capped at the declared size (<a href="https://redirect.github.com/cthackers/adm-zip/issues/568">#568</a>)</li>
<li>Hardened the internal entry-name lookup table against object injection: entry names come from untrusted archives, and a name such as <code>__proto__</code> previously resolved to <code>Object.prototype</code>, crashing <code>addFile</code> and hiding the entry from <code>getEntry</code>/<code>readFile</code>. The table is now prototype-less</li>
</ul>
<p>Bug fixes</p>
<ul>
<li>Fixed a regression (0.5.15) that rejected valid archives using a data descriptor (general-purpose bit 3). The payload is now validated against the authoritative central-directory CRC instead of requiring/parsing the trailing descriptor (<a href="https://redirect.github.com/cthackers/adm-zip/issues/548">#548</a>, <a href="https://redirect.github.com/cthackers/adm-zip/issues/533">#533</a>, <a href="https://redirect.github.com/cthackers/adm-zip/issues/554">#554</a>)</li>
<li>Fixed <code>extractAllTo</code>/<code>extractAllToAsync</code> not restoring directory permissions with <code>keepOriginalPermission</code>; directory modes are applied after their contents are written, deepest path first, and no longer lock the extractor out of a restrictive directory (<a href="https://redirect.github.com/cthackers/adm-zip/issues/530">#530</a>)</li>
<li>Fixed infinite recursion in <code>addLocalFolder</code> when a folder contains a symlink pointing back to an ancestor (e.g. workspace <code>node_modules</code>); the walk now tracks resolved real paths and skips already-visited directories (<a href="https://redirect.github.com/cthackers/adm-zip/issues/541">#541</a>)</li>
<li>Fixed an uncaught exception (<code>ERR_INVALID_ARG_TYPE</code>) that crashed the process when <code>writeFileToAsync</code> could not open the target file (bad permissions, invalid filename, exhausted file descriptors); write failures are now reported through the callback and write errors are no longer silently swallowed (<a href="https://redirect.github.com/cthackers/adm-zip/issues/470">#470</a>, <a href="https://redirect.github.com/cthackers/adm-zip/issues/459">#459</a>, <a href="https://redirect.github.com/cthackers/adm-zip/issues/402">#402</a>)</li>
<li>Fixed directory entries reporting an empty <code>name</code> (e.g. <code>a/b/c/</code> now returns <code>c</code>) (<a href="https://redirect.github.com/cthackers/adm-zip/issues/466">#466</a>)</li>
<li>Fixed <code>extractEntryTo</code> flattening subdirectories when <code>maintainEntryPath</code> is false; the structure below the extracted directory is now preserved instead of collapsing (and overwriting) files by basename (<a href="https://redirect.github.com/cthackers/adm-zip/issues/306">#306</a>)</li>
<li>Fixed a failed <code>utimes</code> aborting extraction; setting the modification time is now best-effort and never fails extraction of already-written content (<a href="https://redirect.github.com/cthackers/adm-zip/issues/379">#379</a>)</li>
<li>Fixed <code>test()</code> always returning false for any archive containing a file (it indexed the entries array with an entry object instead of reading the entry); it now correctly verifies each entry's CRC</li>
</ul>
<p>Performance</p>
<ul>
<li>Faster entry sorting when writing archives with many entries: names are decoded once instead of on every comparison (about 6× faster sort for large archives)</li>
</ul>
<p>Added</p>
<ul>
<li>Bundled TypeScript type definitions (<code>types.d.ts</code>), so <code>@types/adm-zip</code> is no longer required</li>
</ul>
<p>Notes</p>
<ul>
<li>Behavior change: <code>extractEntryTo(dir, target, /* maintainEntryPath */ false)</code> now preserves subdirectories beneath the extracted directory rather than flattening them</li>
<li>Behavior change: extraction no longer fails when the modification time cannot be set</li>
</ul>
<h1>0.5.4 / 2021-03-08</h1>
<ul>
<li>Fixed relative paths</li>
<li>Added zipcrypto encryption</li>
<li>Lower verMade for macOS when generating zip file</li>
</ul>
<h1>0.5.3 / 2021-02-07</h1>
<ul>
<li>Fixed filemode when unzipping</li>
</ul>
<h1>0.5.2 / 2021-01-27</h1>
<ul>
<li>Fixed path traversal issue (GHSL-2020-198)</li>
</ul>
<h1>0.5.1 / 2020-11-27</h1>
<ul>
<li>Incremented version (cthackers)</li>
<li>Fixed outFileName (cthackers)</li>
</ul>
<h1>0.5.0 / 2020-11-19</h1>
<ul>
<li>Added extra parameter to extractEntryTo so target filename can be renamed (cthackers)</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/cthackers/adm-zip/commit/2b4d84087d45344643e0183756e19191d52815cc"><code>2b4d840</code></a> updated minimum node engine version to &gt;= 14</li>
<li><a href="https://github.com/cthackers/adm-zip/commit/dc57f0fcc945571052f73f883b42ef1a7237de4e"><code>dc57f0f</code></a> Hardened entry-name lookup, fixed test(), and sped up entry sorting</li>
<li><a href="https://github.com/cthackers/adm-zip/commit/f81806adc0352ea02d01152d740706f02d0cc371"><code>f81806a</code></a> Made utimes best-effort so it can't abort extraction (<a href="https://redirect.github.com/cthackers/adm-zip/issues/379">#379</a>)</li>
<li><a href="https://github.com/cthackers/adm-zip/commit/ab0432410eaef87a6d1e89efdd7266aa9270641b"><code>ab04324</code></a> Fixed extractEntryTo flattening subdirectories (<a href="https://redirect.github.com/cthackers/adm-zip/issues/306">#306</a>)</li>
<li><a href="https://github.com/cthackers/adm-zip/commit/8a5d9bacd5553d7f0172821658e27f4e4e76c6d5"><code>8a5d9ba</code></a> Fixed empty name for directory entries (<a href="https://redirect.github.com/cthackers/adm-zip/issues/466">#466</a>)</li>
<li><a href="https://github.com/cthackers/adm-zip/commit/3e727907541ba2b5cabc3fdba60b71134bd85825"><code>3e72790</code></a> Fixed uncaught crash in writeFileToAsync on write failure (<a href="https://redirect.github.com/cthackers/adm-zip/issues/470">#470</a>, <a href="https://redirect.github.com/cthackers/adm-zip/issues/459">#459</a>, <a href="https://redirect.github.com/cthackers/adm-zip/issues/402">#402</a>)</li>
<li><a href="https://github.com/cthackers/adm-zip/commit/651ae4c3497f4ec2609dbfafb731da32dfe5e9ad"><code>651ae4c</code></a> Added typescript types</li>
<li><a href="https://github.com/cthackers/adm-zip/commit/e72021dedf1140ec09aa529c703c98e4ac7eb947"><code>e72021d</code></a> Fixed infinite recursion on symlink loops in addLocalFolder (<a href="https://redirect.github.com/cthackers/adm-zip/issues/541">#541</a>)</li>
<li><a href="https://github.com/cthackers/adm-zip/commit/8f3176bef3ab5fe89b587e0b8152ae202f28d14a"><code>8f3176b</code></a> Fixed directory permissions on linux</li>
<li><a href="https://github.com/cthackers/adm-zip/commit/4d2c8f9652618d1f70265df818f33c3d57dd53b2"><code>4d2c8f9</code></a> Fixed error introduced with zip descriptor checks</li>
<li>Additional commits viewable in <a href="https://github.com/cthackers/adm-zip/compare/v0.5.16...v0.6.0">compare view</a></li>
</ul>
</details>
<br />

Updates `mermaid` from 11.15.0 to 11.16.1
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/mermaid-js/mermaid/releases">mermaid's releases</a>.</em></p>
<blockquote>
<h2>mermaid@11.16.1</h2>
<h3>Patch Changes</h3>
<ul>
<li>
<p><a href="https://redirect.github.com/mermaid-js/mermaid/pull/8022">#8022</a> <a href="https://github.com/mermaid-js/mermaid/commit/12d472c9ed43f94814b110da8d7a9ae6dd5266ed"><code>12d472c</code></a> Thanks <a href="https://github.com/aloisklink"><code>@​aloisklink</code></a>! - fix: handle CSS sibling combinators in compileCSS</p>
</li>
<li>
<p><a href="https://redirect.github.com/mermaid-js/mermaid/pull/8022">#8022</a> <a href="https://github.com/mermaid-js/mermaid/commit/2cd6dcf735533b323507e3e889ffdea870540b43"><code>2cd6dcf</code></a> Thanks <a href="https://github.com/aloisklink"><code>@​aloisklink</code></a>! - fix: increase protections against prototype pollution</p>
<p>User-controlled input already has protections against prototype pollution.</p>
<p>Fixes: GHSA-c4c3-pg64-4m4v</p>
</li>
<li>
<p><a href="https://redirect.github.com/mermaid-js/mermaid/pull/8022">#8022</a> <a href="https://github.com/mermaid-js/mermaid/commit/99af3fc35ef0a9a9c8c6314521344d67523ddccf"><code>99af3fc</code></a> Thanks <a href="https://github.com/aloisklink"><code>@​aloisklink</code></a>! - fix(architecture): use <code>Map</code>s and <code>Set</code>s to store groups/services</p>
<p>Services are now rendered in the order they are defined and more service IDs
are now supported.</p>
</li>
<li>
<p><a href="https://redirect.github.com/mermaid-js/mermaid/pull/8022">#8022</a> <a href="https://github.com/mermaid-js/mermaid/commit/2cd6dcf735533b323507e3e889ffdea870540b43"><code>2cd6dcf</code></a> Thanks <a href="https://github.com/aloisklink"><code>@​aloisklink</code></a>! - deprecate: Deprecate the <code>mermaidAPI.setConfig()</code> function</p>
<p>Calling this function has no observable effect, as the next time a
<code>render()</code> or <code>parse()</code> is called, the <code>currentConfig</code> is cleared.</p>
</li>
<li>
<p><a href="https://redirect.github.com/mermaid-js/mermaid/pull/8022">#8022</a> <a href="https://github.com/mermaid-js/mermaid/commit/630aa7e5dd417e1f56bff2a1ce8df2c5ad08d289"><code>630aa7e</code></a> Thanks <a href="https://github.com/aloisklink"><code>@​aloisklink</code></a>! - fix(xychart): support zero-width x-axis ranges</p>
</li>
<li>
<p><a href="https://redirect.github.com/mermaid-js/mermaid/pull/8022">#8022</a> <a href="https://github.com/mermaid-js/mermaid/commit/59b22fad2b3bb04f87a476c84a8a2b24679e607e"><code>59b22fa</code></a> Thanks <a href="https://github.com/aloisklink"><code>@​aloisklink</code></a>! - fix(radar): limit number of ticks to 32</p>
<p>Setting a ticks value higher than this would only show 32 ticks.</p>
</li>
</ul>
<h2>mermaid@11.16.0</h2>
<h3>Minor Changes</h3>
<ul>
<li>
<p><a href="https://redirect.github.com/mermaid-js/mermaid/pull/7535">#7535</a> <a href="https://github.com/mermaid-js/mermaid/commit/ea1c48f53fce5d025388d386c90da8743ee25b13"><code>ea1c48f</code></a> Thanks <a href="https://github.com/ragelink"><code>@​ragelink</code></a>! - feat(cynefin): Adds the Cynefin framework as a new diagram type (beta) to Mermaid (available as <code>cynefin-beta</code>). The Cynefin framework, created by Dave Snowden, is a decision-making framework that categorizes problems into five complexity domains, widely used in agile, incident management, strategy, and organizational design.</p>
</li>
<li>
<p><a href="https://redirect.github.com/mermaid-js/mermaid/pull/7721">#7721</a> <a href="https://github.com/mermaid-js/mermaid/commit/f45cc2cc5683b90990e374a463b7bcad0fd68a38"><code>f45cc2c</code></a> Thanks <a href="https://github.com/notionparallax"><code>@​notionparallax</code></a>! - feat(treeView): add box-drawing character input support for treeView diagrams</p>
</li>
<li>
<p><a href="https://redirect.github.com/mermaid-js/mermaid/pull/7550">#7550</a> <a href="https://github.com/mermaid-js/mermaid/commit/f1f4d45ee0513b64a2bd280087d31656f9d2c786"><code>f1f4d45</code></a> Thanks <a href="https://github.com/DominicBurkart"><code>@​DominicBurkart</code></a>! - feat(xychart): add per-point text labels for xychart line plots</p>
</li>
<li>
<p><a href="https://redirect.github.com/mermaid-js/mermaid/pull/7527">#7527</a> <a href="https://github.com/mermaid-js/mermaid/commit/b4d0442dd1628acb3f71681519e7f47fc8bacf55"><code>b4d0442</code></a> Thanks <a href="https://github.com/notionparallax"><code>@​notionparallax</code></a>! - feat(treeView): Extends the existing treeView-beta diagram with features useful for representing file/directory structures.</p>
</li>
<li>
<p><a href="https://redirect.github.com/mermaid-js/mermaid/pull/7793">#7793</a> <a href="https://github.com/mermaid-js/mermaid/commit/a6f097d580d459dfc3ade3e21030037341f79940"><code>a6f097d</code></a> Thanks <a href="https://github.com/SSDWGG"><code>@​SSDWGG</code></a>! - feat(er): support optional ER attribute types with a <code>?</code> suffix</p>
</li>
<li>
<p><a href="https://redirect.github.com/mermaid-js/mermaid/pull/7772">#7772</a> <a href="https://github.com/mermaid-js/mermaid/commit/37f2e36fa017698b66093ac5518396523a7a3241"><code>37f2e36</code></a> Thanks <a href="https://github.com/devareddy05"><code>@​devareddy05</code></a>! - feat(gantt): support multiple <code>excludes</code> / <code>includes</code> lines so long exclusion lists can be split into commented groups (<a href="https://redirect.github.com/mermaid-js/mermaid/issues/6270">#6270</a>)</p>
</li>
<li>
<p><a href="https://redirect.github.com/mermaid-js/mermaid/pull/7708">#7708</a> <a href="https://github.com/mermaid-js/mermaid/commit/4e63e9d338b6476df283afd4a002072945bc4563"><code>4e63e9d</code></a> Thanks <a href="https://github.com/txmxthy"><code>@​txmxthy</code></a>! - feat(architecture): add <code>align row|column {ids…}</code> directive to architecture-beta diagrams so authors can declare horizontal or vertical alignment of services explicitly.</p>
</li>
<li>
<p><a href="https://redirect.github.com/mermaid-js/mermaid/pull/7760">#7760</a> <a href="https://github.com/mermaid-js/mermaid/commit/05223bee47a424be3ba7805e753b96861d342765"><code>05223be</code></a> Thanks <a href="https://github.com/ngdaniels"><code>@​ngdaniels</code></a>! - feat(pie): Enhance Pie Chart - Enable donut chart, Set legend position, and highlight slice</p>
</li>
<li>
<p><a href="https://redirect.github.com/mermaid-js/mermaid/pull/7251">#7251</a> <a href="https://github.com/mermaid-js/mermaid/commit/216e4e9a61afceae885b00854f79e17373ccad31"><code>216e4e9</code></a> Thanks <a href="https://github.com/ydah"><code>@​ydah</code></a>! - feat(railroad): Add support for Railroad Diagrams (Syntax Diagrams) with four input syntaxes: IR (railroad-beta), EBNF (railroad-ebnf-beta), ABNF (railroad-abnf-beta), and PEG (railroad-peg-beta).</p>
</li>
<li>
<p><a href="https://redirect.github.com/mermaid-js/mermaid/pull/7774">#7774</a> <a href="https://github.com/mermaid-js/mermaid/commit/e5c75e6b797f84f8f652d8771eb1ce6161dd8f89"><code>e5c75e6</code></a> Thanks <a href="https://github.com/ngdaniels"><code>@​ngdaniels</code></a>! - feat(xychart): enable rotate label on X-axis</p>
</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/mermaid-js/mermaid/commit/7ecca0cd7f1658ef74f4e7e91f925724ef403bbf"><code>7ecca0c</code></a> Version Packages (<a href="https://redirect.github.com/mermaid-js/mermaid/issues/8023">#8023</a>)</li>
<li><a href="https://github.com/mermaid-js/mermaid/commit/95b1b9cdba40e7954aee7d8a265577fd3839710c"><code>95b1b9c</code></a> docs: change <code>mermaidAPI.setConfig()</code> changeset (<a href="https://redirect.github.com/mermaid-js/mermaid/issues/8024">#8024</a>)</li>
<li><a href="https://github.com/mermaid-js/mermaid/commit/acc69f172b5ad5405ca8de8f4f79a80505092b3f"><code>acc69f1</code></a> Merge pull request <a href="https://redirect.github.com/mermaid-js/mermaid/issues/8022">#8022</a> from mermaid-js/release/11.16.1</li>
<li><a href="https://github.com/mermaid-js/mermaid/commit/eba72879e94755433403e571d724ca7a448800af"><code>eba7287</code></a> docs: point changesets to correct commit hashes</li>
<li><a href="https://github.com/mermaid-js/mermaid/commit/12d472c9ed43f94814b110da8d7a9ae6dd5266ed"><code>12d472c</code></a> Merge commit from fork</li>
<li><a href="https://github.com/mermaid-js/mermaid/commit/2cd6dcf735533b323507e3e889ffdea870540b43"><code>2cd6dcf</code></a> Merge commit from fork</li>
<li><a href="https://github.com/mermaid-js/mermaid/commit/630aa7e5dd417e1f56bff2a1ce8df2c5ad08d289"><code>630aa7e</code></a> Merge commit from fork</li>
<li><a href="https://github.com/mermaid-js/mermaid/commit/59b22fad2b3bb04f87a476c84a8a2b24679e607e"><code>59b22fa</code></a> Merge commit from fork</li>
<li><a href="https://github.com/mermaid-js/mermaid/commit/99af3fc35ef0a9a9c8c6314521344d67523ddccf"><code>99af3fc</code></a> Merge commit from fork</li>
<li><a href="https://github.com/mermaid-js/mermaid/commit/2337f7ecd629c8e777684a2edff341976230ad67"><code>2337f7e</code></a> Merge branch 'test/improve-example.html' into release/11.16.1</li>
<li>Additional commits viewable in <a href="https://github.com/mermaid-js/mermaid/compare/mermaid@11.15.0...mermaid@11.16.1">compare view</a></li>
</ul>
</details>
<br />

Updates `postcss` from 8.5.10 to 8.5.23
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/postcss/postcss/releases">postcss's releases</a>.</em></p>
<blockquote>
<h2>8.5.23</h2>
<ul>
<li>Do not load source map without <code>opts.from</code> for security reasons.</li>
</ul>
<h2>8.5.22</h2>
<ul>
<li>Fixed custom property losing semicolon before a comment (by <a href="https://github.com/sarathfrancis90"><code>@​sarathfrancis90</code></a>).</li>
</ul>
<h2>8.5.21</h2>
<ul>
<li>Fixed childless at-rule losing semicolon before comment (by <a href="https://github.com/sarathfrancis90"><code>@​sarathfrancis90</code></a>).</li>
<li>Fixed docs (by <a href="https://github.com/isker"><code>@​isker</code></a>).</li>
</ul>
<h2>8.5.20</h2>
<ul>
<li>Fixed missing space if <code>AtRule#params</code> is set after (by <a href="https://github.com/sarathfrancis90"><code>@​sarathfrancis90</code></a>).</li>
<li>Fixed mixing AST error on warnings (by <a href="https://github.com/MahinAnowar"><code>@​MahinAnowar</code></a>).</li>
</ul>
<h2>8.5.19</h2>
<ul>
<li>Fixed cleaning <code>before</code> for new nodes inserted to <code>Root</code> (by <a href="https://github.com/MahinAnowar"><code>@​MahinAnowar</code></a>).</li>
</ul>
<h2>8.5.18</h2>
<ul>
<li>Restricted loading previous source maps file to the <code>opts.from</code> folder for security reasons (use <code>unsafeMap: true</code> to disable the check).</li>
</ul>
<h2>8.5.17</h2>
<ul>
<li>Fixed <code>Maximum call stack size exceeded</code> error.</li>
<li>Fixed Prototype hijacking for <code>postcss.fromJSON()</code>.</li>
<li>Fixed <code>Input#origin()</code> for unmapped end position (by <a href="https://github.com/chatman-media"><code>@​chatman-media</code></a>).</li>
</ul>
<h2>8.5.16</h2>
<ul>
<li>Fixed <code>Input#origin()</code> position (by <a href="https://github.com/mizdra"><code>@​mizdra</code></a>).</li>
<li>Fixed <code>raws</code> after rehydrating a JSON AST (by <a href="https://github.com/sarathfrancis90"><code>@​sarathfrancis90</code></a>).</li>
<li>Fixed putting parent-less node in <code>nodes</code> of new node (by <a href="https://github.com/MahinAnowar"><code>@​MahinAnowar</code></a>).</li>
<li>Fixed computing <code>offset</code> in <code>positionBy()</code> (by <a href="https://github.com/greymoth-jp"><code>@​greymoth-jp</code></a>).</li>
<li>Fixed <code>rangeBy()</code> on <code>index: 0</code> (by <a href="https://github.com/sarathfrancis90"><code>@​sarathfrancis90</code></a>).</li>
</ul>
<h2>8.5.15</h2>
<ul>
<li>Fixed declaration parsing performance (by <a href="https://github.com/homanp"><code>@​homanp</code></a>).</li>
</ul>
<h2>8.5.14</h2>
<ul>
<li>Fixed custom syntax regression (by <a href="https://github.com/43081j"><code>@​43081j</code></a>).</li>
</ul>
<h2>8.5.13</h2>
<ul>
<li>Fixed <code>postcss-scss</code> commend regression.</li>
</ul>
<h2>8.5.12</h2>
<ul>
<li>Fixed reading any file via user-generated CSS.</li>
<li>Added <code>opts.unsafeMap</code> to disable checks.</li>
</ul>
<h2>8.5.11</h2>
<ul>
<li>Fixed nested brackets parsing performance (by <a href="https://github.com/offset"><code>@​offset</code></a>).</li>
</ul>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/postcss/postcss/blob/main/CHANGELOG.md">postcss's changelog</a>.</em></p>
<blockquote>
<h2>8.5.23</h2>
<ul>
<li>Do not load source map without <code>opts.from</code> for security reasons.</li>
</ul>
<h2>8.5.22</h2>
<ul>
<li>Fixed custom property losing semicolon before a comment (by <a href="https://github.com/sarathfrancis90"><code>@​sarathfrancis90</code></a>).</li>
</ul>
<h2>8.5.21</h2>
<ul>
<li>Fixed childless at-rule losing semicolon before comment (by <a href="https://github.com/sarathfrancis90"><code>@​sarathfrancis90</code></a>).</li>
<li>Fixed docs (by <a href="https://github.com/isker"><code>@​isker</code></a>).</li>
</ul>
<h2>8.5.20</h2>
<ul>
<li>Fixed missing space if <code>AtRule#params</code> is set after (by <a href="https://github.com/sarathfrancis90"><code>@​sarathfrancis90</code></a>).</li>
<li>Fixed mixing AST error on warnings (by <a href="https://github.com/MahinAnowar"><code>@​MahinAnowar</code></a>).</li>
</ul>
<h2>8.5.19</h2>
<ul>
<li>Fixed cleaning <code>before</code> for new nodes inserted to <code>Root</code> (by <a href="https://github.com/MahinAnowar"><code>@​MahinAnowar</code></a>).</li>
</ul>
<h2>8.5.18</h2>
<ul>
<li>Restricted loading previous source maps file to the <code>opts.from</code> folder for security reasons (use <code>unsafeMap: true</code> to disable the check).</li>
</ul>
<h2>8.5.17</h2>
<ul>
<li>Fixed <code>Maximum call stack size exceeded</code> error.</li>
<li>Fixed Prototype hijacking for <code>postcss.fromJSON()</code>.</li>
<li>Fixed <code>Input#origin()</code> for unmapped end position (by <a href="https://github.com/chatman-media"><code>@​chatman-media</code></a>).</li>
</ul>
<h2>8.5.16</h2>
<ul>
<li>Fixed <code>Input#origin()</code> position (by <a href="https://github.com/mizdra"><code>@​mizdra</code></a>).</li>
<li>Fixed <code>raws</code> after rehydrating a JSON AST (by <a href="https://github.com/sarathfrancis90"><code>@​sarathfrancis90</code></a>).</li>
<li>Fixed putting parent-less node in <code>nodes</code> of new node (by <a href="https://github.com/MahinAnowar"><code>@​MahinAnowar</code></a>).</li>
<li>Fixed computing <code>offset</code> in <code>positionBy()</code> (by <a href="https://github.com/greymoth-jp"><code>@​greymoth-jp</code></a>).</li>
<li>Fixed <code>rangeBy()</code> on <code>index: 0</code> (by <a href="https://github.com/sarathfrancis90"><code>@​sarathfrancis90</code></a>).</li>
</ul>
<h2>8.5.15</h2>
<ul>
<li>Fixed declaration parsing performance (by <a href="https://github.com/homanp"><code>@​homanp</code></a>).</li>
</ul>
<h2>8.5.14</h2>
<ul>
<li>Fixed custom syntax regression (by <a href="https://github.com/43081j"><code>@​43081j</code></a>).</li>
</ul>
<h2>8.5.13</h2>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/postcss/postcss/commit/eb9e1fe793740bb3280bdf5bf98147f857f011bd"><code>eb9e1fe</code></a> Release 8.5.23 version</li>
<li><a href="https://github.com/postcss/postcss/commit/9d19c78ac91108b3f7d7130e55c6fa806c0efb84"><code>9d19c78</code></a> Update dependencies</li>
<li><a href="https://github.com/postcss/postcss/commit/7beca139e70f9075c6b19700fcb00dd8033e5da8"><code>7beca13</code></a> Does no load source map file without opts.from</li>
<li><a href="https://github.com/postcss/postcss/commit/decea51421682341401575b3740709fda0e12930"><code>decea51</code></a> Typo</li>
<li><a href="https://github.com/postcss/postcss/commit/c18e30d126395d42a0726aa00e03a8f1088985ae"><code>c18e30d</code></a> Update EM banner</li>
<li><a href="https://github.com/postcss/postcss/commit/98a39ad73d163a90be924d5126c771262110f1fc"><code>98a39ad</code></a> Update EM banner</li>
<li><a href="https://github.com/postcss/postcss/commit/a3e48c492ddec0e4879d513b8b995fee887af352"><code>a3e48c4</code></a> Release 8.5.22 version</li>
<li><a href="https://github.com/postcss/postcss/commit/f49d6911795f53b2cfe023bb686bf1144ec30618"><code>f49d691</code></a> Fix custom property losing its semicolon before a comment (<a href="https://redirect.github.com/postcss/postcss/issues/2117">#2117</a>)</li>
<li><a href="https://github.com/postcss/postcss/commit/28e0daf8f2fe5ba9e19ea3f8c27c8fe176f9419e"><code>28e0daf</code></a> Release 8.5.21 version</li>
<li><a href="https://github.com/postcss/postcss/commit/3d2b4e43e38274f233b5609d09687cadad8215d9"><code>3d2b4e4</code></a> Update dependencies</li>
<li>Additional commits viewable in <a href="https://github.com/postcss/postcss/compare/8.5.10...8.5.23">compare view</a></li>
</ul>
</details>
<details>
<summary>Maintainer changes</summary>
<p>This version was pushed to npm by <a href="https://www.npmjs.com/~GitHub%20Actions">GitHub Actions</a>, a new releaser for postcss since your current version.</p>
</details>
<br />

Updates `sharp` from 0.33.5 to 0.35.0
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/lovell/sharp/releases">sharp's releases</a>.</em></p>
<blockquote>
<h2>v0.35.0</h2>
<ul>
<li>
<p>Breaking: Drop support for Node.js 18, now requires Node.js &gt;= 20.9.0.</p>
</li>
<li>
<p>Breaking: Remove <code>install</code> script from <code>package.json</code> file.
Compiling from source is now opt-in via the <code>build</code> script.</p>
</li>
<li>
<p>Breaking: Lossy AVIF output is now tuned using SSIMULACRA2-based <code>iq</code> quality metrics.</p>
</li>
<li>
<p>Breaking: Add <code>limitInputChannels</code> with a default value of 5.</p>
</li>
<li>
<p>Breaking: Remove deprecated <code>failOnError</code> constructor property.</p>
</li>
<li>
<p>Breaking: Remove deprecated <code>paletteBitDepth</code> from <code>metadata</code> response.</p>
</li>
<li>
<p>Breaking: Remove deprecated properties from <code>sharpen</code> operation.</p>
</li>
<li>
<p>Breaking: Rename <code>format.jp2k</code> as <code>format.jp2</code> for API consistency.</p>
</li>
<li>
<p>Upgrade to libvips v8.18.3 for upstream bug fixes.</p>
</li>
<li>
<p>Remove experimental status from WebAssembly binaries.</p>
</li>
<li>
<p>Add prebuilt binaries for FreeBSD (WebAssembly).</p>
</li>
<li>
<p>Deprecate Windows 32-bit (win32-ia32) prebuilt binaries.</p>
</li>
<li>
<p>Ensure TIFF output <code>bitdepth</code> option is limited to 1, 2 or 4.</p>
</li>
<li>
<p>Add AVIF/HEIF <code>tune</code> option for control over quality metrics.
<a href="https://redirect.github.com/lovell/sharp/issues/4227">#4227</a></p>
</li>
<li>
<p>Add <code>keepGainMap</code> and <code>withGainMap</code> to process HDR JPEG images with embedded gain maps.
<a href="https://redirect.github.com/lovell/sharp/issues/4314">#4314</a></p>
</li>
<li>
<p>Add <code>toUint8Array</code> for output image as a <code>TypedArray</code> backed by a transferable <code>ArrayBuffer</code>.
<a href="https://redirect.github.com/lovell/sharp/issues/4355">#4355</a></p>
</li>
<li>
<p>Require prebuilt binaries using static paths to aid code bundling.
<a href="https://redirect.github.com/lovell/sharp/issues/4380">#4380</a></p>
</li>
<li>
<p>TypeScript: Ensure <code>FormatEnum</code> keys match reality.
<a href="https://redirect.github.com/lovell/sharp/issues/4475">#4475</a></p>
</li>
<li>
<p>Add <code>margin</code> option to <code>trim</code> operation.
<a href="https://redirect.github.com/lovell/sharp/issues/4480">#4480</a>
<a href="https://github.com/eddienubes"><code>@​eddienubes</code></a></p>
</li>
<li>
<p>Ensure HEIF primary item is used as default page/frame.
<a href="https://redirect.github.com/lovell/sharp/issues/4487">#4487</a></p>
</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/lovell/sharp/commit/2ed5af48cdf4c7a1c93fc82ff37d64e151bbadb7"><code>2ed5af4</code></a> Release v0.35.0</li>
<li><a href="https://github.com/lovell/sharp/commit/4475cf10e7cf893d366f4e0d12fe1deae56d7398"><code>4475cf1</code></a> Tests: update locator hash for sharp-libvips v1.3.0</li>
<li><a href="https://github.com/lovell/sharp/commit/deb22ddd2fa6a9593bb720ba51e05b8b905504a2"><code>deb22dd</code></a> Upgrade to sharp-libvips v1.3.0</li>
<li><a href="https://github.com/lovell/sharp/commit/07f1be984a2d221d0880f8b2cba6f298caf5370b"><code>07f1be9</code></a> Prerelease v0.35.0-rc.8</li>
<li><a href="https://github.com/lovell/sharp/commit/df1109bf3af863ffbb6c3cfd636fc24723aea64d"><code>df1109b</code></a> Prerelease v0.35.0-rc.7</li>
<li><a href="https://github.com/lovell/sharp/commit/aca49b37152964138a150b8307532708fc0e4a3c"><code>aca49b3</code></a> Upgrade to libvips v8.18.3</li>
<li><a href="https://github.com/lovell/sharp/commit/e9e86f5802a814549ce9007dfa183ad80aa04189"><code>e9e86f5</code></a> Type-check density option before range validation (<a href="https://redirect.github.com/lovell/sharp/issues/4536">#4536</a>)</li>
<li><a href="https://github.com/lovell/sharp/commit/2f0bcf00ed1ec9b3b60fd184ec6c512ba7e3233c"><code>2f0bcf0</code></a> Docs: update supported image formats</li>
<li><a href="https://github.com/lovell/sharp/commit/98e03b83fbc07bd7bb2e421bc2906d4e62d84c7f"><code>98e03b8</code></a> Revert &quot;Guard heif bitdepth property for prebuilt binaries&quot;</li>
<li><a href="https://github.com/lovell/sharp/commit/e4ea2f35eb7194ec7ade46de64bf2a9904c07127"><code>e4ea2f3</code></a> CI: Ignore package minimum age in smoke tests</li>
<li>Additional commits viewable in <a href="https://github.com/lovell/sharp/compare/v0.33.5...v0.35.0">compare view</a></li>
</ul>
</details>
<details>
<summary>Maintainer changes</summary>
<p>This version was pushed to npm by <a href="https://www.npmjs.com/~GitHub%20Actions">GitHub Actions</a>, a new releaser for sharp since your current version.</p>
</details>
<br />

Updates `@hono/node-server` from 1.19.13 to 1.19.17
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/honojs/node-server/releases">@​hono/node-server's releases</a>.</em></p>
<blockquote>
<h2>v1.19.17</h2>
<p>No release notes provided.</p>
<h2>v1.19.14</h2>
<h2>What's Changed</h2>
<ul>
<li>fix: add custom inspect to lightweight Request/Response to prevent TypeError on console.log by <a href="https://github.com/usualoma"><code>@​usualoma</code></a> in <a href="https://redirect.github.com/honojs/node-server/pull/340">honojs/node-server#340</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/honojs/node-server/compare/v1.19.13...v1.19.14">https://github.com/honojs/node-server/compare/v1.19.13...v1.19.14</a></p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/honojs/node-server/commit/71941daede982571f18d2774951f37c475cccefc"><code>71941da</code></a> 1.19.17</li>
<li><a href="https://github.com/honojs/node-server/commit/0208500d8f11b33dd03b50c86df8e132307adf1e"><code>0208500</code></a> ci: add <code>stage</code> option for publishing (<a href="https://redirect.github.com/honojs/node-server/issues/386">#386</a>)</li>
<li><a href="https://github.com/honojs/node-server/commit/cbdf713a67ef38f6a5304488e294381230a52e46"><code>cbdf713</code></a> 1.19.16</li>
<li><a href="https://github.com/honojs/node-server/commit/86e96c24045411b3e3c4a9b61a4c1e755c398a44"><code>86e96c2</code></a> ci: add an action for trusted publisher (<a href="https://redirect.github.com/honojs/node-server/issues/385">#385</a>)</li>
<li><a href="https://github.com/honojs/node-server/commit/99c1a1abd702132302f3da72600d383a25eba32c"><code>99c1a1a</code></a> ci: run on v1.x branch pushes</li>
<li><a href="https://github.com/honojs/node-server/commit/84cb2ee25f567d812b76e0cff4c36899acb157eb"><code>84cb2ee</code></a> Merge commit from fork</li>
<li><a href="https://github.com/honojs/node-server/commit/b5e63a366d9b0ef62ac65fcafd7f69b383b03ff5"><code>b5e63a3</code></a> 1.19.14</li>
<li><a href="https://github.com/honojs/node-server/commit/c02d7770a2d29ea473403211bef0a60639885a28"><code>c02d777</code></a> fix: add custom inspect to lightweight Request/Response to prevent TypeError ...</li>
<li>See full diff in <a href="https://github.com/honojs/node-server/compare/v1.19.13...v1.19.17">compare view</a></li>
</ul>
</details>
<details>
<summary>Maintainer changes</summary>
<p>This version was pushed to npm by <a href="https://www.npmjs.com/~GitHub%20Actions">GitHub Actions</a>, a new releaser for <code>@​hono/node-server</code> since your current version.</p>
</details>
<br />

Updates `body-parser` from 2.2.2 to 2.3.0
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/expressjs/body-parser/releases">body-parser's releases</a>.</em></p>
<blockquote>
<h2>v2.3.0</h2>
<h2>Important: Security</h2>
<ul>
<li>Security fix for <a href="https://www.cve.org/CVERecord?id=CVE-2025-13466">CVE-2026-12590</a> (<a href="https://github.com/expressjs/body-parser/security/advisories/GHSA-v422-hmwv-36x6">GHSA-v422-hmwv-36x6</a>)</li>
</ul>
<h2>What's Changed</h2>
<ul>
<li>build(deps): bump actions/download-artifact from 6.0.0 to 7.0.0 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/681">expressjs/body-parser#681</a></li>
<li>build(deps): bump actions/checkout from 5.0.0 to 6.0.1 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/682">expressjs/body-parser#682</a></li>
<li>build(deps): bump actions/setup-node from 6.0.0 to 6.1.0 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/683">expressjs/body-parser#683</a></li>
<li>build(deps): bump actions/upload-artifact from 5.0.0 to 6.0.0 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/685">expressjs/body-parser#685</a></li>
<li>build(deps): bump github/codeql-action from 4.31.2 to 4.31.9 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/684">expressjs/body-parser#684</a></li>
<li>perf(urlencoded): move empty-body guard to avoid extra function closure by <a href="https://github.com/Phillip9587"><code>@​Phillip9587</code></a> in <a href="https://redirect.github.com/expressjs/body-parser/pull/647">expressjs/body-parser#647</a></li>
<li>Improve ESM compatibility by <a href="https://github.com/Phillip9587"><code>@​Phillip9587</code></a> in <a href="https://redirect.github.com/expressjs/body-parser/pull/697">expressjs/body-parser#697</a></li>
<li>docs: add recommendations for configuring payload limits by <a href="https://github.com/bjohansebas"><code>@​bjohansebas</code></a> in <a href="https://redirect.github.com/expressjs/body-parser/pull/699">expressjs/body-parser#699</a></li>
<li>build(deps): bump actions/setup-node from 6.1.0 to 6.2.0 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/701">expressjs/body-parser#701</a></li>
<li>build(deps): bump github/codeql-action from 4.31.10 to 4.32.0 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/702">expressjs/body-parser#702</a></li>
<li>build(deps): bump actions/checkout from 6.0.1 to 6.0.2 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/700">expressjs/body-parser#700</a></li>
<li>chore:  add explicit type commonjs to package.json by <a href="https://github.com/Phillip9587"><code>@​Phillip9587</code></a> in <a href="https://redirect.github.com/expressjs/body-parser/pull/711">expressjs/body-parser#711</a></li>
<li>deps: update dependencies to latest versions by <a href="https://github.com/Phillip9587"><code>@​Phillip9587</code></a> in <a href="https://redirect.github.com/expressjs/body-parser/pull/708">expressjs/body-parser#708</a></li>
<li>build(deps): bump actions/download-artifact from 7.0.0 to 8.0.0 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/712">expressjs/body-parser#712</a></li>
<li>build(deps): bump github/codeql-action from 4.32.0 to 4.32.4 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/713">expressjs/body-parser#713</a></li>
<li>build(deps): bump actions/upload-artifact from 6.0.0 to 7.0.0 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/714">expressjs/body-parser#714</a></li>
<li>fix: improve limit option validation by <a href="https://github.com/Phillip9587"><code>@​Phillip9587</code></a> in <a href="https://redirect.github.com/expressjs/body-parser/pull/698">expressjs/body-parser#698</a></li>
<li>build(deps): bump github/codeql-action from 4.32.4 to 4.35.1 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/719">expressjs/body-parser#719</a></li>
<li>build(deps): bump actions/setup-node from 6.2.0 to 6.3.0 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/718">expressjs/body-parser#718</a></li>
<li>build(deps): bump actions/download-artifact from 8.0.0 to 8.0.1 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/717">expressjs/body-parser#717</a></li>
<li>perf: eliminate conditional check in json strict mode hot path by <a href="https://github.com/Phillip9587"><code>@​Phillip9587</code></a> in <a href="https://redirect.github.com/expressjs/body-parser/pull/651">expressjs/body-parser#651</a></li>
<li>ci: add node.js 26 to text matrix by <a href="https://github.com/Phillip9587"><code>@​Phillip9587</code></a> in <a href="https://redirect.github.com/expressjs/body-parser/pull/726">expressjs/body-parser#726</a></li>
<li>build(deps): bump actions/setup-node from 6.3.0 to 6.4.0 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/725">expressjs/body-parser#725</a></li>
<li>build(deps): bump actions/upload-artifact from 7.0.0 to 7.0.1 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/724">expressjs/body-parser#724</a></li>
<li>build(deps): bump github/codeql-action from 4.35.1 to 4.35.3 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/723">expressjs/body-parser#723</a></li>
<li>Upgrade &quot;content-type&quot; by <a href="https://github.com/blakeembrey"><code>@​blakeembrey</code></a> in <a href="https://redirect.github.com/expressjs/body-parser/pull/728">expressjs/body-parser#728</a></li>
<li>refactor: switch to const/let and enable eslint no-var rule by <a href="https://github.com/Phillip9587"><code>@​Phillip9587</code></a> in <a href="https://redirect.github.com/expressjs/body-parser/pull/729">expressjs/body-parser#729</a></li>
<li>Update outdated reference to MDN docs by <a href="https://github.com/krzysdz"><code>@​krzysdz</code></a> in <a href="https://redirect.github.com/expressjs/body-parser/pull/730">expressjs/body-parser#730</a></li>
<li>build(deps): bump github/codeql-action from 4.35.3 to 4.36.1 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/731">expressjs/body-parser#731</a></li>
<li>build(deps): bump actions/checkout from 6.0.2 to 6.0.3 by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/expressjs/body-parser/pull/732">expressjs/body-parser#732</a></li>
<li>chore: updated deps to latest by <a href="https://github.com/Phillip9587"><code>@​Phillip9587</code></a> in <a href="https://redirect.github.com/expressjs/body-parser/pull/733">expressjs/body-parser#733</a></li>
<li>2.3.0 by <a href="https://github.com/UlisesGascon"><code>@​UlisesGascon</code></a> in <a href="https://redirect.github.com/expressjs/body-parser/pull/735">expressjs/body-parser#735</a></li>
</ul>
<h2>New Contributors</h2>
<ul>
<li><a href="https://github.com/krzysdz"><code>@​krzysdz</code></a> made their first contribution in <a href="https://redirect.github.com/expressjs/body-parser/pull/730">expressjs/body-parser#730</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/expressjs/body-parser/compare/v2.2.2...v2.3.0">https://github.com/expressjs/body-parser/compare/v2.2.2...v2.3.0</a></p>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/expressjs/body-parser/blob/master/HISTORY.md">body-parser's changelog</a>.</em></p>
<blockquote>
<h1>2.3.0 / 2026-06-15</h1>
<ul>
<li>Security fix for <a href="https://github.com/expressjs/body-parser/security/advisories/GHSA-v422-hmwv-36x6">GHSA-v422-hmwv-36x6</a></li>
<li>fix: use static exports instead of lazy getters to improve ESM compatibility</li>
<li>feat: add subpath exports for individual parsers</li>
<li>fix: improve <code>limit</code> option validation (<a href="https://redirect.github.com/expressjs/body-parser/issues/698">#698</a>)
<ul>
<li>Invalid <code>limit</code> values (e.g. unparseable strings or <code>NaN</code>) now throw instead of being silently ignored, which previously disabled size limit enforcement</li>
<li><code>null</code> and <code>undefined</code> fall back to the default 100kb limit</li>
</ul>
</li>
<li>deps:
<ul>
<li>content-type@^2.0.0</li>
<li>http-errors@^2.0.1</li>
<li>iconv-lite^0.7.2</li>
<li>qs@^6.15.2</li>
<li>raw-body@^3.0.2</li>
<li>type-is@^2.1.0</li>
</ul>
</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/expressjs/body-parser/commit/d0f2ace6c74769da7d19b8661b9a01c01bdb0bf7"><code>d0f2ace</code></a> 2.3.0 (<a href="https://redirect.github.com/expressjs/body-parser/issues/735">#735</a>)</li>
<li><a href="https://github.com/expressjs/body-parser/commit/7d03f2f9d561dafd1576b137713353c95253512c"><code>7d03f2f</code></a> chore: updated deps to latest (<a href="https://redirect.github.com/expressjs/body-parser/issues/733">#733</a>)</li>
<li><a href="https://github.com/expressjs/body-parser/commit/8024ba7a813e6647ed63832d209a2abb8531267a"><code>8024ba7</code></a> build(deps): bump actions/checkout from 6.0.2 to 6.0.3 (<a href="https://redirect.github.com/expressjs/body-parser/issues/732">#732</a>)</li>
<li><a href="https://github.com/expressjs/body-parser/commit/32b4ed4639281f04563adcd41d724ab06c9105d4"><code>32b4ed4</code></a> build(deps): bump github/codeql-action from 4.35.3 to 4.36.1 (<a href="https://redirect.github.com/expressjs/body-parser/issues/731">#731</a>)</li>
<li><a href="https://github.com/expressjs/body-parser/commit/ff0f6b907106ec5a1b81c80f5a552d921c1bc9a5"><code>ff0f6b9</code></a> docs: update outdated reference to MDN docs (<a href="https://redirect.github.com/expressjs/body-parser/issues/730">#730</a>)</li>
<li><a href="https://github.com/expressjs/body-parser/commit/14d001a9c90abc05891d895ad3e9cf0a65b7b34a"><code>14d001a</code></a> refactor: switch to const/let and enable eslint no-var rule (<a href="https://redirect.github.com/expressjs/body-parser/issues/729">#729</a>)</li>
<li><a href="https://github.com/expressjs/body-parser/commit/37f36a27528e65d7216f2c31c7039d3458c72147"><code>37f36a2</code></a> deps: update content-type and type-is (<a href="https://redirect.github.com/expressjs/body-parser/issues/728">#728</a>)</li>
<li><a href="https://github.com/expressjs/body-parser/commit/e1c244bf55fb00a6de4be882b4ed9fc20807d864"><code>e1c244b</code></a> build(deps): bump github/codeql-action from 4.35.1 to 4.35.3 (<a href="https://redirect.github.com/expressjs/body-parser/issues/723">#723</a>)</li>
<li><a href="https://github.com/expressjs/body-parser/commit/e01087f52192e20e2d0f8726d4f28a8d49d06c87"><code>e01087f</code></a> build(deps): bump actions/upload-artifact from 7.0.0 to 7.0.1 (<a href="https://redirect.github.com/expressjs/body-parser/issues/724">#724</a>)</li>
<li><a href="https://github.com/expressjs/body-parser/commit/a7698d30280a3e931ea8841396e5d0ac5414e429"><code>a7698d3</code></a> build(deps): bump actions/setup-node from 6.3.0 to 6.4.0 (<a href="https://redirect.github.com/expressjs/body-parser/issues/725">#725</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/expressjs/body-parser/compare/v2.2.2...v2.3.0">compare view</a></li>
</ul>
</details>
<br />

Updates `brace-expansion` from 1.1.15 to 1.1.18
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/juliangruber/brace-expansion/commit/758fcd6d188a95c2342818519c77b8c06794552b"><code>758fcd6</code></a> 1.1.18</li>
<li><a href="https://github.com/juliangruber/brace-expansion/commit/27fbeed22b4fdf2c5f732f66bcf84d43f4a26c6e"><code>27fbeed</code></a> Merge commit from fork</li>
<li><a href="https://github.com/juliangruber/brace-expansion/commit/5c57cc2519dfb067e188b7cb0733fffbd02946bf"><code>5c57cc2</code></a> 1.1.17</li>
<li><a href="https://github.com/juliangruber/brace-expansion/commit/d757f1dde7808bcbcd7a4628ab913e5185ed3d57"><code>d757f1d</code></a> npm ignore <code>.claude</code></li>
<li><a href="https://github.com/juliangruber/brace-expansion/commit/cb4b9e47cc2ec777c14b2b4492fb431a56f6a031"><code>cb4b9e4</code></a> fix: backport GHSA-mh99-v99m-4gvg (<a href="https://redirect.github.com/juliangruber/brace-expansion/issues/129">#129</a>)</li>
<li><a href="https://github.com/juliangruber/brace-expansion/commit/447763a91a613cfa67ac73096cbc1de9a2304f97"><code>447763a</code></a> 1.1.16</li>
<li><a href="https://github.com/juliangruber/brace-expansion/commit/d74e63030c012e3b7ae81657b8d665619cd51b95"><code>d74e630</code></a> fix: v1 backport for CVE-2026-13149 (<a href="https://redirect.github.com/juliangruber/brace-expansion/issues/122">#122</a>)</li>
<li>See full diff in <a href="https://github.com/juliangruber/brace-expansion/compare/v1.1.15...v1.1.18">compare view</a></li>
</ul>
</details>
<br />

Updates `dompurify` from 3.4.11 to 3.4.13
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/cure53/DOMPurify/releases">dompurify's releases</a>.</em></p>
<blockquote>
<h2>DOMPurify 3.4.13</h2>
<ul>
<li>Fixed an issue with hook removal during <code>IN_PLACE</code> sanitization, thanks <a href="https://github.com/koyokr"><code>@​koyokr</code></a></li>
<li>Fixed an issue with hooks potentially bypassing the clone guard, thanks <a href="https://github.com/AkshayjainG"><code>@​AkshayjainG</code></a></li>
<li>Fixed an issue with DOM clobbering via <code>ownerDocument</code> during <code>IN_PLACE</code>, thanks <a href="https://github.com/AkshayjainG"><code>@​AkshayjainG</code></a></li>
<li>Bumped several dependencies where possible</li>
</ul>
<h2>DOMPurify 3.4.12</h2>
<ul>
<li>Fixed an issue where a hook would not get called for custom elements, thanks <a href="https://github.com/Rikuxx0"><code>@​Rikuxx0</code></a></li>
<li>Hardened the handling of hooks removing elements, <a href="https://github.com/mkrause-bee360"><code>@​mkrause-bee360</code></a></li>
<li>Added support for a few new SVG attributes, thanks <a href="https://github.com/cbn-falias"><code>@​cbn-falias</code></a> &amp; <a href="https://github.com/Develop-KIM"><code>@​Develop-KIM</code></a></li>
<li>Hardened the handling of declarative partial updates</li>
<li>Updated the documentation is several spots, README, wiki, etc.</li>
<li>Bumped several dependencies where possible</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/cure53/DOMPurify/commit/3067f774676975de12306effd6db6ad7a9a8c17f"><code>3067f77</code></a> release: 3.4.13 (<a href="https://redirect.github.com/cure53/DOMPurify/issues/1562">#1562</a>)</li>
<li><a href="https://github.com/cure53/DOMPurify/commit/a9ca1e537422319a557a9a2aa61f003b23b4a197"><code>a9ca1e5</code></a> release: 3.4.12 (<a href="https://redirect.github.com/cure53/DOMPurify/issues/1537">#1537</a>)</li>
<li>See full diff in <a href="https://github.com/cure53/DOMPurify/compare/3.4.11...3.4.13">compare view</a></li>
</ul>
</details>
<br />

Updates `engine.io` from 6.6.4 to 6.6.9
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/socketio/socket.io/releases">engine.io's releases</a>.</em></p>
<blockquote>
<h2>engine.io@6.6.9</h2>
<p>The <code>ws</code> dependency was bumped to <code>~8.21.0</code> following <a href="https://github.com/advisories/GHSA-96hv-2xvq-fx4p">CVE-2026-48779</a>.</p>
<h3>Dependencies</h3>
<ul>
<li><a href="https://github.com/websockets/ws/releases/tag/8.21.0"><code>ws@~8.21.0</code></a> (<a href="https://github.com/websockets/ws/compare/8.20.1...8.21.0">diff</a>)</li>
</ul>
<h2>engine.io-client@6.6.5</h2>
<p>The <code>ws</code> dependency was bumped to <code>~8.20.1</code> following <a href="https://github.com/advisories/GHSA-58qx-3vcg-4xpx">CVE-2026-45736</a>.</p>
<p>Note from the <code>ws</code> maintainers:</p>
<blockquote>
<p>Although the calculated CVSS severity is medium, the actual severity is believed to be low, as the flaw is only exploitable through misuse that is unlikely in practice.</p>
</blockquote>
<h3>Dependencies</h3>
<ul>
<li><a href="https://github.com/websockets/ws/releases/tag/8.20.1"><code>ws@~8.20.1</code></a> (<a href="https://github.com/websockets/ws/compare/8.18.3...8.20.1">diff</a>)</li>
</ul>
<h2>engine.io@6.6.8</h2>
<p>The <code>ws</code> dependency was bumped to <code>~8.20.1</code> following <a href="https://github.com/advisories/GHSA-58qx-3vcg-4xpx">CVE-2026-45736</a>.</p>
<p>Note from the <code>ws</code> maintainers:</p>
<blockquote>
<p>Although the calculated CVSS severity is medium, the actual severity is believed to be low, as the flaw is only exploitable through misuse that is unlikely in practice.</p>
</blockquote>
<h3>Bug Fixes</h3>
<ul>
<li>clean up resources upon WebTransport handshake failure (<a href="https://github.com/socketio/socket.io/commit/f86b95fdba6dd260b3d2f57e69537aeb8de904bb">f86b95f</a>)</li>
</ul>
<h3>Dependencies</h3>
<ul>
<li><a href="https://github.com/websockets/ws/releases/tag/8.20.1"><code>ws@~8.20.1</code></a> (<a href="https://github.com/websockets/ws/compare/8.18.3...8.20.1">diff</a>)</li>
</ul>
<h2>engine.io@6.6.7</h2>
<h3>Bug Fixes</h3>
<ul>
<li>close HTTP requests with invalid content type (<a href="https://github.com/socketio/socket.io/commit/fc11285e14964c2132d122164bf130c355f60671">fc11285</a>)</li>
<li>handle invalid packets when upgrading to WebTransport (<a href="https://github.com/socketio/socket.io/commit/1fa1f46cd420ac5b57bb4c04c959b58f3c79158c">1fa1f46</a>)</li>
<li>prevent WebTransport connections when a middleware is registered (<a href="https://github.com/socketio/socket.io/commit/d1f5aa93722a7f1ed729b96f771daf92a3dfdaf7">d1f5aa9</a>)</li>
</ul>
<h3>Dependencies</h3>
<ul>
<li><a href="https://github.com/websockets/ws/releases/tag/8.18.3"><code>ws@~8.18.3</code></a> (no change)</li>
</ul>
<h2>engine.io@6.6.6</h2>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/socketio/socket.io/commit/9dbec8128fa76c3143e93cf41991e903adfdc6da"><code>9dbec81</code></a> chore(release): engine.io@6.6.9</li>
<li><a href="https://github.com/socketio/socket.io/commit/3ad4e1f2dcf0e8b7d1bb05892be5ede2ab100abf"><code>3ad4e1f</code></a> docs: improve example with PM2</li>
<li><a href="https://github.com/socketio/socket.io/commit/0e5afeeba45b1b3dc926584253ac93e9d0c9eae1"><code>0e5afee</code></a> docs: add example with PM2</li>
<li><a href="https://github.com/socketio/socket.io/commit/eab9623c8476308e735472ce1bf70e90eb3de604"><code>eab9623</code></a> docs(eio): correct maxHttpBufferSize default in JSDoc (<a href="https://redirect.github.com/socketio/socket.io/issues/5508">#5508</a>)</li>
<li><a href="https://github.com/socketio/socket.io/commit/c17890c5e5bd3a2f2e40ca240059906c51156d49"><code>c17890c</code></a> docs: add documentation about WebTransport</li>
<li><a href="https://github.com/socketio/socket.io/commit/20df6ae561e379dabdceecbdf0532ac052994cc9"><code>20df6ae</code></a> docs(examples): add client-side load balancing example</li>
<li><a href="https://github.com/socketio/socket.io/commit/16d19236132293c415f511aa5631de558be9ab70"><code>16d1923</code></a> ci(publish): enable staged publishing</li>
<li><a href="https://github.com/socketio/socket.io/commit/ad48a9bac723303d8bde81c4394828822abe57e0"><code>ad48a9b</code></a> docs(examples): add example with HTTP/2</li>
<li><a href="https://github.com/socketio/socket.io/commit/190572d2459681a757e23e6010939ac5e53fdfcf"><code>190572d</code></a> refactor(eio-client): remove XMLHttpRequest from the definition file</li>
<li><a href="https://github.com/socketio/socket.io/commit/fad463c54d04799e1592361b0fd8344a5fab960d"><code>fad463c</code></a> docs(examples): fix duplicate self messages (<a href="https://redirect.github.com/socketio/socket.io/issues/5341">#5341</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/socketio/socket.io/compare/engine.io@6.6.4...engine.io@6.6.9">compare view</a></li>
</ul>
</details>
<details>
<summary>Maintainer changes</summary>
<p>This version was pushed to npm by <a href="https://www.npmjs.com/~GitHub%20Actions">GitHub Actions</a>, a new releaser for engine.io since your current version.</p>
</details>
<br />

Updates `find-my-way` from 9.2.0 to 9.7.0
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/delvedor/find-my-way/releases">find-my-way's releases</a>.</em></p>
<blockquote>
<h2>v9.7.0</h2>
<h2>What's Changed</h2>
<ul>
<li>fix: backtrack on regex param mismatch by <a href="https://github.com/mcollina"><code>@​mcollina</code></a> in <a href="https://redirect.github.com/delvedor/find-my-way/pull/427">delvedor/find-my-way#427</a></li>
<li>fix: apply root path fallback for optional params in off() by <a href="https://github.com/aquie00t"><code>@​aquie00t</code></a> in <a href="https://redirect.github.com/delvedor/find-my-way/pull/428">delvedor/find-my-way#428</a></li>
<li>ci: add node v26 to test matrix by <a href="https://github.com/aquie00t"><code>@​aquie00t</code></a> in <a href="https://redirect.github.com/delvedor/find-my-way/pull/435">delvedor/find-my-way#435</a></li>
<li>perf(host): cache regex lookup results in HostStorage by <a href="https://github.com/aquie00t"><code>@​aquie00t</code></a> in <a href="https://redirect.github.com/delvedor/find-my-way/pull/436">delvedor/find-my-way#436</a></li>
<li>chore: bump inquirer from 13.4.3 to 14.0.2 in the dev-dependencies group by <a href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot] in <a href="https://redirect.github.com/delvedor/find-my-way/pull/437">delvedor/find-my-way#437</...

_Description has been truncated_
