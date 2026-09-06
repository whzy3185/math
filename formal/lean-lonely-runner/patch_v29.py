from pathlib import Path

p = Path('formal/lean-lonely-runner/project/LonelyRunner/SecondCoefficients.lean')
s = p.read_text()
s = s.replace('''lemma shiftedChoose_nonneg (k : ℕ) (z : ℤ) : 0 ≤ shiftedChoose k z := by
  unfold shiftedChoose
  split <;> simp
''','''lemma shiftedChoose_nonneg (k : ℕ) (z : ℤ) : 0 ≤ shiftedChoose k z := by
  simp [shiftedChoose]
''',1)
s = s.replace('interval_cases z <;> norm_num [shiftedChoose]',
              'interval_cases z <;> norm_num [shiftedChoose, Int.toNat]',3)
p.write_text(s)
