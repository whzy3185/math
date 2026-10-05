#!/usr/bin/env python3
"""Final bounded review-history, failure-order, and gate-separation regressions."""
from pathlib import Path
import argparse,importlib.util,tempfile,json,copy,hashlib
ap=argparse.ArgumentParser();ap.add_argument('--candidate',default=str(Path(__file__).resolve().parents[1]));ap.add_argument('--output',required=True);a=ap.parse_args();R=Path(a.candidate)
s=importlib.util.spec_from_file_location('cf',R/'tests/complete_fixture.py');cf=importlib.util.module_from_spec(s);s.loader.exec_module(cf)
results=[]
def run(name,mutate,expect='reject',post=None,valid=None):
 with tempfile.TemporaryDirectory() as td:
  p=Path(td);o,d=cf.complete_fixture(p);mutate(o,d,p);f=cf.materialize(p,o,d)
  if post:post(o,d,p);f.write_text(json.dumps(o))
  try:
   out=cf.m.readiness_check(f);actual='accept' if out.get('ready_for_human_submission_decision') else 'reject';met=actual==expect and (valid is None or out.get('record_valid')==valid);results.append({'name':name,'expected':expect,'expected_record_valid':valid,'actual':actual,'expectation_met':met,'result':out})
  except Exception as e:results.append({'name':name,'expected':expect,'actual':'crash','expectation_met':False,'exception':type(e).__name__+': '+str(e)})
run('complete_control',lambda *args:None,'accept',valid=True)
def legacy(o,d,p):
 c=copy.deepcopy(o['review_contexts'][0]);c.update(context_id='legacy',reviewed_version='v0',rounds_used=2,retired=True,reviewer_id='old-R',editor_id='old-E');v=copy.deepcopy(d['version_registry']['versions'][0]);v.update(version_id='v0',parent_version=None);v['review_contexts']=[copy.deepcopy(c)];d['version_registry']['versions'].insert(0,v);o['review_contexts'].append(copy.deepcopy(c));d['version_registry']['versions'][1]['review_contexts'].append(copy.deepcopy(c))
run('positive_retired_context_historical_retention',legacy,'accept',valid=True)
def alias(o,d,p):
 (p/'docs').mkdir();(p/'docs'/'proof_obligations.json').write_bytes((p/'proof_obligations.json').read_bytes());(p/'alias').symlink_to(p/'docs',target_is_directory=True);o['linked_records']['proof_obligations']['path']='alias/proof_obligations.json'
run('top_linked_symlink_parent',lambda *args:None,post=alias)
def tied(o,d,p):
 c=copy.deepcopy(cf.rec(d,'S14'));c.update(receipt_id='same-time-fail',result='fail');c['details']['replay_exit_code']=1;d['receipts']['receipts'].append(c)
run('conflicting_latest_receipts_same_timestamp',tied)
def relabel(o,d,p):
 v=copy.deepcopy(d['version_registry']['versions'][0]);v.update(version_id='v0',parent_version=None);v['review_contexts'][0].update(context_id='retired-old-context',reviewed_version='v0',rounds_used=2,retired=True);d['version_registry']['versions'].insert(0,v)
run('retired_executor_relabelled_across_versions',relabel)
run('consent_wrong_source_fingerprint',lambda o,d,p:cf.rec(d,'S15')['details'].update(source_fingerprint='0'*64))
run('consent_missing_source_fingerprint',lambda o,d,p:cf.rec(d,'S15')['details'].pop('source_fingerprint',None))
def continuation(o,d,p):
 o['gates'][9]['status']='blocked';o['gates'][9]['notes']='Disclosed exposure; no pristine initial review claimed'
 o['review_contexts'][0].update(exposure='contaminated_disclosed',rounds_used=2,retired=True)
 d['version_registry']['versions'][0]['review_contexts']=copy.deepcopy(o['review_contexts'])
 d['receipts']['receipts']=[x for x in d['receipts']['receipts'] if x['gate']!='S09']
run('disclosed_continuation_closes_issues_without_blindness',continuation,'reject',valid=True)
out={'candidate':str(R),'files':{n:hashlib.sha256((R/'scripts'/n).read_bytes()).hexdigest() for n in ['workflow_check.py','readiness_links.py','exact_bindings.py','schema_guard.py']},'total':len(results),'met':sum(x['expectation_met'] for x in results),'results':results};Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2));[print('OK' if x['expectation_met'] else 'BUG',x['name'],x['actual'],x.get('result',{}).get('record_valid')) for x in results]
