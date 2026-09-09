# LITERATURE_AUDIT — 2026-09-09

Status: two-pass novelty audit after material theorem strengthening; no open-status certification.

## S0 — exact seed

W. Qin, P. Zheng, **Boundedness in a production–consumption chemotaxis model with signal-dependent motility**, *Applied Mathematics Letters* 180 (2026), 109995.

Exact model:
\[
u_t=\Delta(\varphi(v)u),\qquad v_t=\Delta v+u-\alpha uv.
\]
They prove global classical uniform boundedness under an explicit smallness condition involving \(\varphi'^2/\varphi\), assuming \(\varphi>0\) and \(\varphi'<0\). Their paper frames large-time stabilization for the constant-sensitivity T-cell model as prior work, but the displayed main result for their signal-dependent-motility model is boundedness.

Relation to target: same model. Our stabilization theorem begins after boundedness and, in its current proved form, removes the sign condition on \(\varphi'\) from the stabilization mechanism.

## S1 — closest production–consumption stabilization analogue

Y. Tao, M. Winkler, **Stabilization in a chemotaxis system modelling T-cell dynamics with simultaneous production and consumption of signals**, *European Journal of Applied Mathematics* 36 (2025), 570–583.

Model:
\[
u_t=\Delta u-\nabla\cdot(u\nabla v),\qquad v_t=\Delta v+u-\alpha uv.
\]
They prove global solvability and stabilization to \((\bar u_0,1/\alpha)\) under small-signal/large-consumption assumptions.

Relation: same production–consumption reaction in the signal equation, but different cell equation (classical sensitivity rather than signal-dependent motility).

## S2 — direct signal-consumption motility analogue

D. Li, J. Zhao, **Global boundedness and large time behavior of solutions to a chemotaxis–consumption system with signal-dependent motility**, *ZAMP* 72 (2021).

Model:
\[
u_t=\Delta(\gamma(v)u),\qquad v_t=\Delta v-uv.
\]
For positive motility they prove boundedness and exponential convergence to constant equilibria.

Relation: same motility structure but pure consumption instead of simultaneous production–consumption. The strengthened abstract theorem now contains this reaction law as the special case \(F(s)=-s\), so this source must be discussed as a predecessor rather than ignored.

## S3 — AML precedent for “boundedness + exponential stabilization”

F. Gao, H. Zhan, **Boundedness and exponential stabilization for time–space fractional parabolic–elliptic Keller–Segel model in higher dimensions**, *Applied Mathematics Letters* 144 (2023), 108699.

Relation: different model, but demonstrates that AML treats exponential stabilization built on boundedness as a suitable Letter-level contribution.

## S4 — broader “boundedness implies convergence” risk

There are precedents in other chemotaxis/tumor-invasion systems explicitly phrased as boundedness implying exponential convergence. Therefore that slogan alone cannot carry novelty.

There are also several signal-dependent-motility papers with asymptotic stabilization under logistic, indirect production, or indirect consumption mechanisms, including:
- Lv–Wang, JMAA 2020, indirect production + logistic source;
- Lv–Wang, Proc. R. Soc. Edinburgh A 2020, generalized logistic source;
- Liu–Gao–Guo, ZAMP 2026, indirect signal production/consumption and global dynamics;
- Huang–Wang–Ke, CSIAM Trans. Appl. Math. 2026, indirect consumption with degenerate motility.

These are materially different systems, but they raise the bar for how the present theorem must be positioned.

## Strengthened theorem after pass 1

The proof has been upgraded from the exact Qin–Zheng kinetics to the general system
\[
u_t=\Delta(\varphi(v)u),\qquad v_t=\Delta v+uF(v),
\]
under a dissipativity hypothesis: there are \(v_*\) and \(\beta>0\) such that
\[
(s-v_*)F(s)\le-\beta(s-v_*)^2
\]
on the bounded signal range.

Under uniform boundedness of \(u\), the proved conclusion is
\[
\|u(t)-\bar u_0\|_{L^p}
+\|v(t)-v_*\|_{W^{1,\infty}}
\le C_pe^{-\lambda_pt}
\qquad\forall p<\infty.
\]
The signal \(L^2\)-decay actually needs only a uniform \(L^2\)-bound on \(u\).

## Pass-2 search result for the abstract theorem

Search variants included exact and synonym forms of
\[
u_t=\Delta(\gamma(v)u),\qquad v_t=\Delta v+uF(v),
\]
combined with stabilization, large-time behavior, dissipative kinetics, boundedness implies convergence, and signal-dependent/density-suppressed motility.

No source located in this pass states the above abstract dissipativity-to-exponential-stabilization principle. Search results instead concern specific logistic, production, consumption, prey-taxis, or indirect-signal systems.

This remains **Observed**, not a certified novelty statement.

## Current theorem-to-theorem positioning

The strongest defensible contribution architecture is now:

1. **General structural theorem:** boundedness plus one-sided dissipative signal kinetics forces exponential stabilization for signal-dependent motility, without any monotonicity requirement on \(\varphi\).
2. **Mechanism:** an elementary mass-weighted coercivity inequality closes the signal energy without eventual pointwise positivity/Harnack.
3. **Timely exact corollary:** the Qin–Zheng 2026 production–consumption model has \(F(s)=1-\alpha s\), hence \(v_*=1/\alpha\) and \(\beta=\alpha\); their bounded solution therefore stabilizes exponentially.
4. **Unification:** the pure consumption law \(F(s)=-s\) is another special case, linking the principle to Li–Zhao 2021.

This is substantially stronger than writing a model-specific follow-up note.

## Remaining novelty obligations before manuscript freeze

1. Forward citations / citing papers of Qin–Zheng 2026.
2. Same-author follow-ups by Qin and Zheng.
3. Exact theorem comparison with Li–Zhao 2021: hypotheses on positive/nonmonotone motility, norm/rate of convergence, and proof mechanism.
4. Exact theorem comparison with Liu–Gao–Guo ZAMP 2026 on indirect signal mechanisms.
5. Search MathSciNet/zbMATH/Google Scholar style variants for abstract \(F(v)\) kinetics and the phrase “dissipative signal kinetics”.
6. Re-run the search immediately before submission freeze.
