#!/usr/bin/env python3
"""New-schema independent positive control and narrow contradiction tests."""
import argparse,copy,hashlib,importlib.util,json,tempfile
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--scripts',default=str(Path(__file__).resolve().parents[1]/'scripts'));p.add_argument('--output',required=True);a=p.parse_args()
s=importlib.util.spec_from_file_location('checker',Path(a.scripts)/'workflow_check.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def sh(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def evidence(p):return {'path':p.name,'sha256':sh(p)}
def fixture(r):
 (r/'evidence.txt').write_text('Synthetic evidence for administrative validator testing only.\n')
 (r/'manuscript.tex').write_text('Synthetic source\n');(r/'manuscript.pdf').write_bytes(b'%PDF-1.4\n%Synthetic test fixture, not a mathematical paper\n%%EOF\n')
 ev=[evidence(r/'evidence.txt')];pdf=evidence(r/'manuscript.pdf');source=evidence(r/'manuscript.tex')
 c={'id':'C1','statement':'A stated theorem','hypotheses':['explicit'],'quantifiers':'all objects in domain','dependencies':[],'evidence_kind':'analyticProved','verification_state':'audited','novelty_status':'not_assessed','scope_exclusions':['outside domain'],'formal_coverage':'unformalized','evidence':copy.deepcopy(ev)}
 context={'context_id':'ctx1','reviewer_id':'R','editor_id':'E','rounds_used':1,'retired':False,'initial_inherited_history':False,'exposure':'clean','reviewed_version':'v1','exposure_evidence':copy.deepcopy(ev)}
 gates=[{'id':g,'status':'pass','owner':'custodian','notes':'Synthetic test','acceptance':'Synthetic attributed acceptance','version':'v1','evidence':copy.deepcopy(ev),'review_context_id':'ctx1'} for g in m.STAGES]
 gates[12].update(status='not_applicable',justification='No formalization claimed',approved_by='E')
 o={'schema_version':'1.0','paper':'test','version':'v1','recorded_utc':'2026-10-05T00:00:00Z','pdf_sha256':pdf['sha256'],'input_pdf':pdf,'input_sources':[source],'claims':[c],'gates':gates,'blockers':[],'review_contexts':[context],'submission':{'authors_confirmed':True,'journal_selected':True,'consent_confirmed':True,'disclosures_checked':True,'automatic_submission':False,'publication_authorized':False,'notes':'Synthetic administrative fixture, not real consent'}}
 ob={'id':'O1','claim_id':'C1','status':'discharged','acceptance':'Synthetic obligation discharged','checked_by':'R','evidence':copy.deepcopy(ev)}
 issue={'issue_id':'R1','severity':'major','original_location':'1','disposition':'accepted','change_kind':'editorial','response':'Synthetic repair','new_location':'1','affected_claims':['C1'],'evidence':copy.deepcopy(ev),'reviewer_closure':'closed'}
 docs={'proof_obligations':{'paper':'test','version':'v1','obligations':[ob,dict(copy.deepcopy(ob),id='O2')]},'review_response':{'schema_version':'1.0','paper':'test','baseline_version':'v0','new_version':'v1','reviewer_id':'R','editor_id':'E','issues':[issue]},'version_registry':{'schema_version':'1.0','paper':'test','versions':[{'version_id':'v1','parent_version':'v0','created_utc':'2026-10-05T00:00:00Z','source_commit':None,'files':[source,pdf],'pdf_sha256':pdf['sha256'],'changed_claims':[],'invalidated_gates':[],'editor_id':'E','review_contexts':[copy.deepcopy(context)]}]},'receipts':{'paper':'test','version':'v1','receipts':[]}}
 details={
 'S00':('venue_policy',{'venue':'Example Journal','official_policy_urls':['https://example.org/policy'],'actual_ai_uses':['drafting'],'compatibility_basis':'Synthetic compatibility decision'}),
 'S08':('mathematical_audit',{'claim_ids':['C1'],'coverage':'All declared claims','review_report_sha256':ev[0]['sha256']}),
 'S09':('blind_review',{'context_id':'ctx1','packet_manifest_sha256':'a'*64,'pdf_sha256':pdf['sha256'],'no_inherited_history':True,'exposure':'clean'}),
 'S11':('rereview',{'context_id':'ctx1','pdf_sha256':pdf['sha256'],'closed_issue_ids':['R1'],'review_report_sha256':ev[0]['sha256']}),
 'S13':('pdf_visual_qa',{'pdf_sha256':pdf['sha256'],'page_count':1,'inspected_pages':[1]}),
 'S14':('archive_replay',{'url':'https://example.org/archive','archive_sha256':'a'*64,'anonymous_retrieval':True,'entrypoint':'python checker.py','replay_exit_code':0,'fresh_output_sha256':'b'*64}),
 'S15':('authorship_consent',{'authors':['Synthetic Author'],'journal':'Example Journal','approval_scope':'final manuscript and selected journal','consent_evidence':copy.deepcopy(ev)})}
 for g,(typ,d) in details.items():docs['receipts']['receipts'].append({'receipt_id':g+'-receipt','gate':g,'type':typ,'version':'v1','result':'pass','recorded_by':'test-author','recorded_utc':'2026-10-05T00:00:00Z','evidence':copy.deepcopy(ev),'details':d})
 return o,docs
def rec(d,g):return next(x for x in d['receipts']['receipts'] if x['gate']==g)
cs=importlib.util.spec_from_file_location('complete_fixture',Path(a.scripts).parent/'tests'/'complete_fixture.py');cf=importlib.util.module_from_spec(cs);cs.loader.exec_module(cf)
results=[]
def case(name,fn,expected='reject'):
 with tempfile.TemporaryDirectory() as td:
  r=Path(td);o,d=cf.complete_fixture(r);fn(o,d,r);o['linked_records']={}
  for k,x in d.items():
   f=r/(k+'.json');f.write_text(json.dumps(x));o['linked_records'][k]=evidence(f)
  f=r/'record.json';f.write_text(json.dumps(o))
  try:
   out=m.readiness_check(f);actual='accept' if out.get('ready_for_human_submission_decision') else 'reject'
   results.append({'name':name,'expected':expected,'actual':actual,'expectation_met':actual==expected,'result':out})
  except Exception as e:results.append({'name':name,'expected':expected,'actual':'crash','expectation_met':False,'error':type(e).__name__+': '+str(e)})
case('new_structurally_complete_control',lambda o,d,r:None,expected='accept')
case('all_linked_records_empty_objects',lambda o,d,r:[d.__setitem__(k,{}) for k in d])
case('all_linked_records_empty_lists',lambda o,d,r:[d.__setitem__(k,[]) for k in d])
case('delete_one_required_closed_obligation',lambda o,d,r:d['proof_obligations']['obligations'].pop())
case('delete_required_review_issue',lambda o,d,r:d['review_response'].update(issues=[]))
case('receipt_refers_to_nonexistent_context',lambda o,d,r:rec(d,'S09')['details'].update(context_id='never-created'))
case('receipt_refers_to_wrong_packet_hash',lambda o,d,r:rec(d,'S09')['details'].update(packet_manifest_sha256='0'*64))
case('closed_issue_ids_disagree',lambda o,d,r:rec(d,'S11')['details'].update(closed_issue_ids=['not-a-real-issue']))
case('policy_and_consent_journals_disagree',lambda o,d,r:rec(d,'S15')['details'].update(journal='A different journal'))
case('receipt_scalar_hash_invalid',lambda o,d,r:rec(d,'S14')['details'].update(archive_sha256='not-a-hash',fresh_output_sha256='not-a-hash'))
case('receipt_boolean_false_exit_code',lambda o,d,r:rec(d,'S14')['details'].update(replay_exit_code=False))
case('receipt_false_consent_evidence',lambda o,d,r:rec(d,'S15')['details'].update(authors=False,journal=False,consent_evidence=False))
case('review_response_identity_unbound',lambda o,d,r:d['review_response'].update(reviewer_id='not-R',editor_id='not-E'))
case('obligation_not_applicable_without_reason',lambda o,d,r:[x.update(status='not_applicable') for x in d['proof_obligations']['obligations']])
def historical(o,d,r):
 v=copy.deepcopy(d['version_registry']['versions'][0]);v.update(version_id='v0',parent_version=None)
 v['review_contexts'][0].update(rounds_used=2,retired=True,reviewed_version='v0')
 d['version_registry']['versions'].insert(0,v)
case('historical_context_retired_then_round_count_reset',historical)
def linksym(o,d,r):
 (r/'actual').mkdir();(r/'actual'/'ev.txt').write_text('existing bytes');(r/'alias').symlink_to(r/'actual',target_is_directory=True)
 d['proof_obligations']['obligations'][0]['evidence']=[{'path':'alias/ev.txt','sha256':sh(r/'actual'/'ev.txt')}]
case('linked_evidence_symlink_parent',linksym)
def wrong_packet(o,d,r):
 p=r/'packet_identity.json';x=json.loads(p.read_text());x['files'][0]['sha256']='0'*64;p.write_text(json.dumps(x))
 rec(d,'S09')['details'].update(packet_manifest=evidence(p),packet_manifest_sha256=sh(p))
case('packet_manifest_contains_wrong_pdf_identity',wrong_packet)
def change_source(o,d,r):
 (r/'manuscript.tex').write_text('Completely different source without review or new version')
 o['input_sources'][0]=evidence(r/'manuscript.tex')
 d['version_registry']['versions'][0]['files'][0]=evidence(r/'manuscript.tex')
case('changed_source_but_review_receipts_not_invalidated',change_source)
case('version_inventory_omits_current_source',lambda o,d,r:d['version_registry']['versions'][0].update(files=[o['input_pdf']]))
def reverse_history(o,d,r):
 v=copy.deepcopy(d['version_registry']['versions'][0]);v.update(version_id='v0',parent_version=None)
 v['review_contexts'][0].update(rounds_used=2,retired=True,reviewed_version='v0')
 d['version_registry']['versions'].append(v)
case('retired_history_bypass_by_reordering_versions',reverse_history)
def samecount(o,d,r):
 v=copy.deepcopy(d['version_registry']['versions'][0]);v.update(version_id='v0',parent_version=None)
 v['review_contexts'][0].update(rounds_used=1,retired=False,reviewed_version='v0')
 d['version_registry']['versions'].insert(0,v)
case('same_context_reviewed_new_version_without_round_increment',samecount)
def additional_context(o,d,r):
 c=copy.deepcopy(o['review_contexts'][0]);c.update(context_id='old-context',reviewer_id='old-R',editor_id='old-E',reviewed_version='v0',retired=True)
 o['review_contexts'].append(c);d['version_registry']['versions'][0]['review_contexts'].append(copy.deepcopy(c))
 d['review_response'].update(reviewer_id='old-R',editor_id='old-E')
case('response_identity_matches_unrelated_old_context',additional_context)
case('consent_evidence_empty_object_entry',lambda o,d,r:rec(d,'S15')['details'].update(consent_evidence=[{}]))
case('blind_packet_ref_missing_path',lambda o,d,r:rec(d,'S09')['details'].update(packet_manifest={'sha256':rec(d,'S09')['details']['packet_manifest_sha256']}))
case('archive_ref_missing_path',lambda o,d,r:rec(d,'S14')['details'].update(archive={'sha256':rec(d,'S14')['details']['archive_sha256']}))
case('policy_missing_sources_boolean',lambda o,d,r:rec(d,'S00')['details'].update(official_policy_urls=False,actual_ai_uses=False,compatibility_basis=False))
case('na_obligation_for_claimed_theorem_without_alternative',lambda o,d,r:[x.update(status='not_applicable',justification='No proof check needed',approved_by='E') for x in d['proof_obligations']['obligations']])
def failed_receipt(o,d,r):
 c=copy.deepcopy(rec(d,'S14'));c.update(receipt_id='later-fail',result='fail',recorded_utc='2026-10-05T01:00:00Z');c['details']['replay_exit_code']=1;d['receipts']['receipts'].append(c)
case('later_failed_replay_ignored_due_earlier_pass',failed_receipt)
out={'checker_sha256':sh(Path(a.scripts)/'workflow_check.py'),'link_checker_sha256':sh(Path(a.scripts)/'readiness_links.py'),'total':len(results),'met':sum(x['expectation_met'] for x in results),'results':results};Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2));[print('OK' if x['expectation_met'] else 'BUG',x['name'],x['actual']) for x in results]
