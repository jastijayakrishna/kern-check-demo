// The price of a basket, in cents: each item's price times its quantity.
export function total(items) {
  let cents = 0;
  for (const line of items) {
    if (!Number.isInteger(line.price) || line.price < 0) throw new Error(`Bad price: ${line.price}`);
    if (!Number.isInteger(line.qty) || line.qty < 1) throw new Error(`Bad quantity: ${line.qty}`);
    cents += line.price * line.qty;
  }
  return cents;
}

// Baskets of 100.00 or more get 10% off, rounded down to the cent.
export function discount(cents) {
  return cents >= 10000 ? Math.floor(cents * 0.9) : cents;
}

// Shipping costs 4.99, and is free from 50.00 (after the discount).
export function shipping(cents) {
  return cents >= 5000 ? 0 : 499;
}

// What the customer pays.
export function checkout(items) {
  const after = discount(total(items));
  return after + shipping(after);
}
