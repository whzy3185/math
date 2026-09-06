from pathlib import Path

root = Path('formal/lean-lonely-runner/project')
p = root / 'LonelyRunner/FirstRelationShape.lean'
p.write_text(r'''import LonelyRunner.ResonanceExtraction

namespace LonelyRunner

set_option maxRecDepth 100000
set_option maxHeartbeats 0

/-!
# Reading the short odd relation from a negative first-certificate coefficient

For kernel computation we encode oddness by `coordSum r % 2 = 1`; `Int.odd_iff` converts this
back to the mathematical predicate `Odd (coordSum r)`.
-/

/-- The support/parity conditions forced by a negative coefficient of the first certificate. -/
def ShortOddRelation (r : Relation) : Prop :=
  ((r 0).natAbs ≤ 4 ∧ (r 1).natAbs ≤ 4 ∧
   (r 2).natAbs ≤ 4 ∧ (r 3).natAbs ≤ 4) ∧
  ((if (r 0).natAbs = 4 then 1 else 0) +
   (if (r 1).natAbs = 4 then 1 else 0) +
   (if (r 2).natAbs = 4 then 1 else 0) +
   (if (r 3).natAbs = 4 then 1 else 0) ≤ 1) ∧
  coordSum r % 2 = 1

/-- The parity component really says that the coordinate sum is odd. -/
theorem ShortOddRelation.odd {r : Relation} (h : ShortOddRelation r) : Odd (coordSum r) := by
  exact Int.odd_iff.mpr h.2.2

/-- The explicit coordinate bounds imply the uniform `Fin 4` bound used in the paper. -/
theorem ShortOddRelation.bound {r : Relation} (h : ShortOddRelation r) (i : Fin 4) :
    (r i).natAbs ≤ 4 := by
  fin_cases i <;> simp_all [ShortOddRelation]

/-- A computable support finset. -/
def firstSupportComputable : Finset Relation := supportBox.toFinset

/-- The forbidden set: negative coefficients which would violate the short/odd conditions. -/
def badNegativeFirstCoefficients : Finset Relation :=
  firstSupportComputable.filter fun r => firstCoeff r < 0 ∧ ¬ ShortOddRelation r

/-- Kernel-computable exhaustiveness check for the coefficient-shape lemma. -/
theorem badNegativeFirstCoefficients_empty : badNegativeFirstCoefficients = ∅ := by decide

/-- Any negative coefficient occurring in the complete support box has the desired short odd shape. -/
theorem shortOddRelation_of_negativeCoeff
    {r : Relation} (hr : r ∈ firstSupportComputable) (hneg : firstCoeff r < 0) :
    ShortOddRelation r := by
  by_contra hbad
  have hmem : r ∈ badNegativeFirstCoefficients := by
    exact Finset.mem_filter.mpr ⟨hr, hneg, hbad⟩
  rw [badNegativeFirstCoefficients_empty] at hmem
  simpa using hmem

/-- A negative coefficient is automatically nonzero as a relation because the constant
coefficient of the first certificate vanishes. -/
theorem nonzeroRelation_of_negativeCoeff {r : Relation} (hneg : firstCoeff r < 0) :
    r ≠ zeroRelation := negative_first_resonance_nonzero hneg

#print axioms badNegativeFirstCoefficients_empty
#print axioms shortOddRelation_of_negativeCoeff
#print axioms ShortOddRelation.odd

end LonelyRunner
''')
