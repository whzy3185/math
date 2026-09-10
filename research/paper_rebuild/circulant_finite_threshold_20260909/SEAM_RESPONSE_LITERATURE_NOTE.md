# Literature note: Laplacian perturbations, effective resistance, and the seam-response proof

This note records literature relevant to `ODD_RESONANCE_SEAM_RESPONSE.md`.  It is contextual only: the `2x2` response theorem in this project is proved directly by rank-one identities and a Schur complement.

## 1. Weighted Laplacian definiteness and effective resistance

Daniel Zelazo and Mathias Bürger, **On the Definiteness of the Weighted Laplacian and its Connection to Effective Resistance**, arXiv:1408.2187 (2014), study when graph Laplacians with negative edge weights remain positive semidefinite.  For a single adverse edge, the admissible magnitude is governed by the effective resistance between its endpoints in the positive subnetwork; the paper also develops multiple-edge extensions.

Wei Chen, Ji Liu, Yongxin Chen, Sei Zhen Khong, Dan Wang, Tamer Başar, Li Qiu and Karl H. Johansson, **Characterizing the positive semidefiniteness of signed Laplacians via Effective Resistances**, Proceedings of the 55th IEEE Conference on Decision and Control (2016), 985--990, DOI `10.1109/CDC.2016.7798396`, give a generalized effective-resistance matrix criterion for Laplacians with multiple adverse weights.

Karel Devriendt, **Effective resistance is more than distance: Laplacians, simplices and the Schur complement**, *Linear Algebra and its Applications* 639 (2022), 24--49, DOI `10.1016/j.laa.2022.01.002`, is a useful modern reference for the Schur-complement viewpoint on Laplacians and effective resistance.

## 2. Relation to the present finite signed-circulant problem

Our matrix is not introduced as an arbitrary weighted Laplacian with negative edge weights.  Instead an exact two-walk calculation produces

\[
8I-A^2=L_\Sigma+E_-+E_+,
\]

where `L_Sigma` is a genuine positive signed-edge-square Laplacian and `E_-,E_+` are two off-diagonal seam terms.  The identities

\[
E_-=d_-d_-^T-r_-r_-^T,
\qquad
E_+=r_+r_+^T-d_+d_+^T
\]

turn this into

\[
8I-A^2=H-UU^T,
\]

with `H>0` and `U` having two columns.  Thus positivity is equivalent to

\[
I_2-U^TH^{-1}U>0.
\]

This is mathematically analogous to a two-port effective-resistance test, but the paper should present the above derivation explicitly rather than cite a control-theory result as a black box.

## 3. Recommended manuscript wording

A safe formulation is:

> The two seam terms admit an exact two-port reduction.  After moving the positive rank-one pieces into the signed Laplacian, the remaining adverse perturbation has rank two.  A Schur-complement calculation therefore reduces the positivity of `8I-A_sigma^2` to a `2x2` response matrix.  This is analogous to effective-resistance criteria for Laplacians with adverse edge weights, although the criterion required here follows directly from the finite defect identity.

Avoid calling `U^TH^{-1}U` literally the classical effective-resistance matrix unless the incidence/terminal convention is matched carefully.  `Seam-response matrix` or `two-port response matrix` is the safer primary terminology.

## 4. Why this improves the paper's architecture

The fixed-step absorbers at `s=5,7,9,11,13` should now be presented as concrete sufficient certificates for the same exact response condition, not as five unrelated tricks.  The logical order in the final manuscript should be:

1. derive the universal two-seam defect identity;
2. derive the `2x2` response criterion;
3. prove fixed-step threshold theorems by local certificates / finite bases;
4. state the remaining two-parameter response problem as the natural general frontier.

This makes the new odd-resonance section read as one structural theorem plus applications, rather than a sequence of ad hoc computations.