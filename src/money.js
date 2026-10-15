// Cents as money for people to read: 12345 -> "123.45 EUR".
export function money(cents, currency = 'EUR') {
  const sign = cents < 0 ? '-' : '';
  const abs = Math.abs(cents);
  return `${sign}${Math.floor(abs / 100)}.${String(abs % 100).padStart(2, '0')} ${currency}`;
}
