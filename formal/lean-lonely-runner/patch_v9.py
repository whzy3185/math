from pathlib import Path

root = Path('formal/lean-lonely-runner/project')
p = root / 'LonelyRunner/FirstRelationShape.lean'
p.write_text(r'''import LonelyRunner.ResonanceExtraction

namespace LonelyRunner

set_option maxRecDepth 100000
set_option maxHeartbeats 0

/-!
# Reading the short odd relation from a negative first-certificate coefficient

This version reuses the already kernel-checked `firstCoeffFiniteCheck_true`; it does not perform a
second coefficient enumeration.  A tiny independent support-box check supplies the trivial
coordinate bounds.
-/

/-- The support/parity conditions forced by a negative coefficient of the first certificate. -/
def ShortOddRelation (r : Relation) : Prop :=
  (∀ i : Fin 4, (r i).natAbs ≤ 4) ∧
  ((if (r 0).natAbs = 4 then 1 else 0) +
   (if (r 1).natAbs = 4 then 1 else 0) +
   (if (r 2).natAbs = 4 then 1 else 0) +
   (if (r 3).natAbs = 4 then 1 else 0) ≤ 1) ∧
  Odd (coordSum r)

/-- Cheap Boolean check that every explicit coordinate in the support box has absolute value ≤ 4. -/
def supportBoundsOK (r : Relation) : Bool :=
  decide ((r 0).natAbs ≤ 4) &&
  decide ((r 1).natAbs ≤ 4) &&
  decide ((r 2).natAbs ≤ 4) &&
  decide ((r 3).natAbs ≤ 4)

def supportBoundsCheck : Bool := supportBox.all supportBoundsOK

theorem supportBoundsCheck_true : supportBoundsCheck = true := by decide

/-- Recover coordinate bounds from membership in the explicit support list. -/
theorem support_bounds_of_mem {r : Relation} (hr : r ∈ supportBox) :
    (r 0).natAbs ≤ 4 ∧ (r 1).natAbs ≤ 4 ∧
    (r 2).natAbs ≤ 4 ∧ (r 3).natAbs ≤ 4 := by
  have hall : supportBox.all supportBoundsOK = true := by
    simpa [supportBoundsCheck] using supportBoundsCheck_true
  have h := List.all_eq_true.mp hall r hr
  simpa [supportBoundsOK] using h

/-- A computable support finset retained for the interface used downstream. -/
def firstSupportComputable : Finset Relation := supportBox.toFinset

/-- Any negative coefficient occurring in the complete support box has the desired short odd shape. -/
theorem shortOddRelation_of_negativeCoeff
    {r : Relation} (hrfin : r ∈ firstSupportComputable) (hneg : firstCoeff r < 0) :
    ShortOddRelation r := by
  have hr : r ∈ supportBox := by
    simpa [firstSupportComputable] using hrfin
  have hall : supportBox.all (fun r => supportShapeOK r && firstCoeffSignOK r) = true := by
    simpa [firstCoeffFiniteCheck] using firstCoeffFiniteCheck_true
  have hchecks := List.all_eq_true.mp hall r hr
  simp only [Bool.and_eq_true] at hchecks
  have hshape : supportShapeOK r = true := hchecks.1
  have hsign : firstCoeffSignOK r = true := hchecks.2
  have hcne : firstCoeff r ≠ 0 := by omega
  have hcount :
      (if (r 0).natAbs = 4 then 1 else 0) +
      (if (r 1).natAbs = 4 then 1 else 0) +
      (if (r 2).natAbs = 4 then 1 else 0) +
      (if (r 3).natAbs = 4 then 1 else 0) ≤ 1 := by
    simpa [supportShapeOK, hcne] using hshape
  have hodd : Odd (coordSum r) := by
    by_contra hnotodd
    have heven : Even (coordSum r) := Int.not_odd_iff_even.mp hnotodd
    have hpos : 0 < firstCoeff r := by
      simpa [firstCoeffSignOK, hcne, heven] using hsign
    omega
  have hb := support_bounds_of_mem hr
  have hforall : ∀ i : Fin 4, (r i).natAbs ≤ 4 := by
    intro i
    fin_cases i <;> simp_all
  exact ⟨hforall, hcount, hodd⟩

/-- A negative coefficient is automatically nonzero because the constant coefficient vanishes. -/
theorem nonzeroRelation_of_negativeCoeff {r : Relation} (hneg : firstCoeff r < 0) :
    r ≠ zeroRelation := negative_first_resonance_nonzero hneg

#print axioms supportBoundsCheck_true
#print axioms shortOddRelation_of_negativeCoeff

end LonelyRunner
''')
