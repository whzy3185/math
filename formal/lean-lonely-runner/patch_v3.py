from pathlib import Path
root=Path('formal/lean-lonely-runner/project')
p=root/'LonelyRunner/FirstCoefficients.lean'
s=p.read_text()
old='''def supportShapeOK (r : Relation) : Bool :=\n  decide (\n    (if (r 0).natAbs = 4 then 1 else 0) +\n    (if (r 1).natAbs = 4 then 1 else 0) +\n    (if (r 2).natAbs = 4 then 1 else 0) +\n    (if (r 3).natAbs = 4 then 1 else 0) ≤ 1)\n'''
new='''def supportShapeOK (r : Relation) : Bool :=\n  if firstCoeff r = 0 then true\n  else decide (\n    (if (r 0).natAbs = 4 then 1 else 0) +\n    (if (r 1).natAbs = 4 then 1 else 0) +\n    (if (r 2).natAbs = 4 then 1 else 0) +\n    (if (r 3).natAbs = 4 then 1 else 0) ≤ 1)\n'''
assert old in s
p.write_text(s.replace(old,new))
