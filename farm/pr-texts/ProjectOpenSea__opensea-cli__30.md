# feat: add TOON output format for LLM-efficient data serialization

# feat: add TOON output format for LLM-efficient data serialization

## Summary

Adds [TOON (Token-Oriented Object Notation)](https://github.com/toon-format/toon) as a third `--format` option alongside `json` and `table`. TOON is a compact, human-readable encoding of JSON that uses ~40% fewer tokens, making it ideal for piping CLI output into AI agent context windows.

The encoder is implemented from scratch in `src/toon.ts` following the [TOON v3.0 spec](https://github.com/toon-format/spec/blob/main/SPEC.md) — no external dependency added. It handles:
- Primitive values with spec-compliant quoting/escaping (§7)
- YAML-like indented objects (§8)
- Inline primitive arrays with `[N]:` headers (§9.1)
- Tabular arrays of uniform objects with `[N]{fields}:` headers (§9.3)
- Expanded list format for mixed/non-uniform arrays (§9.4)
- Objects as list items (§10)

**Usage:** `opensea collections list --format toon`

Changes:
- New `src/toon.ts` — standalone TOON encoder (~338 lines)
- `OutputFormat` type (`"json" | "table" | "toon"`) replaces inline string unions across all command files
- `formatToon` and `OutputFormat` exported from SDK index for programmatic use
- 30 new tests in `test/toon.test.ts` covering primitives, objects, all array forms, the spec's hikes example, and `formatOutput` integration
- README updated with TOON format documentation, example output, and SDK usage snippet

**Confidence: 🟡 MEDIUM** — Encoder follows the spec and passes unit tests including the canonical hikes example, but has not been tested against real OpenSea API response shapes (deeply nested NFT metadata, protocol_data, etc.).

## Review & Testing Checklist for Human

- [ ] **Verify TOON output with real API responses** — Run a few real commands like `opensea collections get boredapeyachtclub --format toon` and `opensea tokens trending --format toon` to confirm the output is useful and correctly structured. Nested API responses (listings with `protocol_data`, NFTs with `traits`) are the most likely to surface encoding issues.
- [ ] **Audit quoting rules in `needsQuoting()`** against [TOON spec §7.2](https://github.com/toon-format/spec/blob/main/SPEC.md#72-quoting-rules-for-string-values-encoding) — especially for values containing URLs (colons), descriptions with commas, and wallet addresses starting with `0x` (leading-zero check).
- [ ] **Review expanded list encoding** (`encodeExpandedList` + bottom half of `encodeArray`) — these handle the complex case of non-uniform arrays and have significant code overlap. Check correctness for objects-as-list-items per §9.4/§10 and consider whether the duplication should be refactored.
- [ ] **Verify README example** — The example TOON output in the README uses synthetic field names (`market_cap`, `price_usd`). Confirm these roughly match actual `/api/v2/tokens/trending` response shapes or update to match reality.

### Notes
- Only encoding (JSON→TOON) is implemented; decoding is not needed since this is an output format.
- The delimiter is hardcoded to comma. Tab/pipe delimiters from the spec are not exposed — could be a future enhancement if needed.

Link to Devin run: https://app.devin.ai/sessions/73e236d755164371a78158c3de534841
Requested by: @CodySearsOS
