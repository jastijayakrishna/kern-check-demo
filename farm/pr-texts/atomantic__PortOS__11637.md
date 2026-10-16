# Make YouTube thumbnails worth clicking, with an A/B set for Test & Compare

<!-- claude-projects-attribution: {"github_login":"atomanticagent"} -->
_Requested by **Adam** · [project thread](https://claude.ai/code/project/chan_01MHsZJWDCuzCr94pGQXuXdV?thread=cmsg_01MHsZJWDCuzCr94pGQXuXdV5BrKvba35SaNfvqMNX6Qx3)_

Before: the publishing kit cut six frames at performance-shot midpoints, which could land mid-cut, mid-dissolve or under a burned-in lyric, padded with black bars on a non-16:9 master. The YouTube post uploaded one of them bare; the UI said to "add title text before uploading" by hand.

After: the kit judges two frames per shot (inside the shot's middle, in a lyric-free moment when the shot has one), scores each for crisp detail, contrast and exposure, and keeps the best frame of each shot, best first, cropped to fill 16:9. A new **YouTube thumbnail** card on the Publish step makes the thumbnail from any of those frames, a shot's still, a cover image or image history: cropped 16:9, the title set large with a drop shadow in the cover's own lettering on one side, clear of the subject and the duration badge, no artist name. A new cover design re-sets it, and the YouTube post uploads it. **Paint the title with the image model** sends the chosen frame to the default image generator with a visible thumbnail brief (shown as a chip, with Show full prompt) plus the user's own direction, and the painted result becomes the thumbnail bare. Up to three made thumbnails can be kept as an **A/B test** set for YouTube Studio's Test & Compare.

How: `lib/musicVideoCoverOverlay.js` now lays out on a `{ width, height }` box with a `thumbnail` frame preset (larger type, 46% text width, bottom clear zone, shadow, no tag); a square cover lays out exactly as before. `coverArtCompose.js` shares one crop+letter path for both. Frame choice lives in `services/musicVideo/thumbnailFrames.js`; the composed thumbnail, paint request and test set in `services/musicVideo/youtubeThumbnail.js` (`publishKit.youtubeThumbnail`, `publishKit.youtubeThumbnailTests`, additive fields), with routes under `/publish-kit/youtube-thumbnail`. A kit rebuild keeps any frame a made thumbnail was cut from. Image calls happen only when the user presses Paint. The old `PUT /publish-kit/thumbnail` stays for older clients.

Tests: frame candidates/pick/score, thumbnail layout, compose + payload + re-set on design change + rebuild retention + paint queue/settle/failure + test set through the real store and sharp, and the client card. `npm run pregate` passes.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01RFy6BzWzSpp7sFjUYxuR1u
