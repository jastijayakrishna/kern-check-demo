# feat(tunnel): replace rathole with frp (TCP + UDP everywhere)

Swaps rathole → frp (fatedier/frp) for **every** tunnel: the gateway relay, the k8s reverse tunnel, and the exit hops.

## Why
rathole is TCP-only. Egress via an exit node therefore dropped UDP — QUIC/HTTP3 fell back to TCP, a degraded experience vs direct egress. frp carries TCP **and** UDP, so exits stop being second-class. Bonus: one tunnel tool everywhere instead of reasoning about rathole's limits per-path.

## What it does
- **frps is dumb** — bind port `7000` + auth token, no per-service config. Every proxy is declared **client-side** by frpc. Consequence: `createGateway` no longer takes an exit list, and adding an exit needs **no gateway change** (its frpc declares its own `remotePort`).
- **https bind moves server→client** — `httpsRemotePort` is `8443` when Xray owns `:443` (frp = its decoy backend) else `443`. Computed in `main.ts`, passed to `createIngress`.
- **Exits gain UDP** — ss-rust flips `tcp_only` → `tcp_and_udp`, each exit gets a **tcp+udp proxy pair**, and the exit Service exposes both. QUIC/HTTP3 egresses at the exit end-to-end.
- Firewall `2333` → `7000`. `ratholeVersion` → `frpVersion` (`v0.70.0`). k8s client image `rapiz1/rathole` → `the official fatedier/frpc:v0.70.0`.

## Load-bearing decision: no VPS replacement
frps installs over **SSH** (`command.remote`, idempotent) rather than cloud-init, and the server's `userData` is `ignoreChanges`'d. A tunnel swap must **not** replace the live VPS — that would rotate the public IP and destroy the on-box REALITY private key (breaking every client profile). The install also `systemctl disable --now rathole`.

## How to verify
1. **`pulumi preview` first** — confirm the `gateway` hcloud.Server shows **no replacement** (only the new `frp-install`/`frp-config` commands + the frpc Deployment replacing the rathole one). This is the one thing to eyeball before deploying.
2. Deploy. Home services (`blit.cc`, Navidrome, files) still served → reverse tunnel works.
3. Pick `exit-oldboy`, `curl ifconfig.me` → home IP (TCP path).
4. Hit a QUIC/HTTP3 site through the exit → UDP now traverses (was impossible on rathole).

## Runtime-untested (hence draft)
Config correctness (frps.toml/frpc.toml schema, the snowdreamtech entrypoint reading `/etc/frp/frpc.toml`) and the UDP-over-frp exit path can't be checked without a deploy. Shell escaping in the frps installer was rendered + `bash -n`'d. Typecheck/lint/tests green.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
