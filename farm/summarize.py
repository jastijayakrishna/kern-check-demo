#!/usr/bin/env python3
import json
import os
import re
import statistics
import sys
from collections import Counter, defaultdict


def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def text(path, tail=None):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            s = f.read()
    except OSError:
        return ""
    return s[-tail:] if tail else s


def key_of(repo, number):
    return f"{repo.replace('/', '__')}__{number}"


def cell(s, limit=None):
    s = " ".join(str(s).split())
    if limit and len(s) > limit:
        s = s[: limit - 1] + "…"
    return s.replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")


def count(v):
    if isinstance(v, list):
        return len(v)
    if isinstance(v, bool):
        return int(v)
    if isinstance(v, (int, float)):
        return int(v)
    return 0


def crash_reason(folder, timing):
    err = text(os.path.join(folder, "check.err"), tail=20000) if folder else ""
    if timing and timing.get("finished") is False and timing.get("why"):
        return str(timing["why"])
    for line in reversed([l for l in err.splitlines() if l.strip()]):
        try:
            j = json.loads(line)
        except ValueError:
            continue
        if isinstance(j, dict) and (j.get("reason") or j.get("why")):
            return str(j.get("reason") or j.get("why"))
    if timing:
        if timing.get("why"):
            return str(timing["why"])
        if timing.get("exit_code") not in (None, 0):
            last = [l for l in err.splitlines() if l.strip()]
            return f"kern check exited with {timing['exit_code']}" + (f": {last[-1]}" if last else "")
    if folder is None:
        return "the job uploaded nothing (it failed before its last step, or was cancelled)"
    last = [l for l in err.splitlines() if l.strip()]
    return last[-1] if last else "no receipt and no reason recorded"


def shape(reason):
    r = re.sub(r"\b[0-9a-f]{7,40}\b", "<sha>", reason)
    r = re.sub(r"`[^`]*`", "`…`", r)
    r = re.sub(r"\"[^\"]*\"", "\"…\"", r)
    r = re.sub(r"(?<![\w.])(?:[\w@.+-]+/)+[\w@.+-]*", "<path>", r)
    r = re.sub(r"\d+(\.\d+)?", "N", r)
    return " ".join(r.split())[:220]


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    root, prs_path = sys.argv[1], sys.argv[2]
    out_path = sys.argv[3] if len(sys.argv) > 3 else None
    prs = load(prs_path) or []
    info = {key_of(p["repo"], p["number"]): p for p in prs}
    plan = load(os.path.join(root, "plan", "plan.json"))
    wanted = [key_of(p["repo"], p["number"]) for p in (plan if isinstance(plan, list) else prs)]
    folders = {}
    if os.path.isdir(root):
        for name in sorted(os.listdir(root)):
            if name.startswith("receipt-") and os.path.isdir(os.path.join(root, name)):
                folders[name[len("receipt-"):]] = os.path.join(root, name)
    wanted += [k for k in folders if k not in wanted]

    rows, reasons, crashes = [], defaultdict(list), defaultdict(list)
    decisions, statuses, by_agent = Counter(), Counter(), defaultdict(Counter)
    sums, seconds = Counter(), []
    kinds = {"blocked": Counter(), "look": Counter()}
    known_bad = []
    for k in wanted:
        p = info.get(k, {})
        folder = folders.get(k)
        receipt = load(os.path.join(folder, "receipt.json")) if folder else None
        if not isinstance(receipt, dict) and folder:
            printed = load(os.path.join(folder, "check.json"))
            receipt = printed if isinstance(printed, dict) and printed.get("decision") else None
        timing = (load(os.path.join(folder, "timing.json")) if folder else None) or {}
        repo = p.get("repo") or timing.get("repo") or k
        number = p.get("number") or timing.get("number") or ""
        agent = p.get("agent") or timing.get("agent") or "?"
        name = f"{repo}#{number}"
        secs = timing.get("seconds")
        if isinstance(secs, (int, float)):
            seconds.append(secs)
        if not isinstance(receipt, dict):
            why = crash_reason(folder, timing)
            crashes[shape(why)].append((name, why))
            decisions["NO RECEIPT"] += 1
            by_agent[agent]["NO RECEIPT"] += 1
            rows.append([name, agent, "NO RECEIPT", why, "", "", "", "", "", "", "", "", secs if secs is not None else ""])
            if p.get("known_bad"):
                known_bad.append((name, agent, "NO RECEIPT", p.get("evidence", ""), 0, 0))
            continue
        decision = str(receipt.get("decision") or "?")
        decisions[decision] += 1
        by_agent[agent][decision] += 1
        if timing.get("exit_code") not in (None, 0):
            decision += f" (kern exited {timing['exit_code']})"
        for side in ("blocked", "look"):
            for x in receipt.get(side) or []:
                if isinstance(x, dict):
                    kinds[side][str(x.get("kind") or "?")] += 1
        tests = receipt.get("tests") if isinstance(receipt.get("tests"), dict) else {}
        rules = receipt.get("rules") if isinstance(receipt.get("rules"), dict) else {}
        status = str(tests.get("status") or "?")
        statuses[status] += 1
        why = str(tests.get("why") or "")
        if status == "RAN":
            shown = "RAN" + (f" ({tests['runner']})" if tests.get("runner") else "")
        else:
            shown = status + (": " + why if why else "")
            if status == "NOT_RUN":
                reasons[shape(why or "no reason given")].append((name, why or "no reason given"))
        n = {f: count(tests.get(f)) for f in ("kept", "broke", "flaky", "gone", "added")}
        n["powers"] = count(rules.get("powers"))
        n["tricks"] = count(rules.get("tricks"))
        n["not_checked"] = count(receipt.get("not_checked") if "not_checked" in receipt else rules.get("not_checked"))
        sums.update(n)
        rows.append([name, agent, decision, shown, n["kept"], n["broke"], n["flaky"], n["gone"], n["added"],
                     n["powers"], n["tricks"], n["not_checked"], secs if secs is not None else ""])
        if p.get("known_bad"):
            known_bad.append((name, agent, decision, p.get("evidence", ""), count(receipt.get("blocked")), count(receipt.get("look"))))

    md = ["# Kern farm: `kern check` on real agent pull requests", ""]
    md.append(f"{len(rows)} pull requests. The AI part was off (`KERN_CHECK_AI=0`).")
    md.append("")
    head = ["repo#PR", "agent", "decision", "tests", "kept", "broke", "flaky", "gone", "added", "powers", "tricks", "not_checked", "seconds"]
    md.append("| " + " | ".join(head) + " |")
    md.append("|" + "|".join(["---"] * 4 + ["---:"] * 9) + "|")
    for r in rows:
        md.append("| " + " | ".join(cell(x, 90 if i == 3 else None) for i, x in enumerate(r)) + " |")
    md.append("")
    md.append("## Totals")
    md.append("")
    md.append("- Decisions: " + (", ".join(f"{v} {k}" for k, v in decisions.most_common()) or "none"))
    md.append("- Tests: " + (", ".join(f"{v} {k}" for k, v in statuses.most_common()) or "none"))
    md.append("- Tests kept {kept}, broke {broke}, flaky {flaky}, gone {gone}, added {added}".format(**{f: sums[f] for f in ("kept", "broke", "flaky", "gone", "added")}))
    md.append(f"- Powers {sums['powers']}, tricks {sums['tricks']}, not checked {sums['not_checked']}")
    for side in ("blocked", "look"):
        if kinds[side]:
            md.append(f"- Items behind `{side}`, by kind: " + ", ".join(f"{k} {v}" for k, v in kinds[side].most_common()))
    if seconds:
        md.append(f"- Seconds per pull request: median {statistics.median(seconds):.0f}, longest {max(seconds):.0f}, all together {sum(seconds):.0f}")
    md.append("- By agent: " + "; ".join(f"{a}: " + ", ".join(f"{v} {k}" for k, v in c.most_common()) for a, c in sorted(by_agent.items())))
    if known_bad:
        md += ["", "## Known-bad pull requests (later reverted or fixed)", "",
               "Kern should not say `clear` for these.", "",
               "| repo#PR | agent | decision | blocked items | look items | evidence |", "|---|---|---|---:|---:|---|"]
        for name, agent, decision, evidence, b, l in known_bad:
            md.append(f"| {cell(name)} | {cell(agent)} | {cell(decision)} | {b} | {l} | {cell(evidence)} |")
    md += ["", "## Why the tests did not run (NOT_RUN), most common first", ""]
    if not reasons:
        md.append("None.")
    for _, items in sorted(reasons.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        md.append(f"- **{len(items)}×** {cell(items[0][1], 400)}")
        md.append("  - " + ", ".join(cell(n) for n, _ in items))
    md += ["", "## Jobs with no receipt (Kern or the job stopped), most common first", ""]
    if not crashes:
        md.append("None.")
    for _, items in sorted(crashes.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        md.append(f"- **{len(items)}×** {cell(items[0][1], 400)}")
        md.append("  - " + ", ".join(cell(n) for n, _ in items))
    out = "\n".join(md) + "\n"
    sys.stdout.write(out)
    if out_path:
        with open(out_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(out)


if __name__ == "__main__":
    main()
