import importlib.util,json,hashlib,tempfile,unittest
from pathlib import Path
s=importlib.util.spec_from_file_location('checker',Path(__file__).parents[1]/'scripts/workflow_check.py')
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class Tests(unittest.TestCase):
 def packet(self,text='Theorem with proof.\n',name='manuscript.tex'):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);r=Path(t.name)
  (r/name).write_text(text)
  (r/'packet.json').write_text(json.dumps({'schema_version':'1.0','packet_id':'test','files':[{'path':name,'sha256':m.sha(r/name),'role':'manuscript_source'}]}));return r
 def test_clean(self):self.assertTrue(m.packet_check(self.packet())['lint_pass'])
 def test_status_metadata(self):self.assertFalse(m.packet_check(self.packet('"verified_via": "GitHub"'))['lint_pass'])
 def test_saved_success_json(self):self.assertFalse(m.packet_check(self.packet('{"status":"PASS"}',name='input.json'))['lint_pass'])
 def test_nested_saved_verdict(self):self.assertFalse(m.packet_check(self.packet('{"items":[{"verdict":"sound"}]}',name='input.json'))['lint_pass'])
 def test_verdict(self):self.assertFalse(m.packet_check(self.packet('independent manuscript integration PASS'))['lint_pass'])
 def test_extra_file(self):
  r=self.packet();(r/'old.txt').write_text('old');self.assertFalse(m.packet_check(r)['lint_pass'])
 def test_changed_bytes(self):
  r=self.packet();(r/'manuscript.tex').write_text('changed');self.assertFalse(m.packet_check(r)['lint_pass'])
 def test_report_name(self):self.assertFalse(m.packet_check(self.packet(name='referee.md'))['lint_pass'])
 def test_symlink(self):
  r=self.packet();(r/'alias').symlink_to(r/'manuscript.tex');self.assertFalse(m.packet_check(r)['lint_pass'])
 def test_path_escape(self):
  r=self.packet();a=json.loads((r/'packet.json').read_text());a['files'][0]['path']='../outside';(r/'packet.json').write_text(json.dumps(a));self.assertFalse(m.packet_check(r)['lint_pass'])
 def record(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);r=Path(t.name);(r/'evidence.txt').write_text('attestation')
  e=[{'path':'evidence.txt','sha256':m.sha(r/'evidence.txt')}]
  c={'id':'C1','statement':'A stated theorem','hypotheses':['explicit'],'quantifiers':'all objects in domain','dependencies':[],'evidence_kind':'analyticProved','verification_state':'audited','novelty_status':'not_assessed','scope_exclusions':['outside domain'],'formal_coverage':'unformalized','evidence':e}
  gates=[{'id':i,'status':'pass','owner':'custodian','acceptance':'specific attestation','version':'v1','evidence':e,'review_context_id':'new'} for i in m.STAGES]
  o={'schema_version':'1.0','paper':'test','version':'v1','recorded_utc':'2026-10-05T00:00:00Z','claims':[c],'gates':gates,'blockers':[],'review_contexts':[{'context_id':'new','reviewer_id':'R','editor_id':'E','rounds_used':1,'retired':False,'initial_inherited_history':False,'exposure':'clean','reviewed_version':'v1'}],'submission':{'authors_confirmed':True,'journal_selected':True,'consent_confirmed':True,'disclosures_checked':True,'automatic_submission':False}}
  f=r/'record.json';f.write_text(json.dumps(o));return f,o
 def changed(self,fn):
  f,o=self.record();fn(o);f.write_text(json.dumps(o));return m.readiness_check(f)
 def test_generic_attestations_not_complete(self):
  f,o=self.record();self.assertFalse(m.readiness_check(f)['ready_for_human_submission_decision'])
 def test_pending_not_ready(self):self.assertFalse(self.changed(lambda o:o['gates'][1].update(status='pending'))['ready_for_human_submission_decision'])
 def test_stale_version(self):self.assertFalse(self.changed(lambda o:o['gates'][1].update(version='v0'))['record_valid'])
 def test_round_limit(self):self.assertFalse(self.changed(lambda o:o['review_contexts'][0].update(rounds_used=3))['record_valid'])
 def test_retire_two_rounds(self):self.assertFalse(self.changed(lambda o:o['review_contexts'][0].update(rounds_used=2))['record_valid'])
 def test_same_editor(self):self.assertFalse(self.changed(lambda o:o['review_contexts'][0].update(editor_id='R'))['record_valid'])
 def test_contaminated(self):self.assertFalse(self.changed(lambda o:o['review_contexts'][0].update(exposure='contaminated_disclosed'))['ready_for_human_submission_decision'])
 def test_claim_cycle(self):self.assertFalse(self.changed(lambda o:o['claims'][0].update(dependencies=['C1']))['record_valid'])
 def test_unknown_dependency(self):self.assertFalse(self.changed(lambda o:o['claims'][0].update(dependencies=['missing']))['record_valid'])
 def test_finite_domain(self):self.assertFalse(self.changed(lambda o:o['claims'][0].update(evidence_kind='finiteVerified'))['record_valid'])
 def test_no_authors(self):self.assertFalse(self.changed(lambda o:o['submission'].update(authors_confirmed=False))['record_valid'])
 def test_unjustified_na(self):self.assertFalse(self.changed(lambda o:o['gates'][1].update(status='not_applicable'))['record_valid'])
 def test_bad_hash(self):self.assertFalse(self.changed(lambda o:o['claims'][0]['evidence'][0].update(sha256='0'*64))['record_valid'])
if __name__=='__main__':unittest.main()
