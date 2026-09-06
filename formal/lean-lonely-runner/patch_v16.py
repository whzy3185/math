from pathlib import Path

p = Path('formal/lean-lonely-runner/project/LonelyRunner/FirstLaurent.lean')
s = p.read_text()

old = '''    _ = ((2 - 2 * Real.cos (phaseAngleInt v i t) : ℝ) : ℂ) := by
      simp only [← Complex.ofReal_cos]
      norm_num [Complex.ofReal_sub, Complex.ofReal_mul] <;> ring
'''
new = '''    _ = ((2 - 2 * Real.cos (phaseAngleInt v i t) : ℝ) : ℂ) := by
      rw [← Complex.ofReal_cos]
      rw [Complex.ofReal_sub, Complex.ofReal_mul]
      norm_num
'''
assert old in s
s = s.replace(old,new,1)

old = '''    _ = ((2 * (3 + Real.cos (phaseAngleInt v 0 t) + Real.cos (phaseAngleInt v 1 t) +
        Real.cos (phaseAngleInt v 2 t) + Real.cos (phaseAngleInt v 3 t)) : ℝ) : ℂ) := by
          simp only [← Complex.ofReal_cos]
          norm_num [Complex.ofReal_add, Complex.ofReal_mul] <;> ring
'''
new = '''    _ = ((2 * (3 + Real.cos (phaseAngleInt v 0 t) + Real.cos (phaseAngleInt v 1 t) +
        Real.cos (phaseAngleInt v 2 t) + Real.cos (phaseAngleInt v 3 t)) : ℝ) : ℂ) := by
          rw [← Complex.ofReal_cos, ← Complex.ofReal_cos, ← Complex.ofReal_cos, ← Complex.ofReal_cos]
          rw [Complex.ofReal_mul]
          rw [Complex.ofReal_add, Complex.ofReal_add, Complex.ofReal_add, Complex.ofReal_add]
          norm_num
'''
assert old in s
s = s.replace(old,new,1)

p.write_text(s)
