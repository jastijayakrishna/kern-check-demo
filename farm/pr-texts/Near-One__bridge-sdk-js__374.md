# feat(api): add btc_pending_id field to utxo_transfer API schema

Sync SDK with bridge-indexer-rs API changes that added `btc_pending_id` to UTXO transfer responses.

Reference: https://github.com/Near-One/bridge-indexer-rs/pull/277

### Changes
- Added optional `btc_pending_id` string field to `UtxoTransferSchema` in `src/api.ts`
- Updated integration test expectations to validate the new field

<!-- START COPILOT CODING AGENT SUFFIX -->



<details>

<summary>Original prompt</summary>

> Make a PR to add this:
> ```
> <!-- oasdiff-comment -->
> # API Changelog 0.1.0 vs. 0.1.0
> 
> ## GET /api/v1/transfers
> -  added the required property '/items/utxo_transfer/oneOf[subschema #&NoBreak;2]/btc_pending_id' to the response with the '200' status
> 
> 
> ## GET /api/v1/transfers/transfer
> -  added the required property 'utxo_transfer/oneOf[subschema #&NoBreak;2]/btc_pending_id' to the response with the '200' status
> 
> 
> ## GET /api/v2/transfers
> -  added the required property '/items/utxo_transfer/oneOf[subschema #&NoBreak;2]/btc_pending_id' to the response with the '200' status
> 
> 
> ## GET /api/v2/transfers/transfer
> -  added the required property '/items/utxo_transfer/oneOf[subschema #&NoBreak;2]/btc_pending_id' to the response with the '200' status
> 
> 
> ## GET /api/v3/transfers
> -  added the required property '/items/utxo_transfer/oneOf[subschema #&NoBreak;2]/btc_pending_id' to the response with the '200' status
> 
> 
> ## GET /api/v3/transfers/transfer
> -  added the required property '/items/utxo_transfer/oneOf[subschema #&NoBreak;2]/btc_pending_id' to the response with the '200' status
> ```
> 
> And reference https://github.com/Near-One/bridge-indexer-rs/pull/277
> 
> Also in https://github.com/Near-One/bridge-indexer-rs/pull/277 take a look at its openapi.json file


</details>



<!-- START COPILOT CODING AGENT TIPS -->
---

💬 We'd love your input! Share your thoughts on Copilot coding agent in our [2 minute survey](https://gh.io/copilot-coding-agent-survey).
