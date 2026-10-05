#!/usr/bin/env python3
"""Write an explicit synthetic administrative example, not a real paper or consent."""
from pathlib import Path
import argparse,importlib.util
R=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__);p.add_argument('output');a=p.parse_args();out=Path(a.output).resolve()
if out.exists():p.error('refusing to overwrite an existing directory')
out.mkdir(parents=True)
s=importlib.util.spec_from_file_location('complete_fixture',R/'tests/complete_fixture.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
o,d=m.complete_fixture(out);f=m.materialize(out,o,d)
(out/'README.md').write_text('# Synthetic administrative example\n\nEvery author, consent, journal, proof assessment and output here is invented test data. The minimal PDF is only a byte-identity fixture and is not a rendered paper. This example demonstrates schema and record joins; it must never be submitted or represented as real verification.\n\nRun the readiness linter on record.json to see a structurally complete record. The packet linter is a separate interface and does not accept this entire administrative directory as a neutral packet.\n')
print(str(f))
