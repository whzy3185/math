from pathlib import Path
root=Path('formal/lean-lonely-runner/project')
p=root/'LonelyRunner/FirstCoefficients.lean'
s=p.read_text()
s=s.replace('namespace LonelyRunner\n', 'namespace LonelyRunner\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n', 1)
p.write_text(s)
