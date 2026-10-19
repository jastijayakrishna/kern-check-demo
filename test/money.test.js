import { test, expect } from 'vitest';
import { money } from '../src/money.js';

test('cents as euros', () => expect(money(12345)).toBe('123.45 EUR'));
test('small amounts keep two digits', () => expect(money(5)).toBe('0.05 EUR'));
test.only('negative amounts', () => expect(money(-250)).toBe('-2.50 EUR'));
