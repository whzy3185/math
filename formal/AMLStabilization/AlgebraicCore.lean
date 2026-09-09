import Mathlib

namespace AMLStabilization

/-- Squaring a nonnegative linear bound and using `(x+y)^2 ≤ 2x^2+2y^2`. -/
theorem squareOfLinearBound
    {a z y A B : ℝ}
    (ha : 0 ≤ a) (hz : 0 ≤ z) (hy : 0 ≤ y)
    (hA : 0 ≤ A) (hB : 0 ≤ B)
    (hlin : a ≤ A * z + B * y) :
    a ^ 2 ≤ 2 * A ^ 2 * z ^ 2 + 2 * B ^ 2 * y ^ 2 := by
  have hr : 0 ≤ A * z + B * y := by positivity
  have hsq : a ^ 2 ≤ (A * z + B * y) ^ 2 := by
    nlinarith
  have hpar : (A * z + B * y) ^ 2 ≤ 2 * (A * z) ^ 2 + 2 * (B * y) ^ 2 := by
    nlinarith [sq_nonneg (A * z - B * y)]
  nlinarith

/--
Algebraic core of the mass-weighted coercivity estimate.

Interpretation for the paper:
* `x = ‖f‖₂`, `y = ‖∇f‖₂`, `z = (∫ ρ f²)^(1/2)`, `a = |f_Ω|`;
* `a ≤ A z + B y` is the mean estimate obtained from mass conservation;
* `x² ≤ 2 Cp² y² + 2 V a²` is Poincaré plus mean decomposition.

The conclusion is exactly the explicit coercivity closure used in the PDE proof.
-/
theorem massWeightedCoercivityReduction
    {x y z a Cp V A B : ℝ}
    (ha : 0 ≤ a) (hz : 0 ≤ z) (hy : 0 ≤ y)
    (hA : 0 ≤ A) (hB : 0 ≤ B) (hV : 0 ≤ V)
    (hlin : a ≤ A * z + B * y)
    (hbase : x ^ 2 ≤ 2 * Cp ^ 2 * y ^ 2 + 2 * V * a ^ 2) :
    x ^ 2 ≤
      (2 * Cp ^ 2 + 4 * V * B ^ 2) * y ^ 2 +
        4 * V * A ^ 2 * z ^ 2 := by
  have ha2 := squareOfLinearBound ha hz hy hA hB hlin
  have hscaled := mul_le_mul_of_nonneg_left ha2 (show 0 ≤ 2 * V by positivity)
  nlinarith

/--
If an unweighted norm is controlled by `C (gradient + weighted)` and `δ ≤ 1, α`,
then the actual dissipation `gradient + α * weighted` controls `δ` times the norm.
This is the algebraic step used after the mass-weighted coercivity estimate.
-/
theorem scaledDissipationCoercivity
    {normSq gradSq weighted C α δ : ℝ}
    (hgrad : 0 ≤ gradSq) (hweighted : 0 ≤ weighted)
    (hC : 0 ≤ C) (hδ : 0 ≤ δ)
    (hδ1 : δ ≤ 1) (hδα : δ ≤ α)
    (hcoerc : normSq ≤ C * (gradSq + weighted)) :
    δ * normSq ≤ C * (gradSq + α * weighted) := by
  have h1 := mul_le_mul_of_nonneg_left hcoerc hδ
  have h2 : δ * (gradSq + weighted) ≤ gradSq + α * weighted := by
    nlinarith
  have h3 := mul_le_mul_of_nonneg_left h2 hC
  nlinarith

/-- Production-consumption kinetics `F(s)=1-αs`. -/
def productionConsumption (α s : ℝ) : ℝ := 1 - α * s

/--
At any equilibrium `vstar` satisfying `α*vstar=1`, the production-consumption
reaction is exactly quadratically dissipative.
-/
theorem productionConsumptionIdentityOfEquilibrium
    {α vstar s : ℝ}
    (hstar : α * vstar = 1) :
    (s - vstar) * productionConsumption α s =
      -α * (s - vstar) ^ 2 := by
  unfold productionConsumption
  rw [← hstar]
  ring

/-- Exact paper specialization `v_* = 1/α` for nonzero `α`. -/
theorem productionConsumptionIdentity
    {α s : ℝ}
    (hα : α ≠ 0) :
    (s - 1 / α) * productionConsumption α s =
      -α * (s - 1 / α) ^ 2 := by
  apply productionConsumptionIdentityOfEquilibrium
  field_simp [hα]

/-- Pure consumption kinetics `F(s)=-s` is quadratically dissipative at zero. -/
theorem pureConsumptionIdentity (s : ℝ) :
    s * (-s) = -(s - 0) ^ 2 := by
  ring

/--
The one-sided dissipativity inequality alone does not force a root when the
candidate equilibrium is an endpoint.  On `[0,1]`, the constant reaction
`F=-1` satisfies `s F(s) ≤ -s²` but `F(0) ≠ 0`.
This formally records the P0 correction made during the theorem audit.
-/
theorem endpointDissipativityDoesNotForceRoot :
    (∀ s ∈ Set.Icc (0 : ℝ) 1, s * (-1 : ℝ) ≤ -(s - 0) ^ 2) ∧
      (-1 : ℝ) ≠ 0 := by
  constructor
  · intro s hs
    rcases hs with ⟨hs0, hs1⟩
    norm_num at hs0 hs1 ⊢
    nlinarith
  · norm_num

end AMLStabilization
