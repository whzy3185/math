#!/usr/bin/env python3
"""Validate this generic toolkit and optional, explicitly supplied user inputs.
No research dataset is embedded or inferred. Actual input checks are opt-in.
"""
from pathlib import Path
import argparse,json,subprocess,sys
R=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--readiness-record',action='append',default=[],help='Explicit local readiness JSON; may be repeated')
p.add_argument('--packet',action='append',default=[],help='Explicit local neutral packet directory; may be repeated')
p.add_argument('--output-dir',help='Report directory; defaults to validation/')
a=p.parse_args();V=Path(a.output_dir).resolve() if a.output_dir else R/'validation';V.mkdir(parents=True,exist_ok=True)
checks=[];input_results=[]
def run(args,name):
 q=subprocess.run(args,cwd=R,capture_output=True,text=True)
 (V/f'{name}.txt').write_text(q.stdout+q.stderr)
 return q
q=run([sys.executable,'-m','unittest','discover','-s','tests','-v'],'unit_tests')
checks.append({'name':'synthetic_unit_tests','exit_code':q.returncode,'pass':q.returncode==0})
for filename,label,selector in [('check_basic_records.py','synthetic_basic','--candidate'),('check_version_bindings.py','synthetic_bindings','--scripts'),('check_history_edges.py','synthetic_edges','--candidate')]:
 destination=V/(label+'.json')
 target=R/'scripts' if selector=='--scripts' else R
 q=run([sys.executable,str(R/'tests'/filename),selector,str(target),'--output',str(destination)],label)
 try:
  summary=json.loads(destination.read_text());total=summary.get('total',len(summary.get('results',[])));met=summary.get('met',sum(bool(x.get('expectation_met')) for x in summary.get('results',[])))
  good=q.returncode==0 and total>0 and met==total
 except (OSError,ValueError):total=met=0;good=False
 checks.append({'name':label,'cases':total,'expected_dispositions_met':met,'pass':good})
try:
 import jsonschema
 for f in (R/'schemas').glob('*.schema.json'):jsonschema.Draft202012Validator.check_schema(json.loads(f.read_text()))
 checks.append({'name':'eight_generic_schemas','pass':True})
except ImportError:
 checks.append({'name':'optional_jsonschema','pass':None,'note':'Not installed; the dependency-free schema guard remains active in readiness checks'})
for mode,paths in [('readiness',a.readiness_record),('packet',a.packet)]:
 for index,path in enumerate(paths,1):
  label=f'{mode}_{index}';out=V/(label+'.json')
  q=run([sys.executable,str(R/'scripts/workflow_check.py'),mode,str(Path(path).resolve()),'--output',str(out)],label)
  try:
   result=json.loads(out.read_text());valid=result.get('record_valid') if mode=='readiness' else result.get('lint_pass')
  except (OSError,ValueError):result={};valid=False
  # An honestly blocked readiness record may be structurally valid. Its readiness is reported separately.
  checks.append({'name':label,'exit_code':q.returncode,'pass':bool(valid)})
  input_results.append({'name':label,'structurally_valid':bool(valid),'ready_for_human_submission_decision':result.get('ready_for_human_submission_decision'),'packet_lint_pass':result.get('lint_pass')})
result={'test_suite_pass':all(c['pass'] is not False for c in checks),'only_synthetic_inputs':not input_results,'explicit_user_input_checks':len(input_results),'checks':checks,'input_results':input_results,'interpretation':'Generic software checks and synthetic fixtures do not establish any real mathematical result, permission, authorship or venue decision. Explicit user inputs, if any, retain their separate readiness results.'}
(V/'bundle_validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));sys.exit(0 if result['test_suite_pass'] else 2)
