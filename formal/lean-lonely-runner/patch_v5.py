from pathlib import Path
root = Path('formal/lean-lonely-runner/project')
p = root / 'LonelyRunner/FourierOrthogonality.lean'
s = p.read_text()
if 'import Mathlib.Analysis.SpecialFunctions.Integrals.Basic' not in s:
    s = s.replace('import LonelyRunner.FirstCoefficients\n', 'import LonelyRunner.FirstCoefficients\nimport Mathlib.Analysis.SpecialFunctions.Integrals.Basic\n', 1)
s = s.replace('def fourierMode (n : ℤ) (t : ℝ) : ℂ :=', 'noncomputable def fourierMode (n : ℤ) (t : ℝ) : ℂ :=', 1)
s = s.replace('  rw [intervalIntegral.integral_exp_mul_complex (a := (0 : ℝ)) (b := 1) hc]\n',
'''  change (∫ t : ℝ in (0 : ℝ)..1, Complex.exp (c * (t : ℂ))) = 0\n  rw [integral_exp_mul_complex hc]\n''', 1)
s = s.replace('def relationMode (r : Relation) (v : Fin 4 → ℤ) (t : ℝ) : ℂ :=', 'noncomputable def relationMode (r : Relation) (v : Fin 4 → ℤ) (t : ℝ) : ℂ :=', 1)
p.write_text(s)
