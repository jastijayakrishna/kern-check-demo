# chore(deps): bump the rust-dependencies group in /ai-gateway with 6 updates

<!-- aws-preview-pin:start -->
🟡 **Live preview: [pr-18146 app preview](https://pr-18146.preview.langfuse.com)**
<!-- aws-preview-pin:end -->

Bumps the rust-dependencies group in /ai-gateway with 6 updates:

| Package | From | To |
| --- | --- | --- |
| [opentelemetry-http](https://github.com/open-telemetry/opentelemetry-rust) | `0.32.0` | `0.33.0` |
| [opentelemetry](https://github.com/open-telemetry/opentelemetry-rust) | `0.32.0` | `0.33.0` |
| [opentelemetry_sdk](https://github.com/open-telemetry/opentelemetry-rust) | `0.32.1` | `0.33.0` |
| [opentelemetry-otlp](https://github.com/open-telemetry/opentelemetry-rust) | `0.32.0` | `0.33.0` |
| [tracing-opentelemetry](https://github.com/tokio-rs/tracing-opentelemetry) | `0.33.0` | `0.34.0` |
| [opentelemetry-proto](https://github.com/open-telemetry/opentelemetry-rust) | `0.32.0` | `0.33.0` |

Updates `opentelemetry-http` from 0.32.0 to 0.33.0
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/open-telemetry/opentelemetry-rust/releases">opentelemetry-http's releases</a>.</em></p>
<blockquote>
<h2>0.33.0</h2>
<p>See the <a href="https://github.com/open-telemetry/opentelemetry-rust/blob/opentelemetry-0.33.0/docs/release_0.33.md">0.33.0 release notes and migration guidance</a>.</p>
<p>The OTLP exporters for Logs and Metrics remain release candidates. We plan to declare them stable in 0.33.1 after approximately two weeks of validation, provided no issues requiring breaking API changes arise. The Logs and Metrics API and SDK remain stable; Distributed Tracing remains pre-stable.</p>
<h2>opentelemetry-semantic-conventions-0.32.1</h2>
<p>See the <a href="https://github.com/open-telemetry/opentelemetry-rust/blob/opentelemetry-semantic-conventions-0.32.1/opentelemetry-semantic-conventions/CHANGELOG.md">CHANGELOG</a> for details.</p>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/open-telemetry/opentelemetry-rust/blob/opentelemetry-http-0.33.0/docs/release_0.33.md">opentelemetry-http's changelog</a>.</em></p>
<blockquote>
<h1>Release Notes 0.33</h1>
<p>The OTLP exporters for Logs and Metrics remain in release-candidate (RC) status
in OpenTelemetry Rust 0.33.0. We intend to declare them stable in 0.33.1,
approximately two weeks after this release, provided the RC period does not
uncover any issues requiring breaking API changes. During this period, we expect
only compatible fixes, documentation updates, and low-risk internal
optimisations.</p>
<p>OpenTelemetry Rust 0.33.0 brings OTLP retries on by default and completes the
stabilisation cleanups that began in 0.32. The Logs and Metrics API and SDK
remain stable with no breaking changes. The Distributed Tracing API, SDK, and
OTLP exporter remain pre-stable, and this release includes intentional breaking changes in that area
to continue preparing it for stabilisation.</p>
<p>For detailed changelogs of individual crates, refer to their respective
changelog files. This document summarises the key changes.</p>
<h2>Key Changes</h2>
<h3>OTLP Exporters for Logs and Metrics (RC)</h3>
<p>Version 0.33.0 keeps the OTLP exporters for Logs and Metrics in RC for a final
validation period. If no issues requiring breaking API changes are identified,
we intend to declare them stable in 0.33.1 approximately two weeks after this
release.</p>
<h4>Retries enabled by default</h4>
<p>OTLP/HTTP and OTLP/gRPC retries are now enabled by default with exponential
backoff, jitter, and up to 3 retries (4 attempts total). Use
<code>.with_retry_policy(RetryPolicy::disabled())</code> to opt out, or provide a custom
<code>RetryPolicy</code>.</p>
<p>Users of the experimental retry feature flags (<code>experimental-grpc-retry</code> and
<code>experimental-http-retry</code>) should remove them from
<code>Cargo.toml</code>. The <code>retry</code> and <code>retry_classification</code> modules are now
crate-private; replace <code>opentelemetry_otlp::retry</code> imports with
<code>opentelemetry_otlp::RetryPolicy</code> and use its <code>with_*</code> methods instead of
struct literals.</p>
<h4>Stabilisation cleanups</h4>
<ul>
<li><strong>Breaking for callers matching or constructing removed build-error variants:</strong> <code>ExporterBuildError</code> now has two exhaustive variants, <code>InvalidConfiguration(String)</code> and <code>InternalFailure(String)</code>. Update uses of removed variants. Normal exporter builder calls and propagation of build errors with <code>?</code> need no changes. See the <a href="https://github.com/open-telemetry/opentelemetry-rust/blob/opentelemetry-http-0.33.0/opentelemetry-otlp/CHANGELOG.md#0330">OTLP changelog</a> for migration examples.</li>
<li><strong>Breaking</strong> <code>Protocol</code> and <code>Compression</code> are now <code>#[non_exhaustive]</code>.
Exhaustive matches must add a wildcard arm.</li>
<li><strong>Breaking</strong> <code>Protocol::from_env()</code> is now crate-private. Builders resolve
<code>OTEL_EXPORTER_OTLP_PROTOCOL</code> automatically; read the env var directly if
needed.</li>
<li>Invalid OTLP endpoint environment variables (HTTP and gRPC) now produce a</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/19833847cab86c8464c1dfb6d28b1de9c0b50038"><code>1983384</code></a> docs: clarify OTLP 0.33 migration guidance (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3747">#3747</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/dacfeda67b765a9049a84fac686bf77b9d730b40"><code>dacfeda</code></a> chore: Prepare for release v0.33.0 (RC) (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3712">#3712</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/996ac1e398ca2a75bc787a18204c37fa1ff6a8b4"><code>996ac1e</code></a> refactor(http)!: make ResponseBodyTooLarge extensible (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3736">#3736</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/d328c659c626b7853715b02f04275d62a1ebcc53"><code>d328c65</code></a> fix(proto): preserve scope metadata when grouping OTLP logs (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3740">#3740</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/e652efdb4b8bddfb6cb488558a44c2c6f877dfa2"><code>e652efd</code></a> refactor(otlp): finalize exporter build error API (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3692">#3692</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/8809c428e08978a361a0c4284459c876fdc46b60"><code>8809c42</code></a> refactor(otlp)!: separate configuration parsing errors (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3742">#3742</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/cc1c374259f5f57de3371f59c68062d1be7567c2"><code>cc1c374</code></a> feat(otlp): Allow to provide http client wrapped in Arc for user (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3468">#3468</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/e085c6184ad71d38217d4394a4ef2894a446f55d"><code>e085c61</code></a> ci: use supported Debian image for benchmarks (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3744">#3744</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/6c5fd583b2805166393e59b48a827c3a44345a82"><code>6c5fd58</code></a> fix(proto): accept omitted partial success fields (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3739">#3739</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/51b36a72d299e4a6e2b5fdfadaae1f4e8688b127"><code>51b36a7</code></a> fix(otlp): handle enum environment values consistently (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3730">#3730</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/open-telemetry/opentelemetry-rust/compare/opentelemetry-http-0.32.0...opentelemetry-http-0.33.0">compare view</a></li>
</ul>
</details>
<br />

Updates `opentelemetry` from 0.32.0 to 0.33.0
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/open-telemetry/opentelemetry-rust/releases">opentelemetry's releases</a>.</em></p>
<blockquote>
<h2>0.33.0</h2>
<p>See the <a href="https://github.com/open-telemetry/opentelemetry-rust/blob/opentelemetry-0.33.0/docs/release_0.33.md">0.33.0 release notes and migration guidance</a>.</p>
<p>The OTLP exporters for Logs and Metrics remain release candidates. We plan to declare them stable in 0.33.1 after approximately two weeks of validation, provided no issues requiring breaking API changes arise. The Logs and Metrics API and SDK remain stable; Distributed Tracing remains pre-stable.</p>
<h2>opentelemetry-semantic-conventions-0.32.1</h2>
<p>See the <a href="https://github.com/open-telemetry/opentelemetry-rust/blob/opentelemetry-semantic-conventions-0.32.1/opentelemetry-semantic-conventions/CHANGELOG.md">CHANGELOG</a> for details.</p>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/open-telemetry/opentelemetry-rust/blob/opentelemetry-0.33.0/docs/release_0.33.md">opentelemetry's changelog</a>.</em></p>
<blockquote>
<h1>Release Notes 0.33</h1>
<p>The OTLP exporters for Logs and Metrics remain in release-candidate (RC) status
in OpenTelemetry Rust 0.33.0. We intend to declare them stable in 0.33.1,
approximately two weeks after this release, provided the RC period does not
uncover any issues requiring breaking API changes. During this period, we expect
only compatible fixes, documentation updates, and low-risk internal
optimisations.</p>
<p>OpenTelemetry Rust 0.33.0 brings OTLP retries on by default and completes the
stabilisation cleanups that began in 0.32. The Logs and Metrics API and SDK
remain stable with no breaking changes. The Distributed Tracing API, SDK, and
OTLP exporter remain pre-stable, and this release includes intentional breaking changes in that area
to continue preparing it for stabilisation.</p>
<p>For detailed changelogs of individual crates, refer to their respective
changelog files. This document summarises the key changes.</p>
<h2>Key Changes</h2>
<h3>OTLP Exporters for Logs and Metrics (RC)</h3>
<p>Version 0.33.0 keeps the OTLP exporters for Logs and Metrics in RC for a final
validation period. If no issues requiring breaking API changes are identified,
we intend to declare them stable in 0.33.1 approximately two weeks after this
release.</p>
<h4>Retries enabled by default</h4>
<p>OTLP/HTTP and OTLP/gRPC retries are now enabled by default with exponential
backoff, jitter, and up to 3 retries (4 attempts total). Use
<code>.with_retry_policy(RetryPolicy::disabled())</code> to opt out, or provide a custom
<code>RetryPolicy</code>.</p>
<p>Users of the experimental retry feature flags (<code>experimental-grpc-retry</code> and
<code>experimental-http-retry</code>) should remove them from
<code>Cargo.toml</code>. The <code>retry</code> and <code>retry_classification</code> modules are now
crate-private; replace <code>opentelemetry_otlp::retry</code> imports with
<code>opentelemetry_otlp::RetryPolicy</code> and use its <code>with_*</code> methods instead of
struct literals.</p>
<h4>Stabilisation cleanups</h4>
<ul>
<li><strong>Breaking for callers matching or constructing removed build-error variants:</strong> <code>ExporterBuildError</code> now has two exhaustive variants, <code>InvalidConfiguration(String)</code> and <code>InternalFailure(String)</code>. Update uses of removed variants. Normal exporter builder calls and propagation of build errors with <code>?</code> need no changes. See the <a href="https://github.com/open-telemetry/opentelemetry-rust/blob/opentelemetry-0.33.0/opentelemetry-otlp/CHANGELOG.md#0330">OTLP changelog</a> for migration examples.</li>
<li><strong>Breaking</strong> <code>Protocol</code> and <code>Compression</code> are now <code>#[non_exhaustive]</code>.
Exhaustive matches must add a wildcard arm.</li>
<li><strong>Breaking</strong> <code>Protocol::from_env()</code> is now crate-private. Builders resolve
<code>OTEL_EXPORTER_OTLP_PROTOCOL</code> automatically; read the env var directly if
needed.</li>
<li>Invalid OTLP endpoint environment variables (HTTP and gRPC) now produce a</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/19833847cab86c8464c1dfb6d28b1de9c0b50038"><code>1983384</code></a> docs: clarify OTLP 0.33 migration guidance (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3747">#3747</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/dacfeda67b765a9049a84fac686bf77b9d730b40"><code>dacfeda</code></a> chore: Prepare for release v0.33.0 (RC) (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3712">#3712</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/996ac1e398ca2a75bc787a18204c37fa1ff6a8b4"><code>996ac1e</code></a> refactor(http)!: make ResponseBodyTooLarge extensible (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3736">#3736</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/d328c659c626b7853715b02f04275d62a1ebcc53"><code>d328c65</code></a> fix(proto): preserve scope metadata when grouping OTLP logs (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3740">#3740</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/e652efdb4b8bddfb6cb488558a44c2c6f877dfa2"><code>e652efd</code></a> refactor(otlp): finalize exporter build error API (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3692">#3692</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/8809c428e08978a361a0c4284459c876fdc46b60"><code>8809c42</code></a> refactor(otlp)!: separate configuration parsing errors (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3742">#3742</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/cc1c374259f5f57de3371f59c68062d1be7567c2"><code>cc1c374</code></a> feat(otlp): Allow to provide http client wrapped in Arc for user (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3468">#3468</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/e085c6184ad71d38217d4394a4ef2894a446f55d"><code>e085c61</code></a> ci: use supported Debian image for benchmarks (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3744">#3744</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/6c5fd583b2805166393e59b48a827c3a44345a82"><code>6c5fd58</code></a> fix(proto): accept omitted partial success fields (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3739">#3739</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/51b36a72d299e4a6e2b5fdfadaae1f4e8688b127"><code>51b36a7</code></a> fix(otlp): handle enum environment values consistently (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3730">#3730</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/open-telemetry/opentelemetry-rust/compare/opentelemetry-0.32.0...opentelemetry-0.33.0">compare view</a></li>
</ul>
</details>
<br />

Updates `opentelemetry_sdk` from 0.32.1 to 0.33.0
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/open-telemetry/opentelemetry-rust/blob/opentelemetry_sdk-0.33.0/docs/release_0.33.md">opentelemetry_sdk's changelog</a>.</em></p>
<blockquote>
<h1>Release Notes 0.33</h1>
<p>The OTLP exporters for Logs and Metrics remain in release-candidate (RC) status
in OpenTelemetry Rust 0.33.0. We intend to declare them stable in 0.33.1,
approximately two weeks after this release, provided the RC period does not
uncover any issues requiring breaking API changes. During this period, we expect
only compatible fixes, documentation updates, and low-risk internal
optimisations.</p>
<p>OpenTelemetry Rust 0.33.0 brings OTLP retries on by default and completes the
stabilisation cleanups that began in 0.32. The Logs and Metrics API and SDK
remain stable with no breaking changes. The Distributed Tracing API, SDK, and
OTLP exporter remain pre-stable, and this release includes intentional breaking changes in that area
to continue preparing it for stabilisation.</p>
<p>For detailed changelogs of individual crates, refer to their respective
changelog files. This document summarises the key changes.</p>
<h2>Key Changes</h2>
<h3>OTLP Exporters for Logs and Metrics (RC)</h3>
<p>Version 0.33.0 keeps the OTLP exporters for Logs and Metrics in RC for a final
validation period. If no issues requiring breaking API changes are identified,
we intend to declare them stable in 0.33.1 approximately two weeks after this
release.</p>
<h4>Retries enabled by default</h4>
<p>OTLP/HTTP and OTLP/gRPC retries are now enabled by default with exponential
backoff, jitter, and up to 3 retries (4 attempts total). Use
<code>.with_retry_policy(RetryPolicy::disabled())</code> to opt out, or provide a custom
<code>RetryPolicy</code>.</p>
<p>Users of the experimental retry feature flags (<code>experimental-grpc-retry</code> and
<code>experimental-http-retry</code>) should remove them from
<code>Cargo.toml</code>. The <code>retry</code> and <code>retry_classification</code> modules are now
crate-private; replace <code>opentelemetry_otlp::retry</code> imports with
<code>opentelemetry_otlp::RetryPolicy</code> and use its <code>with_*</code> methods instead of
struct literals.</p>
<h4>Stabilisation cleanups</h4>
<ul>
<li><strong>Breaking for callers matching or constructing removed build-error variants:</strong> <code>ExporterBuildError</code> now has two exhaustive variants, <code>InvalidConfiguration(String)</code> and <code>InternalFailure(String)</code>. Update uses of removed variants. Normal exporter builder calls and propagation of build errors with <code>?</code> need no changes. See the <a href="https://github.com/open-telemetry/opentelemetry-rust/blob/opentelemetry_sdk-0.33.0/opentelemetry-otlp/CHANGELOG.md#0330">OTLP changelog</a> for migration examples.</li>
<li><strong>Breaking</strong> <code>Protocol</code> and <code>Compression</code> are now <code>#[non_exhaustive]</code>.
Exhaustive matches must add a wildcard arm.</li>
<li><strong>Breaking</strong> <code>Protocol::from_env()</code> is now crate-private. Builders resolve
<code>OTEL_EXPORTER_OTLP_PROTOCOL</code> automatically; read the env var directly if
needed.</li>
<li>Invalid OTLP endpoint environment variables (HTTP and gRPC) now produce a</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/19833847cab86c8464c1dfb6d28b1de9c0b50038"><code>1983384</code></a> docs: clarify OTLP 0.33 migration guidance (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3747">#3747</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/dacfeda67b765a9049a84fac686bf77b9d730b40"><code>dacfeda</code></a> chore: Prepare for release v0.33.0 (RC) (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3712">#3712</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/996ac1e398ca2a75bc787a18204c37fa1ff6a8b4"><code>996ac1e</code></a> refactor(http)!: make ResponseBodyTooLarge extensible (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3736">#3736</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/d328c659c626b7853715b02f04275d62a1ebcc53"><code>d328c65</code></a> fix(proto): preserve scope metadata when grouping OTLP logs (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3740">#3740</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/e652efdb4b8bddfb6cb488558a44c2c6f877dfa2"><code>e652efd</code></a> refactor(otlp): finalize exporter build error API (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3692">#3692</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/8809c428e08978a361a0c4284459c876fdc46b60"><code>8809c42</code></a> refactor(otlp)!: separate configuration parsing errors (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3742">#3742</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/cc1c374259f5f57de3371f59c68062d1be7567c2"><code>cc1c374</code></a> feat(otlp): Allow to provide http client wrapped in Arc for user (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3468">#3468</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/e085c6184ad71d38217d4394a4ef2894a446f55d"><code>e085c61</code></a> ci: use supported Debian image for benchmarks (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3744">#3744</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/6c5fd583b2805166393e59b48a827c3a44345a82"><code>6c5fd58</code></a> fix(proto): accept omitted partial success fields (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3739">#3739</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/51b36a72d299e4a6e2b5fdfadaae1f4e8688b127"><code>51b36a7</code></a> fix(otlp): handle enum environment values consistently (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3730">#3730</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/open-telemetry/opentelemetry-rust/compare/opentelemetry-semantic-conventions-0.32.1...opentelemetry_sdk-0.33.0">compare view</a></li>
</ul>
</details>
<br />

Updates `opentelemetry-otlp` from 0.32.0 to 0.33.0
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/open-telemetry/opentelemetry-rust/blob/opentelemetry-otlp-0.33.0/docs/release_0.33.md">opentelemetry-otlp's changelog</a>.</em></p>
<blockquote>
<h1>Release Notes 0.33</h1>
<p>The OTLP exporters for Logs and Metrics remain in release-candidate (RC) status
in OpenTelemetry Rust 0.33.0. We intend to declare them stable in 0.33.1,
approximately two weeks after this release, provided the RC period does not
uncover any issues requiring breaking API changes. During this period, we expect
only compatible fixes, documentation updates, and low-risk internal
optimisations.</p>
<p>OpenTelemetry Rust 0.33.0 brings OTLP retries on by default and completes the
stabilisation cleanups that began in 0.32. The Logs and Metrics API and SDK
remain stable with no breaking changes. The Distributed Tracing API, SDK, and
OTLP exporter remain pre-stable, and this release includes intentional breaking changes in that area
to continue preparing it for stabilisation.</p>
<p>For detailed changelogs of individual crates, refer to their respective
changelog files. This document summarises the key changes.</p>
<h2>Key Changes</h2>
<h3>OTLP Exporters for Logs and Metrics (RC)</h3>
<p>Version 0.33.0 keeps the OTLP exporters for Logs and Metrics in RC for a final
validation period. If no issues requiring breaking API changes are identified,
we intend to declare them stable in 0.33.1 approximately two weeks after this
release.</p>
<h4>Retries enabled by default</h4>
<p>OTLP/HTTP and OTLP/gRPC retries are now enabled by default with exponential
backoff, jitter, and up to 3 retries (4 attempts total). Use
<code>.with_retry_policy(RetryPolicy::disabled())</code> to opt out, or provide a custom
<code>RetryPolicy</code>.</p>
<p>Users of the experimental retry feature flags (<code>experimental-grpc-retry</code> and
<code>experimental-http-retry</code>) should remove them from
<code>Cargo.toml</code>. The <code>retry</code> and <code>retry_classification</code> modules are now
crate-private; replace <code>opentelemetry_otlp::retry</code> imports with
<code>opentelemetry_otlp::RetryPolicy</code> and use its <code>with_*</code> methods instead of
struct literals.</p>
<h4>Stabilisation cleanups</h4>
<ul>
<li><strong>Breaking for callers matching or constructing removed build-error variants:</strong> <code>ExporterBuildError</code> now has two exhaustive variants, <code>InvalidConfiguration(String)</code> and <code>InternalFailure(String)</code>. Update uses of removed variants. Normal exporter builder calls and propagation of build errors with <code>?</code> need no changes. See the <a href="https://github.com/open-telemetry/opentelemetry-rust/blob/opentelemetry-otlp-0.33.0/opentelemetry-otlp/CHANGELOG.md#0330">OTLP changelog</a> for migration examples.</li>
<li><strong>Breaking</strong> <code>Protocol</code> and <code>Compression</code> are now <code>#[non_exhaustive]</code>.
Exhaustive matches must add a wildcard arm.</li>
<li><strong>Breaking</strong> <code>Protocol::from_env()</code> is now crate-private. Builders resolve
<code>OTEL_EXPORTER_OTLP_PROTOCOL</code> automatically; read the env var directly if
needed.</li>
<li>Invalid OTLP endpoint environment variables (HTTP and gRPC) now produce a</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/19833847cab86c8464c1dfb6d28b1de9c0b50038"><code>1983384</code></a> docs: clarify OTLP 0.33 migration guidance (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3747">#3747</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/dacfeda67b765a9049a84fac686bf77b9d730b40"><code>dacfeda</code></a> chore: Prepare for release v0.33.0 (RC) (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3712">#3712</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/996ac1e398ca2a75bc787a18204c37fa1ff6a8b4"><code>996ac1e</code></a> refactor(http)!: make ResponseBodyTooLarge extensible (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3736">#3736</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/d328c659c626b7853715b02f04275d62a1ebcc53"><code>d328c65</code></a> fix(proto): preserve scope metadata when grouping OTLP logs (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3740">#3740</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/e652efdb4b8bddfb6cb488558a44c2c6f877dfa2"><code>e652efd</code></a> refactor(otlp): finalize exporter build error API (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3692">#3692</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/8809c428e08978a361a0c4284459c876fdc46b60"><code>8809c42</code></a> refactor(otlp)!: separate configuration parsing errors (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3742">#3742</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/cc1c374259f5f57de3371f59c68062d1be7567c2"><code>cc1c374</code></a> feat(otlp): Allow to provide http client wrapped in Arc for user (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3468">#3468</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/e085c6184ad71d38217d4394a4ef2894a446f55d"><code>e085c61</code></a> ci: use supported Debian image for benchmarks (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3744">#3744</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/6c5fd583b2805166393e59b48a827c3a44345a82"><code>6c5fd58</code></a> fix(proto): accept omitted partial success fields (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3739">#3739</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/51b36a72d299e4a6e2b5fdfadaae1f4e8688b127"><code>51b36a7</code></a> fix(otlp): handle enum environment values consistently (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3730">#3730</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/open-telemetry/opentelemetry-rust/compare/opentelemetry-otlp-0.32.0...opentelemetry-otlp-0.33.0">compare view</a></li>
</ul>
</details>
<br />

Updates `tracing-opentelemetry` from 0.33.0 to 0.34.0
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/tokio-rs/tracing-opentelemetry/blob/v0.1.x/CHANGELOG.md">tracing-opentelemetry's changelog</a>.</em></p>
<blockquote>
<h2><a href="https://github.com/tokio-rs/tracing-opentelemetry/compare/v0.33.0...v0.34.0">0.34.0</a> - 2026-09-20</h2>
<h3>Other</h3>
<ul>
<li>Upgrade to OpenTelemetry 0.33, see <a href="https://github.com/open-telemetry/opentelemetry-rust/blob/main/opentelemetry-sdk/CHANGELOG.md#0330">upstream changelog</a> for details (<a href="https://redirect.github.com/tokio-rs/tracing-opentelemetry/pull/268">#268</a>)</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li>See full diff in <a href="https://github.com/tokio-rs/tracing-opentelemetry/commits">compare view</a></li>
</ul>
</details>
<br />

Updates `opentelemetry-proto` from 0.32.0 to 0.33.0
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/open-telemetry/opentelemetry-rust/releases">opentelemetry-proto's releases</a>.</em></p>
<blockquote>
<h2>0.33.0</h2>
<p>See the <a href="https://github.com/open-telemetry/opentelemetry-rust/blob/opentelemetry-0.33.0/docs/release_0.33.md">0.33.0 release notes and migration guidance</a>.</p>
<p>The OTLP exporters for Logs and Metrics remain release candidates. We plan to declare them stable in 0.33.1 after approximately two weeks of validation, provided no issues requiring breaking API changes arise. The Logs and Metrics API and SDK remain stable; Distributed Tracing remains pre-stable.</p>
<h2>opentelemetry-semantic-conventions-0.32.1</h2>
<p>See the <a href="https://github.com/open-telemetry/opentelemetry-rust/blob/opentelemetry-semantic-conventions-0.32.1/opentelemetry-semantic-conventions/CHANGELOG.md">CHANGELOG</a> for details.</p>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/open-telemetry/opentelemetry-rust/blob/opentelemetry-proto-0.33.0/docs/release_0.33.md">opentelemetry-proto's changelog</a>.</em></p>
<blockquote>
<h1>Release Notes 0.33</h1>
<p>The OTLP exporters for Logs and Metrics remain in release-candidate (RC) status
in OpenTelemetry Rust 0.33.0. We intend to declare them stable in 0.33.1,
approximately two weeks after this release, provided the RC period does not
uncover any issues requiring breaking API changes. During this period, we expect
only compatible fixes, documentation updates, and low-risk internal
optimisations.</p>
<p>OpenTelemetry Rust 0.33.0 brings OTLP retries on by default and completes the
stabilisation cleanups that began in 0.32. The Logs and Metrics API and SDK
remain stable with no breaking changes. The Distributed Tracing API, SDK, and
OTLP exporter remain pre-stable, and this release includes intentional breaking changes in that area
to continue preparing it for stabilisation.</p>
<p>For detailed changelogs of individual crates, refer to their respective
changelog files. This document summarises the key changes.</p>
<h2>Key Changes</h2>
<h3>OTLP Exporters for Logs and Metrics (RC)</h3>
<p>Version 0.33.0 keeps the OTLP exporters for Logs and Metrics in RC for a final
validation period. If no issues requiring breaking API changes are identified,
we intend to declare them stable in 0.33.1 approximately two weeks after this
release.</p>
<h4>Retries enabled by default</h4>
<p>OTLP/HTTP and OTLP/gRPC retries are now enabled by default with exponential
backoff, jitter, and up to 3 retries (4 attempts total). Use
<code>.with_retry_policy(RetryPolicy::disabled())</code> to opt out, or provide a custom
<code>RetryPolicy</code>.</p>
<p>Users of the experimental retry feature flags (<code>experimental-grpc-retry</code> and
<code>experimental-http-retry</code>) should remove them from
<code>Cargo.toml</code>. The <code>retry</code> and <code>retry_classification</code> modules are now
crate-private; replace <code>opentelemetry_otlp::retry</code> imports with
<code>opentelemetry_otlp::RetryPolicy</code> and use its <code>with_*</code> methods instead of
struct literals.</p>
<h4>Stabilisation cleanups</h4>
<ul>
<li><strong>Breaking for callers matching or constructing removed build-error variants:</strong> <code>ExporterBuildError</code> now has two exhaustive variants, <code>InvalidConfiguration(String)</code> and <code>InternalFailure(String)</code>. Update uses of removed variants. Normal exporter builder calls and propagation of build errors with <code>?</code> need no changes. See the <a href="https://github.com/open-telemetry/opentelemetry-rust/blob/opentelemetry-proto-0.33.0/opentelemetry-otlp/CHANGELOG.md#0330">OTLP changelog</a> for migration examples.</li>
<li><strong>Breaking</strong> <code>Protocol</code> and <code>Compression</code> are now <code>#[non_exhaustive]</code>.
Exhaustive matches must add a wildcard arm.</li>
<li><strong>Breaking</strong> <code>Protocol::from_env()</code> is now crate-private. Builders resolve
<code>OTEL_EXPORTER_OTLP_PROTOCOL</code> automatically; read the env var directly if
needed.</li>
<li>Invalid OTLP endpoint environment variables (HTTP and gRPC) now produce a</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/19833847cab86c8464c1dfb6d28b1de9c0b50038"><code>1983384</code></a> docs: clarify OTLP 0.33 migration guidance (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3747">#3747</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/dacfeda67b765a9049a84fac686bf77b9d730b40"><code>dacfeda</code></a> chore: Prepare for release v0.33.0 (RC) (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3712">#3712</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/996ac1e398ca2a75bc787a18204c37fa1ff6a8b4"><code>996ac1e</code></a> refactor(http)!: make ResponseBodyTooLarge extensible (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3736">#3736</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/d328c659c626b7853715b02f04275d62a1ebcc53"><code>d328c65</code></a> fix(proto): preserve scope metadata when grouping OTLP logs (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3740">#3740</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/e652efdb4b8bddfb6cb488558a44c2c6f877dfa2"><code>e652efd</code></a> refactor(otlp): finalize exporter build error API (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3692">#3692</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/8809c428e08978a361a0c4284459c876fdc46b60"><code>8809c42</code></a> refactor(otlp)!: separate configuration parsing errors (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3742">#3742</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/cc1c374259f5f57de3371f59c68062d1be7567c2"><code>cc1c374</code></a> feat(otlp): Allow to provide http client wrapped in Arc for user (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3468">#3468</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/e085c6184ad71d38217d4394a4ef2894a446f55d"><code>e085c61</code></a> ci: use supported Debian image for benchmarks (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3744">#3744</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/6c5fd583b2805166393e59b48a827c3a44345a82"><code>6c5fd58</code></a> fix(proto): accept omitted partial success fields (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3739">#3739</a>)</li>
<li><a href="https://github.com/open-telemetry/opentelemetry-rust/commit/51b36a72d299e4a6e2b5fdfadaae1f4e8688b127"><code>51b36a7</code></a> fix(otlp): handle enum environment values consistently (<a href="https://redirect.github.com/open-telemetry/opentelemetry-rust/issues/3730">#3730</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/open-telemetry/opentelemetry-rust/compare/opentelemetry-proto-0.32.0...opentelemetry-proto-0.33.0">compare view</a></li>
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
