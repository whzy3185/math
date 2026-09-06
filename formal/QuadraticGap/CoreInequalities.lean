import Mathlib

namespace QuadraticGap

/-- Algebraic factorization used in the two-Chebyshev decomposition.
The variable `delta` is kept abstract; the square-root relation is supplied
as a hypothesis so that the lemma is purely algebraic. -/
theorem denominator_factorization
    (w t delta : ℝ)
    (hdelta : delta ^ 2 = t * (t + 32)) :
    (1 - 6 * w + w ^ 2) ^ 2 - t * w * (1 + w) ^ 2 =
      (1 - (6 + t / 2 + delta / 2) * w + w ^ 2) *
      (1 - (6 + t / 2 - delta / 2) * w + w ^ 2) := by
  nlinarith [hdelta]

/-- Exact covariance identity for a two-point probability distribution. -/
theorem two_point_covariance_identity
    (α f0 f1 g0 g1 : ℝ) :
    α * (f1 * g1) + (1 - α) * (f0 * g0) -
        (α * f1 + (1 - α) * f0) *
          (α * g1 + (1 - α) * g0) =
      α * (1 - α) * (f1 - f0) * (g1 - g0) := by
  ring

/-- Increasing functions are nonnegatively correlated on a two-point space. -/
theorem two_point_covariance
    (α f0 f1 g0 g1 : ℝ)
    (hα0 : 0 ≤ α)
    (hα1 : α ≤ 1)
    (hf : f0 ≤ f1)
    (hg : g0 ≤ g1) :
    (α * f1 + (1 - α) * f0) *
        (α * g1 + (1 - α) * g0) ≤
      α * (f1 * g1) + (1 - α) * (f0 * g0) := by
  have h1 : 0 ≤ 1 - α := sub_nonneg.mpr hα1
  have h2 : 0 ≤ f1 - f0 := sub_nonneg.mpr hf
  have h3 : 0 ≤ g1 - g0 := sub_nonneg.mpr hg
  have hprod : 0 ≤ α * (1 - α) * (f1 - f0) * (g1 - g0) :=
    mul_nonneg (mul_nonneg (mul_nonneg hα0 h1) h2) h3
  apply sub_nonneg.mp
  rw [two_point_covariance_identity]
  exact hprod

/-- Abstract form of the mixture-product estimate used to prove
`S_i(t) S_j(t) ≤ 2 S_{i+j}(t)`. -/
theorem two_point_product_bound
    (α f0 f1 g0 g1 u0 u1 : ℝ)
    (hα0 : 0 ≤ α)
    (hα1 : α ≤ 1)
    (hf : f0 ≤ f1)
    (hg : g0 ≤ g1)
    (h0 : f0 * g0 ≤ 2 * u0)
    (h1 : f1 * g1 ≤ 2 * u1) :
    (α * f1 + (1 - α) * f0) *
        (α * g1 + (1 - α) * g0) ≤
      2 * (α * u1 + (1 - α) * u0) := by
  have hcov := two_point_covariance α f0 f1 g0 g1 hα0 hα1 hf hg
  have hnonneg : 0 ≤ 1 - α := sub_nonneg.mpr hα1
  have hmix :
      α * (f1 * g1) + (1 - α) * (f0 * g0) ≤
        2 * (α * u1 + (1 - α) * u0) := by
    nlinarith [mul_nonneg hα0 (sub_nonneg.mpr h1),
      mul_nonneg hnonneg (sub_nonneg.mpr h0)]
  exact le_trans hcov hmix

end QuadraticGap
