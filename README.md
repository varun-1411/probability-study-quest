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
