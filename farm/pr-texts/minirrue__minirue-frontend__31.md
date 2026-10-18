# fix(track): the tracking page says something true (#60)

The customer-facing half of minirrue/minirue-backend#60.

## What it said

The confirmation page links every customer to `/orders/{id}/track`. That page's carrier view is for a future that has not arrived — MiniRue has no shipping-service integration, the dashboard's own panel says so with every control disabled, so no `fulfillment_shipments` row is ever created.

With no shipment it rendered one sentence, for every order, forever:

> Your order has been received and is being prepared for shipment. Tracking information will appear here once your order ships.

True on the day the order is placed. **A lie once it has been delivered**, and still shown to somebody whose order was cancelled a week ago.

## Correcting my own issue text

I wrote in #60 that the link *"can never show anything"*, and that overstated it — the page did render a graceful empty state. The defect is narrower and more specific: **the empty state was unconditional**, so it went on promising a parcel to people whose order had already arrived or been refunded.

## What it says now

The order's **own status**, which was already fetched on that page and used for nothing but printing the order number:

```
● Confirmed        We have your order and your payment.
● Being prepared   Your order is being packed.
○ On its way
○ Delivered
```

Cancelled and refunded orders are handled *before* the list is reached, and a missing order says so rather than implying a parcel exists. Those two were the worst of it — "being prepared for shipment" on a refunded order.

When a carrier is signed, the shipment view above takes over and this becomes the fallback it was always meant to be. **Nothing about the carrier path changed.**

## Accessibility

- the current step carries `aria-current="step"`, and the list is labelled — the page exists to answer *"where is my order"*, and a screen reader has to be able to answer it
- the reached dot **fills** rather than only tinting: a shape change, so it survives a greyscale display and any colour-vision difference

The fill is asserted in the CSS specifically, because that is where it would be lost — a later "simplify the palette" pass that dropped the background would leave two greys and no other difference.

## Tests — 10

They read the source rather than rendering. The page is an async server component awaiting two API calls; rendering it means mocking `next/headers`, the fetch client and the auth cookie to assert four `<li>` elements — machinery that would then need maintaining, to check something structural.

The file says plainly that this is the weaker option and what it can still catch: the page going back to a hardcoded sentence, or losing the accessible state.

One of them checks the old copy is gone from the **code** while still present in the **comment** that explains why it went — the reason it changed is worth keeping, so "is the string in the file" is the wrong question.

632 tests passing. `tsc` and `next build` clean.

Ships `minirue-frontend@0.52.0`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01B6eD4Vf5YMMKKBaxyL2w5q
