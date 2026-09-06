from pathlib import Path

p = Path('formal/lean-lonely-runner/project/LonelyRunner/FirstLaurent.lean')
s = p.read_text()

old_q = '''  have h := exp_I_add_exp_neg_I (phaseAngleInt v i t)\n  norm_num\n  calc\n'''
new_q = '''  have h := exp_I_add_exp_neg_I (phaseAngleInt v i t)\n  simp only [mul_one, one_mul, add_zero]\n  calc\n'''
assert old_q in s
s = s.replace(old_q, new_q, 1)

old_l = '''  have h3 := exp_I_add_exp_neg_I (phaseAngleInt v 3 t)\n  norm_num\n  calc\n'''
new_l = '''  have h3 := exp_I_add_exp_neg_I (phaseAngleInt v 3 t)\n  simp only [mul_one, one_mul, add_zero]\n  calc\n'''
assert old_l in s
s = s.replace(old_l, new_l, 1)

p.write_text(s)
