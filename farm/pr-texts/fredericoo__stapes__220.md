# feat(battler): leave remains naming who died and what killed them

TL;DR: A death put everything a body owned on the floor and left no trace of *whose* death it had been. A body may now also leave remains — a tile its author picks — engraved with who it was and described by what killed it. Along the way a placement's single text splits in two, so a skull's cause of death is not recited to everybody who walks past it.

## A sign is read to you; everything else waits to be asked

A placement had one text on it, `description`, and two things read it: a look, and **anybody standing next to it**. The second is what a sign is for — a sign whose words you had to discover a modifier to see would simply be walked past — but it was the only text a placement had, so it was also the only place to put a line of prose on an object. The bill came in with the skulls: a cell people keep dying on collects them, and eleven skulls was eleven sentences hanging in the air over the ground.

- **`inscription`** is what is *written on* a thing. Recited to whoever walks up to it, shown under the name on a look, shown on the card. This is the old `description`, renamed, and every sign in the world is one.
- **`description`** is what examining the thing tells you. It reaches the screen only where somebody asked about *that object* — the item card, and a look they aimed.

The line between them is **who is asking**. Walking past a shelf is not a question; pointing at one thing is, which is also why a look shows both — you cannot be spammed by a label you aimed at.

Two name fallbacks follow the inscription rather than the description, because it was the inscription doing that job all along: a sign in your bag is called what it says rather than "Sign", and so is a stone in the cast bar.

**The map file has a version now, and it is 2.** `MAP_FILE_VERSION` sits on the in-memory shape as well as the file so there is one answer rather than two that could drift, and `parseMap` is the only place an older one exists: a version-1 file has every `description` lifted into `inscription` on the way in. The lift is unconditional because that is all the field could have meant — a version-2 file may carry both, and guessing per placement would put a skull's cause of death into every passer-by's mouth. Every route the map takes goes through `parseMap` — the file, the checkpoint blob, an editor save, `/api/seed` — so the live world's ten signs survive the rename without anything else knowing about it.

## What a body leaves

**`BattlerDef.remains` names a tile a body drops where it falls.** Absent means nothing, which is every body in the world but two: a world where every rat leaves a keepsake is knee-deep in rats' skulls by the evening. But a boss worth killing once is exactly the case that wants to say otherwise, and that is a decision for whoever authors the boss rather than for `kill`. On the battler block because only a battler can die. The player leaves `skull-player`; the cave troll leaves the `Troll skull` that was already in the catalogue.

**The tile is chosen and nothing else is.** What lands is engraved with whoever the body was — its tile's name for a creature, their own name for a player — and described by what killed it. An author picks the art and the world writes on it.

**A name with a hole in it.** `PlacedTile.engraved` fills the `%s` in a tile's own name, so `skull-player` is named `%s's skull` and the placement says whose. A name on the def would make every skull in the world one anonymous kind of thing. A tile whose name has no `%s` in it ignores the engraving, which is what lets the plain `Troll skull` be a perfectly good thing for a troll to leave. The substitution lives in one place (`app/lib/engraving.ts`) and is read wherever an item is named.

**A record of what killed you.** `Blame` is `{ source, by? }` and rides into `applyDamage`, which hands it to the death it causes:

- `Cause of death: Fangs by Wolf` — a blow, named after the weapon and whoever swung it
- `Cause of death: Burned by Flame` — a condition, n
