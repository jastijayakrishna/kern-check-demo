import { describe, test, expect } from 'vitest';
import { total, discount, shipping, checkout } from '../src/cart.js';

describe('total', () => {
  test('adds price times quantity', () => expect(total([{ price: 250, qty: 2 }, { price: 99, qty: 1 }])).toBe(599));
  test('an empty basket costs nothing', () => expect(total([])).toBe(0));
  test('refuses a negative price', () => expect(() => total([{ price: -1, qty: 1 }])).toThrow('Bad price'));
  test('refuses a zero quantity', () => expect(() => total([{ price: 100, qty: 0 }])).toThrow('Bad quantity'));
});

describe('discount', () => {
  test('10% off from 100.00', () => expect(discount(10000)).toBe(9000));
  test('nothing off below 100.00', () => expect(discount(9999)).toBe(9999));
});

describe('shipping', () => {
  test('free from 50.00', () => expect(shipping(5000)).toBe(0));
  test('4.99 below 50.00', () => expect(shipping(4999)).toBe(499));
});

test('checkout: discount first, then shipping', () => expect(checkout([{ price: 5000, qty: 2 }])).toBe(9000));

describe('checkout with a coupon', () => {
  test('SAVE5 comes off after the basket discount: 100.00 -> 90.00 -> 85.00, free shipping', () =>
    expect(checkout([{ price: 5000, qty: 2 }], 'SAVE5')).toBe(8500));
  test('WELCOME10 comes off before shipping is decided: 52.00 -> 46.80 + 4.99', () =>
    expect(checkout([{ price: 5200, qty: 1 }], 'WELCOME10')).toBe(5179));
  test('WELCOME10 is capped at 20.00: 300.00 -> 270.00 -> 250.00', () =>
    expect(checkout([{ price: 30000, qty: 1 }], 'WELCOME10')).toBe(25000));
  test('SAVE5 applies at exactly 25.00: 20.00 + 4.99', () =>
    expect(checkout([{ price: 2500, qty: 1 }], 'SAVE5')).toBe(2499));
  test('SAVE5 does nothing below 25.00', () => expect(checkout([{ price: 2499, qty: 1 }], 'SAVE5')).toBe(2998));
  test('an unknown code changes nothing', () => expect(checkout([{ price: 1000, qty: 1 }], 'NOPE')).toBe(1499));
  test('no code changes nothing', () => expect(checkout([{ price: 1000, qty: 1 }])).toBe(1499));
});
