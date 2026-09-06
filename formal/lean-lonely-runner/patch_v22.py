from pathlib import Path

p = Path('formal/lean-lonely-runner/project/LonelyRunner/FirstLaurent.lean')
s = p.read_text()

old_q = '''    _ = ((2 - 2 * Real.cos (phaseAngleInt v i t) : ℝ) : ℂ) := by
      rw [← Complex.ofReal_cos]
      rw [Complex.ofReal_sub, Complex.ofReal_mul]
      norm_num
'''
new_q = '''    _ = ((2 - 2 * Real.cos (phaseAngleInt v i t) : ℝ) : ℂ) := by
      rw [Complex.ofReal_sub, Complex.ofReal_mul]
      change (2 : ℂ) - (2 : ℂ) * (Real.cos (phaseAngleInt v i t) : ℂ) =
        (2 : ℂ) - (2 : ℂ) * (Real.cos (phaseAngleInt v i t) : ℂ)
      rfl
'''
assert old_q in s
s = s.replace(old_q, new_q, 1)

old_l = '''    _ = ((2 * (3 + Real.cos (phaseAngleInt v 0 t) + Real.cos (phaseAngleInt v 1 t) +
        Real.cos (phaseAngleInt v 2 t) + Real.cos (phaseAngleInt v 3 t)) : ℝ) : ℂ) := by
          rw [← Complex.ofReal_cos, ← Complex.ofReal_cos, ← Complex.ofReal_cos, ← Complex.ofReal_cos]
          rw [Complex.ofReal_mul]
          rw [Complex.ofReal_add, Complex.ofReal_add, Complex.ofReal_add, Complex.ofReal_add]
          norm_num
          ring
'''
new_l = '''    _ = ((2 * (3 + Real.cos (phaseAngleInt v 0 t) + Real.cos (phaseAngleInt v 1 t) +
        Real.cos (phaseAngleInt v 2 t) + Real.cos (phaseAngleInt v 3 t)) : ℝ) : ℂ) := by
          rw [Complex.ofReal_mul]
          rw [Complex.ofReal_add, Complex.ofReal_add, Complex.ofReal_add, Complex.ofReal_add]
          change (6 : ℂ) + (2 : ℂ) * (Real.cos (phaseAngleInt v 0 t) : ℂ) +
              (2 : ℂ) * (Real.cos (phaseAngleInt v 1 t) : ℂ) +
              (2 : ℂ) * (Real.cos (phaseAngleInt v 2 t) : ℂ) +
              (2 : ℂ) * (Real.cos (phaseAngleInt v 3 t) : ℂ) =
            (2 : ℂ) * ((3 : ℂ) + (Real.cos (phaseAngleInt v 0 t) : ℂ) +
              (Real.cos (phaseAngleInt v 1 t) : ℂ) +
              (Real.cos (phaseAngleInt v 2 t) : ℂ) +
              (Real.cos (phaseAngleInt v 3 t) : ℂ))
          ring
'''
assert old_l in s
s = s.replace(old_l, new_l, 1)

p.write_text(s)
