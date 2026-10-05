import tempfile,unittest,json
from pathlib import Path
from complete_fixture import complete_fixture,materialize,m
class LinkedTests(unittest.TestCase):
 def check(self,mutate):
  with tempfile.TemporaryDirectory() as t:
   root=Path(t);o,d=complete_fixture(root);mutate(o,d,root);return m.readiness_check(materialize(root,o,d))
 def test_complete_positive_administrative_control(self):
  r=self.check(lambda o,d,r:None);self.assertTrue(r['ready_for_human_submission_decision'],r)
 def test_empty_linked_docs(self):self.assertFalse(self.check(lambda o,d,r:[d.__setitem__(k,{}) for k in d])['ready_for_human_submission_decision'])
 def test_required_obligation_removed(self):self.assertFalse(self.check(lambda o,d,r:d['proof_obligations']['obligations'].pop())['ready_for_human_submission_decision'])
 def test_required_issue_removed(self):self.assertFalse(self.check(lambda o,d,r:d['review_response'].update(issues=[]))['ready_for_human_submission_decision'])
 def test_false_exit_code(self):
  def f(o,d,r):next(z for z in d['receipts']['receipts'] if z['gate']=='S14')['details']['replay_exit_code']=False
  self.assertFalse(self.check(f)['ready_for_human_submission_decision'])
 def test_bad_packet_binding(self):
  def f(o,d,r):next(z for z in d['receipts']['receipts'] if z['gate']=='S09')['details']['packet_manifest_sha256']='0'*64
  self.assertFalse(self.check(f)['ready_for_human_submission_decision'])
if __name__=='__main__':unittest.main()

class GateSeparationTests(unittest.TestCase):
 def test_disclosed_rereview_does_not_clear_pristine_gate(self):
  with tempfile.TemporaryDirectory() as t:
   root=Path(t);o,d=complete_fixture(root)
   o['gates'][9].update(status='blocked',notes='Prior exposure remains disclosed')
   o['review_contexts'][0]['exposure']='contaminated_disclosed'
   d['version_registry']['versions'][0]['review_contexts'][0]['exposure']='contaminated_disclosed'
   d['receipts']['receipts']=[z for z in d['receipts']['receipts'] if z['gate']!='S09']
   result=m.readiness_check(materialize(root,o,d))
   self.assertTrue(result['record_valid'],result)
   self.assertFalse(result['ready_for_human_submission_decision'])
 def test_equal_time_failure_cannot_hide_behind_pass(self):
  import copy
  with tempfile.TemporaryDirectory() as t:
   root=Path(t);o,d=complete_fixture(root)
   z=copy.deepcopy(next(z for z in d['receipts']['receipts'] if z['gate']=='S14'))
   z.update(receipt_id='tied-failure',result='fail');z['details']['replay_exit_code']=1;d['receipts']['receipts'].append(z)
   self.assertFalse(m.readiness_check(materialize(root,o,d))['ready_for_human_submission_decision'])
