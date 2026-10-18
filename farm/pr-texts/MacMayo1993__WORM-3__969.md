# Add additive glow halo to the worm trail (no post-processing)

Gives the worm trail a neon glow by mirroring the Glow worm's glowAltRef overlay: a second additive instanced-mesh disc layered over the most-recent trail daubs, tinted with the skin's glow colour and scaled up from the same daub transform.

This is deliberately NOT a screen-space bloom pass. It is plain extra geometry sitting on the trail's surface positions, so by construction it cannot bloom the background or the cube interior — the failure mode of a global Bloom effect. Capped to the newest TRAIL_GLOW_CAP daubs so the glow tracks the active worm and per-frame cost stays bounded.


Claude-Session: https://claude.ai/code/session_01DBKwy2WHT442FPBhaRo7qo

## Description
Please include a summary of the change and which issue is fixed.

## Type of change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)

## Checklist:

- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings

