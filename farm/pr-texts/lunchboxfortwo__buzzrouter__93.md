# Give every hub community its own channel on our relay

Every connected community now gets its own `channel-<community-id>` on
`relay.buzzrouter.com` instead of sharing `general` — for future connections and
retroactively for `buzz.trustysquire.ai`.

The design was written first and is below. It is coherent, but it starts with a
correction to the premise, so read §0.

## 0. One correction to the premise

"Today every connected community's traffic lands in `general`" is true today and
will stop being true the moment a third community connects — and it is worth
being precise about why, because it decides what the new channels carry.

Routing is addressed (`src/shared-channels/addressing.ts`). A message only
leaves its community when it opens with `@[slug]`, and it is delivered to that
one community's own bound channel on its own relay. So peer-to-peer traffic
(`@[a]` → `@[b]`) never touches `relay.buzzrouter.com` at all. What actually
lands in `general` is only the traffic addressed to **BuzzRouter itself**. That
looks like "everything" right now because trustysquire is the only peer, so
BuzzRouter is the only address that resolves.

Nothing in this PR changes that, and nothing should: mirroring every peer's
cross-community traffic onto our relay would be a privacy expansion nobody asked
for.

## 1. What a dedicated channel actually carries

`channel-<X>` on our relay is **BuzzRouter's inbox for community X**. It carries:

- inbound: messages X's members address to `@[buzzrouter]`, which used to land
  in `general`;
- outbound: what our staff type in that channel addressed back to `@[x]`.

It does not carry X's traffic to any other community. So the value is real but
specific: it is a per-tenant support/collaboration channel, and it is exactly the
pain that shows up at three peers — today two peers' conversations interleave in
one `general` and every reply has to re-address the community it is answering.

**`general` is still needed, in a reduced role.** It stays BuzzRouter's ordinary
hub endpoint and remains the fallback destination for a peer that has no
dedicated channel yet (a provisioning failure, or the ~10 minute window after a
new community connects). It also still *sends* to anyone, so a reply typed there
is never silently dropped. Once a peer has its own channel, `general` stops
receiving from that peer.

One thing this does **not** do: `@[buzzrouter]` addressing stays required in the
dedicated channel even though the channel already implies the destination.
Making a dedicated channel's unaddressed messages route to its peer is a change
to the addressing contract, not to this feature, so it is deliberately left out.

## 2. Schema change

Confirmed against the live schema first:

```
"shared_channel_endpoints_shared_channel_id_community_id_key" UNIQUE CONSTRAINT, btree (shared_channel_id, community_id)
```

So yes — BuzzRouter, being one community, could hold exactly one endpoint on the
one hub row, and therefore exactly one channel. One-channel-per-peer is
impossible without changing this.

`migrations/20260804T0200_hub_dedicated_peer_channels.sql` adds
`dedicated_to_community_id` (nullable): the peer an endpoint exists to talk to.
NULL is the ordinary endpoint every participant already has. The old uniqueness
is preserved as a partial index over exactly those rows, plus a second partial
index giving at most one dedicated endpoint per (owner, peer). No existing row
changes and the hub is still one `shared_channels` row.

Routing then follows from the column, in `ingestBridgeMessage`'s destination
query — three predicates:

1. a dedicated endpoint exchanges with its one peer only, in both directions;
2. same rule applied to the source side, so a reply typed in `channel-<X>`
   cannot be addressed out to `@[y]`;
3. an ordinary endpoint yields to a dedicated one for that source.

(1) is not cosmetic. Without it, a message addressed to BuzzRouter matches *every*
BuzzRouter endpoint and gets copied into every other peer's dedicated channel —
a cross-community leak. Without (3) i
