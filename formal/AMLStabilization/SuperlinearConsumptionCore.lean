import Mathlib

namespace AMLStabilization

/-- `C¹`-compatible odd extension of a superlinear consumption law. -/
noncomputable def superlinearConsumption (m s : ℝ) : ℝ :=
  -s * |s| ^ (m - 1)

/--
Exact dissipativity identity for the superlinear consumption law:
`s * F(s) = -|s|^(m+1)`.  This is valid for arbitrary real `s` and `m>1`.
-/
theorem superlinearConsumptionIdentity
    {m s : ℝ} (hm : 1 < m) :
    s * superlinearConsumption m s = -|s| ^ (m + 1) := by
  unfold superlinearConsumption
  by_cases hs : s = 0
  · subst s
    have hm1 : m + 1 ≠ 0 := ne_of_gt (by linarith : 0 < m + 1)
    simp [Real.zero_rpow hm1]
  · have habs : 0 < |s| := abs_pos.mpr hs
    have hsquare : s * s = |s| ^ (2 : ℝ) := by
      rw [Real.rpow_two, sq_abs, pow_two]
    calc
      s * (-s * |s| ^ (m - 1)) = -(s * s) * |s| ^ (m - 1) := by ring
      _ = -(|s| ^ (2 : ℝ)) * |s| ^ (m - 1) := by rw [hsquare]
      _ = -( |s| ^ (2 : ℝ) * |s| ^ (m - 1)) := by ring
      _ = -|s| ^ ((2 : ℝ) + (m - 1)) := by rw [Real.rpow_add habs]
      _ = -|s| ^ (m + 1) := by congr 2 <;> ring

/-- The superlinear law has an equilibrium at zero. -/
theorem superlinearConsumption_zero (m : ℝ) :
    superlinearConsumption m 0 = 0 := by
  simp [superlinearConsumption]

/-- Pointwise manuscript dissipativity with `q=m+1` and `beta=1`. -/
theorem superlinearConsumption_dissipative
    {m s : ℝ} (hm : 1 < m) :
    s * superlinearConsumption m s ≤ -(1 : ℝ) * |s| ^ (m + 1) := by
  rw [superlinearConsumptionIdentity hm]
  ring_nf
  exact le_rfl

end AMLStabilization
