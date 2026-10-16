# Rename GitHub org references from get-convex to convex

## Summary
**Note:** GitHub Pages URLs change from `get-convex.github.io/agent` to `convex.github.io/agent`. Old `*.github.io` URLs do **not** redirect after an org rename.

The GitHub org was renamed from `get-convex` to `convex`. This points old-org references at `convex`: `package.json` repository/homepage/bugs URLs, README/docs links, `get-convex.github.io` Pages URLs, `ghcr.io` images, and `owner/repo` shorthands (`skills-lock.json` sources, `get-convex/<repo>#N` refs).

GitHub redirects most old URLs, so most of this is tidying links. Anything that actually breaks under the old name is called out above.

The rewrite used a scoped regex: `get-convex` followed by `/`, `#`, or `.github.io`. Files the edit pushed out of Prettier style were reformatted with the repo's own Prettier version.

----

By submitting this pull request, I confirm that you can use, modify, copy, and redistribute this contribution, under the terms of your choice.


Link to Devin session: https://app.devin.ai/sessions/b5b2e61384834a2383855bd8149b9816
Open in Devin Desktop: https://app.devin.ai/desktop/session/b5b2e61384834a2383855bd8149b9816?variant=devin
