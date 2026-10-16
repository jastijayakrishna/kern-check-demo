# Fix Deno v2 bundler incompatibility in ASN.1 certificate decoding

Deno v2's bundler renames internal ASN.1 class constructors (e.g., `LocalSimpleStringValueBlock` → `LocalSimpleStringValueBlock2`), breaking certificate parsing that relied on `constructor.name` string matching.

## Changes

Refactored `decodeValue()` in `lib/certUtils.js` to use property-based type detection instead of constructor name strings:

**Before:**
```javascript
function decodeValue(valueBlock) {
  const blockType = Object.getPrototypeOf(valueBlock).constructor.name;
  switch (blockType) {
    case "LocalSimpleStringValueBlock":
      return valueBlock.value;
    case "LocalIntegerValueBlock":
      return valueBlock.valueDec;
    // ... fails when bundler renames these classes
  }
}
```

**After:**
```javascript
function decodeValue(valueBlock) {
  // Wrapper objects (OctetString, BmpString, Utf8String, Constructed)
  if ("valueBlock" in valueBlock && valueBlock.valueBlock) {
    const innerBlock = valueBlock.valueBlock;
    if ("value" in innerBlock && typeof innerBlock.value === "string") {
      return innerBlock.value;  // String types
    }
    // ... other wrapper types
  }
  
  // Value blocks
  if ("valueDec" in valueBlock) return valueBlock.valueDec;  // Integer
  if ("unusedBits" in valueBlock) return new Uint8Array(valueBlock.valueHex)[0];  // BitString
  // ... other value block types
}
```

Type detection now relies on structural properties that bundlers preserve:
- Integer blocks: presence of `valueDec` getter
- Bit strings: `unusedBits` + `valueHex` properties
- String types: `value` string property (checked before `valueHex` since both exist)
- Constructed blocks: `value` array property with explicit wrapper exclusion

**CI Workflow Update:**
Re-enabled `deno task build` in `.github/workflows/test.yml` to run the complete Deno build process including bundling and testing against bundled code, validating the fix in CI.

Fixes #178

<!-- START COPILOT CODING AGENT SUFFIX -->



<details>

<summary>Original prompt</summary>

> Create a fork and have a look at the recent issue describing problems with new deno  bundler.


</details>



<!-- START COPILOT CODING AGENT TIPS -->
---

💬 We'd love your input! Share your thoughts on Copilot coding agent in our [2 minute survey](https://gh.io/copilot-coding-agent-survey).
