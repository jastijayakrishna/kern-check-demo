# Stage Six: a Jozi story — 16-mission diesel-cartel arc, dialogue engine, blackout break-in

The story and mission buildout: a 3-act criminal arc where the player joins the diesel cartel that induces load shedding and sells the city its own light back — and personally causes the blackouts that become their stealth cover.

- **16 new missions + 2 side pieces** across the whole world: train rides and a precision train-driving job, tailing, escort defence with ambush waves, a fuel-tanker gentle-drive, breaker-room sabotage that triggers real load shedding, a showroom steal inside your own blackout, collections, markerless street-name riddles, fly + skydive onto the Ponte forecourt, a branching Two Fires choice with exclusive mission tails, and a hold-out finale that settles your reputation citywide.
- **Flagship "Dark House"**: a Kelvin Yard break-in that is physically impossible while the grid is up, and the game never tells you the trick — a banned-word test enforces that no player-facing copy ever names it. Teaching is purely experiential two missions earlier.
- **Engine (extend, not rewrite)**: follow/survive objective kinds; composable conditions[]/failIf[] with diegetic failure copy; hidden/markerless objectives; objective-boundary checkpoints; prerequisites + story flags (save v3 with migration); a lightweight dialogue card (E-advance); StoryDirector; DepotSecurity routed through the BlackoutStealth concealment predicate; MISSION_SCRIPTS declarative mission runtime replacing hardcoded Game.ts logic; 12 collectible Grid Diary lore pages.
- **Boot-order regression guard**: a new test asserts every Game-constructor dependency is initialised before first use (caught in playtest: yard guards spawned before PopulationSystem existed).

Gate: lint, tsc -b, 1443+ tests green including scripted walkthrough sims of every mission's completion and failure paths.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
