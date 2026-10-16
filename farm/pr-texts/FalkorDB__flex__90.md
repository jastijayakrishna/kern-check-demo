# Fix Jaccard correctness for duplicate inputs and remove throwaway allocations

`src/similarity/jaccard.js` computed union/intersection sizes by materializing arrays, and it counted duplicates from the left-hand input as multiple intersection hits. That could produce invalid results greater than `1` and added unnecessary allocations on every call.

- **Implementation**
  - Compute Jaccard over deduplicated sets for both inputs.
  - Count intersection size directly by iterating `setA` and checking membership in `setB`.
  - Derive union size from set cardinalities instead of building a union array.

- **Correctness**
  - Prevent duplicate values in either input from inflating the intersection.
  - Preserve existing behavior for invalid inputs (`null`) and empty unions (`0`).

- **Regression coverage**
  - Add focused tests for duplicate-heavy inputs in both execution paths:
    - `flex.sim.jaccard(...)`
    - direct JS module invocation

```js
const setA = new Set(a);
const setB = new Set(b);

let intersectionSize = 0;
for (const value of setA) {
    if (setB.has(value)) intersectionSize++;
}

const unionSize = setA.size + setB.size - intersectionSize;
return unionSize === 0 ? 0 : intersectionSize / unionSize;
```

> [!WARNING]
>
> <details>
> <summary>Firewall rules blocked me from connecting to one or more addresses (expand for details)</summary>
>
> #### I tried to connect to the following addresses, but was blocked by firewall rules:
>
> - `0.0.0.0.in-addr.arpa`
>   - Triggering command: `/usr/bin/node node server.js` (dns block)
>   - Triggering command: `/usr/bin/node node server.js docker0` (dns block)
>
> If you need me to access, download, or install something from one of these locations, you can either:
>
> - Configure [Actions setup steps](https://gh.io/copilot/actions-setup-steps) to set up my environment, which run before the firewall is enabled
> - Add the appropriate URLs or hosts to the custom allowlist in this repository's [Copilot coding agent settings](https://github.com/FalkorDB/flex/settings/copilot/coding_agent) (admins only)
>
> </details>

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>fix+perf: jaccard.js — Unnecessary array materialization and correctness bug</issue_title>
> <issue_description>**Parent:** FalkorDB/flex#77
> **Impact:** High
> **File:** `src/similarity/jaccard.js:19-24`
> 
> ## Problem
> 
> Both union and intersection are materialized as arrays just to read `.length`, creating multiple throwaway allocations:
> 
> ```js
> const unionArray = [...new Set([...a, ...b])];       // 3 intermediate allocations
> const setB = new Set(b);
> const intersectionArray = a.filter(x => setB.has(x)); // 1 throwaway array
> ```
> 
> ### Correctness bug
> 
> Because `a` is not deduplicated before filtering, duplicates in `a` count as multiple intersection hits. For example, `jaccard([1,1,1], [1])` returns 3/1 = 3, which is mathematically invalid (Jaccard similarity must be in [0, 1]).
> 
> ## Fix
> 
> Compute sizes without materializing arrays, and deduplicate both inputs:
> 
> ```js
> const setA = new Set(a);
> const setB = new Set(b);
> 
> let intersectionSize = 0;
> for (const x of setA) {
>     if (setB.has(x)) intersectionSize++;
> }
> 
> const unionSize = setA.size + setB.size - intersectionSize;
> return unionSize === 0 ? 0 : intersectionSize / unionSize;
> ```</issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes FalkorDB/flex#80

<!-- START COPILOT CODING AGENT TIPS -->
---

💬 We'd love your input! Share your thoughts on Copilot coding agent in our [2 minute survey](https://gh.io/copilot-coding-agent-survey).
