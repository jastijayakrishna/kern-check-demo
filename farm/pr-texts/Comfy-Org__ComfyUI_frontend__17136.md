# chore(deps): bump the vue group with 3 updates

Bumps the vue group with 3 updates: [vue-component-type-helpers](https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers), [vue-tsc](https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc) and [vue](https://github.com/vuejs/core).

Updates `vue-component-type-helpers` from 3.3.9 to 3.3.11
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vuejs/language-tools/releases">vue-component-type-helpers's releases</a>.</em></p>
<blockquote>
<h2>v3.3.11</h2>
<h3>language-core</h3>
<ul>
<li><strong>fix:</strong> generate full fragment props for type checking (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6155">#6155</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
</ul>
<h3>language-service</h3>
<ul>
<li><strong>fix:</strong> invalidate tag and prop casing detection after template changes (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6172">#6172</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
<li><strong>refactor:</strong> make name casing detection reactive (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6173">#6173</a>) - Thanks to <a href="https://github.com/KazariEX"><code>@​KazariEX</code></a>!</li>
</ul>
<h3>component-meta</h3>
<ul>
<li><strong>fix:</strong> invalidate module resolution caches when deleting files (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6163">#6163</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
</ul>
<h3>tsc</h3>
<ul>
<li><strong>fix:</strong> make extension retry errors serializable across IPC (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6162">#6162</a>) - Thanks to <a href="https://github.com/KazariEX"><code>@​KazariEX</code></a>!</li>
</ul>
<h3>vscode</h3>
<ul>
<li><strong>feat:</strong> allow disabling the welcome page (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6165">#6165</a>) - Thanks to <a href="https://github.com/pierreedbrg"><code>@​pierreedbrg</code></a>!</li>
</ul>
<h2>Our Sponsors ❤️</h2>
<!-- raw HTML omitted -->
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/vuejs/language-tools/blob/master/CHANGELOG.md">vue-component-type-helpers's changelog</a>.</em></p>
<blockquote>
<h2>3.3.11 (2026-08-21)</h2>
<h3>language-core</h3>
<ul>
<li><strong>fix:</strong> generate full fragment props for type checking (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6155">#6155</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
</ul>
<h3>language-service</h3>
<ul>
<li><strong>fix:</strong> invalidate tag and prop casing detection after template changes (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6172">#6172</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
<li><strong>refactor:</strong> make name casing detection reactive (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6173">#6173</a>) - Thanks to <a href="https://github.com/KazariEX"><code>@​KazariEX</code></a>!</li>
</ul>
<h3>component-meta</h3>
<ul>
<li><strong>fix:</strong> invalidate module resolution caches when deleting files (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6163">#6163</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
</ul>
<h3>tsc</h3>
<ul>
<li><strong>fix:</strong> make extension retry errors serializable across IPC (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6162">#6162</a>) - Thanks to <a href="https://github.com/KazariEX"><code>@​KazariEX</code></a>!</li>
</ul>
<h3>vscode</h3>
<ul>
<li><strong>feat:</strong> allow disabling the welcome page (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6165">#6165</a>) - Thanks to <a href="https://github.com/pierreedbrg"><code>@​pierreedbrg</code></a>!</li>
</ul>
<h2>3.3.10 (2026-08-15)</h2>
<h3>language-core</h3>
<ul>
<li><strong>fix:</strong> ignore trailing whitespace after generic parameter commas - Thanks to <a href="https://github.com/KazariEX"><code>@​KazariEX</code></a>!</li>
<li><strong>fix:</strong> resolve <code>v-for</code> item type over generic sources (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6141">#6141</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
<li><strong>fix:</strong> do not extract SFC blocks across inline Markdown code (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6145">#6145</a>) - Thanks to <a href="https://github.com/lazerg"><code>@​lazerg</code></a>!</li>
</ul>
<h3>language-service</h3>
<ul>
<li><strong>fix:</strong> serialize template data provider access across concurrent requests (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6154">#6154</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
</ul>
<h3>tsc</h3>
<ul>
<li><strong>fix:</strong> support different extension sets across project references (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6146">#6146</a>) - Thanks to <a href="https://github.com/lazerg"><code>@​lazerg</code></a>!</li>
</ul>
<h3>typescript-plugin</h3>
<ul>
<li><strong>fix:</strong> resolve requests against the owning project (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6152">#6152</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
</ul>
<h3>vscode</h3>
<ul>
<li><strong>feat:</strong> patch <code>typescript.js</code> via <code>--require</code> to support read-only file systems (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6149">#6149</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
<li><strong>fix:</strong> isolate custom TypeScript plugin paths between profiles (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6148">#6148</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vuejs/language-tools/commit/f521b39b402ebaaa9ee70faf5a60a895544ed9e9"><code>f521b39</code></a> v3.3.11 (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6174">#6174</a>)</li>
<li><a href="https://github.com/vuejs/language-tools/commit/977995f07e39baf1a46bb42552d48ec0e896485f"><code>977995f</code></a> v3.3.10 (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/component-type-helpers/issues/6160">#6160</a>)</li>
<li>See full diff in <a href="https://github.com/vuejs/language-tools/commits/v3.3.11/packages/component-type-helpers">compare view</a></li>
</ul>
</details>
<br />

Updates `vue-tsc` from 3.3.9 to 3.3.11
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vuejs/language-tools/releases">vue-tsc's releases</a>.</em></p>
<blockquote>
<h2>v3.3.11</h2>
<h3>language-core</h3>
<ul>
<li><strong>fix:</strong> generate full fragment props for type checking (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6155">#6155</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
</ul>
<h3>language-service</h3>
<ul>
<li><strong>fix:</strong> invalidate tag and prop casing detection after template changes (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6172">#6172</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
<li><strong>refactor:</strong> make name casing detection reactive (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6173">#6173</a>) - Thanks to <a href="https://github.com/KazariEX"><code>@​KazariEX</code></a>!</li>
</ul>
<h3>component-meta</h3>
<ul>
<li><strong>fix:</strong> invalidate module resolution caches when deleting files (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6163">#6163</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
</ul>
<h3>tsc</h3>
<ul>
<li><strong>fix:</strong> make extension retry errors serializable across IPC (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6162">#6162</a>) - Thanks to <a href="https://github.com/KazariEX"><code>@​KazariEX</code></a>!</li>
</ul>
<h3>vscode</h3>
<ul>
<li><strong>feat:</strong> allow disabling the welcome page (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6165">#6165</a>) - Thanks to <a href="https://github.com/pierreedbrg"><code>@​pierreedbrg</code></a>!</li>
</ul>
<h2>Our Sponsors ❤️</h2>
<!-- raw HTML omitted -->
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/vuejs/language-tools/blob/master/CHANGELOG.md">vue-tsc's changelog</a>.</em></p>
<blockquote>
<h2>3.3.11 (2026-08-21)</h2>
<h3>language-core</h3>
<ul>
<li><strong>fix:</strong> generate full fragment props for type checking (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6155">#6155</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
</ul>
<h3>language-service</h3>
<ul>
<li><strong>fix:</strong> invalidate tag and prop casing detection after template changes (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6172">#6172</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
<li><strong>refactor:</strong> make name casing detection reactive (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6173">#6173</a>) - Thanks to <a href="https://github.com/KazariEX"><code>@​KazariEX</code></a>!</li>
</ul>
<h3>component-meta</h3>
<ul>
<li><strong>fix:</strong> invalidate module resolution caches when deleting files (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6163">#6163</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
</ul>
<h3>tsc</h3>
<ul>
<li><strong>fix:</strong> make extension retry errors serializable across IPC (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6162">#6162</a>) - Thanks to <a href="https://github.com/KazariEX"><code>@​KazariEX</code></a>!</li>
</ul>
<h3>vscode</h3>
<ul>
<li><strong>feat:</strong> allow disabling the welcome page (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6165">#6165</a>) - Thanks to <a href="https://github.com/pierreedbrg"><code>@​pierreedbrg</code></a>!</li>
</ul>
<h2>3.3.10 (2026-08-15)</h2>
<h3>language-core</h3>
<ul>
<li><strong>fix:</strong> ignore trailing whitespace after generic parameter commas - Thanks to <a href="https://github.com/KazariEX"><code>@​KazariEX</code></a>!</li>
<li><strong>fix:</strong> resolve <code>v-for</code> item type over generic sources (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6141">#6141</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
<li><strong>fix:</strong> do not extract SFC blocks across inline Markdown code (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6145">#6145</a>) - Thanks to <a href="https://github.com/lazerg"><code>@​lazerg</code></a>!</li>
</ul>
<h3>language-service</h3>
<ul>
<li><strong>fix:</strong> serialize template data provider access across concurrent requests (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6154">#6154</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
</ul>
<h3>tsc</h3>
<ul>
<li><strong>fix:</strong> support different extension sets across project references (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6146">#6146</a>) - Thanks to <a href="https://github.com/lazerg"><code>@​lazerg</code></a>!</li>
</ul>
<h3>typescript-plugin</h3>
<ul>
<li><strong>fix:</strong> resolve requests against the owning project (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6152">#6152</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
</ul>
<h3>vscode</h3>
<ul>
<li><strong>feat:</strong> patch <code>typescript.js</code> via <code>--require</code> to support read-only file systems (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6149">#6149</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
<li><strong>fix:</strong> isolate custom TypeScript plugin paths between profiles (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6148">#6148</a>) - Thanks to <a href="https://github.com/serkodev"><code>@​serkodev</code></a>!</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vuejs/language-tools/commit/f521b39b402ebaaa9ee70faf5a60a895544ed9e9"><code>f521b39</code></a> v3.3.11 (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6174">#6174</a>)</li>
<li><a href="https://github.com/vuejs/language-tools/commit/05ab00944825815fb5dc5e70a468893a1476fde9"><code>05ab009</code></a> fix(tsc): replace symbol <code>retryToken</code> with error to allow IPC serialization (...</li>
<li><a href="https://github.com/vuejs/language-tools/commit/fd6dadab91832f60ade8020de6c6947a1115a55f"><code>fd6dada</code></a> fix(language-core): generate full fragment props for typecheck (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6155">#6155</a>)</li>
<li><a href="https://github.com/vuejs/language-tools/commit/977995f07e39baf1a46bb42552d48ec0e896485f"><code>977995f</code></a> v3.3.10 (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6160">#6160</a>)</li>
<li><a href="https://github.com/vuejs/language-tools/commit/cb65247aa3c8ad2e858d13c7d60d2c0de76e3777"><code>cb65247</code></a> fix(tsc): support different extension sets across project references (<a href="https://github.com/vuejs/language-tools/tree/HEAD/packages/tsc/issues/6146">#6146</a>)</li>
<li>See full diff in <a href="https://github.com/vuejs/language-tools/commits/v3.3.11/packages/tsc">compare view</a></li>
</ul>
</details>
<br />

Updates `vue` from 3.5.41 to 3.5.42
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vuejs/core/releases">vue's releases</a>.</em></p>
<blockquote>
<h2>v3.5.42</h2>
<p>For stable releases, please refer to <a href="https://github.com/vuejs/core/blob/main/CHANGELOG.md">CHANGELOG.md</a> for details.
For pre-releases, please refer to <a href="https://github.com/vuejs/core/blob/minor/CHANGELOG.md">CHANGELOG.md</a> of the <code>minor</code> branch.</p>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/vuejs/core/blob/main/CHANGELOG.md">vue's changelog</a>.</em></p>
<blockquote>
<h2><a href="https://github.com/vuejs/core/compare/v3.5.41...v3.5.42">3.5.42</a> (2026-08-27)</h2>
<h3>Bug Fixes</h3>
<ul>
<li><strong>hydration:</strong> handle async component unmount before lazy hydration (<a href="https://redirect.github.com/vuejs/core/issues/15252">#15252</a>) (<a href="https://github.com/vuejs/core/commit/6e1814aa355aad8dd32a89873e95267297ae0609">6e1814a</a>)</li>
<li><strong>hydration:</strong> handle moving unresolved async fragment (<a href="https://redirect.github.com/vuejs/core/issues/15263">#15263</a>) (<a href="https://github.com/vuejs/core/commit/a72036f66bcb9a4f3b3737cda19eeba1bc531e15">a72036f</a>)</li>
<li><strong>runtime-core:</strong> avoid caching unmounted suspense children (<a href="https://redirect.github.com/vuejs/core/issues/15291">#15291</a>) (<a href="https://github.com/vuejs/core/commit/b535917d46d5c6e28c1d3b9185bfa1665127c73a">b535917</a>), closes <a href="https://redirect.github.com/vuejs/core/issues/15288">#15288</a></li>
<li><strong>runtime-core:</strong> keep .trim result when combined with .number v-model modifier (<a href="https://redirect.github.com/vuejs/core/issues/15346">#15346</a>) (<a href="https://github.com/vuejs/core/commit/f8d42e1cf2a0ccb43c50fad6e972cb130c53824e">f8d42e1</a>)</li>
<li><strong>runtime-core:</strong> resolve $el for dev root comment fragment (<a href="https://redirect.github.com/vuejs/core/issues/15313">#15313</a>) (<a href="https://github.com/vuejs/core/commit/8654f35118a1165ac30fd398ceaff8849c44d9d5">8654f35</a>), closes <a href="https://redirect.github.com/vuejs/core/issues/12680">#12680</a></li>
<li><strong>runtime-dom:</strong> support !important on CSS custom properties in style binding (<a href="https://redirect.github.com/vuejs/core/issues/15348">#15348</a>) (<a href="https://github.com/vuejs/core/commit/31da934fcbe73ab8ed187bf820c80b24ced474be">31da934</a>)</li>
<li><strong>server-renderer:</strong> reject CR in attribute names (<a href="https://redirect.github.com/vuejs/core/issues/15266">#15266</a>) (<a href="https://github.com/vuejs/core/commit/a2b40db9a83b36ed9da3a16403cf8f040262d73f">a2b40db</a>)</li>
<li><strong>shared:</strong> correctly compare Map and Set values (<a href="https://redirect.github.com/vuejs/core/issues/15328">#15328</a>) (<a href="https://github.com/vuejs/core/commit/ef82a26775952a665545d3771788bd23b2efec91">ef82a26</a>), closes <a href="https://redirect.github.com/vuejs/core/issues/15320">#15320</a></li>
<li><strong>suspense:</strong> don't treat the leaving branch as the fallback while its mount is pending (<a href="https://redirect.github.com/vuejs/core/issues/15333">#15333</a>) (<a href="https://github.com/vuejs/core/commit/cd1974562357dd73101d048f207a694a4e5310ec">cd19745</a>), closes <a href="https://redirect.github.com/vuejs/core/issues/15332">#15332</a></li>
<li><strong>v-model:</strong> re-sync select when model is overridden in change handler (<a href="https://redirect.github.com/vuejs/core/issues/15298">#15298</a>) (<a href="https://github.com/vuejs/core/commit/6eaecc14d8151a7d258b80ce0519e5ecc17a2bef">6eaecc1</a>), closes <a href="https://redirect.github.com/vuejs/core/issues/10505">#10505</a></li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vuejs/core/commit/d63616ca17de965ed32dcb449a4c5cd9982f15d2"><code>d63616c</code></a> release: v3.5.42</li>
<li><a href="https://github.com/vuejs/core/commit/b8543dcf06eea9b5ca3e4550274d4aa4af21662b"><code>b8543dc</code></a> Revert &quot;fix(compiler-core): handle invalid static arg in same-name v-bind sho...</li>
<li><a href="https://github.com/vuejs/core/commit/38577161c0cfcd4e1013eec0030b781a32fc3744"><code>3857716</code></a> fix(compiler-core): handle invalid static arg in same-name v-bind shorthand (...</li>
<li><a href="https://github.com/vuejs/core/commit/31da934fcbe73ab8ed187bf820c80b24ced474be"><code>31da934</code></a> fix(runtime-dom): support !important on CSS custom properties in style bindin...</li>
<li><a href="https://github.com/vuejs/core/commit/f8d42e1cf2a0ccb43c50fad6e972cb130c53824e"><code>f8d42e1</code></a> fix(runtime-core): keep .trim result when combined with .number v-model modif...</li>
<li><a href="https://github.com/vuejs/core/commit/cd1974562357dd73101d048f207a694a4e5310ec"><code>cd19745</code></a> fix(suspense): don't treat the leaving branch as the fallback while its mount...</li>
<li><a href="https://github.com/vuejs/core/commit/8654f35118a1165ac30fd398ceaff8849c44d9d5"><code>8654f35</code></a> fix(runtime-core): resolve $el for dev root comment fragment (<a href="https://redirect.github.com/vuejs/core/issues/15313">#15313</a>)</li>
<li><a href="https://github.com/vuejs/core/commit/ef82a26775952a665545d3771788bd23b2efec91"><code>ef82a26</code></a> fix(shared): correctly compare Map and Set values (<a href="https://redirect.github.com/vuejs/core/issues/15328">#15328</a>)</li>
<li><a href="https://github.com/vuejs/core/commit/6eaecc14d8151a7d258b80ce0519e5ecc17a2bef"><code>6eaecc1</code></a> fix(v-model): re-sync select when model is overridden in change handler (<a href="https://redirect.github.com/vuejs/core/issues/15298">#15298</a>)</li>
<li><a href="https://github.com/vuejs/core/commit/b535917d46d5c6e28c1d3b9185bfa1665127c73a"><code>b535917</code></a> fix(runtime-core): avoid caching unmounted suspense children (<a href="https://redirect.github.com/vuejs/core/issues/15291">#15291</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/vuejs/core/compare/v3.5.41...v3.5.42">compare view</a></li>
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


</details>
