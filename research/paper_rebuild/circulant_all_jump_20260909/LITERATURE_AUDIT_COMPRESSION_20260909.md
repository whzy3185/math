# Literature boundary audit for the compressed periodic theorem

Date: 2026-09-09

Status: current targeted audit, not a proof of priority or exhaustive novelty.

## 1. Closest signed-circulant source

Vaibhav Suvagiya, **Signed circulants at the Ramanujan bound**, arXiv:2607.18334 (2026), studies the special graph family `C_n(1,2)`. The retrieved 2026 version classifies the four switching classes under the unbalanced-quadrilateral / alternating-triangle-flux constraint, computes the twisted spectral radius, verifies finite global optimality for small even `n`, and states the twisted global-minimizer conjecture.

The retrieved paper does not formulate the general step family `C_N(1,s)` as an all-jump periodic problem, and it does not contain a theorem organized by `v_2(s)` or a period-`2^{v_2(s)+1}` compression mechanism.

This should be used as the historical motivation for the jump-two starting point, not as the general periodic-operator background.

Primary public source checked:

- arXiv:2607.18334, `Signed circulants at the Ramanujan bound`, posted July 2026.

## 2. Periodic magnetic/Floquet graph theory is established background

The following literature confirms that Floquet fibers, magnetic phases on quotient graphs, and spectral-gap analysis on periodic discrete graphs are standard tools:

- E. Korotyaev and N. Saburova, **Magnetic Schrödinger operators on periodic discrete graphs**, *Journal of Functional Analysis* 272 (2017), 1625--1660, DOI 10.1016/j.jfa.2016.12.015. The paper develops Floquet fiber representations for periodic discrete magnetic operators and studies spectral bands and flux dependence.

- J. S. Fabila-Carrasco, F. Lledó and O. Post, **Spectral gaps and discrete magnetic Laplacians**, *Linear Algebra and its Applications* 547 (2018), 183--216, DOI 10.1016/j.laa.2018.02.006; arXiv:1710.01157. The paper interprets Floquet parameters as magnetic potentials on finite quotients and derives spectral-gap localization methods.

Accordingly Paper I must not present Bloch decomposition, magnetic/Floquet parameters, or the general idea of using a finite quotient to study an infinite periodic graph as new.

## 3. Block-Jacobi transfer matrices are established background

Transfer-matrix methods for block Jacobi recurrences are also standard. For example, the literature on block Jacobi matrices explicitly formulates generalized eigenvector recurrences and associated matrix transfer maps.

The novelty claim, if ultimately retained, therefore cannot be "we use a 4 x 4 transfer matrix". It must concern the problem-specific reduction and theorem produced by that transfer matrix.

## 4. What appears specific to the present work

The current Paper-I theorem package contains the following problem-specific combination:

1. the period-two variational parity bifurcation for signed step operators;
2. the two-defect flux word with signed-reflection chirality for every even half-period `L`;
3. the theorem that for every
   \[
   s=L(2q+1),\qquad L\ge4\text{ even},
   \]
   that period-`2L` two-defect phase has continuous squared Bloch edge below `8`;
4. the `2`-adic specialization
   \[
   v_2(s)=k\ge2
   \Longrightarrow
   \text{period }2^{k+1}\text{ suffices};
   \]
5. the uniform quadratic gap and sharp constant
   \[
   L^2g_{L,q}\to4\arccos^2(1/3)
   \]
   uniformly in the odd multiplier;
6. eventual exact locking of the global Bloch edge to the periodic phase `z=1`.

Targeted searches on 2026-09-09 using combinations of

- `signed circulant`,
- `C_N(1,s)`,
- `2-adic`,
- `period compression`,
- `two-defect`,
- `periodic signed graph`,
- `block Jacobi`,
- `Floquet spectral gap`

did not return a public paper directly matching this theorem package.

This is evidence for a potentially new result, **not** a proof that no prior result exists.

## 5. Required caution in the manuscript

Safe wording:

> We are not aware of a previous result giving a `2`-adic short-period construction of this form for signed step circulants. The Floquet and transfer-matrix tools used in the proof are standard; the arithmetic compression theorem and the resulting constants are the problem-specific contribution.

Unsafe wording until a broader MathSciNet/Zentralblatt-style bibliography audit is completed:

> This is the first theorem of its kind.

or

> No previous work studies such a phenomenon.

## 6. Remaining literature checks before submission

The final bibliography audit should still inspect:

- flux-phase theorems and reflection positivity for tight-binding/signing models;
- signed Cayley graph spectra beyond circulants;
- periodic voltage graphs and magnetic graph operators with finite defect patterns;
- transfer/discriminant formulas for matrix-valued periodic Jacobi operators;
- any recent 2025--2026 work citing Suvagiya's signed-circulant preprint.

The present search is strong enough to guide the paper architecture but not yet strong enough for an absolute priority claim.