import { describe, test, expect } from 'vitest';
import { coupon } from '../src/cart.js';

describe('coupon', () => {
  test('WELCOME10 takes 10% off', () => expect(coupon(5000, 'WELCOME10')).toBe(4500));
  test('WELCOME10 rounds the saving down to the cent', () => expect(coupon(999, 'WELCOME10')).toBe(900));
  test('WELCOME10 takes the full 20.00 at exactly 200.00', () => expect(coupon(20000, 'WELCOME10')).toBe(18000));
  test('WELCOME10 is capped at 20.00', () => expect(coupon(30000, 'WELCOME10')).toBe(28000));
  test('SAVE5 takes 5.00 off from 25.00', () => expect(coupon(2500, 'SAVE5')).toBe(2000));
  test('SAVE5 does nothing below 25.00', () => expect(coupon(2499, 'SAVE5')).toBe(2499));
  test('an unknown code changes nothing', () => expect(coupon(1000, 'NOPE')).toBe(1000));
  test('no code changes nothing', () => expect(coupon(1000)).toBe(1000));
});
