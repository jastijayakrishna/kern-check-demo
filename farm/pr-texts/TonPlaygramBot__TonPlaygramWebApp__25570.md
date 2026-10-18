# Add device-local social profile linking (UI, storage, normalization, tests)

### Motivation
- Provide a lightweight way for users to save official social profile links on-device without OAuth or developer apps.
- Make profiles quickly accessible from the Social Manager for opening profiles and counting linked destinations.

### Description
- Add a profile linking UI: `ProfileLinkSheet` component, edit/save/remove flows, and corresponding CSS for a bottom sheet (`index.css`).
- Persist device-local links with `loadLinkedProfiles` and `saveLinkedProfiles` and add `normalizeSocialProfile` to validate/normalize usernames and profile URLs for supported platforms (`webapp/src/utils/socialProfileLinks.js`).
- Integrate links into the Social Admin page by showing linked profiles in account cards, updating overview counts to include linked profiles, and wiring state for `profileEditor`/`profileInput` and message flows in `SocialAdmin.jsx`.
- Add unit tests for normalization rules in `webapp/src/utils/socialProfileLinks.test.js` and import new icon buttons used in the sheet.

### Testing
- Ran unit tests for `normalizeSocialProfile` using `vitest` (file `webapp/src/utils/socialProfileLinks.test.js`), and the tests for username/url normalization and validation passed.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a957442bdec832989df405cb9c480b2)
