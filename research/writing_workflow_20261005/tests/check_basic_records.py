#!/usr/bin/env python3
"""Independent adversarial bookkeeping tests; no mathematical truth checking."""
import argparse, copy, hashlib, importlib.util, json, tempfile, traceback
from pathlib import Path
P=argparse.ArgumentParser(); P.add_argument('--candidate', default=str(Path(__file__).resolve().parents[1])); P.add_argument('--output', required=True); a=P.parse_args()
R=Path(a.candidate)
s=importlib.util.spec_from_file_location('checker',R/'scripts/workflow_check.py'); m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
try:
 import jsonschema
 schema=json.loads((R/'schemas/readiness.schema.json').read_text())
except ImportError: jsonschema=None
results=[]
def sh(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def fixture(root):
 (root/'evidence.txt').write_text('Generic attestation, no machine-readable stage receipt.\n')
 (root/'manuscript.tex').write_text('Version 1 manuscript bytes.\n')
 e=[{'path':'evidence.txt','sha256':sh(root/'evidence.txt')}]
 c={'id':'C1','statement':'A stated theorem','hypotheses':['explicit'],'quantifiers':'all objects in domain','dependencies':[],'evidence_kind':'analyticProved','verification_state':'audited','novelty_status':'not_assessed','scope_exclusions':['outside domain'],'formal_coverage':'unformalized','evidence':copy.deepcopy(e)}
 gates=[{'id':i,'status':'pass','owner':'custodian','notes':'Generic attestation','acceptance':'specific attestation','version':'v1','evidence':copy.deepcopy(e),'review_context_id':'new'} for i in m.STAGES]
 return {'schema_version':'1.0','paper':'test','version':'v1','recorded_utc':'2026-10-05T00:00:00Z','pdf_sha256':'0'*64,'claims':[c],'gates':gates,'blockers':[],'review_contexts':[{'context_id':'new','reviewer_id':'R','editor_id':'E','rounds_used':1,'retired':False,'initial_inherited_history':False,'exposure':'clean','reviewed_version':'v1'}],'submission':{'authors_confirmed':True,'journal_selected':True,'consent_confirmed':True,'disclosures_checked':True,'automatic_submission':False,'publication_authorized':False,'notes':'All flags asserted; no named authors or consent receipt'}}
def case(name, change, expected='reject', packet=False):
 with tempfile.TemporaryDirectory() as d:
  root=Path(d); obj=fixture(root)
  if packet:
   obj={'schema_version':'1.0','packet_id':'test','files':[{'path':'manuscript.tex','sha256':sh(root/'manuscript.tex'),'role':'manuscript_source'}]}; (root/'evidence.txt').unlink()
  change(obj,root)
  path=root/('packet.json' if packet else 'record.json'); path.write_text(json.dumps(obj))
  schema_errors=[]
  schema_checked = jsonschema is not None and not packet
  if schema_checked:
   schema_errors=[e.message for e in jsonschema.Draft202012Validator(schema).iter_errors(obj)]
  schema_state = {
   'schema_valid': (not schema_errors) if schema_checked else None,
   'schema_check_performed': schema_checked,
   'schema_check_reason': None if schema_checked else ('Optional full JSON Schema validation is not run for packet cases in this harness' if packet else 'Optional jsonschema package is unavailable; full JSON Schema validation was not performed')
  }
  try:
   out=m.packet_check(root) if packet else m.readiness_check(path)
   accepted=out.get('lint_pass') if packet else out.get('ready_for_human_submission_decision')
   disposition='accept' if accepted else 'reject'
   results.append({'name':name,'expected':expected,'actual':disposition,'expectation_met':disposition==expected,**schema_state,'schema_errors':schema_errors,'result':out})
  except Exception as e:results.append({'name':name,'expected':expected,'actual':'crash','expectation_met':False,'exception':type(e).__name__+': '+str(e),**schema_state,'schema_errors':schema_errors})
case('baseline_generic_evidence_cannot_establish_stage_receipts',lambda o,r:None)
case('stale_evidence_sha',lambda o,r:o['claims'][0]['evidence'][0].update(sha256='0'*64))
case('missing_evidence_file',lambda o,r:(r/'evidence.txt').unlink())
case('traversal_evidence_path',lambda o,r:o['claims'][0]['evidence'][0].update(path='../outside.txt'))
def symlink(o,r):
 (r/'alias.txt').symlink_to(r/'evidence.txt');o['claims'][0]['evidence'][0]['path']='alias.txt'
case('symlink_evidence_path',symlink)
case('self_cyclic_proof_dependency',lambda o,r:o['claims'][0].update(dependencies=['C1']))
def cycle(o,r):
 c=copy.deepcopy(o['claims'][0]);c.update(id='C2',dependencies=['C1']);o['claims'][0]['dependencies']=['C2'];o['claims'].append(c)
case('two_node_proof_cycle',cycle)
case('omitted_proof_obligation_table',lambda o,r:None)
case('disputed_claim_all_stages_pass',lambda o,r:o['claims'][0].update(verification_state='disputed'))
case('blocked_claim_all_stages_pass',lambda o,r:o['claims'][0].update(verification_state='blocked'))
case('unreviewed_claim_all_stages_pass',lambda o,r:o['claims'][0].update(verification_state='unreviewed'))
case('invalid_verified_state',lambda o,r:o['claims'][0].update(verification_state='verified'))
case('review_context_three_rounds',lambda o,r:o['review_contexts'][0].update(rounds_used=3))
def dupcontext(o,r):
 c=o['review_contexts'][0];c.update(rounds_used=2,retired=True);x=copy.deepcopy(c);x.update(rounds_used=1,retired=False);o['review_contexts'].append(x)
case('same_context_split_into_three_rounds',dupcontext)
def renamed(o,r):
 c=o['review_contexts'][0];c.update(rounds_used=2,retired=True);x=copy.deepcopy(c);x.update(context_id='pretend-new',rounds_used=1,retired=False);o['review_contexts'].append(x)
case('retired_reviewer_relabelled_as_new_context',renamed)
case('reviewer_editor_same_identity',lambda o,r:o['review_contexts'][0].update(editor_id='R'))
case('missing_reviewer_identity',lambda o,r:o['review_contexts'][0].pop('reviewer_id'))
case('stale_review_version',lambda o,r:o['review_contexts'][0].update(reviewed_version='v0'))
case('current_pdf_hash_not_bound_to_any_file',lambda o,r:o.update(pdf_sha256='f'*64))
def rewrite(o,r):
 (r/'manuscript.tex').write_text('Substantially different version 2 content without version bump.\n')
case('manuscript_bytes_changed_without_version_bump',rewrite)
def badexposure(o,r):
 o['review_contexts'][0]['exposure_evidence']=[{'path':'missing_exposure_log.json','sha256':'0'*64}]
case('missing_exposure_receipt_ignored',badexposure)
case('S14_remote_verified_without_receipt',lambda o,r:o['gates'][14].update(acceptance='Public archive retrieved anonymously and replayed; no receipt exists'))
case('unknown_policy_but_S00_pass',lambda o,r:o['gates'][0].update(acceptance='No journal chosen; policy unknown'))
case('author_consent_boolean_false',lambda o,r:o['submission'].update(consent_confirmed=False))
case('author_consent_boolean_true_no_people_or_receipt',lambda o,r:None)
case('schema_missing_required_submission',lambda o,r:o.pop('submission'))
def formalna(o,r):
 o['claims'][0].update(formal_coverage='formalized')
 o['gates'][12].update(status='not_applicable',justification='No formalization claimed',approved_by='E')
case('formalized_claim_but_formal_gate_na',formalna)
def pubunpub(o,r):
 o['claims'][0].update(evidence_kind='PublishedEstablished',primary_publication='arXiv:1234.5678',publication_status='unpublished')
case('published_established_but_unpublished',pubunpub)
case('empty_context_id_passes_clean_binding',lambda o,r:(o['review_contexts'][0].update(context_id=''),o['gates'][9].update(review_context_id=''),o['gates'][11].update(review_context_id='')))
case('empty_editor_identity',lambda o,r:o['review_contexts'][0].update(editor_id=''))
case('packet_stale_hash',lambda o,r:o['files'][0].update(sha256='0'*64),packet=True)
case('packet_missing_file',lambda o,r:(r/'manuscript.tex').unlink(),packet=True)
case('packet_traversal',lambda o,r:o['files'][0].update(path='../outside'),packet=True)
case('packet_nonobject_row',lambda o,r:o.update(files=['manuscript.tex']),packet=True)
case('packet_nonstring_hash',lambda o,r:o['files'][0].update(sha256=123),packet=True)
case('packet_nonstring_path',lambda o,r:o['files'][0].update(path=['manuscript.tex']),packet=True)
case('packet_review_verdict_in_id',lambda o,r:o.update(packet_id='PRIOR_REVIEW_ACCEPTED_PROVED_ALL_PASS'),packet=True)
case('packet_clean_input',lambda o,r:None,expected='accept',packet=True)
out={'candidate':str(R),'checker_sha256':sh(R/'scripts/workflow_check.py'),'total':len(results),'met':sum(x['expectation_met'] for x in results),'results':results}
Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2))
for x in results:print(('OK' if x['expectation_met'] else 'BUG'),x['name'],x['actual'],'schema_valid='+str(x.get('schema_valid')))
