# feat(exits): selectable egress exit nodes (rathole + ss-rust)

**Draft** — logic is verified (typecheck/lint/schema/`buildProfile` structure), but the runtime path (rathole exit tunnel, ss egress IP, the detour→loopback chain) needs a deploy + your test. First slice of the exit-nodes spec: **single gateway + one home k8s exit**, written for the general gateways × exits cross-product.

## What

A second, independent axis on top of the entry gateways. The client picks **entry** (which gateway) *and* **egress** (direct at the gateway, or via an exit node that NATs out its own IP — e.g. the home residential link).

An **exit** = substrate-agnostic `rathole client + ss-rust`: a k8s Deployment now (`modules/exit.ts`), a cloud-init VPS later. Add one with:
```yaml
jaritanet:exits:
  - name: home
    port: 9000
```

## How (the load-bearing bit)

Reached through the **existing rathole tunnel, not the tailnet**. Each exit's ss port is surfaced on **every gateway's loopback** `127.0.0.1:<port>` via a rathole service entry (same pattern as the Reality decoy `dest`). The client's `exit-<name>` outbound is Shadowsocks to `127.0.0.1:<port>` with `detour: entry-select` — a detour resolves the inner address at the *gateway* end, so `127.0.0.1:<port>` hits that exit's rathole loopback there. **The port is one declared value** (gateway bind = rathole client target = client outbound), so it's identical across gateways — the invariant that lets one exit outbound work via any entry.

- `buildProfile` now emits `entry-select` (gateway/transport) + `exit-select` (`[direct, exit-…]`); `route.final → exit-select`; tailnet `100.x` + DNS stay on `entry-select` (egress at the gateway, never via an exit).
- `gateway.ts` rathole **server** gains `[server.services.exit-*]` loopback binds; `ingress.ts` rathole **client** gains `[client.services.exit-*] → ss service`, with a config-hash annotation so the client pod rolls when exits change.
- No kernel forwarding (connection-level only); pod egress SNATs to the node IP.
- ss password: one Pulumi secret → ss ConfigMap + client outbound (no drift).

## Verified

typecheck, lint 0/0, schema regen, and `buildProfile` structure-tested with and without an exit (correct `entry-select`/`exit-select`/`exit-<name>` SS `127.0.0.1:<port>` detour, `final → exit-select`, tailnet on `entry-select`; backward-compatible when no exits).

## Acceptance checks to run on deploy (why it's draft)

- **Egress IP** — `curl ifconfig.me` from the exit pod returns oldboy's **home ISP IP** (confirm microk8s CNI SNATs pod egress to the node IP).
- **Selectors compose** — pick entry ∈ gateways and exit ∈ {direct, home} independently; traffic enters via the chosen gateway and egresses at the chosen exit.
- **Reality/hy2 entry unchanged**; **idempotent** re-`up` is a no-op.

## Deferred (from the spec, deliberately)
- Capability-URL **rotation** — conflicts with sing-box auto-update (rotating the URL strands the device on the old one). Kept the static slug + in-place update. Flagged for discussion.
- VPS-substrate exits (cloud-init) — same `exits` entry, different substrate; k8s first.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
