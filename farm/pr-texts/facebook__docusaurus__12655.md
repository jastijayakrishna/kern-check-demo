# feat(core): support referencing assets with the standard new URL(path, import.meta.url) syntax (AI-assisted)

## Pre-flight checklist

- [x] I have read the [Contributing Guidelines on pull requests](https://github.com/facebook/docusaurus/blob/main/CONTRIBUTING.md#pull-requests).
- [x] **If this is a code change**: I have written unit tests and/or added dogfooding pages to fully verify the new behavior.
- [ ] **If this is a new API or substantial change**: the PR has an accompanying issue (closes #0000) and the maintainers have approved on my working plan.

## Motivation

Stacked on #12651 (asset modules migration).

`require('./img.png')` has always been the way to reference an asset inline in JSX, but it's CommonJS and bundler-specific. `import()` can't replace it inline because it's async. The standard and portable syntax is [`new URL('./img.png', import.meta.url)`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL): it works natively in browsers and Node.js, and in Vite, Parcel, webpack and Rspack.

```jsx
<img src={new URL('./img.png', import.meta.url).href} />
```

webpack and Rspack already support it as asset modules, but it didn't work correctly in Docusaurus:

- **SSR:** the server bundle resolves `import.meta.url` to a `file://` URL, so the HTML contained `src="file:///baseUrl/assets/images/img-hash.png"`. Setting `module.parser.javascript.url: 'relative'` makes `new URL()` return the same relative URL (`/baseUrl/assets/images/img-hash.png`) on the server and client.
- **SVGR and ideal-image plugins:** they transformed the referenced file into a JS module (React component, responsive image object). Their rules now exclude `new URL()` references (`dependency: {not: 'url'}`), so `new URL()` always returns the asset URL.

## Test Plan

- New dogfooding cases with small (inlined) and large images, relative paths and the `@site` alias, file names with spaces, an SVG, a PDF and `<IdealImage>`, in JSX and MDX, on our website where the ideal-image and SVGR plugins are enabled. I checked the SSR HTML with webpack and Rspack, then the browser: images load after hydration and after client-side navigation, with no hydration errors.

### Test links

Deploy preview: https://deploy-preview-12655--docusaurus-2.netlify.app/

- Dogfooding pages: https://deploy-preview-12655--docusaurus-2.netlify.app/tests/pages/new-url-assets/, https://deploy-preview-12655--docusaurus-2.netlify.app/tests/docs/tests/images/ (`new URL()` images section)
- Updated docs: https://deploy-preview-12655--docusaurus-2.netlify.app/docs/markdown-features/assets/#images (URL syntax tab), https://deploy-preview-12655--docusaurus-2.netlify.app/docs/static-assets/#in-jsx

## Related issues/PRs

- #12651

(AI-assisted)

🤖 Generated with [Claude Code](https://claude.com/claude-code)
