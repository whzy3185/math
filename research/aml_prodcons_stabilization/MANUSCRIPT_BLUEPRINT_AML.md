# MANUSCRIPT_BLUEPRINT_AML

Target: *Applied Mathematics Letters*
Date: 2026-09-09

## Preferred title

**A boundedness-to-stabilization principle for chemotaxis with signal-dependent motility**

Alternatives:
1. **Exponential stabilization from boundedness in signal-dependent-motility chemotaxis systems**
2. **Dissipative signal kinetics enforce exponential stabilization under signal-dependent motility**

The preferred title is broader than the Qin–Zheng model and makes the structural contribution visible immediately.

## Core message in one sentence

For
\[
u_t=\Delta(\varphi(v)u),\qquad v_t=\Delta v+uF(v),
\]
uniform boundedness of the cell density, together with a one-sided dissipative equilibrium of \(F\), forces exponential stabilization, independently of the sign of \(\varphi'\); the recent AML production–consumption model is an immediate corollary.

## Draft abstract content

We establish a boundedness-to-stabilization principle for a class of chemotaxis systems with signal-dependent motility. If the signal kinetics has a uniformly dissipative equilibrium \(v_*\), then every global classical solution with uniformly bounded cell density converges exponentially to the homogeneous state \((\bar u_0,v_*)\): the signal converges in \(W^{1,\infty}\) and the cell density in every finite \(L^p\). No monotonicity of the motility function is required in the stabilization argument. The key step is a mass-weighted Poincaré-type coercivity estimate which converts the signal dissipation into a spectral gap without an eventual pointwise lower bound for the cell density. As an application, we obtain exponential stabilization for the recent production–consumption model of Qin and Zheng (Applied Mathematics Letters, 2026).

Do not freeze this wording until novelty comparison with Li–Zhao 2021 and ZAMP 2026 is complete.

## Main theorem placement

Put the general theorem on page 1, before extended literature discussion.

### Theorem 1 — abstract stabilization

Let \(\Omega\subset\mathbb R^n\) be smooth, bounded and connected. Let \(\varphi\in C^1(I)\) be positive on a compact signal interval \(I\), and \(F\in C^1(I)\). Assume there exist \(v_*\in I\), \(\beta>0\) such that
\[
(s-v_*)F(s)\le-\beta(s-v_*)^2,\qquad s\in I.
\]
If a nonnegative global classical solution has positive conserved cell mass and
\[
\sup_{t>0}\|u(t)\|_\infty<\infty,
\]
then for every \(p<\infty\),
\[
\|u(t)-\bar u_0\|_{L^p}+\|v(t)-v_*\|_{W^{1,\infty}}
\le C_pe^{-\lambda_pt}.
\]
No sign restriction on \(\varphi'\) is needed.

### Proposition 2 — weaker hypothesis for signal decay

If only
\[
\sup_t\|u(t)\|_2<\infty,
\]
then
\[
\|v(t)-v_*\|_2\le Ce^{-\lambda t}.
\]

This should be included only if it fits naturally without diluting the main theorem.

### Corollary 3 — Qin–Zheng production–consumption model

For
\[
F(s)=1-\alpha s,
\qquad v_*=1/\alpha,
\]
condition (D) holds exactly:
\[
(s-1/\alpha)(1-\alpha s)=-\alpha(s-1/\alpha)^2.
\]
Therefore every bounded global classical solution of the Qin–Zheng system stabilizes exponentially. In particular, their 2026 boundedness theorem supplies the hypothesis.

## Key lemma — the only lemma that deserves prominence

### Lemma (mass-weighted coercivity)

If \(\rho\ge0\), \(\int_\Omega\rho=m>0\), and \(\|\rho\|_2\le K\), then
\[
\|f\|_2^2\le C_{\Omega,m,K}
\left(\|\nabla f\|_2^2+\int_\Omega\rho f^2\right)
\]
for every \(f\in H^1(\Omega)\).

This is the proof-engine of the paper. It avoids Harnack/eventual positivity and works for sign-changing \(v-v_*\).

## Suggested six-page architecture

### Page 1 — Introduction + theorem

Four paragraphs only:
1. signal-dependent motility and the 2026 production–consumption motivation;
2. nearest stabilization literature: Tao–Winkler 2025 and Li–Zhao 2021;
3. precise gap: boundedness known for exact model, stabilization mechanism not isolated for dissipative kinetics;
4. contribution and why monotonicity disappears after boundedness.

State Theorem 1 and Corollary 3 on page 1 or early page 2.

### Pages 2–3 — Coercivity + signal stabilization

- prove mass-weighted coercivity in ~8 lines;
- set \(w=v-v_*\);
- energy + dissipativity + coercivity gives exponential \(L^2\);
- one paragraph Duhamel/Neumann semigroup upgrade to \(W^{1,\infty}\).

### Pages 3–4 — Cell stabilization

- set \(q=u-\bar u_0\);
- one energy identity;
- Young + Poincaré + signal gradient decay;
- interpolate \(L^2\) with bounded \(L^\infty\) to every finite \(L^p\).

### Page 4–5 — Exact model corollary + comparison

- verify \(F(s)=1-\alpha s\) in one line;
- cite Qin–Zheng boundedness theorem;
- explain that \(\varphi'<0\) belongs to the boundedness input, not the stabilization principle;
- mention pure consumption \(F(s)=-s\) as a unifying special case, while clearly crediting Li–Zhao 2021.

### Remaining space — references

Keep bibliography lean (~15–20 references). Avoid broad chemotaxis history beyond what is needed for theorem positioning.

## What not to include

- numerical simulations;
- a separate preliminaries section;
- Harnack/eventual positivity route;
- long discussion of biological modeling;
- multiple variants of the same theorem;
- an \(L^\infty\) rate for \(u\) unless it is closed cleanly without lengthening the paper;
- claims that the problem is “open” until final search audit.

## Referee-facing novelty sentence (working version)

The new point is not the general fact that bounded chemotaxis solutions may stabilize; rather, it is the identification of a model-independent dissipativity mechanism which converts boundedness into exponential stabilization for the signal-dependent-motility class, without a motility monotonicity assumption, and which applies directly to the newly studied production–consumption model.

This sentence must be rechecked against final prior art before use.

## Current readiness

- Correctness of finite-\(p\) theorem: strong; core proof closed modulo standard published semigroup estimate already pinned.
- Exact-model corollary: mathematically closed given Qin–Zheng boundedness theorem.
- General theorem novelty: promising, not certified.
- Optional \(u\)-\(L^\infty\) exponential rate: not needed; still available as a strengthening target.
- Manuscript prose: not yet frozen.
