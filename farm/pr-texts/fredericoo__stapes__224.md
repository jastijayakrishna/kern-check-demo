# feat(net): scope the tick stream to what each client can see

TL;DR: A client was sent the chunks near its own body on join and then told about every cell that changed anywhere in the world on every tick. The join scaled with the player and the tick stream scaled with everybody else. The tick stream is now scoped per client, by **two** reaches — terrain by the chunk subscription, a body by how far away it is — and noises and speech go to whoever could see the cell they happened in.

Twenty people in twenty corners of the world each heard the other nineteen neighbourhoods walk about, none of which they could see.

## Two reaches, because they are bounded by different things

The first version of this scoped everything by the chunk subscription, and measuring it on the real map showed it saves almost nothing. The subscription is a square **176 cells across**, because it is sized by the light bake — 47 of its 79 cells are `LIGHT_CHUNK_SIZE` plus `LIGHT_APRON`, the map a cached bake reads beyond the window it fills. `data/map.json` is 168 wide, and every creature in it stands between x -74 and 57, y -69 and 87. So from anywhere a player would actually be, the whole inhabited world is inside the square — and the brain budget walks two dozen creatures somewhere in it every round.

A body feeds none of that bake: every body tile is `lightPassing`, and `terrainHeight` skips a person. What bounds a body is what the client could draw or be lit by — half the view, `MESH_WINDOW_MARGIN`, and `MAX_LIGHT_LEVEL`, because it may be carrying a lantern. That is 33 cells on your own storey, plus one per storey between you.

Measured over 20 simulated seconds on the den map, one player at the spawn:

| | cells/tick | KB/s |
| --- | --- | --- |
| every socket, as `main` does it | 15.0 | 39.5 |
| scoped by the chunk subscription | 14.5 | 38.1 |
| bodies scoped by what you can see | 9.5 | 25.0 |

At the mouth of the den: 14.3 → 9.1 cells/tick. Sixty cells past the last creature, the chunk reach already does the work: 7.7 → 0.2 → 0.0.

## Noises and speech went by storey

They do not ride the patch — they have their own fan-out — and they were scoped by level alone, which on one floor of a den is every crunch, gulp, hiss and howl in the world. Both are drawn *at a cell*, hanging over the body that made them, so a client too far away to see that cell draws nothing whatever it is told. Measured with four people in the den and a watcher 60 cells past the last creature: **six noises made in 30 seconds, five delivered to the watcher, none of them one it could see.**

Reading the brains alone says this cannot happen: every authored brain noise fires on noticing a player, so an empty part of the map is silent. The brains are one of three sources — a stone's `sound` is the second, and `consume.sound` is the third, which is a deer eating a berry and is nobody's reaction to anything.

## What this changes

- **`app/net/scope.ts`** is the rule, as pure functions: terrain by the chunk it is in, a body by `withinBodyReach`, an event by the body it is about or — where it names none, like an arrow or a floating damage number — the cell it happened in. `joined` and `left` reach everybody, because they carry the headcount.
- **`sendToNearby`** replaces `sendToLevel` for noise and chat: the storey test stays, with the body reach on top of it.
- **A client is never sent a body it has not been told about.** Cells, the `hello` map and every chunk handover go out with the distant bodies taken out (`visibleStack`). The cheaper arrangement — stop sending a creature's steps, leave the cells alone — puts its tile in the client's board for ever, in a cell nothing will rewrite: too far to draw, and `fitsTile` counts a creature as solid, so the client would refuse its own player a step into a cell a deer left an hour ago.
- That is also what makes the saving possible: a cell whose change is only bodies moving is, with those bodies taken out, the cell the client already has, so it is not sent. A creature's step is two such cells.
- **`announ
