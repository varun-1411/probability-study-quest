import datetime as dt, json
from pathlib import Path
HERE = Path(__file__).parent
start = dt.date(2026,11,23)  # Week 1 Monday
H = 6  # hours per track per week
theory = [("0.1","Proofs, sets, functions",12),("0.2","Real analysis",60),("0.4","Multivariable calculus",12),
  ("0.5","Measure theory",72),("0.7","Functional analysis",24),
  ("1.1","Elementary probability",12),("1.2","Probability spaces & RVs",36),("1.3","Expectation & transforms",24),
  ("1.4","Convergence & limit theorems",36),("1.5","Conditional expectation",18),("1.6","Martingales & concentration",36),
  ("2.1","Sampling & data reduction",24),("2.2","Point estimation",24),("2.3","Tests & intervals",24),("2.4","Asymptotic theory",24),
  ("2.5","Regression & linear models",24),("2.6","Bayesian & computational",24),("2.7","Input/output analysis",24),
  ("6.1","Strategic & extensive games",36),("6.2","Repeated & stochastic games",24),("6.3","Algorithmic GT & mechanisms",24),
  ("6.4","Congestion & traffic equilibrium",12),("6.5","Queueing games & platforms",36),
  ("4.7","Revenue management & pricing",24)]
model = [("0.3","Linear algebra & matrices",48),("0.8","ODEs & transforms",36),("0.6","Optimization",24),
  ("3.1","Discrete-time Markov chains",24),("3.2","Poisson & renewal",36),("3.3","Continuous-time Markov chains",24),
  ("3.4","Queueing theory",48),("3.5","Matrix-analytic methods",36),("3.6","Simulation & gradients",36),("3.7","Stochastic approximation",36),("3.9","Numerical methods for Markov chains",18),
  ("4.1","Finite-horizon DP",24),("4.2","Discounted MDPs",24),("4.3","Average & total cost",24),("4.4","Control of queues",36),
  ("4.5","Constrained MDPs & POMDPs",12),("4.6","Approximate DP",36),
  ("5.1","Tabular RL review",12),("5.2","RL convergence theory",36),("5.3","Bandits",24),("5.4","Policy gradient & actor-critic",36),("5.6","Deep RL for operations",36)]
def expand(mods):
    seq=[]
    for code,name,h in mods:
        w=int(round(h/H))
        for i in range(w): seq.append((code,name,i+1,w))
    return seq
T=expand(theory); M=expand(model)
n=max(len(T),len(M)); print("study weeks", len(T), len(M))
rows=[]; cal=0; study=0; boss_n=0
while study<n:
    study+=1; cal+=1
    d=start+dt.timedelta(weeks=cal-1)
    t=T[study-1] if study<=len(T) else None
    m=M[study-1] if study<=len(M) else None
    rows.append(dict(cal=cal,study=study,date=d.isoformat(),
        theory=(f"{t[0]} {t[1]} ({t[2]}/{t[3]})" if t else "Catch-up / review"),
        model=(f"{m[0]} {m[1]} ({m[2]}/{m[3]})" if m else "Catch-up / review"), boss=""))
    if study%12==0 or study==n:
        boss_n+=1; cal+=1; d=start+dt.timedelta(weeks=cal-1)
        rows.append(dict(cal=cal,study="",date=d.isoformat(),theory="BOSS WEEK %d: review + exit checks"%boss_n,model="BOSS WEEK %d: catch-up + reward"%boss_n,boss="Boss %d"%boss_n))
end=start+dt.timedelta(weeks=cal-1, days=6)
print("calendar weeks",cal,"boss",boss_n,"end",end)
# phase spans in calendar dates
def span(track_seq, prefixes):
    ws=[r for r in rows if r['study']!='' and any((r[track_seq]).startswith(p) for p in prefixes)]
    a=dt.date.fromisoformat(ws[0]['date']); b=dt.date.fromisoformat(ws[-1]['date'])+dt.timedelta(days=6)
    return a.isoformat(), b.isoformat()
spans = {
 'th-found': span('theory',['0.']),'th-prob': span('theory',['1.']),'th-stat': span('theory',['2.']),'th-game': span('theory',['6.']),
 'mo-found': span('model',['0.']),'mo-proc': span('model',['3.']),'mo-mdp': span('model',['4.']),'mo-rl': span('model',['5.'])}
print(json.dumps(spans,indent=1))
print("boss dates",[r['date'] for r in rows if r['boss']])
# module finish weeks
fin={}
for r in rows:
    if r['study']=='':continue
    for k in ('theory','model'):
        code=r[k].split(' ')[0]; fin[code]=(r['cal'],r['date'])
json.dump(dict(rows=rows,spans=spans,fin=fin,theory=theory,model=model),open(HERE/'sched.json','w'),indent=1)

