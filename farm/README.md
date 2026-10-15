# Kern farm

Runs `kern check` on real merged pull requests that AI agents (Copilot, Devin, Codex, Claude, Cursor) wrote in well-known
companies' public JS/TS repositories. Each pull request gets its own GitHub Actions job and receipt; a last job adds them up.

## What is here

- `prs.json`: 60 pull requests, 12 per agent. Each has `repo`, `number`, `agent`, `title`, `base_sha` and `head_sha` as GitHub
  reports them, `merged_at`, `runner` (the test runner Kern finds in the root package.json at `base_sha`) and `why` it was picked.
  `merge_base` is where the branch left its base; Kern compares it with `head_sha`, as Kern's own workflows do.
  `known_bad: true` marks a change that was later reverted or fixed; `evidence` links the proof.
- `pr-texts/<owner>__<name>__<number>.md`: each pull request's title and text, given to Kern as `pr.md`.
- `farm.yml`: the workflow. `summarize.py`: turns the receipts into one table.

## How to run it

1. Push branch `one` to `jastijayakrishna/Kerner`: every job builds Kern from it.
2. Make a public test repository. Copy this folder into it as `farm/`, and `farm.yml` to `.github/workflows/farm.yml`.
3. Actions, then farm, then Run workflow. `limit` runs only the first N pull requests (0 runs all). 20 jobs run at once.
   The list is ordered so that a small `limit` gives every agent and small repositories first.
4. Each job builds Kern (static, as Kern's own CI does; cached by Cargo.lock), installs gVisor, makes a throwaway verifier as
   `drive/action.yml` does, fetches the commits with `--depth=200`, runs `KERN_CHECK_AI=0 kern check`, and always runs
   `kern drive clean`. It uploads `receipt-<owner>__<name>__<number>`: receipt.json, receipt.md, timing.json, step.log,
   check.json and check.err.
5. The `summary` job puts the table on the run's summary page and uploads `summary.md`.

To summarize downloaded artifacts by hand: `python3 summarize.py <artifacts-folder> prs.json summary.md`.

Jobs run on plain `ubuntu-24.04` runners, as a customer's would, so running out of disk, memory or time is a finding too.
A job that crashes or times out still uploads its timing and log; the summary shows it as `NO RECEIPT`, with the reason.
