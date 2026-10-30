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
  test('free from 60.00', () => expect(shipping(6000)).toBe(0));
  test('4.99 below 60.00', () => expect(shipping(5999)).toBe(499));
});

test('checkout: discount first, then shipping', () => expect(checkout([{ price: 5000, qty: 2 }])).toBe(9000));
