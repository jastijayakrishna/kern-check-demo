# Disable 3D human characters and add feature flag to disable voice commentary

### Motivation
- Reduce runtime complexity and resource use by disabling 3D human characters and temporarily opt out voice commentary due to speech synthesis reliability/privacy concerns.

### Description
- Set `ENABLE_3D_HUMAN_CHARACTERS` to `false` to globally disable 3D human characters in the arena.
- Introduce `ENABLE_VOICE_COMMENTARY` (default `false`) and make commentary initialization respect this flag by setting `commentaryMuted` to `true` when disabled.
- Short-circuit commentary-related code paths (speech support effect, `enqueueMurlanCommentary`, `unlockCommentary`, and the game-state-driven commentary effect) to early-return when `ENABLE_VOICE_COMMENTARY` is `false`.
- Preserve existing commentary preferences and queuing logic when the flag is enabled so behavior is unchanged when voice commentary is turned back on.

### Testing
- Ran unit tests with `yarn test`, which passed.
- Ran linter with `yarn lint`, which passed.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a958aa06c1483299d2eec96839beddc)
