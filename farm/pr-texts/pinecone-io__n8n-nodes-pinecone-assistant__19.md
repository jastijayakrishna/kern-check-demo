# Pinecone credential property names

Rename duplicate `notice` properties in PineconeApi credentials to prevent potential UI interference issues.

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Only changes internal property identifiers for credential notices; no auth logic or API behavior changes, but could affect any code referencing the old `notice` key.
> 
> **Overview**
> Updates `credentials/PineconeApi.credentials.ts` to rename the two `notice`-type properties from the duplicate `name: 'notice'` to distinct keys (`deprecationNotice` and `promoNotice`), preventing potential credential UI interference while keeping behavior and messaging the same.
> 
> <sup>Written by [Cursor Bugbot](https://cursor.com/dashboard?tab=bugbot) for commit 0f548184e09f6aef3f84e42b9d9d9be9ae15e7c1. This will update automatically on new commits. Configure [here](https://cursor.com/dashboard?tab=bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
