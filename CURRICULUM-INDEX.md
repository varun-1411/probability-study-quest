# Curriculum index — probability → stochastic processes → MDPs → RL → game theory

Source of truth: the live doc "Probability → Stochastic Processes → MDPs → RL → Game Theory: Research-Aligned Curriculum" (https://claude.ai/artifact/YQgvydscMpbENNTDQYPLhk). This file is a compact index so problem sets keep consistent numbering. Created 2026-11-16.

## Style (user asked 2026-11-16): plain language, intuition first, then rigor
- Module loop: story (taxi stand) → picture → precise definitions/proofs → practice → teach-back.
- Problem sets and solutions: plain-words explanation first, then the rigorous argument.
- User asked 2026-11-16 that notes be elaborate, not rushed: Module 0.1 was rewritten to this standard (about 7,500 words of notes). Every section: the idea in plain words and why probability needs it, the precise definition, worked examples (taxi stand), common mistakes, quick checks with answers; proofs start with a one-line plan. Write all future modules this way. Module 0.2 was written before this request in the compressed style; offer to expand it.

## Problem-set format (every module, "PS <module>")
- 20–25 problems: I Intuition (2–3), A Drill (6–8), B Proof (6–8), C Engineering (3–5), D Code lab in Python (1–2), T Taxi thread (1).
- Hints plus full solutions in a separate file. Exit check: 3-hour closed-book, pass at 70%.
- Pace assumption: 12 h/week (4 read/reprove, 5 problems, 2 code, 1 review). Weeks below are full / fast.

## Study app (main home, replaces the sheet)
- "Probability Study Quest" https://claude.ai/artifact/646yyG8GEYHXpB4VCX5fKS (slug 28ec9c7d-fb53-4639-a8b7-c9f5d5ba5c65). Published from files: index.html, plan.json, modules/<id>.json.
- Progress lives in the app's db doc `progress/state` (weeks{n:{done,hours}}, mods{code:{ps,code,teach,exit,solved{}}}, badges{}, taxi{}, rewards{}, doubts{code:[{q,a,t}]}, lastLevel). Read it with db_get before writing the next problem set, and check `doubts` for questions the user asked in the app's notes "Have a doubt?" box. Capabilities declared: db (rules: progress read/write admin), user, sample.
- Sharing: link viewers can read notes/problems; their progress saves only in their browser; Ask Claude does not work for them. "Can edit" invitees could read/overwrite the owner's progress doc, so advise "Can view".
- Content source + build: markdown per module (notes, then "### <id>" problems with "#### Hint" / "#### Solution"); build.py makes modules/<id>.json for the app and a LaTeX PDF (hints and solutions at the back). Add a module = publish_files patch with modules/<id>.json + plan.json (available flag).
- Modules done so far: diag (28 prompts, no solutions by design), 0.1 (notes + 23 problems), 0.2 Real analysis (written 2026-11-16 at the user's request; notes + 23 problems; D1 = uniformization vs expm on the taxi birth-death chain, T1 = uniform-in-time truncation bound, N = 190 for Lambda*T = 132 at 1e-6). Next: 0.3 before Week 1, unless the user's requests say otherwise. The app hides the Requested tag once a module is available, so old entries in `requests` can be ignored.
- Every module has a preview in the app (plan.json modules[].outline: topics, read, problems, needs, why). User can tap "Request the reviewed version": stored in progress `requests{code: timestamp}`. Write requested modules first, oldest request first.
- On-the-spot drafts (Claude version only): "Generate it now (draft)" calls Claude from the page (modelTier complex, cache off) in 7 parts: notes, then problems in batches I1–I3+A1–A3 | A4–A7 | B1–B4 | B5–B8 | C1–C3 | D1+T1. Stored in db doc `drafts/<code>` {code, title, notes, parts{p1..p6}, pend, status partial|complete, startedAt, finishedAt}; rule drafts read/write admin. The app renders drafts with marked@12.0.2 and shows a "Draft, not yet reviewed" banner. A published modules/<code>.json always wins over a draft.
- "Review module X": read `drafts/X` with db_get on the app artifact, check every proof and run every code lab, fix errors, convert to src/content/mX.md, build JSON + PDF, publish to the artifact and GitHub. The reviewed file then replaces the draft automatically.
- Backup: Rewards screen has Download backup / Copy backup / Restore from file (JSON {app, saved, progress}). Capabilities now: db, user, sample, downloads.
- Build sources: repo src/ (authoritative; build.py, schedule_build.py, outlines.py, content/*.md). Copies in this project under claude/app-src/ are refreshed when they change. To rebuild: clone the repo, run src/schedule_build.py then src/build.py (writes docs/modules/<id>.json, docs/plan.json, pdf/), then publish_files patch to slug 28ec9c7d-fb53-4639-a8b7-c9f5d5ba5c65 and push.
- Old sheet "Study Schedule & XP Tracker" https://claude.ai/artifact/MzxAEHRihyx2FeHG4yRs2f is superseded; delete only if the user asks.

## Schedule + rewards
- Two tracks, 6 h/week each. Week 0 = 16–22 Nov 2026 (diagnostic); Week 1 = 23 Nov 2026; boss week every 13th week (weeks 13, 26, …, 117); fast path ends ~18 Feb 2029.
- Theory track order: 0.1, 0.2, 0.4, 0.5, 0.7, 1.1–1.6, 2.1–2.7, 6.1–6.5. Modeling track order: 0.3, 0.8, 0.6, 3.1–3.7, 4.1–4.6, 5.1–5.4, 5.6.
- XP: diagnostic 100; PS 100; code lab 50; exit ≥70% 150 (+50 at ≥85%); teach-back 100; taxi step 150; 10+ h week 20; boss cleared 300; badges 50–600.
- Levels (XP): 1 Set Builder 0; 2 Epsilon Hunter 750; 3 Measure Keeper 2000; 4 Almost Surely 3750; 5 Queue Whisperer 6000; 6 Unbiased Estimator 8500; 7 Bellman's Apprentice 11000; 8 Policy Optimizer 13500; 9 Equilibrium Seeker 16500; 10 Grandmaster of Uncertainty 20000.

## Modules
### Phase 0 — Foundations (53 / 24 wks)
- 0.1 Proofs, sets, functions — Velleman; Hammack (3/1)
- 0.2 Real analysis — Abbott; Rudin ch. 1–7 (10/5)
- 0.3 Linear algebra + matrix analysis (Perron–Frobenius, M-matrices, matrix exponential, Kronecker) — Axler LADR 4e; Horn & Johnson (8/4)
- 0.4 Multivariable calculus — Rudin ch. 9–10 / Munkres (3/1)
- 0.5 Measure theory — Axler MIRA / Tao; Folland ch. 1–3 (10/6)
- 0.6 Optimization (LP duality, KKT, convexity, SGD) — Boyd & Vandenberghe; Bertsimas & Tsitsiklis (6/2)
- 0.7 Functional analysis light (Banach fixed point, projections) — Kreyszig (4/2)
- 0.8 ODEs + transforms (x' = Ax, matrix exponential, Picard, Lyapunov/LaSalle stability; Laplace & Laplace–Stieltjes incl. numerical inversion; Fourier + convolution theorem; z-transforms) — Hirsch, Smale & Devaney; Schiff; Stein & Shakarchi (6/3)
- 0.9 PDE primer, optional (heat/transport, characteristics, Kolmogorov backward + Fokker–Planck, HJB) — Strauss; only before 3.8 or 6.6 (3/0)
- Verdict given to user: ODEs needed (CTMCs, SA ODE method, fluid limits); Laplace needed (M/G/1, renewal, transient CTMC); Fourier mostly covered via characteristic functions; PDEs optional.

### Phase 1 — Rigorous probability (24 / 13.5 wks) — covers Bilkent IE 523 + martingales
Lecture spine: Jagannathan NPTEL "Probability Foundations for Electrical Engineers" (notes modules 0–5).
- 1.1 Elementary probability — Bertsekas & Tsitsiklis; Blitzstein & Hwang (4/1)
- 1.2 Probability spaces, RVs, Borel–Cantelli, 0–1 laws — Rosenthal; G&S One Thousand Exercises (4/3)
- 1.3 Expectation, inequalities, transforms — G&S 4e ch. 3–5 (4/2)
- 1.4 Convergence, LLN, CLT, Poisson limit — Durrett 5e ch. 2–3; Shiryaev Problems (5/3)
- 1.5 Conditional expectation — Williams ch. 9 (2/1.5)
- 1.6 Martingales + concentration — Williams ch. 10–14; Vershynin HDP ch. 2 (5/3)

### Phase 2 — Statistics (25 / 14 wks)
- 2.1 Sampling, sufficiency, exponential families — Casella & Berger ch. 5–6 (4/2)
- 2.2 Point estimation — C&B ch. 7 (4/2)
- 2.3 Tests and intervals — C&B ch. 8–9 (4/2)
- 2.4 Asymptotics — C&B ch. 10; van der Vaart (3/2)
- 2.5 Regression, GLMs — Wasserman; ISLP (3/2)
- 2.6 Bayesian + computational — Wasserman; BDA3 (4/2)
- 2.7 Input/output analysis for stochastic models — Law; Asmussen & Glynn (3/2)

### Phase 3 — Stochastic processes (39 / 20 wks)
- 3.1 DTMCs, mixing — Norris ch. 1; Levin & Peres (4/2)
- 3.2 Poisson + renewal — Gallager; Ross (5/3)
- 3.3 CTMCs, uniformization, phase-type — Norris ch. 2–3; Kulkarni (4/2)
- 3.4 Queueing (incl. time-varying, fluid/diffusion, double-ended) — Harchol-Balter; Whitt (6/4)
- 3.5 Matrix-analytic methods / QBDs — Latouche & Ramaswami; Neuts (4/3)
- 3.6 Simulation + gradient estimation (SPSA, IPA, LR) — Asmussen & Glynn; Spall (4/3)
- 3.7 Stochastic approximation — Borkar 2e; Kushner & Yin (4/3)
- 3.8 Brownian motion + stochastic calculus (optional) — Le Gall (8/0)

### Phase 4 — MDPs (20 / 13 wks)
- 4.1 Finite-horizon DP — Bertsekas Vol. I; Ross (3/2)
- 4.2 Discounted — Puterman ch. 6 (3/2)
- 4.3 Average/total cost — Puterman ch. 8–9 (3/2)
- 4.4 Structure + control of queues, CTMDPs — Puterman ch. 11; Sennott (4/3)
- 4.5 Constrained MDPs, POMDPs — Altman; Krishnamurthy (3/1)
- 4.6 Approximate DP — Powell; Bertsekas Vol. II (4/3)

### Phase 5 — RL (22 / 12 wks)
- 5.1 Tabular review — Sutton & Barto (3/1)
- 5.2 Convergence theory — Bertsekas & Tsitsiklis NDP; Szepesvári; Meyn (4/3)
- 5.3 Bandits — Lattimore & Szepesvári (4/2)
- 5.4 Policy gradient, actor–critic — AJKS; Konda & Tsitsiklis (4/3)
- 5.5 Sample complexity (optional) — AJKS (3/0)
- 5.6 Deep RL for operations — Dai & Gluzman 2022; Qin et al. 2020; Lin et al. 2018 (4/3)

### Phase 6 — Game theory (25 / 11 wks)
- 6.1 Strategic + extensive form — Maschler, Solan & Zamir; Osborne & Rubinstein (6/3)
- 6.2 Repeated, stochastic, Markov games — MSZ; Filar & Vrieze (3/2)
- 6.3 Algorithmic game theory, mechanism design — Roughgarden; Nisan et al. (4/2)
- 6.4 Congestion + traffic equilibrium — Sheffi; Roughgarden (3/1)
- 6.5 Queueing games + platform pricing — Hassin & Haviv; Hassin; Banerjee–Johari–Riquelme (4/3)
- 6.6 Mean-field games + MARL (optional) — Carmona & Delarue (5/0)

## Taxi thread (Tier T) — one model grows across phases
Base model: taxis arrive from the city to a buffer of size K; passengers arrive in flight-driven waves.
- P0 generator as block-tridiagonal QBD; P1 Poisson merging + Chernoff overflow bound; P2 rate estimation + GOF; P3 uniformization error bound, matrix-geometric solution, SPSA vs IPA vs LR; P4 CTMDP release policy, threshold proof, LP/RVI, wait constraint; P5 Q-learning/PPO vs exact, bandit surge pricing; P6 Naor-type join-or-cruise game, toll/surge design.

## Paths
- Research core (~53 wks): 0.5, 0.8, 1.4–1.6, 2.4, 2.7, 3.3–3.7, 4.3, 4.4, 4.6, 5.2, 5.4, 6.5
- Fast (~108 wks): all modules, known material in problems-only mode after the placement diagnostic
- Full (~210 wks): all 48 modules at full depth
