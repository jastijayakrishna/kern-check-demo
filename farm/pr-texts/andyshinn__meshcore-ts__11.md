# fix: carry rssi from the V3 signal header onto inbound Messages

## Problem

Inbound messages carried SNR but not RSSI, even though the radio sends both in the same frame header:

```
[code][snr*4 i8][rssi i8][1B rsv][mesh…]
          byte 1   byte 2
```

`decodeChannelMsgV3` and `decodeContactMsgV3` both read `frame.readInt8(1)` for SNR and then jumped straight to byte 4 — the RSSI byte was never read. The raw-data and control-data parsers *do* read it (`frame.readInt8(2)`), which is why RSSI reached `rawPacket` events but never a `Message`.

## Change

- Read `rssi: frame.readInt8(2)` in both V3 decoders.
- Include it in `meta` at the two `messageUpserted` emit sites, alongside `snr`.
- Fix the frame-layout comments, which described bytes 2–3 as "2B reserved".

`MessageMeta.rssi?: number` already existed, so no type change was needed.

## V1 decoders left alone

`decodeChannelMsgV1` / `decodeContactMsgV1` are untouched — those frames have no signal header at all, which is why they hardcode `snrDb: 0`; there is no RSSI byte to read either.

That drove two small design choices:

- `rssi` is **optional** on `ChannelMsgV3` / `ContactMsgV3`, so the V1 decoders compile unchanged rather than being forced to fabricate a value.
- It is spread **conditionally** into `meta` (`...(parsed.rssi !== undefined ? { rssi: parsed.rssi } : {})`) rather than assigned as a possibly-`undefined` key. This matters for channel messages: `upsertMessage` merges re-receipts of the same flood message with `{...existing.meta, ...message.meta}`, so omitting the key keeps a V1 re-receipt from wiping an RSSI that an earlier V3 reception already merged onto that row.

## Note

Mesh observations (`MeshObservations`) carry only `finalSnr`, no RSSI — so unlike SNR, there is no fresher mesh-side RSSI for the channel handler to prefer over the firmware-quoted one. The header value is used as-is.

## Tests

Written first, and confirmed failing against the old decoders (`expected undefined to be -95`) before the fix landed:

- `tests/features/channelMessages.test.ts` — `decodeChannelMsgV3` reads the RSSI byte without disturbing the SNR read.
- `tests/features/directMessages.test.ts` — same for `decodeContactMsgV3`.
- `tests/integration/inbound/message-upserted.test.ts` — a decoded channel message and a decoded DM both carry `meta.rssi` alongside `meta.snr`, end-to-end through the session.

Full suite: 756 tests across 98 files pass; `pnpm typecheck` and `pnpm lint` clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
