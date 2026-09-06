from pathlib import Path

p = Path('formal/lean-lonely-runner/project/LonelyRunner/FirstLaurent.lean')
s = p.read_text()

old = '''theorem exp_I_add_exp_neg_I (x : ℝ) :
    Complex.exp ((x : ℂ) * Complex.I) +
      Complex.exp ((-x : ℂ) * Complex.I) = ((2 * Real.cos x : ℝ) : ℂ) := by
  rw [Complex.exp_mul_I, Complex.exp_mul_I]
  simp [Real.cos_neg, Real.sin_neg]
  ring
'''
new = '''theorem exp_I_add_exp_neg_I (x : ℝ) :
    Complex.exp ((x : ℂ) * Complex.I) +
      Complex.exp ((-x : ℂ) * Complex.I) =
      (2 : ℂ) * (Real.cos x : ℂ) := by
  rw [Complex.exp_mul_I, Complex.exp_mul_I]
  simp [Real.cos_neg, Real.sin_neg]
  ring
'''
assert old in s
s = s.replace(old,new,1)

# Replace the final two cast proofs after the v17 transformations.
old = '''    _ = ((2 - 2 * Real.cos (phaseAngleInt v i t) : ℝ) : ℂ) := by
      rw [Complex.ofReal_sub, Complex.ofReal_mul]
      norm_num
'''
new = '''    _ = ((2 - 2 * Real.cos (phaseAngleInt v i t) : ℝ) : ℂ) := by
      rw [Complex.ofReal_sub, Complex.ofReal_mul]
      norm_num
'''
assert old in s
# unchanged text intentionally: with the new Euler RHS it now has the correct normal form.

old2 = '''    _ = ((2 * (3 + Real.cos (phaseAngleInt v 0 t) + Real.cos (phaseAngleInt v 1 t) +
        Real.cos (phaseAngleInt v 2 t) + Real.cos (phaseAngleInt v 3 t)) : ℝ) : ℂ) := by
          rw [Complex.ofReal_mul]
          rw [Complex.ofReal_add, Complex.ofReal_add, Complex.ofReal_add, Complex.ofReal_add]
          norm_num
          ring
'''
new2 = '''    _ = ((2 * (3 + Real.cos (phaseAngleInt v 0 t) + Real.cos (phaseAngleInt v 1 t) +
        Real.cos (phaseAngleInt v 2 t) + Real.cos (phaseAngleInt v 3 t)) : ℝ) : ℂ) := by
          rw [Complex.ofReal_mul]
          rw [Complex.ofReal_add, Complex.ofReal_add, Complex.ofReal_add, Complex.ofReal_add]
          norm_num
          ring
'''
assert old2 in s

p.write_text(s)
