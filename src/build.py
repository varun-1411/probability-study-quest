"""Build app module JSON + PDF from content/*.md, and plan.json from the schedule."""
import json, re, subprocess, sys, hashlib, datetime as dt
from outlines import O
from pathlib import Path

SRC = Path(__file__).parent
ROOT = SRC.parent
SITE = ROOT / "docs"
TIERS = {"I": "Intuition", "A": "Drill", "B": "Proof", "C": "Engineering",
         "D": "Code lab", "T": "Taxi thread"}


def pandoc_html(md: str) -> str:
    if not md.strip():
        return ""
    out = subprocess.run(["pandoc", "-f", "markdown", "-t", "html", "--mathjax", "--no-highlight"],
                         input=md, capture_output=True, text=True, check=True)
    return out.stdout.strip()


def parse(path: Path):
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    meta = {}
    for line in m.group(1).splitlines():
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"')
    body = text[m.end():]
    notes, probs = body.split("<!-- PROBLEMS -->")
    notes = notes.replace("<!-- NOTES -->", "").strip()
    problems = []
    for chunk in re.split(r"\n### ", "\n" + probs.strip())[1:]:
        head, _, rest = chunk.partition("\n")
        pid = head.strip()
        parts = re.split(r"\n#### (Hint|Solution)\n", "\n" + rest)
        prompt = parts[0].strip()
        sec = {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}
        if pid.startswith("Q"):
            tier = "Phase " + pid[1]
        else:
            tier = TIERS[pid[0]]
        problems.append(dict(id=pid, tier=tier, prompt=prompt,
                             hint=sec.get("Hint", ""), solution=sec.get("Solution", "")))
    return meta, notes, problems


def build_module(path: Path):
    meta, notes, problems = parse(path)
    data = dict(id=meta["id"], title=meta["title"], track=meta.get("track", ""),
                weeks=meta.get("weeks", ""), notesHtml=pandoc_html(notes), notesSrc=notes, problems=[])
    for p in problems:
        data["problems"].append(dict(
            id=p["id"], tier=p["tier"], promptSrc=p["prompt"],
            promptHtml=pandoc_html(p["prompt"]), hintHtml=pandoc_html(p["hint"]),
            solutionHtml=pandoc_html(p["solution"])))
    raw = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    data["version"] = hashlib.sha1(raw.encode()).hexdigest()[:10]
    out = SITE / "modules" / f"{meta['id']}.json"
    out.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    print(f"{out.name}: {out.stat().st_size/1024:.1f} KB, {len(problems)} problems")
    if meta["id"] != "diag":
        build_pdf(meta, notes, problems)
    return meta


def build_pdf(meta, notes, problems):
    lines = [f"# Notes", "", notes, "", "# Problem set", ""]
    for p in problems:
        lines += [f"**{p['id']} ({p['tier']}).** {p['prompt']}", ""]
    lines += ["# Hints", ""]
    for p in problems:
        if p["hint"]:
            lines += [f"**{p['id']}.**", "", p["hint"], ""]
    lines += ["# Solutions", ""]
    for p in problems:
        if p["solution"]:
            lines += [f"**{p['id']}.**", "", p["solution"], ""]
    md = "\n".join(lines)
    # demote the notes' "##" headings under "# Notes" stay as subsections
    pdf = ROOT / "pdf" / f"Module-{meta['id']}.pdf"
    cmd = ["pandoc", "-f", "markdown", "-o", str(pdf), "--pdf-engine=xelatex",
           "-M", f"title=Module {meta['id']}: {meta['title']}",
           "-M", "subtitle=Probability roadmap · notes, problem set, hints and solutions",
           "-V", "geometry:margin=2.4cm", "-V", "fontsize=11pt", "-V", "colorlinks=true",
           "-V", "linkcolor=blue", "--toc", "-V", "toc-depth=2", "-V", "documentclass=article"]
    subprocess.run(cmd, input=md, text=True, check=True)
    print(f"{pdf.name}: {pdf.stat().st_size/1024:.1f} KB")


def build_plan(available):
    S = json.loads((SRC / "sched.json").read_text())
    core = {"0.5", "0.8", "1.4", "1.5", "1.6", "2.4", "2.7", "3.3", "3.4", "3.5", "3.6", "3.7", "3.9",
            "4.3", "4.4", "4.6", "4.7", "5.2", "5.4", "6.5"}
    order = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.1", "1.2", "1.3", "1.4",
             "1.5", "1.6", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "3.1", "3.2", "3.3", "3.4",
             "3.5", "3.6", "3.7", "3.8", "3.9", "4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7", "4.8", "5.1", "5.2", "5.3",
             "5.4", "5.5", "5.6", "6.1", "6.2", "6.3", "6.4", "6.5", "6.6"]
    names = {c: n for c, n, h in S["theory"] + S["model"]}
    names.update({"0.9": "PDE primer", "3.8": "Brownian motion & stochastic calculus",
                  "5.5": "Sample complexity", "6.6": "Mean-field games & MARL",
                  "4.8": "Optimal control & fluid models"})
    th = {c for c, n, h in S["theory"]}
    mods = []
    for c in order:
        fin = S["fin"].get(c)
        tp, rd, pr, nd, why = O[c]
        mods.append(dict(code=c, name=names[c], outline=dict(topics=tp, read=rd, problems=pr, needs=nd, why=why),
                         track=("Theory" if c in th else "Modeling") if fin else "Optional",
                         finish=(dt.date.fromisoformat(fin[1]) + dt.timedelta(days=6)).isoformat() if fin else None,
                         core=c in core, available=c in available))
    weeks = [dict(n=0, date="2026-11-16", theory="Placement diagnostic", model="Placement diagnostic",
                  boss=False, diag=True)]
    for r in S["rows"]:
        weeks.append(dict(n=r["cal"], date=r["date"], theory=r["theory"], model=r["model"],
                          boss=bool(r["boss"]), diag=False))
    levels = [[1, "Set Builder", 0, "Starting line: you are here"],
              [2, "Epsilon Hunter", 750, "Movie or F1 race night"],
              [3, "Measure Keeper", 2000, "A book you want that is not a textbook"],
              [4, "Almost Surely", 3750, "New MMA or sports gear"],
              [5, "Queue Whisperer", 6000, "A day trip"],
              [6, "Unbiased Estimator", 8500, "Cross one item off your wishlist"],
              [7, "Bellman's Apprentice", 11000, "Tickets to a match, concert or show"],
              [8, "Policy Optimizer", 13500, "A weekend trip"],
              [9, "Equilibrium Seeker", 16500, "Upgrade something you use every day"],
              [10, "Grandmaster of Uncertainty", 20000, "The big one: a Northeast India trip"]]
    badges = [["first-proof", "First Proof", "First Tier B problem solved with no hints", 50, "manual"],
              ["counterexamples", "Counterexample Collector", "10 counterexamples built", 100, "manual"],
              ["streak-4", "On a Roll", "4 weeks in a row with 10+ hours", 100, "auto"],
              ["streak-12", "Iron Habit", "12 weeks in a row with 10+ hours", 300, "auto"],
              ["streak-26", "Half-Year Machine", "26 weeks in a row with 10+ hours", 600, "auto"],
              ["sim-agrees", "Simulation Agrees", "A code-lab result lands inside its theoretical confidence interval", 50, "manual"],
              ["bug-hunter", "Bug Hunter", "Find a real error in a textbook or in one of my problem sets", 100, "manual"],
              ["no-hint", "No-Hint Hero", "A whole problem set without opening the hints", 150, "manual"],
              ["taxi-architect", "Taxi Architect", "All seven taxi-thread steps done", 500, "auto"]]
    taxi = ["Write the taxi-stand generator as a block-tridiagonal QBD; prove irreducibility",
            "Prove merged zone arrivals are Poisson; Chernoff-bound buffer overflow",
            "Estimate time-varying arrival rates; test exponential interarrivals",
            "Uniformization error bound; matrix-geometric solution; compare SPSA, IPA and LR gradients",
            "Taxi release as a CTMDP; prove the threshold policy; solve by LP and RVI",
            "Q-learning and PPO against the exact policy; bandit surge pricing",
            "Join-or-cruise queueing game; design the toll or surge that aligns it"]
    plan = dict(version=dt.date.today().isoformat(), start="2026-11-23", weeks=weeks, modules=mods,
                levels=levels, badges=badges, taxi=taxi)
    (SITE / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, separators=(",", ":")))
    print(f"plan.json: {(SITE/'plan.json').stat().st_size/1024:.1f} KB, {len(weeks)} weeks, {len(mods)} modules")


if __name__ == "__main__":
    avail = []
    for f in sorted((SRC / "content").glob("*.md")):
        meta = build_module(f)
        avail.append(meta["id"])
    build_plan(avail)
