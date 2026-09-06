from pathlib import Path

p = Path('formal/lean-lonely-runner/project/LonelyRunner/FirstLaurent.lean')
s = p.read_text()

start = s.index('theorem eval_qBase')
end = s.index('noncomputable def firstCertificateAtInt', start)

replacement = r'''theorem eval_qBase (v : Fin 4 → ℤ) (i : Fin 4) (t : ℝ) :
    evalSparse v t (qBase i) = ((2 - 2 * Real.cos (phaseAngleInt v i t) : ℝ) : ℂ) := by
  simp only [qBase, evalSparse_cons, evalSparse_nil]
  rw [relationMode_zero, relationMode_basis, relationMode_neg_basis]
  have h := exp_I_add_exp_neg_I (phaseAngleInt v i t)
  norm_num
  calc
    _ = (2 : ℂ) -
          (Complex.exp ((phaseAngleInt v i t : ℂ) * Complex.I) +
           Complex.exp ((-phaseAngleInt v i t : ℂ) * Complex.I)) := by ring
    _ = (2 : ℂ) - (2 : ℂ) * (Real.cos (phaseAngleInt v i t) : ℂ) := by rw [h]
    _ = ((2 - 2 * Real.cos (phaseAngleInt v i t) : ℝ) : ℂ) := by
      norm_num [Complex.ofReal_sub, Complex.ofReal_mul]

theorem eval_firstLinear (v : Fin 4 → ℤ) (t : ℝ) :
    evalSparse v t firstLinear =
      ((2 * (3 + Real.cos (phaseAngleInt v 0 t) + Real.cos (phaseAngleInt v 1 t) +
        Real.cos (phaseAngleInt v 2 t) + Real.cos (phaseAngleInt v 3 t)) : ℝ) : ℂ) := by
  simp only [firstLinear, evalSparse_cons, evalSparse_nil]
  rw [relationMode_zero,
      relationMode_basis, relationMode_neg_basis,
      relationMode_basis, relationMode_neg_basis,
      relationMode_basis, relationMode_neg_basis,
      relationMode_basis, relationMode_neg_basis]
  have h0 := exp_I_add_exp_neg_I (phaseAngleInt v 0 t)
  have h1 := exp_I_add_exp_neg_I (phaseAngleInt v 1 t)
  have h2 := exp_I_add_exp_neg_I (phaseAngleInt v 2 t)
  have h3 := exp_I_add_exp_neg_I (phaseAngleInt v 3 t)
  norm_num
  calc
    _ = (6 : ℂ) +
        (Complex.exp ((phaseAngleInt v 0 t : ℂ) * Complex.I) + Complex.exp ((-phaseAngleInt v 0 t : ℂ) * Complex.I)) +
        (Complex.exp ((phaseAngleInt v 1 t : ℂ) * Complex.I) + Complex.exp ((-phaseAngleInt v 1 t : ℂ) * Complex.I)) +
        (Complex.exp ((phaseAngleInt v 2 t : ℂ) * Complex.I) + Complex.exp ((-phaseAngleInt v 2 t : ℂ) * Complex.I)) +
        (Complex.exp ((phaseAngleInt v 3 t : ℂ) * Complex.I) + Complex.exp ((-phaseAngleInt v 3 t : ℂ) * Complex.I)) := by ring
    _ = (6 : ℂ) + (2 : ℂ) * (Real.cos (phaseAngleInt v 0 t) : ℂ) +
        (2 : ℂ) * (Real.cos (phaseAngleInt v 1 t) : ℂ) +
        (2 : ℂ) * (Real.cos (phaseAngleInt v 2 t) : ℂ) +
        (2 : ℂ) * (Real.cos (phaseAngleInt v 3 t) : ℂ) := by rw [h0, h1, h2, h3]
    _ = ((2 * (3 + Real.cos (phaseAngleInt v 0 t) + Real.cos (phaseAngleInt v 1 t) +
        Real.cos (phaseAngleInt v 2 t) + Real.cos (phaseAngleInt v 3 t)) : ℝ) : ℂ) := by
          norm_num [Complex.ofReal_mul, Complex.ofReal_add]
          ring

'''

s = s[:start] + replacement + s[end:]
p.write_text(s)
