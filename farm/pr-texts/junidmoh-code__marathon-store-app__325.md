# fix(cleanup): registration finds the shoe first — tongue-label style number + size, one save

Owner correction to the HubCleanup registration flow (PR #324 follow-up): a **barcode scan was the way in, and that was the wrong model**. Nothing is created during registration — every shoe already exists in the catalogue. Registration attaches exactly two facts to an existing product: its **style number off the label inside the tongue**, and **what size is on display**.

## The corrected flow
1. **Find the shoe** — two equal, prominent paths: search the catalogue by name, or tap it in the **Not yet registered** list (products holding stock at this hub, never seen on the floor). A shop-barcode scan survives only as a clearly-subordinate shortcut under a divider ("Shortcut, if this shoe happens to carry one of our shop barcode stickers"). All three paths build the panel through **one constructor** (`registerPanelFor`) — provably the same screen.
2. **The panel** — photo, name, current stock **by location**.
3. **Style number** — "📷 Photograph the tongue label" runs the **same `readStyleCodeLabel` OCR the intake gate uses** (one clean candidate auto-fills; several become tap-chips); typing stays available and is never shape-gated. Copy is explicit everywhere: *"the label inside the tongue … Not the shop barcode sticker, not the box."* A reasoned skip exists (label unreadable / missing / brand prints none). A code **another live product already owns blocks the save** and routes to Merge — the duplicate case is surfaced, never guessed into.
4. **Size** — the grid stays visually dominant. **One save** writes both facts: the `received` movement (deterministic id — double registration still adds one unit, unchanged), the register record with its code fields, and a `/style_code_captures` enqueue (`origin: "displayCheck"`, `capturedAt: serverNowMs()`) so claiming/collision handling stay server-side, same as every other capture surface. A code already on file shows as satisfied and enqueues nothing.

**Unchanged:** the Count pass stays scan-first exactly as built; Pine stays out of every path; no rules change needed (capture queue + /settings are already writable as required).

## Mutation table (bug reintroduced → tests FAIL → restored → PASS)

| # | Required proof | Mutation | Result |
|---|---|---|---|
| 1 | Registration refuses to complete without the style-number fact | requirement check removed | 1 fail → 21 pass |
| 2 | Size + code saved in ONE action (capture rides the save) | enqueue decoupled | 3 fail → 21 pass |
| 3 | Search / list / shortcut land on the SAME panel | constructor made divergent | 1 fail → 21 pass |
| 4 | Tongue-label read accepted (single clean candidate) | OCR accept dropped | 1 fail → 21 pass |
| 5 | Manual entry accepted as the fallback | typing stops satisfying the step | 1 fail → 42 pass |
| 6 | Double registration still adds ONE unit | deterministic id + slot guard dropped | 2 fail → 21 pass |

Registration is reachable and completable **without any barcode**: every test in the two-facts suite identifies the product directly and asserts the barcode index is never touched.

Suites: frontend **1246 green** (69 files), functions untouched (543 green on main), build green.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01ERtzZhww4EK8rbdGHJCFZ2


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Start stock registration from catalogue search or the unregistered-stock list, with barcode scanning available as an optional shortcut.
  * Capture display size and manufacturer style number together during registration.
  * Read style numbers by label scan, choose from multiple results, enter them manually, or skip with a reason.
  * View stock by location while registering.
  * Access count panels from search results and the full stock list.

* **Bug Fixes**
  * Prevent incomplete registrations and block conflicting style numbers.
  * Improved messaging for items that have already been register
