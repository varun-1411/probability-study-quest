# Probability Study Quest

A self-study course from rigorous probability to stochastic processes, MDPs, reinforcement learning and game theory, built around one running engineering case: an airport taxi stand.

## Open the app

- **Website (any browser, no login):** https://varun-1411.github.io/probability-study-quest/
  Progress is saved in your browser. Use *Rewards → Download backup* to move it between devices.
- **Claude version (Ask Claude hints, progress synced to a Claude account):** https://claude.ai/artifact/646yyG8GEYHXpB4VCX5fKS

Both run the same code from `docs/`.

## What is here

| Path | Contents |
| --- | --- |
| `ROADMAP.md` | The full curriculum: phases, modules, books, schedule, rewards, research thread |
| `CURRICULUM-INDEX.md` | Compact index used to keep module numbering and formats consistent |
| `docs/` | The study app (GitHub Pages site): `index.html`, `plan.json`, `modules/<id>.json` |
| `pdf/` | Each module as a PDF: notes, problem set, then hints and full solutions |
| `src/content/` | Module sources in Markdown with LaTeX (notes, then `### <id>` problems with `#### Hint` and `#### Solution`) |
| `src/` | Build scripts: `schedule_build.py` (dated two-track schedule), `build.py` (app JSON, PDFs, plan), `outlines.py` (module previews) |
| `assets/` | Roadmap diagrams |

## Continuing from any Claude account

This repo is the home of the course, independent of any one Claude account. From a Claude session on any account connected to this GitHub account, attach this repository and say what you need, for example "write module 3.5" or "rebuild and publish". New modules go in `src/content/`; run `python3 src/schedule_build.py` and `python3 src/build.py` (needs pandoc and XeLaTeX), then commit `docs/` and `pdf/`.

## Your progress

Progress is not stored in this repo. Download a backup from the app now and then, and keep it somewhere safe; *Rewards → Restore from file* loads it into either version of the app.

## Moving to a new Claude account

Claude accounts cannot change their email address, and conversations, projects and memory do not transfer between personal accounts. Everything the course needs is in this repo, so a new account can rebuild it in about ten minutes.

1. **In the old account:** *Rewards → Download backup* in the app. Optionally, in Settings, export your memory as text.
2. **In the new account, make a project** (for example "prob theory") with the same description, and upload `CURRICULUM-INDEX.md` from this repo.
3. **In a chat in that project, ask Claude:** "Set up my study app from github.com/varun-1411/probability-study-quest. Follow the README section *Moving to a new Claude account*." Claude then:
   - publishes `docs/index.html`, `docs/plan.json` and every `docs/modules/*.json` as one artifact titled "Probability Study Quest", keeping the same paths;
   - declares its capabilities as `{"db": {"rules": [{"path": "progress", "read": "admin", "write": "admin"}, {"path": "drafts", "read": "admin", "write": "admin"}]}, "downloads": {}, "sample": {}, "user": {}}`;
   - sets `LINKS.claude` in `docs/index.html` to the new artifact's URL, republishes, and commits that change here (pushing needs the Claude GitHub app to have access to this repo);
   - updates the app URL and slug in `CURRICULUM-INDEX.md` and in the project's copy of it.
4. **Open the new app:** *Rewards → Restore from file* with your backup. Your XP, weeks, solved problems, doubts and rewards come back.
5. **Memory (optional):** paste the exported memory into the new account's memory import (Settings), or just tell Claude the few things that matter.

Unreviewed module drafts generated in the old app are not in the backup; reviewed modules are, because they live in this repo.
