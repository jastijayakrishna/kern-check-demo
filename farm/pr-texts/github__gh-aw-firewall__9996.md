# Make alias resolution price-aware and support long-context pricing

With the AI-credit guard active, aliases could select newer unpriced models and cause detection requests to be rejected. Pricing overlays and shared catalogs also lacked long-context tiers, undercounting Haiku 5.5 usage above 100k prompt tokens.

- **Alias resolution:** Skip unpriced candidates at each alias level, log the skipped model, and retain the existing highest-version fallback when no candidate has a price. Guard-off and default-pricing behavior is unchanged.
- **Tiered pricing:** Add optional long-context tiers to operator overlays and shared catalog entries. Above the configured threshold, all token categories use the tier’s rates; malformed tiers invalidate their entry.
- **Haiku 5.5:** Add curated base and long-context prices, including the 100k-token threshold.

Example shared-catalog entry (rates are USD per million tokens):

```yaml
longContext:
  threshold: 100000
  input: 0.5
  cachedInput: 0.05
  cacheWrite: 0.625
  output: 2.5
  reasoning: 2.5
```

<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes #9994
