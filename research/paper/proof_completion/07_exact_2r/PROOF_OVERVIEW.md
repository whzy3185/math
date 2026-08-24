# Proof Overview

## 1. Two local modes per interface

The one-G6 squared eigenspace at `c6` has dimension two. Choose an orthonormal
basis `psi_(j,+),psi_(j,-)` at each translated or reflected interface. The
labels refer to the unsquared eigenvalues `+sqrt(c6)` and `-sqrt(c6)`.

## 2. Truncate and control the Gram matrix

Cut off both modes inside disjoint interface plateaux. Exact Floquet bounds
give tail norm below `73 q_F^ell` for each mode. Same-interface and
different-interface overlaps are retained in one `2r x 2r` Gram matrix.
For `D>=1040` it lies within `1/2` of the identity and is invertible.

## 3. Obtain at least `2r` eigenvalues

Each truncated mode has residual at most `1752 q_F^ell`. Gram
orthonormalization yields a `2r`-dimensional subspace on which the residual
from `c6` is smaller than the window radius `1/400`. The spectral theorem
then forces the window projection to have rank at least `2r`.

## 4. Obtain at most `2r` eigenvalues

On the orthogonal complement of all truncated modes, every interface
localization is orthogonal to the full rank-two local eigenspace. The
single-interface complement cap and an exact range-four IMS estimate give

```text
Q_perp H Q_perp<=c6-1/200.
```

Min-max therefore permits at most `2r` eigenvalues above that level, hence at
most `2r` in the fixed window.

## 5. Refine with the `2r` Feshbach operator

The complement resolvent is bounded by `400`. Schur complementation on the
Gram-orthonormalized `2r`-space gives the coordinate equation
`H_eff(z)-zI_(2r)`. Exact norm estimates split the effective operator into a
first-order interaction and a quadratic resolvent remainder, producing the
constant `3505r` in the exponential bound.

## Proof architecture

```text
rank-two local theorem + exact Floquet constants
  -> 2r quasimodes and Gram control
  -> lower spectral count
  -> codimension-2r IMS complement cap
  -> upper spectral count
  -> 2r-dimensional Feshbach refinement.
```

## Publication placement

- `MAIN_TEXT_REQUIRED`: the exact-count theorem and the five-step chain from
  two local modes through lower and upper counts.
- `APPENDIX_REQUIRED`: cutoff geometry, Gram constants, IMS arithmetic,
  Schur-complement formulas, and the `3505r` estimate.
- `REPRODUCIBILITY_ONLY`: the 32 Floquet chart records, certificate schema,
  independent reconstruction details, and tamper tests.
