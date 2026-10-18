# fix: decode repeater status against the real RepeaterStats struct

`decodeStatusFields` (`src/protocol/repeater.ts`) decoded the `PUSH_STATUS_RESPONSE` payload against a layout that does not exist. Every field except battery-on-an-idle-repeater was garbage.

## Wrong vs. right

The firmware `memcpy`s `struct RepeaterStats` straight onto the wire — packed, naturally aligned, little-endian, no padding ([`examples/simple_repeater/MyMesh.h:44`](https://github.com/ripplebiz/MeshCore/blob/main/examples/simple_repeater/MyMesh.h)):

```c
struct RepeaterStats {
  uint16_t batt_milli_volts;
  uint16_t curr_tx_queue_len;
  int16_t  noise_floor;
  int16_t  last_rssi;
  uint32_t n_packets_recv;
  uint32_t n_packets_sent;
  uint32_t total_air_time_secs;
  uint32_t total_up_time_secs;
  uint32_t n_sent_flood, n_sent_direct;
  uint32_t n_recv_flood, n_recv_direct;
  uint16_t err_events;                // was 'n_full_events'
  int16_t  last_snr;   // x 4
  uint16_t n_direct_dups, n_flood_dups;
  uint32_t total_rx_air_time_secs;
  uint32_t n_recv_errors;
};
```

| Offset | Was (wrong) | Is (firmware) |
| --- | --- | --- |
| 0 | `battery` u32 | `batt_milli_volts` **u16** |
| 2 | — | `curr_tx_queue_len` **u16** |
| 4 | `tx_queue` u32 | `noise_floor` **i16** |
| 6 | — | `last_rssi` **i16** |
| 8 | `free_queue` u32 — **no such field** | `n_packets_recv` u32 |
| 12 | `last_rssi` i16 | `n_packets_sent` u32 |
| 14 | `n_packets_rx` u32 | — |
| 16 | — | `total_air_time_secs` u32 |
| 20 | — | `total_up_time_secs` u32 |
| … | everything shifted by 2–6 bytes | … |
| 40 | — | `err_events` u16 |
| 42 | — | `last_snr` i16 (÷4) |
| 44/46 | `n_*_dups` as **u8** | `n_direct_dups` / `n_flood_dups` **u16** |
| 48 | — | `total_rx_air_time_secs` u32 — **was missing** |
| 52 | — | `n_recv_errors` u32 — **was missing** |

The widths were wrong from byte 2 onward, `free_queue` was invented, and `noise_floor`, `total_rx_air_time_secs` and `n_recv_errors` were absent entirely. Both official libraries agree with the firmware and disagreed with us — [`meshcore_py`](https://github.com/fdlamotte/meshcore_py) `parse_status()` and [`meshcore.js`](https://github.com/liamcottle/meshcore.js) `getStatus()`, which quotes the struct field by field.

## Why battery looked fine

Reading `[0..3]` as a u32 yields `batt_mv | (curr_tx_queue_len << 16)`. On an idle repeater the queue is `0`, so the high half is zero and the u32 read happens to equal `batt_mv` — the one case anybody checks against a working radio. With 3 packets queued, a 4.02 V battery reports as **200.628 V**. Every field after it was read from the wrong offset and was wrong regardless of queue depth.

## The old test encoded the bug

`tests/repeater.test.ts` built its fixture to *our* wrong layout (`writeUInt32LE(4020, 0)` / `writeUInt32LE(2, 4)`), so it asserted that the broken decoder decoded the broken fixture. It confirmed the bug rather than catching it — and, because it used a 2-packet queue in a `u32` it wrote itself, it never tripped the battery corruption either.

It now serialises the real firmware struct and asserts all 18 decoded fields, with cases for:

- a **non-zero `curr_tx_queue_len`** — the case that exposes the battery error;
- an idle repeater (queue 0), so the previously-passing case stays covered;
- a **legacy 52-byte frame** (pre-firmware-v1.12.0, no `n_recv_errors`);
- a truncated payload, which degrades to fewer fields rather than throwing;
- `n_*_dups` above 255, proving they are u16 and no longer wrap.

Verified the new assertions fail against the old decoder (5 failures, including `expected 200.628 to be 4.02`). The `tests/integration/inbound/repeater-admin.test.ts` fixture built the same wrong layout and is corrected too.

## Field-name changes on the `repeaterStatus` event

The `StatusField { name, value, unit? }` shape and the `formatUptime` treatment of uptime are unchanged. Names:

- **Added:** `Noise floor` (dBm), `RX airtime` (s), `RX errors`.
- **Renamed:** `Airtime` → `TX airtime` (it is `total_air_time_secs`; ambiguous now that `RX airtime` exists);
