from pathlib import Path

root = Path('formal/lean-lonely-runner/project')
(root / 'LonelyRunner/SecondCoefficients.lean').write_text(r'''import LonelyRunner.SecondAnalytic
import LonelyRunner.LineContributions

namespace LonelyRunner

set_option maxRecDepth 100000
set_option maxHeartbeats 0

/-!
# Coefficient signs for the second Fourier certificate

The coefficient of exponent `s` in `G_k` is a parity sign times a positive bracket.  For the only
three values of `k` used by the proof (`3`, `4`, and `9`), we certify the one-dimensional binomial
ratio bound by finitely many kernel-reduced cases, then combine the four coordinates algebraically.
-/

/-- Positive bracket in the coefficient formula for `G_k`. -/
def secondBracket (k : ℕ) (s : Relation) : ℤ :=
  shiftedChoose (k + 1) (s 0) *
    shiftedChoose (k + 1) (s 1) *
    shiftedChoose (k + 1) (s 2) *
    shiftedChoose (k + 1) (s 3) -
  128 *
    (shiftedChoose k (s 0) *
      shiftedChoose k (s 1) *
      shiftedChoose k (s 2) *
      shiftedChoose k (s 3))

/-- Exact coefficient formula, with parity sign written as a power of `-1`. -/
def secondCoeff (k : ℕ) (s : Relation) : ℤ :=
  ((-1 : ℤ) ^ (coordSum s).natAbs) * secondBracket k s

/-- Coordinate support of `G_k`. -/
def InSecondSupport (k : ℕ) (s : Relation) : Prop :=
  ∀ i : Fin 4,
    -(((k + 1 : ℕ) : ℤ)) ≤ s i ∧ s i ≤ ((k + 1 : ℕ) : ℤ)

lemma shiftedChoose_nonneg (k : ℕ) (z : ℤ) : 0 ≤ shiftedChoose k z := by
  unfold shiftedChoose
  split <;> simp

/-- One-dimensional `7/2` ratio certificate for `k=3`. -/
lemma coordRatioData_k3 (z : ℤ) (hlo : (-4 : ℤ) ≤ z) (hhi : z ≤ 4) :
    0 < shiftedChoose 4 z ∧
      (shiftedChoose 3 z = 0 ∨
        7 * shiftedChoose 3 z ≤ 2 * shiftedChoose 4 z) := by
  interval_cases z <;> norm_num [shiftedChoose]

/-- One-dimensional `7/2` ratio certificate for `k=4`. -/
lemma coordRatioData_k4 (z : ℤ) (hlo : (-5 : ℤ) ≤ z) (hhi : z ≤ 5) :
    0 < shiftedChoose 5 z ∧
      (shiftedChoose 4 z = 0 ∨
        7 * shiftedChoose 4 z ≤ 2 * shiftedChoose 5 z) := by
  interval_cases z <;> norm_num [shiftedChoose]

/-- One-dimensional `7/2` ratio certificate for `k=9`. -/
lemma coordRatioData_k9 (z : ℤ) (hlo : (-10 : ℤ) ≤ z) (hhi : z ≤ 10) :
    0 < shiftedChoose 10 z ∧
      (shiftedChoose 9 z = 0 ∨
        7 * shiftedChoose 9 z ≤ 2 * shiftedChoose 10 z) := by
  interval_cases z <;> norm_num [shiftedChoose]

/-- Four one-dimensional ratio bounds imply the strict `128` product bound. -/
lemma bracketProduct_pos
    {A0 A1 A2 A3 B0 B1 B2 B3 : ℤ}
    (hA0 : 0 < A0) (hA1 : 0 < A1) (hA2 : 0 < A2) (hA3 : 0 < A3)
    (hB0 : 0 ≤ B0) (hB1 : 0 ≤ B1) (hB2 : 0 ≤ B2) (hB3 : 0 ≤ B3)
    (hR0 : B0 = 0 ∨ 7 * B0 ≤ 2 * A0)
    (hR1 : B1 = 0 ∨ 7 * B1 ≤ 2 * A1)
    (hR2 : B2 = 0 ∨ 7 * B2 ≤ 2 * A2)
    (hR3 : B3 = 0 ∨ 7 * B3 ≤ 2 * A3) :
    0 < A0 * A1 * A2 * A3 - 128 * (B0 * B1 * B2 * B3) := by
  by_cases hz0 : B0 = 0
  · rw [hz0]
    simp
    positivity
  by_cases hz1 : B1 = 0
  · rw [hz1]
    simp
    positivity
  by_cases hz2 : B2 = 0
  · rw [hz2]
    simp
    positivity
  by_cases hz3 : B3 = 0
  · rw [hz3]
    simp
    positivity
  have hB0p : 0 < B0 := lt_of_le_of_ne hB0 (Ne.symm hz0)
  have hB1p : 0 < B1 := lt_of_le_of_ne hB1 (Ne.symm hz1)
  have hB2p : 0 < B2 := lt_of_le_of_ne hB2 (Ne.symm hz2)
  have hB3p : 0 < B3 := lt_of_le_of_ne hB3 (Ne.symm hz3)
  have hr0 : 7 * B0 ≤ 2 * A0 := hR0.resolve_left hz0
  have hr1 : 7 * B1 ≤ 2 * A1 := hR1.resolve_left hz1
  have hr2 : 7 * B2 ≤ 2 * A2 := hR2.resolve_left hz2
  have hr3 : 7 * B3 ≤ 2 * A3 := hR3.resolve_left hz3
  have h01a : (7 * B0) * (7 * B1) ≤ (2 * A0) * (7 * B1) :=
    mul_le_mul_of_nonneg_right hr0 (by positivity)
  have h01b : (2 * A0) * (7 * B1) ≤ (2 * A0) * (2 * A1) :=
    mul_le_mul_of_nonneg_left hr1 (by positivity)
  have h01 := le_trans h01a h01b
  have h012a : ((7 * B0) * (7 * B1)) * (7 * B2) ≤
      ((2 * A0) * (2 * A1)) * (7 * B2) :=
    mul_le_mul_of_nonneg_right h01 (by positivity)
  have h012b : ((2 * A0) * (2 * A1)) * (7 * B2) ≤
      ((2 * A0) * (2 * A1)) * (2 * A2) :=
    mul_le_mul_of_nonneg_left hr2 (by positivity)
  have h012 := le_trans h012a h012b
  have h0123a : (((7 * B0) * (7 * B1)) * (7 * B2)) * (7 * B3) ≤
      (((2 * A0) * (2 * A1)) * (2 * A2)) * (7 * B3) :=
    mul_le_mul_of_nonneg_right h012 (by positivity)
  have h0123b : (((2 * A0) * (2 * A1)) * (2 * A2)) * (7 * B3) ≤
      (((2 * A0) * (2 * A1)) * (2 * A2)) * (2 * A3) :=
    mul_le_mul_of_nonneg_left hr3 (by positivity)
  have h0123 := le_trans h0123a h0123b
  have hscaled :
      2401 * (B0 * B1 * B2 * B3) ≤ 16 * (A0 * A1 * A2 * A3) := by
    calc
      2401 * (B0 * B1 * B2 * B3) =
          (((7 * B0) * (7 * B1)) * (7 * B2)) * (7 * B3) := by ring
      _ ≤ (((2 * A0) * (2 * A1)) * (2 * A2)) * (2 * A3) := h0123
      _ = 16 * (A0 * A1 * A2 * A3) := by ring
  have hBprod : 0 < B0 * B1 * B2 * B3 := by positivity
  have hstrict :
      2048 * (B0 * B1 * B2 * B3) < 2401 * (B0 * B1 * B2 * B3) := by
    nlinarith
  have hcombined :
      2048 * (B0 * B1 * B2 * B3) < 16 * (A0 * A1 * A2 * A3) :=
    lt_of_lt_of_le hstrict hscaled
  nlinarith

lemma secondBracket_pos_of_coordData
    (k : ℕ) (s : Relation)
    (h0 : 0 < shiftedChoose (k + 1) (s 0) ∧
      (shiftedChoose k (s 0) = 0 ∨ 7 * shiftedChoose k (s 0) ≤ 2 * shiftedChoose (k + 1) (s 0)))
    (h1 : 0 < shiftedChoose (k + 1) (s 1) ∧
      (shiftedChoose k (s 1) = 0 ∨ 7 * shiftedChoose k (s 1) ≤ 2 * shiftedChoose (k + 1) (s 1)))
    (h2 : 0 < shiftedChoose (k + 1) (s 2) ∧
      (shiftedChoose k (s 2) = 0 ∨ 7 * shiftedChoose k (s 2) ≤ 2 * shiftedChoose (k + 1) (s 2)))
    (h3 : 0 < shiftedChoose (k + 1) (s 3) ∧
      (shiftedChoose k (s 3) = 0 ∨ 7 * shiftedChoose k (s 3) ≤ 2 * shiftedChoose (k + 1) (s 3))) :
    0 < secondBracket k s := by
  unfold secondBracket
  exact bracketProduct_pos
    h0.1 h1.1 h2.1 h3.1
    (shiftedChoose_nonneg k (s 0)) (shiftedChoose_nonneg k (s 1))
    (shiftedChoose_nonneg k (s 2)) (shiftedChoose_nonneg k (s 3))
    h0.2 h1.2 h2.2 h3.2

/-- Strict bracket positivity throughout the support for `k=3`. -/
theorem secondBracket_pos_k3 {s : Relation} (h : InSecondSupport 3 s) :
    0 < secondBracket 3 s := by
  have hs0 := h 0
  have hs1 := h 1
  have hs2 := h 2
  have hs3 := h 3
  norm_num at hs0 hs1 hs2 hs3
  exact secondBracket_pos_of_coordData 3 s
    (coordRatioData_k3 (s 0) hs0.1 hs0.2)
    (coordRatioData_k3 (s 1) hs1.1 hs1.2)
    (coordRatioData_k3 (s 2) hs2.1 hs2.2)
    (coordRatioData_k3 (s 3) hs3.1 hs3.2)

/-- Strict bracket positivity throughout the support for `k=4`. -/
theorem secondBracket_pos_k4 {s : Relation} (h : InSecondSupport 4 s) :
    0 < secondBracket 4 s := by
  have hs0 := h 0
  have hs1 := h 1
  have hs2 := h 2
  have hs3 := h 3
  norm_num at hs0 hs1 hs2 hs3
  exact secondBracket_pos_of_coordData 4 s
    (coordRatioData_k4 (s 0) hs0.1 hs0.2)
    (coordRatioData_k4 (s 1) hs1.1 hs1.2)
    (coordRatioData_k4 (s 2) hs2.1 hs2.2)
    (coordRatioData_k4 (s 3) hs3.1 hs3.2)

/-- Strict bracket positivity throughout the support for `k=9`. -/
theorem secondBracket_pos_k9 {s : Relation} (h : InSecondSupport 9 s) :
    0 < secondBracket 9 s := by
  have hs0 := h 0
  have hs1 := h 1
  have hs2 := h 2
  have hs3 := h 3
  norm_num at hs0 hs1 hs2 hs3
  exact secondBracket_pos_of_coordData 9 s
    (coordRatioData_k9 (s 0) hs0.1 hs0.2)
    (coordRatioData_k9 (s 1) hs1.1 hs1.2)
    (coordRatioData_k9 (s 2) hs2.1 hs2.2)
    (coordRatioData_k9 (s 3) hs3.1 hs3.2)

#print axioms secondBracket_pos_k3
#print axioms secondBracket_pos_k4
#print axioms secondBracket_pos_k9

end LonelyRunner
''')

main = root / 'LonelyRunner.lean'
s = main.read_text()
imp = 'import LonelyRunner.SecondCoefficients\n'
if imp not in s:
    s += imp
main.write_text(s)
