from pathlib import Path

root = Path('formal/lean-lonely-runner/project')
p = root / 'LonelyRunner/ResonanceExtraction.lean'
p.write_text(r'''import LonelyRunner.FourierOrthogonality

namespace LonelyRunner

/-!
# From negative Fourier mass to a short resonance

This file isolates the finite implication needed after Fourier orthogonality:
a negative sum of resonant Laurent coefficients contains a negative resonant coefficient.
-/

/-- The finite support as a `Finset`. -/
noncomputable def firstSupport : Finset Relation := supportBox.toFinset

/-- Sum of first-certificate coefficients whose monomials are resonant at the speed vector `v`. -/
noncomputable def firstResonanceMass (v : Fin 4 → ℤ) : ℤ :=
  (firstSupport.filter (fun r => relationDot r v = 0)).sum firstCoeff

/-- Generic finite lemma: a negative finite sum contains a negative summand. -/
theorem exists_negative_summand_of_sum_neg
    {α : Type*} [DecidableEq α]
    (s : Finset α) (a : α → ℤ)
    (hneg : s.sum a < 0) :
    ∃ x ∈ s, a x < 0 := by
  by_contra hnone
  have hnonneg : ∀ x ∈ s, 0 ≤ a x := by
    intro x hx
    by_contra hxneg
    have hlt : a x < 0 := lt_of_not_ge hxneg
    exact hnone ⟨x, hx, hlt⟩
  have hsum : 0 ≤ s.sum a := by
    apply Finset.sum_nonneg
    intro x hx
    exact hnonneg x hx
  exact (not_lt_of_ge hsum) hneg

/-- If the resonant mass of the first certificate is negative, there is a negative-coefficient
Laurent monomial whose integer frequency vanishes. -/
theorem exists_negative_first_resonance
    (v : Fin 4 → ℤ)
    (hneg : firstResonanceMass v < 0) :
    ∃ r ∈ firstSupport, relationDot r v = 0 ∧ firstCoeff r < 0 := by
  classical
  unfold firstResonanceMass at hneg
  obtain ⟨r, hr, hrc⟩ :=
    exists_negative_summand_of_sum_neg
      (firstSupport.filter (fun r => relationDot r v = 0)) firstCoeff hneg
  have hmem := Finset.mem_filter.mp hr
  exact ⟨r, hmem.1, hmem.2, hrc⟩

/-- A negative first-certificate coefficient cannot be the zero relation, because the constant
coefficient vanishes. -/
theorem negative_first_resonance_nonzero
    {r : Relation} (hneg : firstCoeff r < 0) : r ≠ zeroRelation := by
  intro hr
  subst r
  rw [firstCoeff_zero] at hneg
  omega

#print axioms exists_negative_summand_of_sum_neg
#print axioms exists_negative_first_resonance
#print axioms negative_first_resonance_nonzero

end LonelyRunner
''')
