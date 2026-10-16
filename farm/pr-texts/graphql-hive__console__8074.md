# fix: drop redundant `sdl_store_unique_id` index

# Background

This drops an redundant index that is already covered by the tables primary key. It will not make a big impact but will save some bytes and probably nano/milliseconds.
