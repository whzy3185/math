# DEEP NOVELTY AUDIT — 2026-09-09

Target journal: *Applied Mathematics Letters*

Status: theorem-to-theorem prior-art audit after strengthening. This document does **not** certify that the problem is open or that the theorem is novel. It records what was located, what is already known, and the safest current contribution claim.

## Current theorem under audit

For
\[
 u_t=\Delta(\varphi(v)u),\qquad v_t=\Delta v+uF(v),
\]
assume a global nonnegative classical solution, conserved positive cell mass, a compact signal range, uniform boundedness of \(u\), \(\varphi\in C^1\) with \(\min\varphi>0\), and an equilibrium \(v_*\) satisfying
\[
F(v_*)=0,
\qquad
(s-v_*)F(s)\le-\beta(s-v_*)^2.
\]
Then for every finite \(p\),
\[
\|u(t)-\bar u_0\|_{L^p}
+\|v(t)-v_*\|_{W^{1,\infty}}
\le C_pe^{-\lambda_pt}.
\]
The stabilization implication does not require \(\varphi'<0\).

The exact 2026 AML production–consumption model is obtained from
\[
F(s)=1-\alpha s,\qquad v_*=1/\alpha.
\]

## P0 correction found during audit

The previous draft said the dissipativity inequality alone implies \(F(v_*)=0\). This is false when \(v_*\) is an endpoint of the admissible signal interval. The general theorem has therefore been corrected to assume \(F(v_*)=0\) explicitly. This does not change either the production–consumption or pure-consumption special case.

---

## Comparison matrix

| Source | Cell equation / signal law | Main large-time result | Relation to present theorem | Collision risk |
|---|---|---|---|---|
| Qin–Zheng, AML 180 (2026), 109995 | \(u_t=\Delta(\varphi(v)u)\); \(v_t=\Delta v+u-\alpha uv\) | Global uniformly bounded classical solution under an explicit motility condition | **Exact same model**, but located main theorem is boundedness rather than stabilization | Key seed; no direct collision located |
| Tao–Winkler, EJAM 36 (2025), 570–583 | \(u_t=\Delta u-\nabla\cdot(u\nabla v)\); same \(v_t=\Delta v+u-\alpha uv\) | Stabilization to \((\bar u_0,1/\alpha)\) under small-signal / large-consumption assumptions | Same biological reaction, different chemotactic flux | Medium |
| D. Li–J. Zhao, ZAMP 72 (2021), Art. 57 | \(u_t=\Delta(\gamma(v)u)\); \(v_t=\Delta v-uv\) | Global bounded classical solution for positive motility; exponential convergence to constant equilibria | **Same motility structure**, pure consumption \(F(s)=-s\), which is contained in our abstract class | High predecessor risk |
| X. Li–L. Wang–X. Pan, ZAMP 72 (2021), Art. 170 | \(u_t=\Delta(r(v)u)+\mu u(1-u)\); \(v_t=\Delta v-uv\) | Boundedness and exponential convergence to \((1,0)\) | Same motility + pure consumption, but logistic cell source destroys mass conservation | Medium |
| G. Li–M. Winkler, CMS 21 (2023), 299–322 | \(u_t=\Delta(u\phi(v))\); \(v_t=\Delta v-uv\) | Global very weak solutions; stabilization in \(n\le3\) for positive \(\phi\) | Same motility + pure consumption; much weaker solution setting and different objective | Medium/high predecessor |
| L. Wang, JDE 348 (2023), 191–222 | signal-dependent motility + consumption + logistic source | Boundedness/global dynamics and convergence | Different reaction and mass balance | Medium |
| Liu–Gao–Guo, ZAMP 77 (2026), Art. 26 | signal-dependent motility with **indirect** signal production/consumption | Boundedness and exponential stabilization in several indirect cases | Three-component / indirect mechanism, not the present two-component local law | Medium |
| Zhao–Wang, ZAMP 76 (2025), Art. 229 | signal-dependent motility with indirect production/consumption | Boundedness and asymptotic behavior in indirect models | Three-component mechanism | Low/medium |
| Zheng–Wang, ZAMP 77 (2026), Art. 46 | classical chemotactic sensitivity with synchronous production/consumption | Improved global boundedness criterion | Same production/consumption idea, different flux | Low |

---

## What is already known and must not be claimed as new

### 1. Exponential stabilization with signal-dependent motility is not new in itself

Li–Zhao (2021) already prove exponential convergence for the direct pure-consumption system
\[
u_t=\Delta(\gamma(v)u),\qquad v_t=\Delta v-uv
\]
with positive motility. Therefore a sentence such as

> “We establish exponential stabilization for chemotaxis with signal-dependent motility for the first time.”

would be false.

### 2. Stabilization for simultaneous production–consumption kinetics is not new in itself

Tao–Winkler study
\[
u_t=\Delta u-\nabla\cdot(u\nabla v),\qquad v_t=\Delta v+u-\alpha uv
\]
and prove stabilization to \((\bar u_0,1/\alpha)\). Hence the biological reaction mechanism cannot itself carry novelty.

### 3. “Boundedness implies stabilization” is too broad a slogan

The chemotaxis literature contains many boundedness-plus-stabilization results, including logistic and indirect-signal variants. The paper must identify the precise structural implication, not advertise the generic slogan as unprecedented.

### 4. The mass-weighted coercivity inequality should not be advertised as a new functional inequality

It is elementary and follows from Poincaré plus control of the mean. The safe claim is that it provides a short mechanism tailored to the present proof, not that the inequality itself is new.

---

## What was NOT located in the audit

The search was repeated using exact equations, exact paper title, author names, and variants involving:

- production–consumption / simultaneous production and consumption;
- signal-dependent / density-suppressed motility;
- stabilization / exponential stabilization / large-time behavior / global dynamics / relaxation;
- abstract kinetics \(uF(v)\), dissipative reaction, one-sided dissipativity;
- same-author follow-ups and recent 2025–2026 work.

No located source states exponential stabilization for the **exact Qin–Zheng two-component signal-dependent-motility production–consumption system**.

No located source states the exact abstract principle under the hypothesis
\[
F(v_*)=0,
\qquad
(s-v_*)F(s)\le-\beta(s-v_*)^2
\]
with the finite-\(p\) / \(W^{1,\infty}\) exponential conclusion and no monotonicity assumption on \(\varphi\) in the stabilization stage.

These are negative search observations, **not** proofs of novelty or open status.

---

## Theorem-to-theorem assessment

### Exact-model corollary: strongest novelty position

For Qin–Zheng's exact model,
\[
u_t=\Delta(\varphi(v)u),\qquad v_t=\Delta v+u-\alpha uv,
\]
their theorem supplies boundedness under a strong condition on \(\varphi\). The present argument shows that once any bounded global classical solution is available, its large-time dynamics are rigid:
\[
(u,v)\to(\bar u_0,1/\alpha)
\]
exponentially in finite \(L^p\times W^{1,\infty}\), without using the sign of \(\varphi'\) in the stabilization step.

This appears to complete the boundedness result by identifying the asymptotic state and rate for the same model.

Current confidence: **medium-high as a model-specific gap**, but still Observed rather than certified.

### Abstract theorem: stronger mathematics, higher novelty risk

The abstract \(F(v)\) theorem unifies the production–consumption and pure-consumption kinetics. No direct statement was located. However, because the pure-consumption case already has strong prior results, a referee could view the abstract theorem as a clean generalization of a familiar mechanism unless the paper emphasizes a genuinely sharper feature.

Current confidence: **medium**.

### No-monotonicity stabilization implication

The proof only needs positive \(\varphi\) and bounded \(\varphi'\) on the actual signal range, not \(\varphi'<0\). This separation between assumptions needed for boundedness and assumptions needed for relaxation is potentially useful and should be stated precisely:

> monotonicity is not required for the conditional stabilization theorem.

Do **not** phrase this as weakening the full Qin–Zheng global-existence theorem; their monotonicity/smallness assumptions still enter when their result is used to guarantee boundedness.

Current confidence: **mathematically proved; novelty significance medium**.

---

## Safe and unsafe manuscript claims

### Safe now

- “We prove a conditional exponential-stabilization principle for bounded classical solutions of a class of signal-dependent-motility systems with dissipative signal kinetics.”
- “The stabilization implication requires positivity, but not monotonicity, of the motility on the bounded signal range.”
- “As an application, the bounded solutions obtained by Qin and Zheng (2026) converge exponentially to \((\bar u_0,1/\alpha)\).”
- “The proof uses a mass-weighted coercivity estimate to close the signal energy directly, without an eventual pointwise lower bound for the cell density.”

### Unsafe now

- “This is the first stabilization result for signal-dependent motility.”
- “The production–consumption stabilization problem was open.”
- “Our weighted Poincaré inequality is new.”
- “We remove the Qin–Zheng assumptions on \(\varphi\)” without the qualifier “from the stabilization implication only.”
- “The general theorem is novel” as a certified statement before another pre-submission search.

---

## Referee-style risk assessment

### Risk R1 — “The generalization is routine from Li–Zhao 2021.”
Severity: **high**.

Response strategy: do not rely only on replacing \(-v\) by \(F(v)\). Emphasize the nonzero signal equilibrium \(v_*=1/\alpha\), the exact contemporary AML model, the clean separation of boundedness from asymptotics, and strengthen the convergence norm if possible.

### Risk R2 — finite \(L^p\) convergence of \(u\) may look weaker than nearby stabilization results
Severity: **medium-high**.

Response strategy: close exponential \(L^\infty\)-convergence of \(u\). A plausible route is uniform Hölder regularity for bounded uniformly parabolic solutions for \(t\ge t_0\), followed by Hölder–\(L^2\) interpolation. This should be the next P4 strengthening target before manuscript freeze.

### Risk R3 — “The exact-model corollary is too short.”
Severity: **medium**.

Response strategy: lead with the abstract stabilization theorem, then present Qin–Zheng as a sharp/timely corollary. Keep the proof mechanism structural and concise.

### Risk R4 — novelty overclaim around the coercivity estimate
Severity: **medium**.

Response strategy: call it an elementary mass-weighted coercivity lemma, not a new inequality.

---

## Audit verdict

**Do not abandon the project.** No direct collision with the exact 2026 AML model was located, and the proof gives a clean completion of its long-time dynamics. However, the surrounding pure-consumption literature is strong enough that the paper should not be submitted yet with only the current finite-\(p\) formulation.

Recommended next priority:

\[
\boxed{\text{P4: prove exponential }L^\infty\text{-stabilization of }u.}
\]

If this closes, the natural target statement becomes
\[
\|u(t)-\bar u_0\|_\infty
+\|v(t)-v_*\|_{W^{1,\infty}}
\le Ce^{-\lambda t},
\]
which is substantially cleaner, directly comparable with prior stabilization literature, and better suited to an AML Letter.

After that strengthening, rerun the theorem-to-theorem search once more and only then enter manuscript/referee mode.
