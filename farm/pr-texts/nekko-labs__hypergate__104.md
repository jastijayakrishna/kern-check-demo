# fix(search): CLI search discovers native Homebrew routes (v1.24.0)

## What & why

On a Mac with Homebrew, searching a CLI still offered `npm install -g …`. v1.17.0's ranking already puts a *present* system manager ahead of npm and the daemon already probes `brew` on PATH, so nothing was wrong with the preference — the route simply wasn't there to prefer. `searchCliCatalog` looks up a Homebrew formula on every search and then **throws it away**: curated and npm rows are deduped by package and command first, so the formula that matched the thing you searched for is dropped before ranking can see it.

Found-and-dropped becomes found-and-merged, and the lookup no longer depends on the query happening to be spelled like the formula. Candidate formula names are derived from each result row — its `command`, and `<publisher>-<command>` when it names a publisher, which is what turns Wrangler into homebrew-core's `cloudflare-wrangler` without anything tool-specific being written down. Nothing is added to the curated catalog: hand-written routes still state only what the vendor's own docs state, and this is discovery at search time.

```
candidates(row)      = [row.command, `${slug(publisher)}-${row.command}`]
accept(formula, row) = !formula.deprecated && !formula.disabled
                       && (formula.name === row.command || sameHost(formula.homepage, row.homepage))
row.installs        += { label: 'Homebrew', command: `brew install ${formula.name}`, note }
```

Constraints that matter as much as the mechanism:
- **Bounded**: only the first 3 curated/npm rows, candidate names deduped across the call, the existing query-name lookup reused rather than re-fetched, remaining lookups in parallel and soft-failing. A search must not turn into a fan-out, and static catalog browsing gets no lookups at all — 20+ formulae per catalog load would be absurd.
- **Verified, not guessed**: hostnames are compared, not registrable domains, so `foo.github.io` and `bar.github.io` are not "the same project"; deprecated and disabled formulae are refused.
- **Provenance is visible**: an accepted route carries the new `CliInstallOption.note`, rendered under the command, so the UI never implies the vendor documented a route it doesn't.
- Windows skips the enrichment entirely; homebrew-core's abandoned `playwright-cli` 0.1.x formula is excluded *by construction* — no candidate name derives to it from command `playwright` — rather than by a special case.

## Visual evidence

Same route, viewport, theme and data; `brew` present on PATH in both columns. Wrangler is the interesting one: the route is `brew install cloudflare-wrangler`, a formula name that appears nowhere in the repo.

| Before | After |
| --- | --- |
| ![vercel before](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmctYzhlYjhmYWI4NDZkNGY4N2EyNTk5M2FlZmRjN2Q5NmIiLCJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmctYzhlYjhmYWI4NDZkNGY4N2EyNTk5M2FlZmRjN2Q5NmIvMDk4MjM5NTYtZWEyYi00YjJlLThhYTEtZTNmNTAwMDE0NDBmIiwiaWF0IjoxNzg3OTg0NTIxLCJleHAiOjE3ODg1ODkzMjEsImZpbGVuYW1lIjoic3NfNGJjN2NlYTIucG5nIn0.Kr9AY46U7vWy6dk8xAbC57BcCRemrfrOQmzOv_OUGxQ) | ![vercel after](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmctYzhlYjhmYWI4NDZkNGY4N2EyNTk5M2FlZmRjN2Q5NmIiLCJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmctYzhlYjhmYWI4NDZkNGY4N2EyNTk5M2FlZmRjN2Q5NmIvZDA1ODIwZTMtZTI3NC00MjVlLWJiOTMtZGMyNTJkZDk1YzE0IiwiaWF0IjoxNzg3OTg0NTIxLCJleHAiOjE3ODg1ODkzMjEsImZpbGVuYW1lIjoic3NfYTAyNGYwNjUucG5nIn0.OdpkXXx1Q74h3vveVmCF2qzdcS4-edGvZ8A_Syuej5A) |
| ![wrangler before](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmctYzhlYjhmYWI4NDZkNGY4N2EyNTk5M2FlZmRjN2Q5NmIiLCJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmctYzhlYjhmYWI4NDZkNGY4N2EyNTk5M2FlZmRjN2Q5NmIvY2ZjMjM1NTMtYzMxNS00NTFjLWExYTItOGU0MjYwYWZiNzQ4IiwiaWF0IjoxNzg3OTg0NTIxLCJleHAiOjE3ODg1ODkzMjEsImZpbGVuYW1lIjoic3NfNjVjNWQ2OTQucG5nIn0.2AyKWf_3QznFr1rfjDnmxipjQlcwuZfn5SqR3PuPHeQ) | ![wrangler after](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJvcmctYzhlYjhmYWI4NDZkNGY4N2EyNTk5M2FlZmRjN2Q5NmIiLCJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmctYzhlYjhmYWI4NDZkNGY4N2EyNTk5M2FlZmRjN2Q5NmIvYmRlZmU2MDAtNDliMS00ZDAyLTkyZDEtYzdmZTU3Yjk0MzEwIiwiaWF0IjoxNzg3OTg0NTIxLCJleHAiOjE3ODg1ODkzMjEsImZpbGVuYW1lIjoic3NfNjFjMjI5NzcucG5nIn0.eWQKhhpfiHXLQy2BRCQSs796U0r9z2aMFYIPh7cfsp0) |

## Checklist

- [x] UI change: before/after screenshots attached (plus a short video if animation changed), or "no visual change"
- [x] Build, tests, and typecheck pass locally

328 core tests and 111 daemon tests pass (7 new canned-JSON cases: command match, publisher-derived name, hostname mismatch refused, Playwright never looked up, Windows skipped, soft failure, bounded/deduped lookups, and the enriched row beating npm through `chooseInstall`), workspace builds clean, `version:check` agrees at 1.24.0.


Link to Devin session: https://app.devin.ai/sessions/6c80fd2ae3a94ccaa3eecf42d72af71d
Open in Devin Desktop: https://app.devin.ai/desktop/session/6c80fd2ae3a94ccaa3eecf42d72af71d?variant=devin
