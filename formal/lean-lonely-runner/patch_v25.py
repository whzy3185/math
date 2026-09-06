from pathlib import Path

p = Path('formal/lean-lonely-runner/project/LonelyRunner/FirstCertificateClosure.lean')
s = p.read_text()
old = '''  | nil =>\n      change (∫ _t : ℝ in (0 : ℝ)..1, (0 : ℂ)) = (0 : ℂ)\n      simp\n'''
new = '''  | nil =>\n      simp [firstFourierList]\n'''
assert old in s
p.write_text(s.replace(old, new, 1))
