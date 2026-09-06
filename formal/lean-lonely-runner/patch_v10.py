from pathlib import Path

root = Path('formal/lean-lonely-runner/project')
p = root / 'LonelyRunner/FirstRelationShape.lean'
p.write_text(r'''import LonelyRunner.ResonanceExtraction

namespace LonelyRunner

set_option maxRecDepth 100000
set_option maxHeartbeats 0

/-!
# Reading the short odd relation from a negative first-certificate coefficient

This version performs no second `[-4,4]^4` enumeration.  It reuses the already kernel-checked
`firstCoeffFiniteCheck_true`; coordinate bounds are extracted structurally from membership in
`supportBox`.
-/

/-- The support/parity conditions forced by a negative coefficient of the first certificate. -/
def ShortOddRelation (r : Relation) : Prop :=
  (∀ i : Fin 4, (r i).natAbs ≤ 4) ∧
  ((if (r 0).natAbs = 4 then 1 else 0) +
   (if (r 1).natAbs = 4 then 1 else 0) +
   (if (r 2).natAbs = 4 then 1 else 0) +
   (if (r 3).natAbs = 4 then 1 else 0) ≤ 1) ∧
  Odd (coordSum r)

/-- Every element of the nine-point coordinate list has absolute value at most four. -/
theorem supportCoord_natAbs_le_four {x : ℤ} (hx : x ∈ supportCoords) : x.natAbs ≤ 4 := by
  simp [supportCoords] at hx
  rcases hx with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> decide

/-- Membership in the product support list gives the four coordinate bounds without enumerating
all 6561 points a second time. -/
theorem support_bounds_of_mem {r : Relation} (hr : r ∈ supportBox) :
    ∀ i : Fin 4, (r i).natAbs ≤ 4 := by
  unfold supportBox at hr
  rcases List.mem_flatMap.mp hr with ⟨a, ha, hr⟩
  rcases List.mem_flatMap.mp hr with ⟨b, hb, hr⟩
  rcases List.mem_flatMap.mp hr with ⟨c, hc, hr⟩
  rcases List.mem_map.mp hr with ⟨d, hd, hEq⟩
  subst r
  intro i
  fin_cases i
  · exact supportCoord_natAbs_le_four ha
  · exact supportCoord_natAbs_le_four hb
  · exact supportCoord_natAbs_le_four hc
  · exact supportCoord_natAbs_le_four hd

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
  exact ⟨support_bounds_of_mem hr, hcount, hodd⟩

/-- A negative coefficient is automatically nonzero because the constant coefficient vanishes. -/
theorem nonzeroRelation_of_negativeCoeff {r : Relation} (hneg : firstCoeff r < 0) :
    r ≠ zeroRelation := negative_first_resonance_nonzero hneg

#print axioms supportCoord_natAbs_le_four
#print axioms support_bounds_of_mem
#print axioms shortOddRelation_of_negativeCoeff

end LonelyRunner
''')
