# fix(misc): stop decoding allowed repeat freqs at a zero sentinel

## What

`decodeAllowedRepeatFreq` walked the whole `RESP_ALLOWED_REPEAT_FREQ` frame in 8-byte steps and emitted every pair it found. If a frame ever carried zero-filled entries, we surfaced spurious `{ lowerKhz: 0, upperKhz: 0 }` ranges.

meshcore_py treats a pair where either bound is zero as an end-of-list sentinel and stops parsing there (`ALLOWED_REPEAT_FREQ` branch of `reader.py`):

```python
if min == 0 or max == 0:
    cont = False
else:
    freqs.append({"min": min, "max": max})
```

This matches that. The existing tolerance for a trailing partial (<8 byte) chunk is unchanged.

## Evidence: the firmware does not pad

To be straight about the evidence — I checked the `CMD_GET_ALLOWED_REPEAT_FREQ` handler in `examples/companion_radio/MyMesh.cpp` in the MeshCore firmware, and **it emits an exact count with no padding**:

```cpp
} else if (cmd_frame[0] == CMD_GET_ALLOWED_REPEAT_FREQ) {
  int i = 0;
  out_frame[i++] = RESP_ALLOWED_REPEAT_FREQ;
  for (int k = 0; k < sizeof(repeat_freq_ranges)/sizeof(repeat_freq_ranges[0]) && i + 8 < sizeof(out_frame); k++) {
    auto r = &repeat_freq_ranges[k];
    memcpy(&out_frame[i], &r->lower_freq, 4); i += 4;
    memcpy(&out_frame[i], &r->upper_freq, 4); i += 4;
  }
  _serial->writeFrame(out_frame, i);
}
```

It writes one pair per entry in `repeat_freq_ranges[]` and calls `writeFrame` with the exact byte count, so there is no zero padding to trip over. The default table (`{433000, 433000}`, `{869495, 869495}`, `{918000, 918000}`) and the `ALLOWED_REPEAT_FREQ_RANGE` override both feed that same loop.

So this is **defensive parsing, not a bug anyone has hit**. The value is behavioral parity with meshcore_py, and robustness against a firmware fork or future build that does pad — a zero-kHz "allowed range" is never meaningful output either way.

## Tests

Added to `tests/features/misc.test.ts`:
- the firmware's default three-range table decodes fully
- a frame padded with an all-zero pair stops at the padding
- a pair with only one bound zero acts as the sentinel and drops everything after it
- a frame ending in a 3-byte partial chunk still yields its complete ranges

`pnpm test` (759 tests), `pnpm lint`, and `pnpm typecheck` all pass.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
