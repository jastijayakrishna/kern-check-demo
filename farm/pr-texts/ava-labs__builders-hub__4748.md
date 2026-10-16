# feat(home): open a chain's explorer from the interop drawing

## Summary
On the homepage, hovering a block in the "Any L1 can connect." network drawing shows its name, which makes the blocks look clickable. They weren't. Now clicking a block goes to that chain's explorer page (`/explorer/mainnet/<slug>`), and the cursor turns into a pointer over any block that has one.

- `InteropChapter`: `explorerHref(chainId, chainName)` finds the chain in the catalog by ID first (`catalogOf("mainnet")`) and falls back to a name match in `l1-chains.json`. 62 of the 69 chains in today's `/api/overview-stats` feed match. A chain that doesn't match gets `href: null`, so it keeps its hover label but can't be clicked.
- `NetworkScene`: `NetworkChain` gains `href`, `NetworkSceneProps` gains an optional `onSelect`, and the instanced mesh gets an `onClick` handler. The Canvas cursor is `pointer` only when the hovered block has an `href`.
- A click logs the existing `home_chain_clicked` event (`{ chain, section: "interop", href }`) and then calls `router.push`.

Only the WebGL scene is clickable, so that means viewports 768px and wider. The still image on phones has no click targets, same as before.

Checked locally: hovered a block at 1440px and got a pointer cursor; clicking it went to `/explorer/mainnet/gunzilla`.

![hover](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmctMjJiZmQ3NzYwMDkyNDk2MmJhYWM2OGI3YmQxOTI5NTIvMjNhY2UxNGQtODlhOC00NjE1LTkxNWMtMGFhNDEzMzEzMTExIiwiaWF0IjoxNzkyMDAxMTcxLCJvcmdfaWQiOiJvcmctMjJiZmQ3NzYwMDkyNDk2MmJhYWM2OGI3YmQxOTI5NTIiLCJmaWxlbmFtZSI6ImludGVyb3AtaG92ZXIucG5nIn0.H3V5hl-MOFb38JC1AQuRn0SHX6oYM5ICJyDmYgTKvYQ)

Link to Devin session: https://app.devin.ai/sessions/7519ba8625cd4b92811bf001e1bb2432
Open in Devin Desktop: https://app.devin.ai/desktop/session/7519ba8625cd4b92811bf001e1bb2432?variant=devin
