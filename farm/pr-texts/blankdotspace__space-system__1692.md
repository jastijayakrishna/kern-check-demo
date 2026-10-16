# Make Terms & Privacy pages community-aware; add admin profiles and admin list UI

### Motivation

- Replace static legal copy with community-aware content so Terms and Privacy display the correct `communityId` and publicly-declared community admins.
- Surface community administrator identities (pfp, username, link to `/s/[username]`) so space visitors can see who manages a given space system.

### Description

- Reworked `/terms` and `/privacy` pages to load `systemConfig` and admin profiles server-side by calling `loadSystemConfig()` and `loadCommunityAdminProfiles()` and render new components `TermsContent` and `PrivacyContent`.
- Added `loadCommunityAdminProfiles` util which queries `fidRegistrations` from Supabase and fetches profile data from Neynar to produce `CommunityAdminProfile` records.
- Introduced `AdminList` UI component to render admin avatars/initials, display names, usernames, and links to `/s/[username]`.
- Updated `privacy-content.tsx` with the provided privacy notice copy and a reusable `EFFECTIVE_DATE` constant, and added `terms-content.tsx` to hold dynamic Terms copy.

### Testing

- Attempted to run the dev server with `yarn dev`, but the run failed in this environment due to a lockfile/package resolution error (no successful local server start).
- No automated unit or integration tests were added or executed for these changes.
- Manual/visual QA is recommended to verify admin profiles render and markdown formatting on the live site once dependencies are installed and the dev server can run.

------
[Codex Task](https://chatgpt.com/codex/tasks/task_e_6972a4369f0c83259aaecbf7f6d2b74d)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Community administrator profiles now display dynamically on Privacy and Terms pages with names, identity information, and profile pictures
  * Enhanced transparency of community leadership information

* **Refactor**
  * Privacy and Terms pages migrated to server-side rendering with improved dynamic data loading capabilities

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
