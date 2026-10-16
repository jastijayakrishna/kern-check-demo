# Add comprehensive Jest unit tests for cryptoformat module

# Add comprehensive Jest unit tests for cryptoformat module (rebased for Jest v30)

## Summary
This PR adds 317 lines of comprehensive Jest unit tests to `src/test.js`, expanding test coverage from basic functionality to extensive edge cases, error conditions, and boundary testing for all exported functions (`formatCurrency`, `isCrypto`, `clearCache`) and internal helper functions.

The PR has been rebased from master to include the Jest v30.1.1 upgrade (previously v24.9.0). All 72 tests pass with the new Jest version.

**Key test additions:**
- **Internal helper function testing**: `isBTCETH`, `IntlNumberFormatSupported`, fallback behavior
- **Edge case coverage**: Invalid inputs (null, undefined, NaN, Infinity), boundary values, locale-specific cases
- **Error handling**: Unsupported currencies, invalid locales, global state corruption scenarios
- **Caching mechanism**: Verification that `clearCache()` works and formatters are reused appropriately  
- **Symbol overrides**: Currency symbol customization functionality
- **Complex parameters**: Decimal places, significant figures, trailing zeroes handling
- **Fallback scenarios**: Behavior when `Intl.NumberFormat` is unavailable

## Review & Testing Checklist for Human
- [ ] **Verify test expectations are correct** - Some test expectations were adjusted during development, manually verify key behaviors match actual library output
- [ ] **Test Jest v30 compatibility** - Run tests in your local environment and CI to ensure the major Jest upgrade doesn't introduce issues
- [ ] **Manual spot-check edge cases** - Try some of the edge cases manually (very small numbers, invalid inputs, etc.) to verify test expectations
- [ ] **Review global state handling** - Tests modify `global.Intl` - ensure this doesn't cause issues in your test environment

### Notes
- All 72 tests pass locally with Jest v30.1.1
- No breaking changes were required for Jest v30 compatibility
- Tests use existing babel configuration and Jest defaults (no jest.config file needed)
- Link to Devin run: https://app.devin.ai/sessions/f64ceefe350e4a42bf304bfacf32c3f7
- Originally requested by: cedric@coingecko.com, rebase requested by: jason.julian
