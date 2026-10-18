# SIG-86: read Kalshi's dollar-denominated price fields (fix blank slate prices)

## Symptom
Every slate row showed the model percentage but `—` for **price** and **edge**, even for games Kalshi is actively quoting (SF@LAR tonight, Puka Nacua 50+ rec yds trading 83¢/18¢).

## Root cause
Kalshi migrated the market payload to **dollar-denominated fields**. The market object no longer carries `yes_bid`/`yes_ask`/`no_bid`/`no_ask` (integer cents) — it now returns `yes_bid_dollars`/`yes_ask_dollars`/`no_bid_dollars`/`no_ask_dollars` as dollar strings (`"0.83"` = 83¢), plus `*_fp` / `*_dollars` for size, volume, last price, and the orderbook.

`sync.ts:296-299` read the old cent fields → `undefined` → `toCents` → `null`, so **every `PriceObservation` was written all-null** → the slate renders `—`. The sync still reported success (markets discovered, contracts upserted), which hid it. (This also explains my earlier wrong "empty books" read — I was checking the renamed fields.)

## Fix
- `KalshiMarket`: add the `*_dollars` fields; mark the integer-cent fields legacy.
- `sync.ts`: `dollarsToCents()` (dollar string/number → 1–99 cents, else null) and `marketSideCents()` (prefer `*_dollars`, fall back to legacy cents); read the book via `marketSideCents`.
- `sync.test.ts`: unit tests for both helpers.

The list endpoint carries `*_dollars`, so no extra per-market orderbook call is needed for the slate, and `yes_ask_dollars` maps directly to the YES ask (no inversion on the list path).

## Verification
- `tsc`, `eslint`, `prettier` clean; **60 kalshi unit tests pass**.
- **Live check** against Kalshi's public API: `KXNFLRECYDS-26SEP10SFLAR-LARPNACUA12-50` → `yes_ask_dollars "0.8300" → 83¢`, `no_ask_dollars "0.1800" → 18¢`, matching Kalshi's UI. Prices will populate on the next price-refresh once deployed.

## Out of scope → SIG-87
`getOrderbookTop` (paper execution) reads the old `orderbook.yes`/`orderbook.no` cent arrays and is broken by the same migration; and the settlement read (`result`/`settled_time`) may be too. Admin/grading paths, not the slate — tracked separately.

Closes SIG-86.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
