"""Synthetic positive administrative fixture. No real theorem, consent, or venue claim."""
import copy,hashlib,json
from pathlib import Path
import importlib.util
s=importlib.util.spec_from_file_location('checker',Path(__file__).parents[1]/'scripts/workflow_check.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
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

def complete_fixture(root):
 o,d=fixture(root)
 d['proof_obligations']['schema_version']='1.0';d['receipts']['schema_version']='1.0'
 d['required_inventory']={'schema_version':'1.0','paper':'test','version':'v1','claim_ids':['C1'],'obligation_ids':['O1','O2'],'issue_ids':['R1']}
 (root/'packet_identity.json').write_text(json.dumps({'schema_version':'1.0','packet_id':'synthetic-v1','files':[{'path':'manuscript.pdf','sha256':o['pdf_sha256'],'role':'manuscript_pdf'},{'path':'manuscript.tex','sha256':sh(root/'manuscript.tex'),'role':'manuscript_source'}]}))
 (root/'archive.zip').write_bytes(b'Synthetic archive identity only')
 (root/'fresh_output.json').write_text('{"synthetic": true}')
 for z in d['receipts']['receipts']:
  if z['gate'] in ['S09','S11']:z['details'].update(packet_manifest=evidence(root/'packet_identity.json'),packet_manifest_sha256=sh(root/'packet_identity.json'))
  if z['gate']=='S14':z['details'].update(archive=evidence(root/'archive.zip'),archive_sha256=sh(root/'archive.zip'),fresh_output=evidence(root/'fresh_output.json'),fresh_output_sha256=sh(root/'fresh_output.json'))
 fp=hashlib.sha256(json.dumps(sorted((x['path'],x['sha256']) for x in [o['input_pdf'],*o['input_sources']]),separators=(',',':')).encode()).hexdigest()
 d['version_registry']['versions'][0]['source_fingerprint']=fp
 for z in d['receipts']['receipts']:
  if z['type']!='venue_policy':z['details']['source_fingerprint']=fp
 return o,d

def materialize(root,o,d):
 o['linked_records']={}
 for k,x in d.items():
  f=root/(k+'.json');f.write_text(json.dumps(x));o['linked_records'][k]=evidence(f)
 f=root/'record.json';f.write_text(json.dumps(o));return f
