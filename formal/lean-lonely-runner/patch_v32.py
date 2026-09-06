from pathlib import Path

root = Path('formal/lean-lonely-runner/project')
(root / 'LonelyRunner/SecondOneDim.lean').write_text(r'''import LonelyRunner.SecondSign
import LonelyRunner.FirstLaurent

namespace LonelyRunner

set_option maxRecDepth 150000
set_option maxHeartbeats 0

/-- Sparse power using the already-verified normalized convolution. -/
def sparsePow : ℕ → SparseLaurent → SparseLaurent
  | 0, _ => [(zeroRelation, 1)]
  | n + 1, p => sparseMul (sparsePow n p) p

/-- Evaluation commutes with sparse powers. -/
theorem eval_sparsePow (n : ℕ) (v : Fin 4 → ℤ) (t : ℝ) (p : SparseLaurent) :
    evalSparse v t (sparsePow n p) = (evalSparse v t p) ^ n := by
  induction n with
  | zero => simp [sparsePow]
  | succ n ih =>
      simp only [sparsePow]
      rw [eval_sparseMul, ih, pow_succ]

/-- Relation supported in coordinate `i` with signed displacement `z`. -/
def coordinateRelation (i : Fin 4) (z : ℤ) : Relation :=
  fun j => z * basisRelation i j

/-- One-dimensional Laurent coefficient `(-1)^z choose(2m,m+z)`. -/
def qPowerCoeff (m : ℕ) (z : ℤ) : ℤ :=
  ((-1 : ℤ) ^ z.natAbs) * shiftedChoose m z

/-- The finite one-dimensional coefficient list for `(2-z-z⁻¹)^m`. -/
def qPowerCoeffPolynomial (m : ℕ) (i : Fin 4) : SparseLaurent :=
  normalizeSparse <|
    (List.range (2 * m + 1)).map fun n =>
      let z : ℤ := (n : ℤ) - (m : ℤ)
      (coordinateRelation i z, qPowerCoeff m z)

/-- Kernel-reduced coefficient identity for power `3`. -/
theorem qBase_pow3_coeffs (i : Fin 4) :
    sparsePow 3 (qBase i) = qPowerCoeffPolynomial 3 i := by
  fin_cases i <;> decide

/-- Kernel-reduced coefficient identity for power `4`. -/
theorem qBase_pow4_coeffs (i : Fin 4) :
    sparsePow 4 (qBase i) = qPowerCoeffPolynomial 4 i := by
  fin_cases i <;> decide

/-- Kernel-reduced coefficient identity for power `5`. -/
theorem qBase_pow5_coeffs (i : Fin 4) :
    sparsePow 5 (qBase i) = qPowerCoeffPolynomial 5 i := by
  fin_cases i <;> decide

/-- Kernel-reduced coefficient identity for power `9`. -/
theorem qBase_pow9_coeffs (i : Fin 4) :
    sparsePow 9 (qBase i) = qPowerCoeffPolynomial 9 i := by
  fin_cases i <;> decide

/-- Kernel-reduced coefficient identity for power `10`. -/
theorem qBase_pow10_coeffs (i : Fin 4) :
    sparsePow 10 (qBase i) = qPowerCoeffPolynomial 10 i := by
  fin_cases i <;> decide

/-- Evaluated one-dimensional expansion for exponent `3`. -/
theorem eval_qPowerCoeffPolynomial3 (v : Fin 4 → ℤ) (i : Fin 4) (t : ℝ) :
    evalSparse v t (qPowerCoeffPolynomial 3 i) = (evalSparse v t (qBase i)) ^ 3 := by
  rw [← qBase_pow3_coeffs i, eval_sparsePow]

/-- Evaluated one-dimensional expansion for exponent `4`. -/
theorem eval_qPowerCoeffPolynomial4 (v : Fin 4 → ℤ) (i : Fin 4) (t : ℝ) :
    evalSparse v t (qPowerCoeffPolynomial 4 i) = (evalSparse v t (qBase i)) ^ 4 := by
  rw [← qBase_pow4_coeffs i, eval_sparsePow]

/-- Evaluated one-dimensional expansion for exponent `5`. -/
theorem eval_qPowerCoeffPolynomial5 (v : Fin 4 → ℤ) (i : Fin 4) (t : ℝ) :
    evalSparse v t (qPowerCoeffPolynomial 5 i) = (evalSparse v t (qBase i)) ^ 5 := by
  rw [← qBase_pow5_coeffs i, eval_sparsePow]

/-- Evaluated one-dimensional expansion for exponent `9`. -/
theorem eval_qPowerCoeffPolynomial9 (v : Fin 4 → ℤ) (i : Fin 4) (t : ℝ) :
    evalSparse v t (qPowerCoeffPolynomial 9 i) = (evalSparse v t (qBase i)) ^ 9 := by
  rw [← qBase_pow9_coeffs i, eval_sparsePow]

/-- Evaluated one-dimensional expansion for exponent `10`. -/
theorem eval_qPowerCoeffPolynomial10 (v : Fin 4 → ℤ) (i : Fin 4) (t : ℝ) :
    evalSparse v t (qPowerCoeffPolynomial 10 i) = (evalSparse v t (qBase i)) ^ 10 := by
  rw [← qBase_pow10_coeffs i, eval_sparsePow]

#print axioms qBase_pow3_coeffs
#print axioms qBase_pow4_coeffs
#print axioms qBase_pow5_coeffs
#print axioms qBase_pow9_coeffs
#print axioms qBase_pow10_coeffs

end LonelyRunner
''')

main = root / 'LonelyRunner.lean'
s = main.read_text()
imp = 'import LonelyRunner.SecondOneDim\n'
if imp not in s:
    s += imp
main.write_text(s)
