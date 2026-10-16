# fix: TilingSprite tilePosition divided by resolution when using Canvas renderer

### Overview

`TilingSprite.tilePosition` was visually divided by the texture resolution on the Canvas renderer. With `resolution = 2`, a `tilePosition.x = 100` only shifted the pattern by 50 CSS pixels, diverging from WebGL/WebGPU behavior. The cause: `Matrix.scale(1/resolution, 1/resolution)` in `CanvasTilingSpritePipe.execute()` scaled `tx`/`ty` along with the basis. The fix saves and restores `tx`/`ty` around the scale so only `a`/`b`/`c`/`d` are adjusted, while the anchor-derived CSS offset is preserved.

Fixes #11939

#### Fixes
- Canvas renderer: `TilingSprite.tilePosition` is now applied in CSS pixel space and matches WebGL/WebGPU when the texture has `resolution > 1`.

##### Pre-Merge Checklist

- [x] Tests and/or benchmarks are included
- [ ] Documentation is changed or added

---

Co-authored-by: GoodBoyDigital <3112434+GoodBoyDigital@users.noreply.github.com>
