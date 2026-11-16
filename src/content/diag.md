---
id: "diag"
title: "Placement diagnostic"
track: Both
weeks: "Week 0"
---

<!-- NOTES -->

## How to take it

Take one block per phase: 60 minutes, closed book, on paper. Solve 3 of the 4 problems in a block cleanly and that phase runs in **fast mode** (problems first, skim the reading).

- Use **Check my answer** under a problem to get quick feedback from Claude on your attempt.
- For grading and re-planning, send your answers (photos or LaTeX) to me in the project chat. I mark each phase full or fast, and every later date in your schedule moves to match.
- Mark Week 0 done on the Today screen when you have sent them: that is your first 100 XP.

There are no model solutions here on purpose: the point is to find out what you can already do.

<!-- PROBLEMS -->

### Q0-1
Prove that a countable union of countable sets is countable. Where does the argument use a choice?

### Q0-2
Let $f_n(x)=x^n$ on $[0,1]$. Does $f_n$ converge uniformly? Decide whether $\lim_n\int_0^1f_n=\int_0^1\lim_nf_n$, and name the theorem that justifies your answer.

### Q0-3
Let $Q$ be the generator of an irreducible finite-state CTMC. Prove that 0 is a simple eigenvalue of $Q$ and that every other eigenvalue has negative real part.

### Q0-4
Derive Fatou's lemma from the monotone convergence theorem. Give an example where its inequality is strict.

### Q1-1
Let $X_1,X_2,\dots$ be i.i.d. with $E|X_1|<\infty$. Prove that $\max(|X_1|,\dots,|X_n|)/n\to0$ almost surely.

### Q1-2
Construct a sequence of random variables that converges in probability but not almost surely. Prove that some subsequence converges almost surely.

### Q1-3
Define $E[X\mid\mathcal G]$ for integrable $X$, prove that it exists using the Radon–Nikodym theorem, and prove the tower property.

### Q1-4
Prove that $\mathrm{Binomial}(n,\lambda/n)$ converges in distribution to $\mathrm{Poisson}(\lambda)$ using characteristic functions.

### Q2-1
$X_1,\dots,X_n$ are i.i.d. Exponential($\lambda$). Find the MLE of $\lambda$, its bias, the UMVUE, and an exact 95% confidence interval for $\lambda$.

### Q2-2
For i.i.d. Poisson counts, find the most powerful test of $\lambda=\lambda_0$ against $\lambda=\lambda_1>\lambda_0$. Show that it is uniformly most powerful against $\lambda>\lambda_0$.

### Q2-3
From $n$ interarrival times and $n$ service times of an M/M/1 queue, give the asymptotic distribution of the MLE of $\rho=\lambda/\mu$, using the delta method.

### Q2-4
With a Gamma prior on a Poisson rate, derive the posterior and the posterior predictive distribution of next hour's count.

### Q3-1
Taxis arrive as a Poisson($\alpha$) process to a buffer of size $K$; passengers arrive as a Poisson($\beta$) process and leave at once if no taxi is waiting. Find the stationary distribution of the number of waiting taxis.

### Q3-2
Derive the Pollaczek–Khinchine formula for the mean waiting time in an M/G/1 queue, using the mean residual service time.

### Q3-3
For a CTMC with bounded rates, prove $P(t)=\sum_{n\ge0}e^{-\Lambda t}\frac{(\Lambda t)^n}{n!}P^n$ with $P=I+Q/\Lambda$, and bound the error of truncating the sum after $N$ terms.

### Q3-4
State the Robbins–Monro step-size conditions. Explain why SPSA needs only two cost evaluations per step, whatever the dimension.

### Q4-1
Prove that the Bellman operator of a discounted MDP is a $\gamma$-contraction in the sup norm, and deduce that value iteration converges.

### Q4-2
Write the primal LP of a finite discounted MDP and its dual. Interpret the dual variables as discounted occupation measures.

### Q4-3
Admission control to an M/M/1 queue: reward $R$ per admitted customer, holding cost $h$ per customer per unit time. Prove that an optimal policy is a threshold policy.

### Q4-4
State the average-cost optimality equation and a condition, such as the unichain condition, under which it has a solution.

### Q5-1
State conditions under which tabular Q-learning converges almost surely, and sketch the stochastic-approximation proof.

### Q5-2
Derive the policy gradient theorem for the discounted objective.

### Q5-3
Explain the deadly triad and describe Baird's counterexample.

### Q5-4
Derive the $O(\log n)$ regret bound of UCB1 for a $K$-armed bandit.

### Q6-1
Prove von Neumann's minimax theorem for finite two-player zero-sum games using LP duality.

### Q6-2
Prove that every finite game has a mixed-strategy Nash equilibrium, using Brouwer's or Kakutani's fixed-point theorem.

### Q6-3
In Naor's observable M/M/1 model, show that the individually optimal joining threshold is at least the socially optimal one, and find the toll that aligns them.

### Q6-4
Show that a Wardrop equilibrium solves Beckmann's convex program, and construct an instance of Braess's paradox.
