# LITERATURE_AUDIT — 2026-09-09

Status: first-round novelty audit only; no open-status certification.

## S0 — exact seed

W. Qin, P. Zheng, **Boundedness in a production–consumption chemotaxis model with signal-dependent motility**, *Applied Mathematics Letters* 180 (2026), 109995.

Exact model:
\[
u_t=\Delta(\varphi(v)u),\qquad v_t=\Delta v+u-\alpha uv.
\]
They prove global classical uniform boundedness under an explicit smallness condition involving \(\varphi'^2/\varphi\), assuming \(\varphi>0\) and \(\varphi'<0\). Their paper frames large-time stabilization for the constant-sensitivity T-cell model as prior work, but the displayed main result for their signal-dependent-motility model is boundedness.

Relation to target: same model; our intended theorem begins after boundedness and seeks exponential stabilization.

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

Relation: same motility structure but pure consumption instead of simultaneous production–consumption. This is an important novelty-risk source and should be theorem-compared carefully.

## S3 — AML precedent for “boundedness + exponential stabilization”

F. Gao, H. Zhan, **Boundedness and exponential stabilization for time–space fractional parabolic–elliptic Keller–Segel model in higher dimensions**, *Applied Mathematics Letters* 144 (2023), 108699.

Relation: different model, but demonstrates that AML treats exponential stabilization built on boundedness as a suitable Letter-level contribution.

## S4 — exact-model novelty risk

Search terms used in the first pass included exact displayed equations and combinations of:
- production–consumption + signal-dependent motility + stabilization;
- asymptotic behavior / large-time behavior / exponential stabilization;
- T-cell + signal-dependent motility;
- boundedness implies stabilization.

No publication located in this first pass states exponential stabilization for the exact Qin–Zheng 2026 system. This is **not** an open-status certificate.

## Theorem-to-theorem comparison target

The paper should not be sold merely as “another stabilization result.” The strongest potentially distinctive statement is:

> For the exact production–consumption motility system, **uniform boundedness of the cell density alone forces exponential stabilization**, and the stabilization mechanism does not require monotonicity of the motility function.

This is stronger in structure than simply appending an asymptotic statement under all Qin–Zheng hypotheses.

## Recheck obligations before freeze

1. Forward citations / citing papers of Qin–Zheng 2026.
2. Same-author follow-ups by Qin and Zheng.
3. 2025–2026 papers with “global dynamics”, “large time behavior”, “relaxation”, or “stabilization” for signal-dependent motility.
4. Compare exact assumptions and convergence rate against Li–Zhao 2021 and Tao–Winkler 2025.
5. Search Chinese author-name variants and preprints/arXiv/Research Square where relevant.
