# chore(deps): bump the npm_and_yarn group across 1 directory with 6 updates

Bumps the npm_and_yarn group with 6 updates in the / directory:

| Package | From | To |
| --- | --- | --- |
| [tar](https://github.com/isaacs/node-tar) | `7.5.13` | `7.5.21` |
| [@babel/core](https://github.com/babel/babel/tree/HEAD/packages/babel-core) | `7.29.0` | `7.29.7` |
| [fast-uri](https://github.com/fastify/fast-uri) | `3.1.2` | `3.1.5` |
| [hono](https://github.com/honojs/hono) | `4.12.25` | `4.13.1` |
| [protobufjs](https://github.com/protobufjs/protobuf.js) | `7.6.4` | `7.6.5` |
| [shell-quote](https://github.com/ljharb/shell-quote) | `1.8.4` | `1.10.0` |


Updates `tar` from 7.5.13 to 7.5.21
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/isaacs/node-tar/commit/0cd9cc3c5814446d3c0cbea6a31d6c00c2c8a9d9"><code>0cd9cc3</code></a> 7.5.21</li>
<li><a href="https://github.com/isaacs/node-tar/commit/631ae59121bf8fc8a22bbae35f074cb9b789cd4a"><code>631ae59</code></a> list: prevent unbounded recursion</li>
<li><a href="https://github.com/isaacs/node-tar/commit/ebbb72094159d003f428dcd1cb28255d37ea4873"><code>ebbb720</code></a> 7.5.20</li>
<li><a href="https://github.com/isaacs/node-tar/commit/2f271963a7fe5a5960aee5dd6adf9647a1e266fd"><code>2f27196</code></a> fix: fully disable and dispose of unzip when aborting parser</li>
<li><a href="https://github.com/isaacs/node-tar/commit/be440da64e9fe80c68c755d8147328ea1cc2a9ad"><code>be440da</code></a> 7.5.19</li>
<li><a href="https://github.com/isaacs/node-tar/commit/2812e9338665659b183aa7226518c307044957d3"><code>2812e93</code></a> add maxDecompressionRatio guard against explosive decompression</li>
<li><a href="https://github.com/isaacs/node-tar/commit/9ecd4d2956fd915507eca018ddc1fea727fbba93"><code>9ecd4d2</code></a> 7.5.18</li>
<li><a href="https://github.com/isaacs/node-tar/commit/9e78bf058b2c22dd4d52e00d8922d5c06fc2f7b5"><code>9e78bf0</code></a> refuse to let header size be less than 0</li>
<li><a href="https://github.com/isaacs/node-tar/commit/e02a4e9e013c4be95302e2eb2047a942b883c27b"><code>e02a4e9</code></a> pax: parse values according to known types</li>
<li><a href="https://github.com/isaacs/node-tar/commit/9cbdb31e5e8dbcb97a642e0f91e2d1e342585946"><code>9cbdb31</code></a> 7.5.17</li>
<li>Additional commits viewable in <a href="https://github.com/isaacs/node-tar/compare/v7.5.13...v7.5.21">compare view</a></li>
</ul>
</details>
<br />

Updates `@babel/core` from 7.29.0 to 7.29.7
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/babel/babel/releases">@​babel/core's releases</a>.</em></p>
<blockquote>
<h2>v7.29.7 (2026-05-25)</h2>
<p>Re-release all packages with npm provenance attestations</p>
<h2>v7.29.6 (2026-05-25)</h2>
<h4>:bug: Bug Fix</h4>
<ul>
<li><code>babel-generator</code>
<ul>
<li><a href="https://redirect.github.com/babel/babel/pull/18014">#18014</a> Catchup source map position in preserveFormat (<a href="https://github.com/nicolo-ribaudo"><code>@​nicolo-ribaudo</code></a>)</li>
</ul>
</li>
<li><code>babel-core</code>
<ul>
<li><a href="https://redirect.github.com/babel/babel/pull/18001">#18001</a> [7.x packport]Improve input source map handling (<a href="https://github.com/JLHwung"><code>@​JLHwung</code></a>)</li>
</ul>
</li>
<li><code>babel-core</code>, <code>babel-generator</code>
<ul>
<li><a href="https://redirect.github.com/babel/babel/pull/17998">#17998</a> Preserve original identifier names from input sourcemaps (<a href="https://github.com/babel/babel/tree/HEAD/packages/babel-core/issues/17992">#17992</a>) (<a href="https://github.com/Andarist"><code>@​Andarist</code></a>)</li>
</ul>
</li>
</ul>
<h4>Committers: 3</h4>
<ul>
<li>Huáng Jùnliàng (<a href="https://github.com/JLHwung"><code>@​JLHwung</code></a>)</li>
<li>Mateusz Burzyński (<a href="https://github.com/Andarist"><code>@​Andarist</code></a>)</li>
<li>Nicolò Ribaudo (<a href="https://github.com/nicolo-ribaudo"><code>@​nicolo-ribaudo</code></a>)</li>
</ul>
<h2>v7.29.5 (2026-05-05)</h2>
<h4>:house:  Internal</h4>
<ul>
<li><code>babel-preset-env</code>
<ul>
<li>Update <code>@babel/*</code> dependencies</li>
</ul>
</li>
</ul>
<h2>v7.29.4 (2026-05-05)</h2>
<h4>:bug: Bug Fix</h4>
<ul>
<li><code>babel-plugin-transform-modules-systemjs</code>
<ul>
<li><a href="https://redirect.github.com/babel/babel/pull/17974">#17974</a> [7.x backport]fix(systemjs): improve module string name support (<a href="https://github.com/JLHwung"><code>@​JLHwung</code></a>)</li>
</ul>
</li>
</ul>
<h4>Committers: 1</h4>
<ul>
<li>Huáng Jùnliàng (<a href="https://github.com/JLHwung"><code>@​JLHwung</code></a>)</li>
</ul>
<h2>v7.29.3 (2026-04-30)</h2>
<h4>:eyeglasses: Spec Compliance</h4>
<ul>
<li><code>babel-parser</code>
<ul>
<li><a href="https://redirect.github.com/babel/babel/pull/17923">#17923</a> Support flow extends bound (<a href="https://github.com/JLHwung"><code>@​JLHwung</code></a>)</li>
</ul>
</li>
</ul>
<h4>:bug: Bug Fix</h4>
<ul>
<li><code>babel-helper-create-class-features-plugin</code>, <code>babel-plugin-proposal-decorators</code>
<ul>
<li><a href="https://redirect.github.com/babel/babel/pull/17931">#17931</a> fix(decorators): replace super within all removed static elements (<a href="https://github.com/JLHwung"><code>@​JLHwung</code></a>)</li>
</ul>
</li>
<li><code>babel-register</code>
<ul>
<li><a href="https://redirect.github.com/babel/babel/pull/17915">#17915</a> Fix thread synchronization issues in <code>@babel/register</code> (<a href="https://github.com/liuxingbaoyu"><code>@​liuxingbaoyu</code></a>)</li>
</ul>
</li>
<li><code>babel-compat-data</code>, <code>babel-plugin-bugfix-safari-rest-destructuring-rhs-array</code>, <code>babel-preset-env</code>
<ul>
<li><a href="https://redirect.github.com/babel/babel/pull/17788">#17788</a> Add bugfix plugin for Safari array rest destructuring bug (<a href="https://github.com/JLHwung"><code>@​JLHwung</code></a>)</li>
</ul>
</li>
</ul>
<h4>:nail_care: Polish</h4>
<ul>
<li><code>babel-parser</code></li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/babel/babel/commit/4fba7541180bf5f58256d8e358b544e3831ad090"><code>4fba754</code></a> v7.29.7</li>
<li><a href="https://github.com/babel/babel/commit/04ea6b27fdac8f40c3481aec2080ac9678779509"><code>04ea6b2</code></a> v7.29.6</li>
<li><a href="https://github.com/babel/babel/commit/99f498a9b9fa0b900d603fbe8f6601bb3b9e42bb"><code>99f498a</code></a> [7.x packport]Improve input source map handling (<a href="https://github.com/babel/babel/tree/HEAD/packages/babel-core/issues/18001">#18001</a>)</li>
<li><a href="https://github.com/babel/babel/commit/feba0a3654c596bd369d1ef1231f5d56666d56dc"><code>feba0a3</code></a> Preserve original identifier names from input sourcemaps (<a href="https://github.com/babel/babel/tree/HEAD/packages/babel-core/issues/17992">#17992</a>) (<a href="https://github.com/babel/babel/tree/HEAD/packages/babel-core/issues/17998">#17998</a>)</li>
<li>See full diff in <a href="https://github.com/babel/babel/commits/v7.29.7/packages/babel-core">compare view</a></li>
</ul>
</details>
<br />

Updates `fast-uri` from 3.1.2 to 3.1.5
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/fastify/fast-uri/releases">fast-uri's releases</a>.</em></p>
<blockquote>
<h2>v3.1.5</h2>
<h2>⚠️ Security Warning</h2>
<p>Fix for <a href="https://github.com/fastify/fast-uri/security/advisories/GHSA-7p8r-x3mc-p8w7">https://github.com/fastify/fast-uri/security/advisories/GHSA-7p8r-x3mc-p8w7</a></p>
<p><strong>Full Changelog</strong>: <a href="https://github.com/fastify/fast-uri/compare/v3.1.4...v3.1.5">https://github.com/fastify/fast-uri/compare/v3.1.4...v3.1.5</a></p>
<h2>v3.1.4</h2>
<h2>⚠️ Security Release</h2>
<p>Fix for <a href="https://github.com/fastify/fast-uri/security/advisories/GHSA-v2hh-gcrm-f6hx">https://github.com/fastify/fast-uri/security/advisories/GHSA-v2hh-gcrm-f6hx</a></p>
<p><strong>Full Changelog</strong>: <a href="https://github.com/fastify/fast-uri/compare/v3.1.3...v3.1.4">https://github.com/fastify/fast-uri/compare/v3.1.3...v3.1.4</a></p>
<h2>v3.1.3</h2>
<h2>⚠️ Security Release</h2>
<ul>
<li>Fixes: <a href="https://github.com/fastify/fast-uri/security/advisories/GHSA-4c8g-83qw-93j6">https://github.com/fastify/fast-uri/security/advisories/GHSA-4c8g-83qw-93j6</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/fastify/fast-uri/compare/v3.1.2...v3.1.3">https://github.com/fastify/fast-uri/compare/v3.1.2...v3.1.3</a></p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/fastify/fast-uri/commit/5e179cbb4636d5f773ed21126e5bd3068e87e94e"><code>5e179cb</code></a> Bumped v3.1.5</li>
<li><a href="https://github.com/fastify/fast-uri/commit/2cad02d6ed428a720499bb7a3c3d6c3d41f10f5a"><code>2cad02d</code></a> Merge commit from fork</li>
<li><a href="https://github.com/fastify/fast-uri/commit/6aeece669e4166b2446a89f17c07a3b15dfb7ed4"><code>6aeece6</code></a> Bumped v3.1.4</li>
<li><a href="https://github.com/fastify/fast-uri/commit/2d50fbabc80e4d0884fe0f6a98fe118ce6faa353"><code>2d50fba</code></a> fix: reject literal backslash in URI authority</li>
<li><a href="https://github.com/fastify/fast-uri/commit/0549fe35b0d482233f3be2816439f3ec803603fa"><code>0549fe3</code></a> Bumped v3.1.3</li>
<li><a href="https://github.com/fastify/fast-uri/commit/2a6d357a18a68e6d812824379fd3388a1ae50d05"><code>2a6d357</code></a> Merge commit from fork</li>
<li>See full diff in <a href="https://github.com/fastify/fast-uri/compare/v3.1.2...v3.1.5">compare view</a></li>
</ul>
</details>
<br />

Updates `hono` from 4.12.25 to 4.13.1
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/honojs/hono/releases">hono's releases</a>.</em></p>
<blockquote>
<h2>v4.13.1</h2>
<h2>What's Changed</h2>
<ul>
<li>fix(trie-router): count every slash a pattern consumes by <a href="https://github.com/Jaybhade"><code>@​Jaybhade</code></a> in <a href="https://redirect.github.com/honojs/hono/pull/5189">honojs/hono#5189</a></li>
<li>fix(utils/stream): re-acquire writer lock when pipe() throws by <a href="https://github.com/Sriharsha-dev369"><code>@​Sriharsha-dev369</code></a> in <a href="https://redirect.github.com/honojs/hono/pull/4988">honojs/hono#4988</a></li>
<li>fix(etag): skip unsafe methods or error responses on non-* case by <a href="https://github.com/na-trium-144"><code>@​na-trium-144</code></a> in <a href="https://redirect.github.com/honojs/hono/pull/5196">honojs/hono#5196</a></li>
</ul>
<h2>New Contributors</h2>
<ul>
<li><a href="https://github.com/Jaybhade"><code>@​Jaybhade</code></a> made their first contribution in <a href="https://redirect.github.com/honojs/hono/pull/5189">honojs/hono#5189</a></li>
<li><a href="https://github.com/Sriharsha-dev369"><code>@​Sriharsha-dev369</code></a> made their first contribution in <a href="https://redirect.github.com/honojs/hono/pull/4988">honojs/hono#4988</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/honojs/hono/compare/v4.13.0...v4.13.1">https://github.com/honojs/hono/compare/v4.13.0...v4.13.1</a></p>
<h2>v4.13.0</h2>
<p>Hono v4.13.0 is now available!</p>
<p>The highlight of this release is performance: a batch of low-level optimizations makes the core request/response path significantly faster — up to 1.25x on common routes in our benchmark. This release also adds first-class support for the HTTP QUERY method, defined in <a href="https://www.rfc-editor.org/rfc/rfc10008.html">RFC 10008</a>, a new Method Not Allowed middleware, and more.</p>
<h2>Performance improvements</h2>
<p>This release includes a series of small optimizations: skipping unnecessary <code>Headers</code> allocations, replacing regex tests with <code>indexOf</code>, allocating internal state lazily, and more.</p>
<p>Here is <a href="https://github.com/honojs/hono/tree/main/benchmarks/fetch"><code>benchmarks/fetch</code></a> comparing v4.12 and v4.13 (<code>ROUNDS=5 ./compare.sh</code>, Bun 1.4.0, Apple Silicon — each measurement runs in a fresh process, and the variant order is reversed every round to avoid warm-up bias):</p>
<table>
<thead>
<tr>
<th>Benchmark</th>
<th align="right">v4.12</th>
<th align="right">v4.13</th>
<th align="right">Speedup</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ping</code> — <code>GET /</code></td>
<td align="right">165.83 ns</td>
<td align="right">163.99 ns</td>
<td align="right">1.01x</td>
</tr>
<tr>
<td><code>query</code> — <code>GET /id/1?name=bun</code></td>
<td align="right">674.40 ns</td>
<td align="right">616.99 ns</td>
<td align="right"><strong>1.09x</strong></td>
</tr>
<tr>
<td><code>json</code> — <code>GET /user</code></td>
<td align="right">528.99 ns</td>
<td align="right">422.44 ns</td>
<td align="right"><strong>1.25x</strong></td>
</tr>
<tr>
<td><code>body</code> — <code>POST /json</code></td>
<td align="right">1.16 µs</td>
<td align="right">1.00 µs</td>
<td align="right"><strong>1.15x</strong></td>
</tr>
</tbody>
</table>
<p>The individual changes:</p>
<ul>
<li>perf(context): iterate the header record with <code>for..in</code> <a href="https://redirect.github.com/honojs/hono/pull/5118">honojs/hono#5118</a></li>
<li>perf(url): replace regex tests with <code>indexOf</code> <a href="https://redirect.github.com/honojs/hono/pull/5121">honojs/hono#5121</a></li>
<li>perf(context): skip <code>Headers</code> creation when there are no headers to merge <a href="https://redirect.github.com/honojs/hono/pull/5122">honojs/hono#5122</a></li>
<li>perf(urls): refactor <code>tryDecodeURIComponent</code> <a href="https://redirect.github.com/honojs/hono/pull/5158">honojs/hono#5158</a></li>
<li>perf(request): allocate <code>#validatedData</code> lazily <a href="https://redirect.github.com/honojs/hono/pull/5175">honojs/hono#5175</a></li>
<li>perf(request): probe the body cache without allocating <a href="https://redirect.github.com/honojs/hono/pull/5176">honojs/hono#5176</a></li>
</ul>
<p>In addition, the RegExpRouter rewrite described below makes route registration plus the first match roughly 20% faster.</p>
<p>Thanks <a href="https://github.com/kibertoad"><code>@​kibertoad</code></a> for the contributions!</p>
<h2>First-class QUERY method support</h2>
<p>The QUERY method — a safe, idempotent method that carries a request body — is now a first-class citizen in Hono. You can define QUERY handlers with <code>app.query()</code>:</p>
<pre lang="ts"><code>const app = new Hono()
<p>&lt;/tr&gt;&lt;/table&gt;<br />
</code></pre></p>
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/honojs/hono/commit/cf785287b5ab41496a333c9c4b53b0f98ac731b9"><code>cf78528</code></a> 4.13.1</li>
<li><a href="https://github.com/honojs/hono/commit/f6aa913c3f8915d0695b77ca3f78f6b8ecb248a0"><code>f6aa913</code></a> fix(etag): skip unsafe methods or error responses on non-* case (<a href="https://redirect.github.com/honojs/hono/issues/5196">#5196</a>)</li>
<li><a href="https://github.com/honojs/hono/commit/cd31bc196eb234bcaaae18ecf889784cf30004fd"><code>cd31bc1</code></a> fix(utils/stream): re-acquire writer lock when pipe() throws (<a href="https://redirect.github.com/honojs/hono/issues/4988">#4988</a>)</li>
<li><a href="https://github.com/honojs/hono/commit/569b4191a291ef7a4116881e521c3a0179407332"><code>569b419</code></a> fix(trie-router): count every slash a pattern consumes (<a href="https://redirect.github.com/honojs/hono/issues/5189">#5189</a>)</li>
<li><a href="https://github.com/honojs/hono/commit/192768fbaf9aa99a45404dc2f171541227c11d20"><code>192768f</code></a> 4.13.0</li>
<li><a href="https://github.com/honojs/hono/commit/b0c2d90eb07fefa6c06dc556c97ed8ecffc8b2c0"><code>b0c2d90</code></a> Merge pull request <a href="https://redirect.github.com/honojs/hono/issues/5154">#5154</a> from honojs/next</li>
<li><a href="https://github.com/honojs/hono/commit/8f0702827002f0ada02434d908853458c17f862d"><code>8f07028</code></a> fix(compress): set Vary: Accept-Encoding on negotiated responses (<a href="https://redirect.github.com/honojs/hono/issues/5137">#5137</a>)</li>
<li><a href="https://github.com/honojs/hono/commit/8a0b18fd9b4d64dd2eb1d7f18e3536fc06cb54b2"><code>8a0b18f</code></a> feat(reg-exp-router): throw UnsupportedPathError during route registration (#...</li>
<li><a href="https://github.com/honojs/hono/commit/3feb3551d46de1f633e82253f12cf1117316be93"><code>3feb355</code></a> fix(jsx): allow a function component to return an array (<a href="https://redirect.github.com/honojs/hono/issues/5179">#5179</a>)</li>
<li><a href="https://github.com/honojs/hono/commit/5d911d2ab7bcb2adb2e974ddd5b17742fb5a0bca"><code>5d911d2</code></a> feat(utils/headers): add HTTP fields newly registered with IANA (<a href="https://redirect.github.com/honojs/hono/issues/5153">#5153</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/honojs/hono/compare/v4.12.25...v4.13.1">compare view</a></li>
</ul>
</details>
<details>
<summary>Maintainer changes</summary>
<p>This version was pushed to npm by <a href="https://www.npmjs.com/~GitHub%20Actions">GitHub Actions</a>, a new releaser for hono since your current version.</p>
</details>
<br />

Updates `protobufjs` from 7.6.4 to 7.6.5
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/protobufjs/protobuf.js/releases">protobufjs's releases</a>.</em></p>
<blockquote>
<h2>protobufjs: v7.6.5</h2>
<h2><a href="https://github.com/protobufjs/protobuf.js/compare/protobufjs-v7.6.4...protobufjs-v7.6.5">7.6.5</a> (2026-07-04)</h2>
<h3>Bug Fixes</h3>
<ul>
<li>handle EOF during options parsing (<a href="https://redirect.github.com/protobufjs/protobuf.js/issues/2352">#2352</a>) (<a href="https://redirect.github.com/protobufjs/protobuf.js/issues/2356">#2356</a>) (<a href="https://github.com/protobufjs/protobuf.js/commit/10fba6d54815ceecca8a06b9a6db490c8f5d2217">10fba6d</a>)</li>
</ul>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/protobufjs/protobuf.js/blob/protobufjs-v7.6.5/CHANGELOG.md">protobufjs's changelog</a>.</em></p>
<blockquote>
<h2><a href="https://github.com/protobufjs/protobuf.js/compare/protobufjs-v7.6.4...protobufjs-v7.6.5">7.6.5</a> (2026-07-04)</h2>
<h3>Bug Fixes</h3>
<ul>
<li>handle EOF during options parsing (<a href="https://redirect.github.com/protobufjs/protobuf.js/issues/2352">#2352</a>) (<a href="https://redirect.github.com/protobufjs/protobuf.js/issues/2356">#2356</a>) (<a href="https://github.com/protobufjs/protobuf.js/commit/10fba6d54815ceecca8a06b9a6db490c8f5d2217">10fba6d</a>)</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/protobufjs/protobuf.js/commit/89048ba0bbf3ed78f77199102f0614dafc2b4860"><code>89048ba</code></a> chore: release protobufjs-v7.x (<a href="https://redirect.github.com/protobufjs/protobuf.js/issues/2357">#2357</a>)</li>
<li><a href="https://github.com/protobufjs/protobuf.js/commit/10fba6d54815ceecca8a06b9a6db490c8f5d2217"><code>10fba6d</code></a> fix: handle EOF during options parsing (<a href="https://redirect.github.com/protobufjs/protobuf.js/issues/2352">#2352</a>) (<a href="https://redirect.github.com/protobufjs/protobuf.js/issues/2356">#2356</a>)</li>
<li>See full diff in <a href="https://github.com/protobufjs/protobuf.js/compare/protobufjs-v7.6.4...protobufjs-v7.6.5">compare view</a></li>
</ul>
</details>
<br />

Updates `shell-quote` from 1.8.4 to 1.10.0
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/ljharb/shell-quote/blob/main/CHANGELOG.md">shell-quote's changelog</a>.</em></p>
<blockquote>
<h2><a href="https://github.com/ljharb/shell-quote/compare/v1.9.0...v1.10.0">v1.10.0</a> - 2026-07-10</h2>
<h3>Merged</h3>
<ul>
<li>[New] <code>parse</code>: add opt-in <code>splitUnquoted</code> option for shell field-splitting of unquoted expansions <a href="https://redirect.github.com/ljharb/shell-quote/pull/1"><code>[#1](https://github.com/ljharb/shell-quote/issues/1)</code></a></li>
</ul>
<h3>Commits</h3>
<ul>
<li>[Fix] <code>parse</code>: match nested <code>${...}</code> braces so nested parameter expansion is consumed as one substitution <a href="https://github.com/ljharb/shell-quote/commit/c0842c8a7a034066da2496a75e91cbe500ff736c"><code>c0842c8</code></a></li>
<li>[Tests] <code>parse</code>: pin single-quote literalness and unmatched-quote handling <a href="https://github.com/ljharb/shell-quote/commit/a0d03e35c8ede24016502c4433b8f5d6b3100a62"><code>a0d03e3</code></a></li>
<li>[readme] remove the space in js code fences so evalmd evaluates them <a href="https://github.com/ljharb/shell-quote/commit/2116fa36aeea77fe8d561b0db46b1f9b26b8cf1b"><code>2116fa3</code></a></li>
<li>[Tests] <code>quote</code>: pin conservative escaping of <code>=</code>, <code>@</code>, <code>^</code>, <code>,</code>, <code>:</code>, <code>!</code> (<a href="https://redirect.github.com/ljharb/shell-quote/issues/11">#11</a>) <a href="https://github.com/ljharb/shell-quote/commit/1c36f3ff77d26d200620c1027e5c271050120b8e"><code>1c36f3f</code></a></li>
<li>[readme] document that <code>quote</code> outputs POSIX quoting, not <code>cmd.exe</code>/PowerShell <a href="https://github.com/ljharb/shell-quote/commit/100e96e0ffadcca97d63dda15651c70b9f83507c"><code>100e96e</code></a></li>
<li>[readme] document <code>parse</code>'s supported parameter-expansion subset <a href="https://github.com/ljharb/shell-quote/commit/e1c75cd6e4a3c60003792c7f2802587d328622cb"><code>e1c75cd</code></a></li>
<li>[Fix] <code>parse</code>: a backslash inside single quotes must not escape the closing quote <a href="https://github.com/ljharb/shell-quote/commit/5d460a332b54b83153297fe7d1964330b28fa491"><code>5d460a3</code></a></li>
<li>[readme] fix stale example outputs <a href="https://github.com/ljharb/shell-quote/commit/2de86f5d44f44d3ac9df36413d8a05f3534cdec6"><code>2de86f5</code></a></li>
<li>[Tests] <code>quote</code>: pin that a backslash with whitespace is not doubled in single quotes (<a href="https://redirect.github.com/ljharb/shell-quote/issues/14">#14</a>) <a href="https://github.com/ljharb/shell-quote/commit/190e236bcf1d81caa8e40e8ea3bb11998575be71"><code>190e236</code></a></li>
<li>[readme] <code>quote</code>: use output verbatim; do not re-quote it (<a href="https://redirect.github.com/ljharb/shell-quote/issues/11">#11</a>) <a href="https://github.com/ljharb/shell-quote/commit/1b364683b1e9e8d078fd3017cde82cf10c9c04a5"><code>1b36468</code></a></li>
<li>[Refactor] <code>parse</code>: fix swapped <code>SINGLE_QUOTE</code>/<code>DOUBLE_QUOTE</code> variable names <a href="https://github.com/ljharb/shell-quote/commit/801af5c935b27d6dcda63b3975d5e92a7b6f887f"><code>801af5c</code></a></li>
<li>[types] fix an error TS v6 ignores but v7 fails on <a href="https://github.com/ljharb/shell-quote/commit/59bbf8b81bf3236842deb72805744d489f650eba"><code>59bbf8b</code></a></li>
<li>[Dev Deps] update <code>@arethetypeswrong/cli</code>, <code>evalmd</code> <a href="https://github.com/ljharb/shell-quote/commit/a04d47516e1cd5b1b4d3f720ddf97561ed0082fc"><code>a04d475</code></a></li>
<li>[Dev Deps] update <code>@arethetypeswrong/ci</code>, <code>eslint</code> <a href="https://github.com/ljharb/shell-quote/commit/d390f9a92b97a04b1f799298634e90dc581021e6"><code>d390f9a</code></a></li>
<li>[Tests] <code>quote</code>: the tilde test escapes every <code>~</code>, not just a leading one (<a href="https://redirect.github.com/ljharb/shell-quote/issues/9">#9</a>) <a href="https://github.com/ljharb/shell-quote/commit/617d119795c7b44d6e49a4d41f80195c4aa5735c"><code>617d119</code></a></li>
</ul>
<h2><a href="https://github.com/ljharb/shell-quote/compare/v1.8.4...v1.9.0">v1.9.0</a> - 2026-06-24</h2>
<h3>Commits</h3>
<ul>
<li>[New] add types <a href="https://github.com/ljharb/shell-quote/commit/dca6e21a02df4cc1a83ed1b5baa4d82df134170a"><code>dca6e21</code></a></li>
<li>[Dev Deps] update <code>eslint</code> <a href="https://github.com/ljharb/shell-quote/commit/9aa9e8f60991f8c4053a29e476795d891ff851ad"><code>9aa9e8f</code></a></li>
<li>[Fix] <code>parse</code>: finalize tokens in linear time (GHSA-395f-4hp3-45gv) <a href="https://github.com/ljharb/shell-quote/commit/7ff5488599d01c323514f02f5efb74088dd134ec"><code>7ff5488</code></a></li>
<li>[actions] update workflows <a href="https://github.com/ljharb/shell-quote/commit/75e849741ffaf2d3aa53ae0e18ef6bf9929ef478"><code>75e8497</code></a></li>
<li>[actions] Windows + node 4/6/7: pin eslint to 9 before install, since npm 2/3 cannot stage eslint 10<code>@types/esrecurse</code> <a href="https://github.com/ljharb/shell-quote/commit/3fb739de44b81c69431947d54fbfc18998dd6d72"><code>3fb739d</code></a></li>
<li>[actions] retry <code>npm install</code> on Windows to survive npm 2/3 staging-rename flake <a href="https://github.com/ljharb/shell-quote/commit/abe0163293c82963fa8a16cfaa87181846d5aced"><code>abe0163</code></a></li>
<li>[actions] Windows + node 5/7: install deps with a modern node <a href="https://github.com/ljharb/shell-quote/commit/b4bafa2e7e58d53d9839b1c24976f61e54b43326"><code>b4bafa2</code></a></li>
<li>[Fix] <code>quote</code>: escape leading <code>~</code> to prevent shell tilde-expansion <a href="https://github.com/ljharb/shell-quote/commit/7a76c1a12d8461c2234a1c655b943cee84cbff91"><code>7a76c1a</code></a></li>
<li>[Dev Deps] update <code>auto-changelog</code>, <code>tape</code> <a href="https://github.com/ljharb/shell-quote/commit/7184b4458b65c17b931e126d8cb5f586c6717dc8"><code>7184b44</code></a></li>
<li>[Dev Deps] apparently <code>jackspeak</code> is no longer in the graph <a href="https://github.com/ljharb/shell-quote/commit/9ba368a4057b9f498b0fef23b5b15543ef81b98c"><code>9ba368a</code></a></li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/ljharb/shell-quote/commit/64988d9a0e73a2ae710488952e3614958ef289d4"><code>64988d9</code></a> v1.10.0</li>
<li><a href="https://github.com/ljharb/shell-quote/commit/617d119795c7b44d6e49a4d41f80195c4aa5735c"><code>617d119</code></a> [Tests] <code>quote</code>: the tilde test escapes every <code>~</code>, not just a leading one (<a href="https://redirect.github.com/ljharb/shell-quote/issues/9">#9</a>)</li>
<li><a href="https://github.com/ljharb/shell-quote/commit/59bbf8b81bf3236842deb72805744d489f650eba"><code>59bbf8b</code></a> [types] fix an error TS v6 ignores but v7 fails on</li>
<li><a href="https://github.com/ljharb/shell-quote/commit/190e236bcf1d81caa8e40e8ea3bb11998575be71"><code>190e236</code></a> [Tests] <code>quote</code>: pin that a backslash with whitespace is not doubled in singl...</li>
<li><a href="https://github.com/ljharb/shell-quote/commit/a04d47516e1cd5b1b4d3f720ddf97561ed0082fc"><code>a04d475</code></a> [Dev Deps] update <code>@arethetypeswrong/cli</code>, <code>evalmd</code></li>
<li><a href="https://github.com/ljharb/shell-quote/commit/b9545b39f4de17aa169410823c98acf58387e474"><code>b9545b3</code></a> [New] <code>parse</code>: add opt-in <code>splitUnquoted</code> option for shell field-splitting of...</li>
<li><a href="https://github.com/ljharb/shell-quote/commit/1b364683b1e9e8d078fd3017cde82cf10c9c04a5"><code>1b36468</code></a> [readme] <code>quote</code>: use output verbatim; do not re-quote it (<a href="https://redirect.github.com/ljharb/shell-quote/issues/11">#11</a>)</li>
<li><a href="https://github.com/ljharb/shell-quote/commit/1c36f3ff77d26d200620c1027e5c271050120b8e"><code>1c36f3f</code></a> [Tests] <code>quote</code>: pin conservative escaping of <code>=</code>, <code>@</code>, <code>^</code>, <code>,</code>, <code>:</code>, <code>!</code> (<a href="https://redirect.github.com/ljharb/shell-quote/issues/11">#11</a>)</li>
<li><a href="https://github.com/ljharb/shell-quote/commit/e1c75cd6e4a3c60003792c7f2802587d328622cb"><code>e1c75cd</code></a> [readme] document <code>parse</code>'s supported parameter-expansion subset</li>
<li><a href="https://github.com/ljharb/shell-quote/commit/c0842c8a7a034066da2496a75e91cbe500ff736c"><code>c0842c8</code></a> [Fix] <code>parse</code>: match nested <code>${...}</code> braces so nested parameter expansion is ...</li>
<li>Additional commits viewable in <a href="https://github.com/ljharb/shell-quote/compare/v1.8.4...v1.10.0">compare view</a></li>
</ul>
</details>
<br />


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
- `@dependabot ignore <dependency name> major version` will close this group update PR and stop Dependabot creating any more for the specific dependency's major version (unless you unignore this specific dependency's major version or upgrade to it yourself)
- `@dependabot ignore <dependency name> minor version` will close this group update PR and stop Dependabot creating any more for the specific dependency's minor version (unless you unignore this specific dependency's minor version or upgrade to it yourself)
- `@dependabot ignore <dependency name>` will close this group update PR and stop Dependabot creating any more for the specific dependency (unless you unignore this specific dependency or upgrade to it yourself)
- `@dependabot unignore <dependency name>` will remove all of the ignore conditions of the specified dependency
- `@dependabot unignore <dependency name> <ignore condition>` will remove the ignore condition of the specified dependency and ignore conditions
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/tldraw/tldraw/network/alerts).

</details>
