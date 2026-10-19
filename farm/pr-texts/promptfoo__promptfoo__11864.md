# chore(deps): update dependency mermaid to v12

## Summary

Upgrade Mermaid to 12.1.0 and update its lockfile entries so reproducible installs actually receive v12. The original override-only change still resolved Mermaid 11.17.2.

Keep the existing documentation diagrams on the Dagre layout and classic appearance; Mermaid 12 otherwise defaults to ELK and the neo look. Update the dependency guidance to explain these settings and require browser checks before introducing new diagram types. The site's Browserslist targets and DOMPurify 3.4.16 security override are unchanged.

Docusaurus theme-mermaid 3.10.2 accepts Mermaid `>=11.6.0`, and the `initialize`/`render`/`bindFunctions` integration remains compatible. Mermaid's Node requirement (`>=22.12.0`) is covered by the repository's minimum (`>=22.22.0`).

## Validation

- Production site build with `SKIP_OG_GENERATION=true`; emitted browser inventory confirms Mermaid 12.1.0, parser 2.0.1, Docusaurus 3.10.2, and DOMPurify 3.4.16.
- 340 site tests, 83 package-manifest tests, site TypeScript check, dependency consistency check, and `npm run l && npm run f` passed.
- All three existing diagrams rendered successfully in actual Chromium 109.0.5414.46, 120.0.6099.28, and 149.0.7827.55: light/dark themes at desktop/mobile widths, 36 rendered diagrams total, plus live theme switching in each browser. This covers the older Chromium targets below Mermaid's published browser floor without raising the site's browser requirements.
- Controlled Mermaid 11.17.2 versus 12.1.0 renderer comparison in the same production pages preserves all labels and node/path counts. At 703 px width, wrapping makes the reference flowchart 154→187 px tall and architecture 566→696 px; no clipping was observed, and sequence geometry is unchanged. Dagre/classic preserves the layout engine and styling, not pixel-identical dimensions.
- Real browser security checks in those same engines verified HTML/event-handler sanitization, rejection of attempts to lower security through diagram directives, disabled click callbacks, preserved safe labels, and invalid-syntax rejection.
- Compared `npm audit` with the current base: no new vulnerable package names or severity-count increases.

Local full-monorepo `npm ci` is blocked by the configured Socket release-age policy on the existing `undici@7.30.1`. Site validation used a separate allowed install pinned to all 47 direct site dependency versions from the candidate lockfile. Full current-head hosted CI must validate the complete committed lockfile before merge.

