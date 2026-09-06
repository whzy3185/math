from pathlib import Path

p = Path('formal/lean-lonely-runner/project/LonelyRunner/FirstCertificateClosure.lean')
p.write_text(r'''import LonelyRunner.FirstLaurent

namespace LonelyRunner

open scoped Interval

/-!
# Closing the first Fourier certificate

This file joins the analytic negativity theorem to the Laurent expansion and Fourier
orthogonality.  The final theorem produces the nonzero short odd integer relation directly from
`LowQuarter` and positivity of the four integer speeds.
-/

/-- Cast a positive natural speed vector to the integer vector used by relation arithmetic. -/
def natSpeedInt (v : Fin 4 → ℕ) : Fin 4 → ℤ := fun i => (v i : ℤ)

@[simp] theorem phaseAngleInt_natSpeedInt (v : Fin 4 → ℕ) (i : Fin 4) (t : ℝ) :
    phaseAngleInt (natSpeedInt v) i t = 2 * Real.pi * ((v i : ℝ) * t) := by
  simp [phaseAngleInt, natSpeedInt]

/-- The signed-integer and natural-speed real certificate definitions agree. -/
theorem firstCertificateAtInt_natSpeedInt (v : Fin 4 → ℕ) (t : ℝ) :
    firstCertificateAtInt (natSpeedInt v) t = firstCertificateAt v t := by
  simp [firstCertificateAtInt, firstCertificateAt, phaseCos, phaseAngleInt, natSpeedInt]

/-- Resonant coefficient mass, kept as a computable list sum. -/
def firstResonanceMassList (v : Fin 4 → ℤ) : ℤ :=
  (supportBox.map fun r => if relationDot r v = 0 then firstCoeff r else 0).sum

/-- Fourier sum attached to an arbitrary finite list of exponent vectors. -/
noncomputable def firstFourierList (L : List Relation) (v : Fin 4 → ℤ) (t : ℝ) : ℂ :=
  (L.map fun r => (firstCoeff r : ℂ) * relationMode r v t).sum

@[simp] theorem firstFourierList_supportBox (v : Fin 4 → ℤ) (t : ℝ) :
    firstFourierList supportBox v t = firstFourierSum v t := rfl

/-- Each relation mode is continuous. -/
theorem continuous_relationMode (r : Relation) (v : Fin 4 → ℤ) :
    Continuous (relationMode r v) := by
  unfold relationMode fourierMode
  fun_prop

/-- A finite list of coefficient-weighted modes is continuous. -/
theorem continuous_firstFourierList (L : List Relation) (v : Fin 4 → ℤ) :
    Continuous (firstFourierList L v) := by
  induction L with
  | nil =>
      change Continuous (fun _ : ℝ => (0 : ℂ))
      exact continuous_const
  | cons r rs ih =>
      change Continuous (fun t : ℝ =>
        (firstCoeff r : ℂ) * relationMode r v t + firstFourierList rs v t)
      exact (continuous_const.mul (continuous_relationMode r v)).add ih

/-- Fourier orthogonality integrated term-by-term over any finite relation list. -/
theorem integral_firstFourierList (L : List Relation) (v : Fin 4 → ℤ) :
    (∫ t : ℝ in (0 : ℝ)..1, firstFourierList L v t) =
      ((L.map fun r => if relationDot r v = 0 then firstCoeff r else 0).sum : ℤ) := by
  induction L with
  | nil =>
      change (∫ _t : ℝ in (0 : ℝ)..1, (0 : ℂ)) = (0 : ℂ)
      simp
  | cons r rs ih =>
      have hterm : IntervalIntegrable
          (fun t : ℝ => (firstCoeff r : ℂ) * relationMode r v t)
          MeasureTheory.volume 0 1 :=
        (continuous_const.mul (continuous_relationMode r v)).intervalIntegrable 0 1
      have hrest : IntervalIntegrable (firstFourierList rs v) MeasureTheory.volume 0 1 :=
        (continuous_firstFourierList rs v).intervalIntegrable 0 1
      change
        (∫ t : ℝ in (0 : ℝ)..1,
          (firstCoeff r : ℂ) * relationMode r v t + firstFourierList rs v t) =
        (((if relationDot r v = 0 then firstCoeff r else 0) +
          (rs.map fun s => if relationDot s v = 0 then firstCoeff s else 0).sum : ℤ) : ℂ)
      rw [intervalIntegral.integral_add hterm hrest]
      rw [intervalIntegral.integral_const_mul]
      rw [integral_relationMode]
      rw [ih]
      by_cases hres : relationDot r v = 0 <;> simp [hres]

/-- Integral of the explicit first Fourier sum is the integer resonant mass. -/
theorem integral_firstFourierSum (v : Fin 4 → ℤ) :
    (∫ t : ℝ in (0 : ℝ)..1, firstFourierSum v t) = (firstResonanceMassList v : ℂ) := by
  simpa [firstResonanceMassList] using integral_firstFourierList supportBox v

/-- The real certificate average equals the resonant coefficient mass. -/
theorem integral_firstCertificateAtInt_eq_resonanceMass (v : Fin 4 → ℤ) :
    (∫ t : ℝ in (0 : ℝ)..1, firstCertificateAtInt v t) = firstResonanceMassList v := by
  have hcomplex :
      (∫ t : ℝ in (0 : ℝ)..1, (firstCertificateAtInt v t : ℂ)) =
        (firstResonanceMassList v : ℂ) := by
    calc
      (∫ t : ℝ in (0 : ℝ)..1, (firstCertificateAtInt v t : ℂ)) =
          ∫ t : ℝ in (0 : ℝ)..1, firstFourierSum v t := by
            apply intervalIntegral.integral_congr
            intro t _ht
            exact (firstFourierSum_eq_certificate v t).symm
      _ = (firstResonanceMassList v : ℂ) := integral_firstFourierSum v
  have hcont : Continuous (fun t : ℝ => (firstCertificateAtInt v t : ℂ)) := by
    unfold firstCertificateAtInt phaseAngleInt firstCertificateValue
    fun_prop
  have hint : IntervalIntegrable (fun t : ℝ => (firstCertificateAtInt v t : ℂ))
      MeasureTheory.volume 0 1 := hcont.intervalIntegrable 0 1
  have hre := intervalIntegral.intervalIntegral_re hint
  rw [hcomplex] at hre
  simpa using hre

/-- Natural-speed version of the average/mass identity. -/
theorem integral_firstCertificateAt_eq_resonanceMass (v : Fin 4 → ℕ) :
    (∫ t : ℝ in (0 : ℝ)..1, firstCertificateAt v t) =
      firstResonanceMassList (natSpeedInt v) := by
  have h := integral_firstCertificateAtInt_eq_resonanceMass (natSpeedInt v)
  simpa only [firstCertificateAtInt_natSpeedInt] using h

/-- Under the low-quarter hypothesis, the resonant first-certificate mass is negative. -/
theorem firstResonanceMassList_neg
    {v : Fin 4 → ℕ} (hpos : ∀ i, 0 < v i) (hlow : LowQuarter v) :
    firstResonanceMassList (natSpeedInt v) < 0 := by
  have hintneg := integral_firstCertificateAt_neg hpos hlow
  rw [integral_firstCertificateAt_eq_resonanceMass] at hintneg
  exact_mod_cast hintneg

/-- A negative finite list sum has a negative summand. -/
theorem exists_negative_of_list_sum_neg
    {α : Type*} (L : List α) (a : α → ℤ)
    (hneg : (L.map a).sum < 0) :
    ∃ x ∈ L, a x < 0 := by
  induction L with
  | nil => simp at hneg
  | cons x xs ih =>
      simp only [List.map_cons, List.sum_cons] at hneg
      by_cases hx : a x < 0
      · exact ⟨x, by simp, hx⟩
      · have hx0 : 0 ≤ a x := le_of_not_gt hx
        have htail : (xs.map a).sum < 0 := by omega
        rcases ih htail with ⟨y, hy, hya⟩
        exact ⟨y, by simp [hy], hya⟩

/-- Negative resonant mass yields an actual negative-coefficient resonance from the support box. -/
theorem exists_negative_resonance_from_mass
    {v : Fin 4 → ℤ} (hneg : firstResonanceMassList v < 0) :
    ∃ r ∈ supportBox, relationDot r v = 0 ∧ firstCoeff r < 0 := by
  unfold firstResonanceMassList at hneg
  obtain ⟨r, hr, hterm⟩ :=
    exists_negative_of_list_sum_neg supportBox
      (fun r => if relationDot r v = 0 then firstCoeff r else 0) hneg
  by_cases hres : relationDot r v = 0
  · exact ⟨r, hr, hres, by simpa [hres] using hterm⟩
  · simp [hres] at hterm

/-- Membership in the list support implies membership in the computable support finset. -/
theorem mem_firstSupportComputable_of_mem_supportBox {r : Relation} (hr : r ∈ supportBox) :
    r ∈ firstSupportComputable := by
  simpa [firstSupportComputable] using hr

/--
**Closed first-certificate theorem.** Strict loneliness below `1/4`, expressed pointwise by
`LowQuarter`, forces a nonzero resonant relation with the exact support and odd-parity constraints
used by the paper.
-/
theorem firstCertificate_forces_short_odd_relation
    {v : Fin 4 → ℕ} (hpos : ∀ i, 0 < v i) (hlow : LowQuarter v) :
    ∃ r : Relation,
      r ≠ zeroRelation ∧
      relationDot r (natSpeedInt v) = 0 ∧
      ShortOddRelation r := by
  have hmass := firstResonanceMassList_neg hpos hlow
  obtain ⟨r, hr, hres, hcoeff⟩ := exists_negative_resonance_from_mass hmass
  have hrfin : r ∈ firstSupportComputable := mem_firstSupportComputable_of_mem_supportBox hr
  exact ⟨r,
    nonzeroRelation_of_negativeCoeff hcoeff,
    hres,
    shortOddRelation_of_negativeCoeff hrfin hcoeff⟩

#print axioms integral_firstCertificateAt_eq_resonanceMass
#print axioms firstCertificate_forces_short_odd_relation

end LonelyRunner
''')
