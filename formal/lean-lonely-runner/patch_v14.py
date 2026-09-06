from pathlib import Path

p = Path('formal/lean-lonely-runner/project/LonelyRunner/FirstLaurent.lean')
s = p.read_text()

old = '''        · have hd : d = -c := by omega
          rw [hd]
          simp [insertNonzero]
          ring
'''
new = '''        · have hd : d = -c := by omega
          rw [hd]
          simp [insertNonzero]
'''
assert old in s
s = s.replace(old, new, 1)

old = '''      · by_cases hlt : relationLexLT r s
        · simp [insertNonzero, hrs, hlt]
          ring
        · simp [insertNonzero, hrs, hlt, ih]
'''
new = '''      · by_cases hlt : relationLexLT r s
        · simp [insertNonzero, hrs, hlt]
        · simp [insertNonzero, hrs, hlt, ih]
'''
assert old in s
s = s.replace(old, new, 1)

s = s.replace('''    _ = ((2 - 2 * Real.cos (phaseAngleInt v i t) : ℝ) : ℂ) := by push_cast; ring
''','''    _ = ((2 - 2 * Real.cos (phaseAngleInt v i t) : ℝ) : ℂ) := by norm_cast
''',1)

old = '''    _ = ((2 * (3 + Real.cos (phaseAngleInt v 0 t) + Real.cos (phaseAngleInt v 1 t) +
        Real.cos (phaseAngleInt v 2 t) + Real.cos (phaseAngleInt v 3 t)) : ℝ) : ℂ) := by
          push_cast
          ring
'''
new = '''    _ = ((2 * (3 + Real.cos (phaseAngleInt v 0 t) + Real.cos (phaseAngleInt v 1 t) +
        Real.cos (phaseAngleInt v 2 t) + Real.cos (phaseAngleInt v 3 t)) : ℝ) : ℂ) := by
          norm_cast
'''
assert old in s
s = s.replace(old,new,1)

p.write_text(s)
