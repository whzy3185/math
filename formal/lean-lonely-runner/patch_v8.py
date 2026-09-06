from pathlib import Path

root = Path('formal/lean-lonely-runner/project')
p = root / 'LonelyRunner/FirstRelationShape.lean'
p.write_text(r'''import LonelyRunner.ResonanceExtraction

namespace LonelyRunner

set_option maxRecDepth 100000
set_option maxHeartbeats 0

/-!
# Reading the short odd relation from a negative first-certificate coefficient

The mathematical predicate and the finite Boolean checker are kept separate.  The latter is used
only for kernel computation; the equivalence theorem returns the ordinary proposition used by the
rest of the proof.
-/

/-- Mathematical support/parity conditions forced by a negative coefficient. -/
def ShortOddRelation (r : Relation) : Prop :=
  ((r 0).natAbs ≤ 4 ∧ (r 1).natAbs ≤ 4 ∧
   (r 2).natAbs ≤ 4 ∧ (r 3).natAbs ≤ 4) ∧
  ((if (r 0).natAbs = 4 then 1 else 0) +
   (if (r 1).natAbs = 4 then 1 else 0) +
   (if (r 2).natAbs = 4 then 1 else 0) +
   (if (r 3).natAbs = 4 then 1 else 0) ≤ 1) ∧
  coordSum r % 2 = 1

/-- Fully computable Boolean version of `ShortOddRelation`. -/
def shortOddRelationBool (r : Relation) : Bool :=
  decide ((r 0).natAbs ≤ 4) &&
  decide ((r 1).natAbs ≤ 4) &&
  decide ((r 2).natAbs ≤ 4) &&
  decide ((r 3).natAbs ≤ 4) &&
  decide (
    (if (r 0).natAbs = 4 then 1 else 0) +
    (if (r 1).natAbs = 4 then 1 else 0) +
    (if (r 2).natAbs = 4 then 1 else 0) +
    (if (r 3).natAbs = 4 then 1 else 0) ≤ 1) &&
  decide (coordSum r % 2 = 1)

/-- Boolean and propositional formulations agree. -/
theorem shortOddRelationBool_true_iff (r : Relation) :
    shortOddRelationBool r = true ↔ ShortOddRelation r := by
  simp [shortOddRelationBool, ShortOddRelation]

/-- The parity component really says that the coordinate sum is odd. -/
theorem ShortOddRelation.odd {r : Relation} (h : ShortOddRelation r) : Odd (coordSum r) := by
  exact Int.odd_iff.mpr h.2.2

/-- The explicit coordinate bounds imply the uniform `Fin 4` bound used in the paper. -/
theorem ShortOddRelation.bound {r : Relation} (h : ShortOddRelation r) (i : Fin 4) :
    (r i).natAbs ≤ 4 := by
  fin_cases i <;> simp_all [ShortOddRelation]

/-- A computable support finset. -/
def firstSupportComputable : Finset Relation := supportBox.toFinset

/-- The forbidden set, defined only through primitive decidable tests. -/
def badNegativeFirstCoefficients : Finset Relation :=
  firstSupportComputable.filter fun r =>
    firstCoeff r < 0 ∧ shortOddRelationBool r = false

/-- Kernel-computable exhaustiveness check for the coefficient-shape lemma. -/
theorem badNegativeFirstCoefficients_empty : badNegativeFirstCoefficients = ∅ := by decide

/-- Any negative coefficient occurring in the complete support box has the desired short odd shape. -/
theorem shortOddRelation_of_negativeCoeff
    {r : Relation} (hr : r ∈ firstSupportComputable) (hneg : firstCoeff r < 0) :
    ShortOddRelation r := by
  have hbool : shortOddRelationBool r = true := by
    cases h : shortOddRelationBool r with
    | false =>
        have hmem : r ∈ badNegativeFirstCoefficients := by
          exact Finset.mem_filter.mpr ⟨hr, hneg, h⟩
        rw [badNegativeFirstCoefficients_empty] at hmem
        simpa using hmem
    | true => exact h
  exact (shortOddRelationBool_true_iff r).mp hbool

/-- A negative coefficient is automatically nonzero because the constant coefficient vanishes. -/
theorem nonzeroRelation_of_negativeCoeff {r : Relation} (hneg : firstCoeff r < 0) :
    r ≠ zeroRelation := negative_first_resonance_nonzero hneg

#print axioms badNegativeFirstCoefficients_empty
#print axioms shortOddRelation_of_negativeCoeff
#print axioms ShortOddRelation.odd

end LonelyRunner
''')
