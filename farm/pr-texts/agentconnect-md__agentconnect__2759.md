# feat(daemon): protect Kimi file API keys in microsandbox

Kimi file API keys currently enter the guest with its native configuration. Project literal `api_key` values from the active `config.toml` to placeholders and reuse the existing microsandbox TLS proxy for explicit supported HTTPS model endpoints. Shared values share a binding, matching copies in seeded files are scrubbed, guest edits cannot authorize new hosts, and retained plaintext or changed credential identities require a new session. File-key discovery now recognizes API-only Kimi configuration.

OAuth keeps its existing shared writable credentials directory and native refresh behavior; it is not shielded by this change. Environment-only credentials, `api_key_env`, provider env bags and arbitrary header credentials remain outside scope. Unsupported routes and service-only keys stay hidden without injection. Amp's existing protection was checked without changing its implementation; real authenticated Amp acceptance still needs a login.

Validation: four focused Kimi tests plus ten Amp/Grok regression tests passed serially in a one-CPU Linux container using bundled test entries and Vitest. Existing runtime HOME/credential tests passed locally (80 passed, two skipped); daemon typecheck, focused lint and formatting passed. An isolated native Kimi Code 2.1.1 probe completed ACP initialize/new/prompt with both a synthetic file key and a placeholder, verifying Bearer transport against a local simulated endpoint. Real provider TLS/model/tool turns inside a VM remain unverified. No existing login or daemon configuration was changed.

Refs #1874

Created by Codex . GPT-6
