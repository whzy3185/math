from pathlib import Path

root = Path('formal/lean-lonely-runner/project')
(root / 'LonelyRunner/SecondAnalytic.lean').write_text(r'''import LonelyRunner.FirstCertificateClosure

namespace LonelyRunner

open Set
open scoped Interval

/-!
# Analytic half of the second Fourier certificate

For
`P = ∏ᵢ (2 - 2 cos(2π vᵢ t))`
we prove under `LowQuarter` that `0 ≤ P < 128`, and that `P > 0` at the same deterministic
interior witness used for the first certificate.  Hence
`Gₖ = P^(k+1) - 128 P^k` is pointwise non-positive and strictly negative somewhere, so its
interval integral is strictly negative.
-/

/-- Real value of the four-factor Riesz product. -/
def secondPValue (c0 c1 c2 c3 : ℝ) : ℝ :=
  (2 - 2 * c0) * (2 - 2 * c1) * (2 - 2 * c2) * (2 - 2 * c3)

/-- Real value of the second certificate `G_k = P^(k+1) - 128 P^k`. -/
def secondCertificateValue (k : ℕ) (c0 c1 c2 c3 : ℝ) : ℝ :=
  secondPValue c0 c1 c2 c3 ^ (k + 1) -
    128 * secondPValue c0 c1 c2 c3 ^ k

lemma fourProduct_lt_128_of_first_lt_two
    {a b c d : ℝ}
    (ha0 : 0 ≤ a) (hb0 : 0 ≤ b) (hc0 : 0 ≤ c) (hd0 : 0 ≤ d)
    (ha2 : a < 2) (hb4 : b ≤ 4) (hc4 : c ≤ 4) (hd4 : d ≤ 4) :
    a * b * c * d < 128 := by
  have hbc1 : b * c ≤ 4 * c := by
    nlinarith [mul_nonneg (sub_nonneg.mpr hb4) hc0]
  have hbc2 : 4 * c ≤ 16 := by nlinarith
  have hbc : b * c ≤ 16 := le_trans hbc1 hbc2
  have hbcd1 : (b * c) * d ≤ 16 * d :=
    mul_le_mul_of_nonneg_right hbc hd0
  have hbcd2 : 16 * d ≤ 64 := by nlinarith
  have hbcd : b * c * d ≤ 64 := le_trans hbcd1 hbcd2
  have hmul : a * (b * c * d) ≤ a * 64 :=
    mul_le_mul_of_nonneg_left hbcd ha0
  have hstrict : a * 64 < 128 := by nlinarith
  calc
    a * b * c * d = a * (b * c * d) := by ring
    _ ≤ a * 64 := hmul
    _ < 128 := hstrict

/-- The Riesz product is non-negative when every cosine is at most one. -/
theorem secondPValue_nonneg
    (c0 c1 c2 c3 : ℝ)
    (h0 : c0 ≤ 1) (h1 : c1 ≤ 1) (h2 : c2 ≤ 1) (h3 : c3 ≤ 1) :
    0 ≤ secondPValue c0 c1 c2 c3 := by
  have hf0 : 0 ≤ 2 - 2 * c0 := by linarith
  have hf1 : 0 ≤ 2 - 2 * c1 := by linarith
  have hf2 : 0 ≤ 2 - 2 * c2 := by linarith
  have hf3 : 0 ≤ 2 - 2 * c3 := by linarith
  unfold secondPValue
  positivity

/-- If one cosine is positive, then the four-factor product is strictly below `128`. -/
theorem secondPValue_lt_128
    (c0 c1 c2 c3 : ℝ)
    (h0lo : -1 ≤ c0) (h1lo : -1 ≤ c1) (h2lo : -1 ≤ c2) (h3lo : -1 ≤ c3)
    (h0hi : c0 ≤ 1) (h1hi : c1 ≤ 1) (h2hi : c2 ≤ 1) (h3hi : c3 ≤ 1)
    (hpos : 0 < c0 ∨ 0 < c1 ∨ 0 < c2 ∨ 0 < c3) :
    secondPValue c0 c1 c2 c3 < 128 := by
  let f0 : ℝ := 2 - 2 * c0
  let f1 : ℝ := 2 - 2 * c1
  let f2 : ℝ := 2 - 2 * c2
  let f3 : ℝ := 2 - 2 * c3
  have hf0n : 0 ≤ f0 := by dsimp [f0]; linarith
  have hf1n : 0 ≤ f1 := by dsimp [f1]; linarith
  have hf2n : 0 ≤ f2 := by dsimp [f2]; linarith
  have hf3n : 0 ≤ f3 := by dsimp [f3]; linarith
  have hf0u : f0 ≤ 4 := by dsimp [f0]; linarith
  have hf1u : f1 ≤ 4 := by dsimp [f1]; linarith
  have hf2u : f2 ≤ 4 := by dsimp [f2]; linarith
  have hf3u : f3 ≤ 4 := by dsimp [f3]; linarith
  rcases hpos with h0 | hrest
  · have hf0lt : f0 < 2 := by dsimp [f0]; linarith
    have h := fourProduct_lt_128_of_first_lt_two hf0n hf1n hf2n hf3n hf0lt hf1u hf2u hf3u
    simpa [secondPValue, f0, f1, f2, f3] using h
  · rcases hrest with h1 | hrest
    · have hf1lt : f1 < 2 := by dsimp [f1]; linarith
      have h := fourProduct_lt_128_of_first_lt_two hf1n hf0n hf2n hf3n hf1lt hf0u hf2u hf3u
      have hreorder : f0 * f1 * f2 * f3 = f1 * f0 * f2 * f3 := by ring
      rw [show secondPValue c0 c1 c2 c3 = f0 * f1 * f2 * f3 by simp [secondPValue, f0, f1, f2, f3]]
      rw [hreorder]
      exact h
    · rcases hrest with h2 | h3
      · have hf2lt : f2 < 2 := by dsimp [f2]; linarith
        have h := fourProduct_lt_128_of_first_lt_two hf2n hf0n hf1n hf3n hf2lt hf0u hf1u hf3u
        have hreorder : f0 * f1 * f2 * f3 = f2 * f0 * f1 * f3 := by ring
        rw [show secondPValue c0 c1 c2 c3 = f0 * f1 * f2 * f3 by simp [secondPValue, f0, f1, f2, f3]]
        rw [hreorder]
        exact h
      · have hf3lt : f3 < 2 := by dsimp [f3]; linarith
        have h := fourProduct_lt_128_of_first_lt_two hf3n hf0n hf1n hf2n hf3lt hf0u hf1u hf2u
        have hreorder : f0 * f1 * f2 * f3 = f3 * f0 * f1 * f2 := by ring
        rw [show secondPValue c0 c1 c2 c3 = f0 * f1 * f2 * f3 by simp [secondPValue, f0, f1, f2, f3]]
        rw [hreorder]
        exact h

/-- Algebraic sign of `G_k` from `0 ≤ P < 128`. -/
theorem secondCertificateValue_nonpos
    (k : ℕ) (c0 c1 c2 c3 : ℝ)
    (hP0 : 0 ≤ secondPValue c0 c1 c2 c3)
    (hP128 : secondPValue c0 c1 c2 c3 < 128) :
    secondCertificateValue k c0 c1 c2 c3 ≤ 0 := by
  let P := secondPValue c0 c1 c2 c3
  have hpow : 0 ≤ P ^ k := pow_nonneg hP0 k
  have hdiff : P - 128 ≤ 0 := by linarith
  unfold secondCertificateValue
  change P ^ (k + 1) - 128 * P ^ k ≤ 0
  rw [pow_succ]
  have hid : P ^ k * P - 128 * P ^ k = P ^ k * (P - 128) := by ring
  rw [hid]
  exact mul_nonpos_of_nonneg_of_nonpos hpow hdiff

/-- Strict algebraic sign of `G_k` from `0 < P < 128`. -/
theorem secondCertificateValue_neg
    (k : ℕ) (c0 c1 c2 c3 : ℝ)
    (hP0 : 0 < secondPValue c0 c1 c2 c3)
    (hP128 : secondPValue c0 c1 c2 c3 < 128) :
    secondCertificateValue k c0 c1 c2 c3 < 0 := by
  let P := secondPValue c0 c1 c2 c3
  have hpow : 0 < P ^ k := pow_pos hP0 k
  have hdiff : P - 128 < 0 := by linarith
  unfold secondCertificateValue
  change P ^ (k + 1) - 128 * P ^ k < 0
  rw [pow_succ]
  have hid : P ^ k * P - 128 * P ^ k = P ^ k * (P - 128) := by ring
  rw [hid]
  exact mul_neg_of_pos_of_neg hpow hdiff

/-- Second certificate along the natural-speed orbit. -/
def secondCertificateAt (k : ℕ) (v : Fin 4 → ℕ) (t : ℝ) : ℝ :=
  secondCertificateValue k
    (phaseCos v 0 t) (phaseCos v 1 t) (phaseCos v 2 t) (phaseCos v 3 t)

/-- Under `LowQuarter`, the second certificate is pointwise non-positive. -/
theorem secondCertificateAt_nonpos
    {v : Fin 4 → ℕ} (h : LowQuarter v) (k : ℕ) (t : ℝ) :
    secondCertificateAt k v t ≤ 0 := by
  rcases h.exists_phaseCos_pos t with ⟨i, hi⟩
  have hp :
      0 < phaseCos v 0 t ∨ 0 < phaseCos v 1 t ∨
      0 < phaseCos v 2 t ∨ 0 < phaseCos v 3 t := by
    fin_cases i <;> simp_all
  have hP0 := secondPValue_nonneg
    (phaseCos v 0 t) (phaseCos v 1 t) (phaseCos v 2 t) (phaseCos v 3 t)
    (Real.cos_le_one _) (Real.cos_le_one _) (Real.cos_le_one _) (Real.cos_le_one _)
  have hP128 := secondPValue_lt_128
    (phaseCos v 0 t) (phaseCos v 1 t) (phaseCos v 2 t) (phaseCos v 3 t)
    (Real.neg_one_le_cos _) (Real.neg_one_le_cos _)
    (Real.neg_one_le_cos _) (Real.neg_one_le_cos _)
    (Real.cos_le_one _) (Real.cos_le_one _)
    (Real.cos_le_one _) (Real.cos_le_one _) hp
  exact secondCertificateValue_nonpos k _ _ _ _ hP0 hP128

/-- At the deterministic interior witness, the Riesz product is strictly positive. -/
theorem secondPValue_strictWitness_pos
    {v : Fin 4 → ℕ} (hpos : ∀ i, 0 < v i) :
    0 < secondPValue
      (phaseCos v 0 (firstStrictTime v))
      (phaseCos v 1 (firstStrictTime v))
      (phaseCos v 2 (firstStrictTime v))
      (phaseCos v 3 (firstStrictTime v)) := by
  have h0 : 0 < 2 - 2 * phaseCos v 0 (firstStrictTime v) := by
    linarith [phaseCos_lt_one_at_firstStrictTime v hpos 0]
  have h1 : 0 < 2 - 2 * phaseCos v 1 (firstStrictTime v) := by
    linarith [phaseCos_lt_one_at_firstStrictTime v hpos 1]
  have h2 : 0 < 2 - 2 * phaseCos v 2 (firstStrictTime v) := by
    linarith [phaseCos_lt_one_at_firstStrictTime v hpos 2]
  have h3 : 0 < 2 - 2 * phaseCos v 3 (firstStrictTime v) := by
    linarith [phaseCos_lt_one_at_firstStrictTime v hpos 3]
  unfold secondPValue
  positivity

/-- The second certificate is strictly negative at the deterministic witness time. -/
theorem secondCertificateAt_strictWitness_neg
    {v : Fin 4 → ℕ} (hpos : ∀ i, 0 < v i) (h : LowQuarter v) (k : ℕ) :
    secondCertificateAt k v (firstStrictTime v) < 0 := by
  rcases h.exists_phaseCos_pos (firstStrictTime v) with ⟨i, hi⟩
  have hp :
      0 < phaseCos v 0 (firstStrictTime v) ∨
      0 < phaseCos v 1 (firstStrictTime v) ∨
      0 < phaseCos v 2 (firstStrictTime v) ∨
      0 < phaseCos v 3 (firstStrictTime v) := by
    fin_cases i <;> simp_all
  have hP0 := secondPValue_strictWitness_pos hpos
  have hP128 := secondPValue_lt_128
    (phaseCos v 0 (firstStrictTime v))
    (phaseCos v 1 (firstStrictTime v))
    (phaseCos v 2 (firstStrictTime v))
    (phaseCos v 3 (firstStrictTime v))
    (Real.neg_one_le_cos _) (Real.neg_one_le_cos _)
    (Real.neg_one_le_cos _) (Real.neg_one_le_cos _)
    (Real.cos_le_one _) (Real.cos_le_one _)
    (Real.cos_le_one _) (Real.cos_le_one _) hp
  exact secondCertificateValue_neg k _ _ _ _ hP0 hP128

/-- The second certificate along the speed orbit is continuous. -/
theorem continuous_secondCertificateAt (k : ℕ) (v : Fin 4 → ℕ) :
    Continuous (secondCertificateAt k v) := by
  unfold secondCertificateAt secondCertificateValue secondPValue phaseCos
  fun_prop

/-- Analytic half of the second Fourier certificate: every `G_k` has strictly negative average. -/
theorem integral_secondCertificateAt_neg
    {v : Fin 4 → ℕ} (hpos : ∀ i, 0 < v i) (h : LowQuarter v) (k : ℕ) :
    (∫ t : ℝ in (0 : ℝ)..1, secondCertificateAt k v t) < 0 := by
  have hlt := intervalIntegral.integral_lt_integral_of_continuousOn_of_le_of_exists_lt
      (show (0 : ℝ) < 1 by norm_num)
      (continuous_secondCertificateAt k v).continuousOn
      continuousOn_const
      (fun t _ht => secondCertificateAt_nonpos h k t)
      ⟨firstStrictTime v,
        ⟨(firstStrictTime_pos v).le, (firstStrictTime_lt_one v).le⟩,
        secondCertificateAt_strictWitness_neg hpos h k⟩
  simpa using hlt

#print axioms integral_secondCertificateAt_neg

end LonelyRunner
''')

main = root / 'LonelyRunner.lean'
s = main.read_text()
imp = 'import LonelyRunner.SecondAnalytic\n'
if imp not in s:
    s += imp
main.write_text(s)
