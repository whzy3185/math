import copy
import json
import unittest

from verify_target_a_full_slow_reproduction import (
    DEFAULT_NARRATIVE,
    DEFAULT_SUMMARY,
    SlowReproductionVerificationError,
    verify_committed_evidence,
    verify_files,
    verify_summary_data,
)


class FullSlowReproductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.summary = json.loads(DEFAULT_SUMMARY.read_text(encoding="utf-8"))
        cls.narrative = DEFAULT_NARRATIVE.read_text(encoding="utf-8")

    def verify(self, summary=None, narrative=None):
        verify_summary_data(
            self.summary if summary is None else summary,
            self.narrative if narrative is None else narrative,
        )

    def assert_rejected(self, summary=None, narrative=None):
        with self.assertRaises(SlowReproductionVerificationError):
            self.verify(summary=summary, narrative=narrative)

    def test_positive_imported_files_and_committed_evidence(self):
        verify_files()

    def test_positive_data_checker(self):
        self.verify()
        verify_committed_evidence(self.summary)

    def test_baseline_tamper_rejected(self):
        summary = copy.deepcopy(self.summary)
        summary["baseline"]["git_commit"] = "0" * 40
        self.assert_rejected(summary=summary)

    def test_state_count_tamper_rejected(self):
        summary = copy.deepcopy(self.summary)
        summary["fresh_regeneration"][3]["spectral_states"] -= 1
        self.assert_rejected(summary=summary)

    def test_checkpoint_chain_tamper_rejected(self):
        summary = copy.deepcopy(self.summary)
        summary["fresh_regeneration"][2]["hashes"]["final_checkpoint_chain_sha256"] = "0" * 64
        self.assert_rejected(summary=summary)

    def test_replay_check_tamper_rejected(self):
        summary = copy.deepcopy(self.summary)
        summary["committed_certificate_replay"]["all_checks_true"] = False
        self.assert_rejected(summary=summary)

    def test_operational_incident_as_mismatch_rejected(self):
        summary = copy.deepcopy(self.summary)
        summary["operational_incidents"][1]["mathematical_mismatch"] = True
        self.assert_rejected(summary=summary)

    def test_manifest_hash_equality_overclaim_rejected(self):
        summary = copy.deepcopy(self.summary)
        summary["comparison"]["fresh_and_committed_manifest_file_hashes_match"] = True
        self.assert_rejected(summary=summary)

    def test_paper_gate_tamper_rejected(self):
        summary = copy.deepcopy(self.summary)
        summary["paper_gate"]["claim_scope_frozen"] = "FAIL"
        self.assert_rejected(summary=summary)

    def test_scope_overclaim_rejected(self):
        narrative = self.narrative.replace("does not claim all-period optimality", "establishes all-period optimality")
        self.assert_rejected(narrative=narrative)


if __name__ == "__main__":
    unittest.main()
