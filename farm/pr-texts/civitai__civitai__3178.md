# feat(trpc): client writes devalue inputs (Phase 3 safe slice; server union-reads)

## What

Flip the **CLIENT** tRPC transformer's `input.serialize` from superjson to devalue (`writeSerialize`) so the browser **writes request inputs as devalue**. This is the safe, ungated slice of Phase 3 of the superjson → devalue transformer migration.

Also switch the `isTooLargeToBatch` URL-budget sizer in `src/utils/trpc.ts` to size with `writeSerialize` (devalue) instead of `superjson.serialize`, so the GET-vs-POST batch decision matches what the client now actually writes.

## Why this is safe (no drain gate, cannot break stale clients)

The server's `input.deserialize` is the format-sniffing **UNION** reader (`unionDeserialize`). It decodes **devalue inputs from updated clients AND superjson inputs from stale clients** that have not yet loaded the new bundle — the two serializers emit disjoint JS types (devalue → string, superjson → object), so a `typeof` sniff routes each to the right decoder. Both formats round-trip, so:

- **No env gate** is needed — the read side already accepts either format.
- **No coordinated rollout** — a browser mid-bundle-swap that still writes superjson is read exactly the same as one that has updated to devalue.

## Benefit

- The server pays the cheaper `devalue.parse` on inputs as clients update, and request bodies / GET URLs get slightly smaller.
- It quietly pre-drains toward a hypothetical future superjson-drop (Phase 3b), which this PR **deliberately does NOT do**.

## Explicitly NOT changed

- The **server read path** (the union sniffer) is untouched.
- `clientTransformer.output.deserialize` **stays the UNION reader** — the client still decodes BOTH a superjson response and a devalue response.
- **superjson is NOT dropped** anywhere; it stays available for the union read path and for rollback.
- No new env gate is added; no server write path changed.

## Tests

Extended `trpc-union-transformer.test.ts`:
- asserts the client now writes a **devalue STRING** on inputs (not a superjson object),
- asserts the **server union read decodes it back** for the rich input types tRPC inputs carry (Date, top-level BigInt cursor, undefined, nested arrays/objects),
- asserts a **stale superjson-written input is still server-readable** (the ungated safety property),
- confirms the client **output read stays the union**.

The existing strict non-POJO devalue write-guard test is unchanged. `tsc --noEmit` clean on the touched files; full transformer suite passes (19 tests).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

