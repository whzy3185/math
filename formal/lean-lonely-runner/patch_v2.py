from pathlib import Path
root=Path('formal/lean-lonely-runner/project')
# LowQuarter: close the unnamed noncomputable section before namespace.
p=root/'LonelyRunner/LowQuarter.lean'
s=p.read_text()
s=s.replace('''#print axioms integral_firstCertificateAt_neg\n\nend LonelyRunner\n''','''#print axioms integral_firstCertificateAt_neg\n\nend\nend LonelyRunner\n''')
p.write_text(s)
# FirstCoefficients: make the convolution expression parser-unambiguous.
p=root/'LonelyRunner/FirstCoefficients.lean'
s=p.read_text()
start=s.index('def firstCoeff (r : Relation) : ℤ :=')
end=s.index('\ndef zeroRelation', start)
new='''def firstCoeff (r : Relation) : ℤ :=\n  let q0 := qCoeff (r 0)\n  let q1 := qCoeff (r 1)\n  let q2 := qCoeff (r 2)\n  let q3 := qCoeff (r 3)\n  (-6 * q0 * q1 * q2 * q3) +\n    (-(qCoeff (r 0 - 1) + qCoeff (r 0 + 1)) * q1 * q2 * q3) +\n    (-(qCoeff (r 1 - 1) + qCoeff (r 1 + 1)) * q0 * q2 * q3) +\n    (-(qCoeff (r 2 - 1) + qCoeff (r 2 + 1)) * q0 * q1 * q3) +\n    (-(qCoeff (r 3 - 1) + qCoeff (r 3 + 1)) * q0 * q1 * q2)\n'''
s=s[:start]+new+s[end:]
p.write_text(s)
