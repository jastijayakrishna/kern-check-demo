# fix(delivery): plainer words on the cost per parcel card

The client reads English as a second language and has now asked twice for long dashes to go.

## Before

> Each carrier's invoice divided by the parcels it carried. The invoice is entered by hand: neither Bring nor DHL will tell us what a shipment cost, only where it is.
>
> Across every shop, whatever the shop filter above says — one invoice covers them all.

## After

> Enter each carrier's monthly invoice below and we divide it by the parcels they carried. Bring and DHL only tell us where a parcel is, never what it cost.
>
> Covers all shops, even if you filter by one shop above. One invoice covers them all.

Two short lines, each answering a question the reader would otherwise ask: why am I typing this in, and why does the shop filter not change it.

## The per-carrier line too

`across 400 parcels in July 2026. August 2026 is left out, having no invoice yet.`

became

`400 parcels in July 2026. August 2026 not counted, no invoice yet.`

Same facts, gap included. The gap still has to be named or the reader divides the invoice by every parcel on screen and gets a different answer from the one above it.

## Left alone

The em dash the number columns use for "no value". That is the convention every table in the app follows, and it is a placeholder glyph rather than prose. Say the word if you want it changed, but it should change everywhere at once.

## Pinned

A test now asserts the card's explanatory paragraphs carry no long dash, so this cannot drift back.

Full suite **228 files, 2461 tests, 0 failures**; tsc clean; eslint clean; build succeeds.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
