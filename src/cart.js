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

// A coupon code takes a further amount off: WELCOME10 gives 10%, capped at 20.00; SAVE5 gives 5.00 on baskets of 25.00 or more.
export function coupon(cents, code) {
  if (code === 'WELCOME10') return cents - Math.min(Math.floor(cents * 0.1), 2000);
  if (code === 'SAVE5' && cents >= 2500) return cents - 500;
  return cents;
}

// Shipping costs 4.99, and is free from 50.00 (after the discount).
export function shipping(cents) {
  return cents >= 5000 ? 0 : 499;
}

// What the customer pays.
export function checkout(items, code) {
  const after = coupon(discount(total(items)), code);
  return after + shipping(after);
}
