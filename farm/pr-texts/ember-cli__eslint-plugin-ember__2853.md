# Update pnpm to v10.34.6

This PR contains the following updates:

| Package | Change | [Age](https://docs.renovatebot.com/merge-confidence/) | [Confidence](https://docs.renovatebot.com/merge-confidence/) |
|---|---|---|---|
| [pnpm](https://pnpm.io) ([source](https://redirect.github.com/pnpm/pnpm/tree/HEAD/pnpm/npm/pnpm)) | [`10.34.5` → `10.34.6`](https://renovatebot.com/diffs/npm/pnpm/10.34.5/10.34.6) | ![age](https://developer.mend.io/api/mc/badges/age/npm/pnpm/10.34.6?slim=true) | ![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/pnpm/10.34.5/10.34.6?slim=true) |

---

### Release Notes

<details>
<summary>pnpm/pnpm (pnpm)</summary>

### [`v10.34.6`](https://redirect.github.com/pnpm/pnpm/releases/tag/v10.34.6)

[Compare Source](https://redirect.github.com/pnpm/pnpm/compare/v10.34.5...v10.34.6)

##### Patch Changes

- [`e7888e5`](https://redirect.github.com/pnpm/pnpm/commit/e7888e5): `pnpm self-update` now resolves and verifies pnpm through registry, authentication, proxy, and TLS settings from trusted non-project configuration. Project configuration and the default project pnpmfile can no longer redirect the pnpm download or disable engine identity verification.

- [`46bc7c9`](https://redirect.github.com/pnpm/pnpm/commit/46bc7c9): pnpm no longer tells you to update itself with Corepack or with `pnpm add -g`:

  - The update notification now suggests `pnpm self-update`, or the [standalone install script](https://pnpm.io/installation) when pnpm is running under Corepack. It used to suggest `corepack use pnpm@<version>`, or `pnpm add -g pnpm` / `pnpm add -g @pnpm/exe` when pnpm was not installed by the standalone script — but `pnpm add -g` refuses to install pnpm and points at `pnpm self-update` anyway, and `@pnpm/exe` is not published for pnpm v12 or newer, where the unscoped `pnpm` package is itself the native executable.
  - `pnpm self-update` under Corepack now points at the standalone install script too, instead of telling you to update pnpm with Corepack.

- [`46bc7c9`](https://redirect.github.com/pnpm/pnpm/commit/46bc7c9): Updated `adm-zip` to v0.6.0, which fixes [a memory-exhaustion vulnerability](https://redirect.github.com/advisories/GHSA-xcpc-8h2w-3j85) where a crafted ZIP file could make it allocate 4 GB of memory. `adm-zip` is used to extract the Node.js, Bun, and Deno archives that pnpm downloads on Windows.

- Updated the embedded Node.js release keys to the current canonical `nodejs/release-keys` list.

- Updated the embedded npm registry signing keys to the set currently advertised by npm.

- [`702ad5f`](https://redirect.github.com/pnpm/pnpm/commit/702ad5f): Update the embedded Node.js release keys with the new key added to [nodejs/release-keys](https://redirect.github.com/nodejs/release-keys) (Stewart X Addison, `655F3B5C1FB3FA8D1A0CA6BDE4A7D232B936D2FD`).

<!-- sponsors -->

#### Platinum Sponsors

<table>
  <tbody>
    <tr>
      <td align="center" valign="middle">
        <a href="https://bit.cloud/?utm_source=pnpm&utm_medium=release_notes" target="_blank"><img src="https://pnpm.io/img/users/bit.svg" width="80" alt="Bit"></a>
      </td>
    </tr>
  </tbody>
</table>

#### Gold Sponsors

<table>
  <tbody>
    <tr>
      <td align="center" valign="middle">
        <a href="https://sanity.io/?utm_source=pnpm&utm_medium=release_notes" target="_blank">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/sanity.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/sanity_light.svg" />
            <img src="https://pnpm.io/img/users/sanity.svg" width="120" alt="Sanity" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://discord.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/discord.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/discord_light.svg" />
            <img src="https://pnpm.io/img/users/discord.svg" width="220" alt="Discord" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://vite.dev/?utm_source=pnpm&utm_medium=release_notes" target="_blank"><img src="https://pnpm.io/img/users/vitejs.svg" width="42" alt="Vite"></a>
      </td>
    </tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://serpapi.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/serpapi_dark.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/serpapi_light.svg" />
            <img src="https://pnpm.io/img/users/serpapi_dark.svg" width="160" alt="SerpApi" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://coderabbit.ai/?utm_source=pnpm&utm_medium=release_notes" target="_blank">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/coderabbit.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/coderabbit_light.svg" />
            <img src="https://pnpm.io/img/users/coderabbit.svg" width="220" alt="CodeRabbit" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://stackblitz.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/stackblitz.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/stackblitz_light.svg" />
            <img src="https://pnpm.io/img/users/stackblitz.svg" width="190" alt="Stackblitz" />
          </picture>
        </a>
      </td>
    </tr>
    <tr>
      <td align="center" valign="middle">
        <a href="https://workleap.com/?utm_source=pnpm&utm_medium=release_notes" target="_blank">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/workleap.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/workleap_light.svg" />
            <img src="https://pnpm.io/img/users/workleap.svg" width="190" alt="Workleap" />
          </picture>
        </a>
      </td>
      <td align="center" valign="middle">
        <a href="https://nx.dev/?utm_source=pnpm&utm_medium=release_notes" target="_blank">
          <picture>
            <source media="(prefers-color-scheme: light)" srcset="https://pnpm.io/img/users/nx.svg" />
            <source media="(prefers-color-scheme: dark)" srcset="https://pnpm.io/img/users/nx_light.svg" />
            <img src="https://pnpm.io/img/users/nx.svg" width="50" alt="Nx" />
          </picture>
        </a>
      </td>
    </tr>
  </tbody>
</table>

<!-- sponsors end -->

</details>

---

### Configuration

📅 **Schedule**: (UTC)

- Branch creation
  - "after 9pm on sunday"
- Automerge
  - At any time (no schedule defined)

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about these updates again.

---

 - [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job log](https://developer.mend.io/github/ember-cli/eslint-plugin-ember).
<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0NC4xMzQuMSIsInVwZGF0ZWRJblZlciI6IjQ0LjEzNC4xIiwidGFyZ2V0QnJhbmNoIjoibWFzdGVyIiwibGFiZWxzIjpbImRlcGVuZGVuY2llcyJdfQ==-->

