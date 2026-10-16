# Fix warning about workspaces in public projects

Thanks for asking me to work on this. I will get started on it and keep this PR's description up to date as I form a plan and make progress.

> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>warning Workspaces can only be enabled in private projects.</issue_title>
> <issue_description>### Issue Description
> 
> I get warning "Workspaces can only be enabled in private projects." when installing `@apollo/client` using `yarn`.
> 
> ### Link to Reproduction
> 
> -
> 
> ### Reproduction Steps
> 
> 1. Create an empty project, run `yarn init`.
> 2. Add `@apollo/client`:
> ```
> $ yarn add graphql rxjs @apollo/client
> yarn add v1.22.22
> info No lockfile found.
> [1/4] Resolving packages...
> [2/4] Fetching packages...
> [3/4] Linking dependencies...
> warning Workspaces can only be enabled in private projects.
> [4/4] Building fresh packages...
> success Saved lockfile.
> warning Workspaces can only be enabled in private projects.
> success Saved 8 new dependencies.
> info Direct dependencies
> ├─ @apollo/client@4.1.7
> ├─ graphql@16.13.2
> └─ rxjs@7.8.2
> info All dependencies
> ├─ @apollo/client@4.1.7
> ├─ @graphql-typed-document-node/core@3.2.0
> ├─ @wry/context@0.7.4
> ├─ @wry/equality@0.5.7
> ├─ graphql-tag@2.12.6
> ├─ graphql@16.13.2
> ├─ optimism@0.18.1
> └─ rxjs@7.8.2
> Done in 1.02s.
> ```
> 
> ### `@apollo/client` version
> 
> 4.1.7</issue_description>
> 
> <agent_instructions>We need to remove the `workspaces` key from `package.json` when creating the build. The script is located at `config/prepareDist.ts` and already removes some fields. Let's also remove `workspaces`. Add additional suggestions to the PR for fields that might also need removing. Do not remove these extra fields until we've reviewed them. If no additional fields, note that as well.</agent_instructions>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> <comment_new><author>@jerelmiller</author><body>
> Hey @broyde 👋 
> 
> Doing a bit of digging around the community and looks like either [updating yarn](https://github.com/yarnpkg/yarn/issues/8580) works (if you need a quick fix) or [removing the `workspaces` key](https://github.com/reduxjs/react-redux/issues/1815) from package.json.
> 
> I don't have a ton of capacity to do that right now, but if you'd want to contribute, we'd accept a PR. Note that we'll probably need to strip out that `workspaces` key during build (when the package.json is copied over into the `dist` directory).
> 
> If not, I'll try and take a look as soon as I get some time available.</body></comment_new>
> </comments>
