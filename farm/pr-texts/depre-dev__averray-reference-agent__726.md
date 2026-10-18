# fix(dispatch): seed npm workspace links instead of refusing them

Closes the third wall on the task-family packet. The code is the implementer's, unmodified; **I committed and published it** because their run stopped at D4's environmental gate before committing anything.

## The fix

`dereference: true` → `dereference: false, verbatimSymlinks: true`, and the filter now classifies a symlink by its **declared target**, resolved against where the link will land in the prepared workspace rather than against the cache where it is merely stored. Regular files keep the original `realpath` containment check.

The detail I'd have got wrong: the destination is computed from `targetNodeModules` — the final path after the staging rename — not from the staging directory. Containment is therefore reasoned about where the link actually ends up.

## Verified independently

Applied to a clean `main` checkout, `npm ci`, typecheck 0, **19/19**.

### The guard bites — but not the way the handback implies

Removing **only** the destination-containment assertion:

```
× rejects a cached symlink whose relative target escapes the workspace
  Tests  1 failed | 18 passed (19)
```

Removing **only** the `path.isAbsolute` guard:

```
  Tests  19 passed (19)
```

So `isAbsolute` is **redundant** — `path.resolve` on an absolute target yields that absolute path, and the containment assertion refuses it regardless. There is **one** load-bearing guard with an early exit in front of it, not two independent ones.

Not a defect, and the redundancy is harmless. But the evidence should not be read as two separately-proven refusal mechanisms, and the containment assertion is the single point of failure for the relative-escape case.

### D4 — the load-bearing half, closed

Colima was down for the implementer at 18:13; it was up at 18:18. The question D4 exists to answer is whether a *preserved* link actually resolves where it lands, since a symlink that survives the copy but dangles in the container would fail silently:

```
$ docker run --rm -v "$WS:/w" -w /w node:22-bookworm-slim \
    node -e 'console.log(require.resolve("@avg/mcp-common"))'
/w/packages/mcp-common/dist/index.js
```

Resolves correctly inside the container. The premise the fix rests on holds.

**Still open:** the full dispatcher → seeded cache → container → `npm test` path. That is coupled to the task-family packet — the existing eleven cases skip seeding entirely — so it should be reported there rather than manufactured here.

## Protocol note

There was no SHA to verify against, because nothing was committed. The #696 rule expects the full head SHA in the handback before review; a stop that leaves work uncommitted has no SHA to state. Worth a line in the protocol so uncommitted work is either committed or explicitly flagged as unverifiable.

