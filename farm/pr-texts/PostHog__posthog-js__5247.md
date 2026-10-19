# chore(deps): bump next from 15.5.24 to 15.5.27 in /playground/react-nextjs in the npm_and_yarn group across 1 directory

Bumps the npm_and_yarn group with 1 update in the /playground/react-nextjs directory: [next](https://github.com/vercel/next.js).

Updates `next` from 15.5.24 to 15.5.27
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vercel/next.js/releases">next's releases</a>.</em></p>
<blockquote>
<h2>v15.5.27</h2>
<p>This release contains security fixes for the following advisories:</p>
<p>Medium:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-f87g-xv8r-7p7x">Information disclosure in Next.js App Router metadata image routes via dynamicParams bypass</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-4jqv-mc3x-m676">Cache poisoning of SSG and ISR pages in self-hosted Next.js applications</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-mcj8-r9mp-w47p">Cache poisoning in Next.js SSG/ISR rendering leads to cross-user content substitution and persistent denial of service</a></li>
</ul>
<h2>v15.5.26</h2>
<p>This release contains additional security hardening for <code>next/og</code>. For more information, check out <a href="https://nextjs.org/blog/nextjs-security-update-september-22-2026">https://nextjs.org/blog/nextjs-security-update-september-22-2026</a></p>
<h2>v15.5.25</h2>
<p>Follow-up release to <a href="https://github.com/vercel/next.js/releases/tag/v15.5.24">v15.5.24</a> re-enabling AVIF Image Optimization when newer versions of <code>sharp</code> are installed (<a href="https://redirect.github.com/vercel/next.js/pull/97954">#97954</a>).</p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vercel/next.js/commit/def7eff9063f79cf58610c15fe58dd78b967c885"><code>def7eff</code></a> v15.5.27</li>
<li><a href="https://github.com/vercel/next.js/commit/52c94abdd2ea5f416f5e8353ea8a2edd3fe311b8"><code>52c94ab</code></a> [lts-maintenance] Scope response cache keys to their source route (<a href="https://redirect.github.com/vercel/next.js/issues/219">#219</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/785f4c2397f25690edf02b5a9f1cd7deaa1abb6d"><code>785f4c2</code></a> [lts-maintenance] Match Next data paths case-sensitively (<a href="https://redirect.github.com/vercel/next.js/issues/197">#197</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/7217d63db316f1650cab9c2a15833155b540766c"><code>7217d63</code></a> [lts-maintenance][webpack] Ensure <code>dynamicParams</code> is respected in `opengraph-...</li>
<li><a href="https://github.com/vercel/next.js/commit/d5979baa545099473b9fde8b6e03f06b3167242f"><code>d5979ba</code></a> [lts-maintenance][ci] Remove PR creation from deploy test workflow (<a href="https://redirect.github.com/vercel/next.js/issues/99093">#99093</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/812ae7db8453c0aa65859ea7b2810007e033487c"><code>812ae7d</code></a> [lts-maintenance][test] Adjust deploy assertions for platform drift and the e...</li>
<li><a href="https://github.com/vercel/next.js/commit/6936da55033075528f0dfad8f2ec29550b8c9053"><code>6936da5</code></a> v15.5.26</li>
<li><a href="https://github.com/vercel/next.js/commit/b49b6ca47ed80a1a3601d63f7ed6c00355ca4bc1"><code>b49b6ca</code></a> [maintenance-lts] Harden next/og SVG serialization</li>
<li><a href="https://github.com/vercel/next.js/commit/f391939d5ec8f1c32b339e902100987be0b6f959"><code>f391939</code></a> [15.5.x][test] Disable deploy tests triggering bot challenge (<a href="https://redirect.github.com/vercel/next.js/issues/98132">#98132</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/013ee1d2f25326197453d129430a6da83b86426d"><code>013ee1d</code></a> v15.5.25</li>
<li>Additional commits viewable in <a href="https://github.com/vercel/next.js/compare/v15.5.24...v15.5.27">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=next&package-manager=npm_and_yarn&previous-version=15.5.24&new-version=15.5.27)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

<details>
<summary>Dependabot commands and options</summary>
<br />

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore <dependency name> major version` will close this group update PR and stop Dependabot creating any more for the specific dependency's major version (unless you unignore this specific dependency's major version or upgrade to it yourself)
- `@dependabot ignore <dependency name> minor version` will close this group update PR and stop Dependabot creating any more for the specific dependency's minor version (unless you unignore this specific dependency's minor version or upgrade to it yourself)
- `@dependabot ignore <dependency name>` will close this group update PR and stop Dependabot creating any more for the specific dependency (unless you unignore this specific dependency or upgrade to it yourself)
- `@dependabot unignore <dependency name>` will remove all of the ignore conditions of the specified dependency
- `@dependabot unignore <dependency name> <ignore condition>` will remove the ignore condition of the specified dependency and ignore conditions
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/PostHog/posthog-js/network/alerts).

</details>
