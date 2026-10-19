# build(deps): bump the rust-dependencies group in /ai-gateway with 3 updates

<!-- aws-preview-pin:start -->
🟡 **Live preview: [pr-18974 app preview](https://pr-18974.preview.langfuse.com)**
<!-- aws-preview-pin:end -->

Bumps the rust-dependencies group in /ai-gateway with 3 updates: [tokio](https://github.com/tokio-rs/tokio), [uuid](https://github.com/uuid-rs/uuid) and [thiserror](https://github.com/dtolnay/thiserror).

Updates `tokio` from 1.53.1 to 1.53.2
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/tokio-rs/tokio/releases">tokio's releases</a>.</em></p>
<blockquote>
<h2>Tokio v1.53.2</h2>
<h1>1.53.2 (October 3rd, 2026)</h1>
<h3>Fixed</h3>
<ul>
<li>fs: handle integer overflow in buffered relative seek (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8574">#8574</a>)</li>
<li>io: revert &quot;always cleanup <code>AsyncFd</code> registration list on deregister&quot; (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8540">#8540</a>)</li>
<li>process: unregister Windows wait before closing child handle (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8564">#8564</a>)</li>
<li>rt: drop blocking pool mutex before shutting down rejected task (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8562">#8562</a>)</li>
<li>sync: fix mpsc index wraparound in block reclamation (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8546">#8546</a>)</li>
<li>sync: forget mpsc <code>Permit</code> before sending value (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8560">#8560</a>)</li>
<li>sync: validate <code>MAX_PERMITS</code> in <code>Semaphore::acquire</code> (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8548">#8548</a>)</li>
<li>sync: wake broadcast <code>Sender::closed</code> outside mutex (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8558">#8558</a>)</li>
<li>task: drop replaced waker outside lock in <code>JoinSet</code> (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8554">#8554</a>)</li>
<li>time: drop timer lock before dropping waker in <code>clear_entry</code> (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8552">#8552</a>)</li>
<li>time: expire timers directly on shutdown without rotating wheel (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8570">#8570</a>)</li>
</ul>
<h3>Fixed (unstable)</h3>
<ul>
<li>fs: clamp <code>io_uring</code> read length to <code>u32::MAX</code> (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8572">#8572</a>)</li>
<li>rt: ignore <code>current_thread</code> task dumps from other runtimes (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8544">#8544</a>)</li>
<li>rt: preserve <code>io_uring</code> context if a completion waker panics (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8566">#8566</a>)</li>
<li>sync: fix semaphore use-after-free and permit leak on tracing panic (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8542">#8542</a>)</li>
<li>taskdump: restore deferred leaf wakes during capture (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8445">#8445</a>)</li>
<li>time: drop stored waker when cancelling alt timer entry (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8550">#8550</a>)</li>
</ul>
<p><a href="https://redirect.github.com/tokio-rs/tokio/issues/8445">#8445</a>: <a href="https://redirect.github.com/tokio-rs/tokio/pull/8445">tokio-rs/tokio#8445</a>
<a href="https://redirect.github.com/tokio-rs/tokio/issues/8572">#8572</a>: <a href="https://redirect.github.com/tokio-rs/tokio/pull/8572">tokio-rs/tokio#8572</a>
<a href="https://redirect.github.com/tokio-rs/tokio/issues/8540">#8540</a>: <a href="https://redirect.github.com/tokio-rs/tokio/pull/8540">tokio-rs/tokio#8540</a>
<a href="https://redirect.github.com/tokio-rs/tokio/issues/8542">#8542</a>: <a href="https://redirect.github.com/tokio-rs/tokio/pull/8542">tokio-rs/tokio#8542</a>
<a href="https://redirect.github.com/tokio-rs/tokio/issues/8544">#8544</a>: <a href="https://redirect.github.com/tokio-rs/tokio/pull/8544">tokio-rs/tokio#8544</a>
<a href="https://redirect.github.com/tokio-rs/tokio/issues/8546">#8546</a>: <a href="https://redirect.github.com/tokio-rs/tokio/pull/8546">tokio-rs/tokio#8546</a>
<a href="https://redirect.github.com/tokio-rs/tokio/issues/8548">#8548</a>: <a href="https://redirect.github.com/tokio-rs/tokio/pull/8548">tokio-rs/tokio#8548</a>
<a href="https://redirect.github.com/tokio-rs/tokio/issues/8550">#8550</a>: <a href="https://redirect.github.com/tokio-rs/tokio/pull/8550">tokio-rs/tokio#8550</a>
<a href="https://redirect.github.com/tokio-rs/tokio/issues/8552">#8552</a>: <a href="https://redirect.github.com/tokio-rs/tokio/pull/8552">tokio-rs/tokio#8552</a>
<a href="https://redirect.github.com/tokio-rs/tokio/issues/8554">#8554</a>: <a href="https://redirect.github.com/tokio-rs/tokio/pull/8554">tokio-rs/tokio#8554</a>
<a href="https://redirect.github.com/tokio-rs/tokio/issues/8558">#8558</a>: <a href="https://redirect.github.com/tokio-rs/tokio/pull/8558">tokio-rs/tokio#8558</a>
<a href="https://redirect.github.com/tokio-rs/tokio/issues/8560">#8560</a>: <a href="https://redirect.github.com/tokio-rs/tokio/pull/8560">tokio-rs/tokio#8560</a>
<a href="https://redirect.github.com/tokio-rs/tokio/issues/8562">#8562</a>: <a href="https://redirect.github.com/tokio-rs/tokio/pull/8562">tokio-rs/tokio#8562</a>
<a href="https://redirect.github.com/tokio-rs/tokio/issues/8564">#8564</a>: <a href="https://redirect.github.com/tokio-rs/tokio/pull/8564">tokio-rs/tokio#8564</a>
<a href="https://redirect.github.com/tokio-rs/tokio/issues/8566">#8566</a>: <a href="https://redirect.github.com/tokio-rs/tokio/pull/8566">tokio-rs/tokio#8566</a>
<a href="https://redirect.github.com/tokio-rs/tokio/issues/8570">#8570</a>: <a href="https://redirect.github.com/tokio-rs/tokio/pull/8570">tokio-rs/tokio#8570</a>
<a href="https://redirect.github.com/tokio-rs/tokio/issues/8574">#8574</a>: <a href="https://redirect.github.com/tokio-rs/tokio/pull/8574">tokio-rs/tokio#8574</a></p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/tokio-rs/tokio/commit/ff0c4068a4ba5f3af0fe3c5657ba42879b6ea599"><code>ff0c406</code></a> chore: prepare Tokio v1.53.2 (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8580">#8580</a>)</li>
<li><a href="https://github.com/tokio-rs/tokio/commit/a762700e41bf027630ba4620cfd80d127b7c801d"><code>a762700</code></a> Merge 'tokio-1.51.5' into 'tokio-1.53.x' (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8577">#8577</a>)</li>
<li><a href="https://github.com/tokio-rs/tokio/commit/ec31a9f62c9426cec415c8c79e0608dd2866bbf7"><code>ec31a9f</code></a> chore: prepare Tokio v1.51.5 (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8579">#8579</a>)</li>
<li><a href="https://github.com/tokio-rs/tokio/commit/625c85108da5ad0d482702a21d7d58a56ea06a48"><code>625c851</code></a> sync: assign semaphore permits before emitting tracing event (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8542">#8542</a>)</li>
<li><a href="https://github.com/tokio-rs/tokio/commit/832dd233293eaa59ba19cc6f5dc4753aab55ac13"><code>832dd23</code></a> sync: avoid leaking semaphore permits on tracing panic (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8542">#8542</a>)</li>
<li><a href="https://github.com/tokio-rs/tokio/commit/826954a2f3b6f595121c38875a5d81ca3e5f6cc6"><code>826954a</code></a> sync: unlink semaphore waiter before emitting tracing event (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8542">#8542</a>)</li>
<li><a href="https://github.com/tokio-rs/tokio/commit/9a479922501eb47102ab844fa40e4b28d1a3c250"><code>9a47992</code></a> process: unregister Windows wait before closing child handle (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8564">#8564</a>)</li>
<li><a href="https://github.com/tokio-rs/tokio/commit/2fc5972b8bd6f51d1ad6df3bcc1a1927d1702663"><code>2fc5972</code></a> fs: handle integer overflow in buffered relative seek (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8574">#8574</a>)</li>
<li><a href="https://github.com/tokio-rs/tokio/commit/85a6d13882e2ccf5c24131b282bab0214b0a493e"><code>85a6d13</code></a> io: revert &quot;always cleanup AsyncFd registration list on deregister&quot; (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8540">#8540</a>)</li>
<li><a href="https://github.com/tokio-rs/tokio/commit/436faa2da3970817653fef98c9abc6c8b4367f51"><code>436faa2</code></a> rt: drop blocking pool mutex before shutting down rejected task (<a href="https://redirect.github.com/tokio-rs/tokio/issues/8562">#8562</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/tokio-rs/tokio/compare/tokio-1.53.1...tokio-1.53.2">compare view</a></li>
</ul>
</details>
<br />

Updates `uuid` from 1.26.1 to 1.27.0
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/uuid-rs/uuid/releases">uuid's releases</a>.</em></p>
<blockquote>
<h2>v1.27.0</h2>
<h2>What's Changed</h2>
<ul>
<li>Accept case-insensitive urn:uuid: prefixes when parsing by <a href="https://github.com/jaideeppyne"><code>@​jaideeppyne</code></a> in <a href="https://redirect.github.com/uuid-rs/uuid/pull/912">uuid-rs/uuid#912</a></li>
<li>Fix ordering of V7 UUIDs created by earlier seconds with later subsec nanos by <a href="https://github.com/KodrAus"><code>@​KodrAus</code></a> in <a href="https://redirect.github.com/uuid-rs/uuid/pull/915">uuid-rs/uuid#915</a></li>
<li>Prepare for 1.27.0 release by <a href="https://github.com/KodrAus"><code>@​KodrAus</code></a> in <a href="https://redirect.github.com/uuid-rs/uuid/pull/917">uuid-rs/uuid#917</a></li>
</ul>
<h2>New Contributors</h2>
<ul>
<li><a href="https://github.com/jaideeppyne"><code>@​jaideeppyne</code></a> made their first contribution in <a href="https://redirect.github.com/uuid-rs/uuid/pull/912">uuid-rs/uuid#912</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/uuid-rs/uuid/compare/v1.26.1...v1.27.0">https://github.com/uuid-rs/uuid/compare/v1.26.1...v1.27.0</a></p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/uuid-rs/uuid/commit/b62154e8be41ce42127cba08ee5e5cef3e2ea971"><code>b62154e</code></a> Merge pull request <a href="https://redirect.github.com/uuid-rs/uuid/issues/917">#917</a> from uuid-rs/cargo/v1.27.0</li>
<li><a href="https://github.com/uuid-rs/uuid/commit/ffd8ec55f20006fa2b5978cc03a1e671835040e9"><code>ffd8ec5</code></a> prepare for 1.27.0 release</li>
<li><a href="https://github.com/uuid-rs/uuid/commit/4b6c10f9dd9cf37809460859ab88071d43703398"><code>4b6c10f</code></a> Merge pull request <a href="https://redirect.github.com/uuid-rs/uuid/issues/915">#915</a> from uuid-rs/fix/v7-ordering</li>
<li><a href="https://github.com/uuid-rs/uuid/commit/a1aa126f97cdc8d9c5c25d56efa0e7bcb9ab0514"><code>a1aa126</code></a> Merge pull request <a href="https://redirect.github.com/uuid-rs/uuid/issues/912">#912</a> from jaideeppyne/fix/urn-prefix-case-insensitive</li>
<li><a href="https://github.com/uuid-rs/uuid/commit/4639d67b0f117a94cf0add01e4c68e674691b49c"><code>4639d67</code></a> fix ordering of V7 UUIDs created by earlier seconds with later subsec nanos</li>
<li><a href="https://github.com/uuid-rs/uuid/commit/272370344a977ee0641ffa4d01b7ad3ca0eda687"><code>2723703</code></a> bump MSRV to 1.89.0</li>
<li><a href="https://github.com/uuid-rs/uuid/commit/a3e64faaf7fdf583260fc18a594b099677855eea"><code>a3e64fa</code></a> refactor: simplify URN prefix parsing</li>
<li><a href="https://github.com/uuid-rs/uuid/commit/5055fd41c7f33c16a1eac3198eac6224ec18b61d"><code>5055fd4</code></a> refactor: inline case-insensitive URN prefix checks</li>
<li><a href="https://github.com/uuid-rs/uuid/commit/cb8b1d51421df4828c11ebca6b54c5986caafef6"><code>cb8b1d5</code></a> refactor: simplify case-insensitive URN parsing</li>
<li><a href="https://github.com/uuid-rs/uuid/commit/285967db45b800ffda5032d12c32e3d4e2620902"><code>285967d</code></a> Accept case-insensitive urn:uuid: prefixes when parsing</li>
<li>See full diff in <a href="https://github.com/uuid-rs/uuid/compare/v1.26.1...v1.27.0">compare view</a></li>
</ul>
</details>
<br />

Updates `thiserror` from 2.0.20 to 2.0.21
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/dtolnay/thiserror/releases">thiserror's releases</a>.</em></p>
<blockquote>
<h2>2.0.21</h2>
<ul>
<li>Fix parsing of generic unit variants in display expressions (<a href="https://redirect.github.com/dtolnay/thiserror/issues/459">#459</a>)</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/dtolnay/thiserror/commit/b1827ee06f81a7d7f954e676771e19a97f9f8e3b"><code>b1827ee</code></a> Release 2.0.21</li>
<li><a href="https://github.com/dtolnay/thiserror/commit/58037b575a2a5543d0d54a49360554325b49f55a"><code>58037b5</code></a> Merge pull request <a href="https://redirect.github.com/dtolnay/thiserror/issues/459">#459</a> from dtolnay/turbofish</li>
<li><a href="https://github.com/dtolnay/thiserror/commit/f82a0cf8f06c71263c2caa26e759f337d2778153"><code>f82a0cf</code></a> Keep track of nested turbofish depth</li>
<li><a href="https://github.com/dtolnay/thiserror/commit/72ea49262d6412ccbc08f1696dda8626409e657d"><code>72ea492</code></a> Raise required compiler to Rust 1.77</li>
<li><a href="https://github.com/dtolnay/thiserror/commit/72eea0d4ddb17ff9fa873aa74469de850021b22e"><code>72eea0d</code></a> Resolve io_other_error clippy lint in tests</li>
<li><a href="https://github.com/dtolnay/thiserror/commit/07f09a2ec934df58508ce4fa5e7fbf27cca552c2"><code>07f09a2</code></a> Raise required compiler to Rust 1.74</li>
<li><a href="https://github.com/dtolnay/thiserror/commit/2715388e8cc5787b3643251f7a7a637e89376688"><code>2715388</code></a> Update ui test suite to nightly-2026-09-22</li>
<li><a href="https://github.com/dtolnay/thiserror/commit/5a306c7d0a8588caaaaa6a7567aeb25c1c10719b"><code>5a306c7</code></a> Update ui test suite to nightly-2026-09-05</li>
<li><a href="https://github.com/dtolnay/thiserror/commit/ef9383b37d7c96b01e10df35d3e9e313c7b98b5a"><code>ef9383b</code></a> Update ui test suite to nightly-2026-08-22</li>
<li><a href="https://github.com/dtolnay/thiserror/commit/8336b8407fbfe69177c504cdbc379db20cf6f131"><code>8336b84</code></a> Update ui tests for version 2.0.20</li>
<li>See full diff in <a href="https://github.com/dtolnay/thiserror/compare/2.0.20...2.0.21">compare view</a></li>
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
