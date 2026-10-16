# Replace node-fetch with Node.js built-in fetch

# Replace node-fetch with Node.js built-in fetch

## Summary
This PR replaces the `node-fetch` dependency with Node.js built-in `fetch` API to reduce external dependencies and use native Node.js functionality.

## Changes
- **Removed** `node-fetch` dependency from `package.json`
- **Updated** `tc39-proposals.js` to use built-in `fetch` instead of importing `node-fetch`
- **Updated** `package-lock.json` by running `npm install`

## Technical Details
- Node.js built-in `fetch` is available in Node.js 18+ (CI uses Node.js 22)
- The API is compatible for this simple GET request use case
- No changes needed to `get-proposal.js` since it imports the function, not the fetch library directly

## Verification
✅ **Tested locally**: Successfully ran `node get-proposal.js --date 2025-06-03` and verified:
- Proposal data was fetched from `https://tc39.es/dataset/proposals.json`
- Data was correctly saved to `static/data/2025-06-03.json`
- Generated JSON contains valid proposal data (9780 lines)

✅ **No remaining references**: Confirmed no other files in the codebase use `node-fetch`

## Benefits
- Reduces external dependencies
- Uses native Node.js functionality
- Maintains full compatibility with existing code
- No breaking changes

Fixes #18

---

**Link to Devin run**: https://app.devin.ai/sessions/6fb7fde55f924f65bc17a0f2bea8f874

**Requested by**: azu (azuciao@gmail.com)
