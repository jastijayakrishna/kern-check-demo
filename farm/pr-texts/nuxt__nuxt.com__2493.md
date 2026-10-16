# fix(content): block prototype pollution in dotted frontmatter

A labelled PR's author controls the frontmatter rendered by its `/pull/:repo/:number` preview. 

`unflattenDotted()` could follow `__proto__` through inherited properties, so a key like `__proto__.draft: true` set `Object.prototype.draft` for the whole server instance and dropped pages from the sitemap.

- Drop dotted keys with a `__proto__`, `constructor` or `prototype` segment
- Read and write only own properties (`Object.hasOwn`) in `unflattenDotted()` and `hoistNavigationPrefix()`
- Skip plain top-level `__proto__` keys, which the YAML parser keeps as own keys and which would swap the result's prototype
- Add tests that check `Object.prototype` and the result's prototype after each payload

🤖 Generated with [Claude Code](https://claude.com/claude-code), reviewed by @larbish before opening.
