# kern-check-demo

A small shop library (a basket's total, a discount, shipping, money for people to read) with its tests.

It shows [Kern](https://github.com/jastijayakrishna/Kerner)'s receipt on real pull requests: every pull request here gets one
comment that says what the change does when it runs, and one status, `Kern`. The whole setup is one file:
[.github/workflows/kern.yml](.github/workflows/kern.yml).

## Use

```js
import { checkout } from './src/cart.js';
import { money } from './src/money.js';

money(checkout([{ price: 4000, qty: 3 }])); // "108.00 EUR": 10% off from 100.00, and free shipping from 50.00
```
