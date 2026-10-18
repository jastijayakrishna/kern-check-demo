# Domino Royal: use Murlan-style multi-seat live video overlay

### Motivation

- Align Domino Royal's in-match live video behavior with Murlan Royale so group/online tables can show multiple remote video seats positioned over player avatars.

### Description

- Removed single-opponent state/rect handling and instead reuse the existing group opponent collections (`groupOpponentRects` / `groupOpponentAnchorElements`) for `domino-royal` so multiple remote peers are handled the same way as `murlanroyale`.
- Compute `opponentNodes` / `opponentBoundsList` for both games and update `setGroupOpponentRects` / `setGroupOpponentAnchorElements` instead of separate `opponentAnchorElement` / `opponentRect` setters.
- Replace the single Domino-only remote video block with a unified `groupOpponentRects.map(...)` renderer that runs for `domino-royal` and `murlanroyale`, and make keys unique by including `gameSlug`.
- Keep existing behavior that hides underlying avatar elements while live video is active by relying on the group-anchor visibility effect so avatars are restored when video ends.

### Testing

- Ran `git diff --check` with no issues reported.
- Ran lint (`npm run lint -- src/components/GameLiveAvatarOverlay.jsx`) and it completed successfully.
- Performed a production build (`npm run build`) and the build completed successfully with generated `dist` assets.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a953df5e0d88329b1a046cf43a272e4)
