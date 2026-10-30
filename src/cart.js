// The price of a basket, in cents: each item's price times its quantity.
export function total(items) {
  let sum = 0;
  for (const item of items) {
    if (!Number.isInteger(item.price) || item.price < 0) throw new Error(`Bad price: ${item.price}`);
    if (!Number.isInteger(item.qty) || item.qty < 1) throw new Error(`Bad quantity: ${item.qty}`);
    sum += item.price * item.qty;
  }
  return sum;
}

// Baskets of 100.00 or more get 10% off, rounded down to the cent.
export function discount(cents) {
  return cents >= 10000 ? Math.floor(cents * 0.9) : cents;
}

// Shipping costs 4.99, and is free from 60.00 (after the discount).
export function shipping(cents) {
  return cents >= 6000 ? 0 : 499;
}

// What the customer pays.
export function checkout(items) {
  const after = discount(total(items));
  return after + shipping(after);
}
