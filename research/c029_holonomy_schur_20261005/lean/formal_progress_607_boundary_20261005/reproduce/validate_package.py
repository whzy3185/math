#!/usr/bin/env python3
"""Check public-file integrity, exact declaration sets, and source-profile isolation."""
from pathlib import Path
import hashlib,json,re
from validate_axioms import validate,tests,STANDARD
R=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def body(p):return '\n'.join(line for line in p.read_text().splitlines() if not line.startswith('import '))
assert tests()['status']=='PASS'
manifest={}
for line in (R/'SHA256SUMS').read_text().splitlines():
    digest,path=line.split('  ',1);assert path not in manifest;manifest[path]=digest
    assert sha(R/path)==digest,path
for profile in ['finite/formal','structural/src']:
    for source in (R/profile).rglob('*.lean'):
        for module in re.findall(r'^import\s+(\S+)',source.read_text(),re.M):
            if module.startswith(('TargetA.','C029')):
                assert (R/profile/(module.replace('.','/')+'.lean')).is_file(),(source,module)
finite=json.loads((R/'evidence/finite607_axioms.json').read_text())
expected=re.findall(r'^#print axioms (\S+)',(R/'finite/formal/R2FiniteSeedAxiomAudit.lean').read_text(),re.M)
assert len(expected)==len(set(expected))==607 and set(finite)==set(expected)
sets=json.loads((R/'evidence/declaration_sets.json').read_text())['sets']
assert set(sets['finite607'])==set(finite)
for key,file,count in [('typed_bridge_audit30','typed30_axioms.json',30),('boundary_structural37','structural37_axioms.json',37)]:
    axes=json.loads((R/'evidence'/file).read_text());assert len(axes)==count and set(axes)==set(sets[key])
    assert all(set(v)<=STANDARD for v in axes.values())
assert all(set(v)<=STANDARD for v in finite.values())
terminal=[]
for label,module,count in [('final_inverse','R2FinalInverseCertificate',3),('terminal_matrix','R2TerminalIdentificationCertificate',5),('finite_identification','R2FiniteSeedIdentification',7)]:
    names=re.findall(r'^#print axioms (\S+)',(R/'finite/formal/TargetA'/f'{module}.lean').read_text(),re.M)
    names=[n if n.startswith('TargetA.') else 'TargetA.'+n for n in names]
    result=validate((R/'evidence'/f'finite_{label}_axioms.log').read_text(),names)
    assert result['count']==count;terminal+=names
assert len(set(terminal))==15 and all(set(finite[n])<=STANDARD for n in terminal)
a=R/'finite/formal/TargetA';b=R/'structural/src/TargetA'
assert (a/'R2RationalRecurrence.lean').read_bytes()==(b/'R2RationalRecurrence.lean').read_bytes()
assert body(a/'R2TerminalSchur.lean')==body(b/'R2TerminalSchur.lean')
print(json.dumps({'status':'PASS','hashed_public_files':len(manifest),'finite_names':607,'typed_names':30,'boundary_names':37,'finite_chain_freshly_rebuilt_by_this_check':False},indent=2))
