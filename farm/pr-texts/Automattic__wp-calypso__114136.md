# Reader: Added noindex to logged out tags pages

Part of the logged-out tag page SEO cleanup.

## Proposed Changes

* Emit `<meta name="robots" content="noindex" />` on the tag-parameterized Discover pages (`/discover/tags?selectedTag=<tag>`, including localized variants like `/es/discover/tags?selectedTag=<tag>`).
* Leave the bare `/discover/tags` page, and every other Discover page, indexable.
* Add a server middleware (`setDiscoverTagNoindex`) that dispatches the robots meta into the document head store. URLs with a query string are never server-side rendered in Calypso (see `setShouldServerSideRender`), so the meta cannot come from the React document head component on the server. The head is still built from the store on every request, so dispatching directly gets the tag into the raw HTML. This is the same approach `setBrowsePluginsNoindex` uses for uncurated plugin browse pages.
* Pass a `noindex` prop to `DiscoverDocumentHead` on the client so the head stays consistent after hydration and on client-side navigation.
* Unit tests for the middleware and the component prop.

## Why are these changes being made?

Logged-out `/tag/<tag>` URLs now redirect to `/discover/tags?selectedTag=<tag>`. Those parameterized pages are a long tail of thin, near-duplicate URLs that compete with the main Discover pages in search results and AI Overviews. Marking them `noindex` tells search engines to drop them while keeping them live for people who follow the links.

Because these URLs skip SSR entirely, crawlers currently receive an empty app shell for them (generic title, no description), so nothing of value is lost by de-indexing them.

## Testing Instructions

The change is server-side, and `yarn start` only builds the server bundle once, so restart the dev server after checking out the branch.

1. Check out this branch and run `yarn start`.
2. In a logged-out browser (or with `curl`), load `view-source:http://calypso.localhost:3000/discover/tags?selectedTag=food`. Confirm the head contains `<meta name="robots" content="noindex"/>`.
3. Repeat for a localized URL, for example `/es/discover/tags?selectedTag=comida`. Confirm the same meta is present.
4. Load `view-source:http://calypso.localhost:3000/discover/tags` and `view-source:http://calypso.localhost:3000/discover`. Confirm there is no robots meta.
5. While logged in, navigate client-side from `/discover` to `/discover/tags?selectedTag=food` and inspect the DOM head. Confirm the robots meta is added, and removed again when navigating back to `/discover`.
6. Run `yarn test-client client/reader/discover`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

