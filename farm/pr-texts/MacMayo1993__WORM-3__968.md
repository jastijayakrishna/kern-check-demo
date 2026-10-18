# Make the worm trail a persistent full-route path

The trail previously rendered only the newest ~80 tiles (capped further by a
256-disc budget) and was recomputed from the gameplay body trail every frame.
It now paints the worm's entire route on the current surface traversal.

 rotation-remapped alongside tileTrail.
- Render the full route with age-based level-of-detail: dense daubs near the
  worm for a smooth stroke, progressively coarser tile strides + daub spacing
  for older history, all inside a raised 4000-disc budget so per-frame cost
  stays bounded no matter how long the run gets.
- Floor the fade so the oldest path stays faintly visible as a "where I've
  been" map instead of fading to nothing.




