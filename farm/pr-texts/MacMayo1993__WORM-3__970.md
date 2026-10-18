# Make parity orbs pop: bloom, glassy shell, plasma core, Fresnel rim

The orbs relied on emissiveIntensity > 1 + toneMapped={false} to fake glow, but the scene had no bloom pass, so those bright values just clamped to flat oversaturated color. This is the core "lame" look.

- GameScene: add a selective Bloom pass to the EffectComposer (mipmapBlur, luminance-thresholded so only emissives bloom). Mount the composer whenever the PiP is off so bloom survives even when AO is gated; drop bloom only under sustained-low-FPS (perfReducedFX).
- ParityOrb: make the body a translucent glassy shell and add the inner plasma core + volumetric haze meshes the animator was already driving but that were never rendered (dead innerCore/innerGlow refs).
- ParityOrb: add a Fresnel rim shader shell for a view-dependent silhouette glow that bloom turns into a halo. Rim hue/intensity follow the existing glow-worm and rainbow animation paths.


Claude-Session: https://claude.ai/code/session_01UcoyGXWVKRm68NQPbKLB6S

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

