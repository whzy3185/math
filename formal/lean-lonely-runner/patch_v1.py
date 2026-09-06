from pathlib import Path
root=Path('formal/lean-lonely-runner/project')
# LineContributions
p=root/'LonelyRunner/LineContributions.lean'
s=p.read_text()
s=s.replace('namespace LonelyRunner\nset_option', 'namespace LonelyRunner\nopen scoped BigOperators\nset_option')
s=s.replace('''def J (k : ℕ) (r : Relation) : ℤ :=\n  ∑ n in Finset.range (2 * k + 1),\n    let j : ℤ := (n : ℤ) - (k : ℤ)\n    ((-1 : ℤ) ^ (j * coordSum r).natAbs) *\n      shiftedChoose k (j * r 0) *\n      shiftedChoose k (j * r 1) *\n      shiftedChoose k (j * r 2) *\n      shiftedChoose k (j * r 3)\n''','''def J (k : ℕ) (r : Relation) : ℤ :=\n  (Finset.range (2 * k + 1)).sum fun n =>\n    let j : ℤ := (n : ℤ) - (k : ℤ)\n    ((-1 : ℤ) ^ (j * coordSum r).natAbs) *\n      shiftedChoose k (j * r 0) *\n      shiftedChoose k (j * r 1) *\n      shiftedChoose k (j * r 2) *\n      shiftedChoose k (j * r 3)\n''')
p.write_text(s)
# LowQuarter
p=root/'LonelyRunner/LowQuarter.lean'
s=p.read_text()
s=s.replace('namespace LonelyRunner\n\nopen Set', 'namespace LonelyRunner\n\nnoncomputable section\n\nopen Set')
s=s.replace('''  have habsy : |y| < Real.pi / 2 := by\n    dsimp [y]\n    rw [abs_mul, abs_of_pos htwoPi]\n    have h := mul_lt_mul_of_pos_left hk htwoPi\n    convert h using 1 <;> ring\n''','''  have habsy : |y| < Real.pi / 2 := by\n    dsimp [y]\n    rw [abs_mul, abs_of_pos htwoPi]\n    calc\n      (2 * Real.pi) * |x - (k : ℝ)| < (2 * Real.pi) * ((1 : ℝ) / 4) :=\n        mul_lt_mul_of_pos_left hk htwoPi\n      _ = Real.pi / 2 := by ring\n''')
s=s.replace('''  have hs : (1 : ℝ) ≤ (speedScale v : ℝ) := by\n    exact_mod_cast (Nat.succ_le_iff.mpr (by omega : 0 < speedScale v))\n''','''  have hsNat : 1 ≤ speedScale v := by\n    unfold speedScale\n    omega\n  have hs : (1 : ℝ) ≤ (speedScale v : ℝ) := by exact_mod_cast hsNat\n''')
s=s.replace('''  have hspos : (0 : ℝ) < (speedScale v : ℝ) := by positivity\n''','''  have hsNat : 0 < speedScale v := by\n    unfold speedScale\n    omega\n  have hspos : (0 : ℝ) < (speedScale v : ℝ) := by exact_mod_cast hsNat\n''')
s=s.replace('''  · have h := mul_lt_mul_of_pos_left hfraclt (mul_pos (by norm_num) Real.pi_pos)\n    convert h using 1 <;> ring\n''','''  · have htwoPi : 0 < 2 * Real.pi := by positivity\n    calc\n      2 * Real.pi * ((v i : ℝ) * firstStrictTime v)\n          < 2 * Real.pi * ((1 : ℝ) / 2) :=\n            mul_lt_mul_of_pos_left hfraclt htwoPi\n      _ = Real.pi := by ring\n''')
p.write_text(s)
