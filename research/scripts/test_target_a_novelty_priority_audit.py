import copy
import json
import unittest

from verify_target_a_novelty_priority_audit import (
    DEFAULT_AUDIT,
    DEFAULT_LEDGER,
    DEFAULT_NARRATIVE,
    DEFAULT_SNAPSHOT,
    DEFAULT_TIMELINE,
    NoveltyAuditVerificationError,
    verify_audit_data,
    verify_files,
)


class NoveltyPriorityAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = json.loads(DEFAULT_AUDIT.read_text(encoding="utf-8"))
        cls.ledger = json.loads(DEFAULT_LEDGER.read_text(encoding="utf-8"))
        cls.snapshot = json.loads(DEFAULT_SNAPSHOT.read_text(encoding="utf-8"))
        cls.narrative = DEFAULT_NARRATIVE.read_text(encoding="utf-8")
        cls.timeline = DEFAULT_TIMELINE.read_text(encoding="utf-8")

    def verify(self, audit=None, ledger=None, snapshot=None, narrative=None, timeline=None):
        verify_audit_data(
            self.audit if audit is None else audit,
            self.ledger if ledger is None else ledger,
            self.snapshot if snapshot is None else snapshot,
            self.narrative if narrative is None else narrative,
            self.timeline if timeline is None else timeline,
        )

    def assert_rejected(self, **kwargs):
        with self.assertRaises(NoveltyAuditVerificationError):
            self.verify(**kwargs)

    def test_positive_imported_files_and_hashes(self):
        verify_files()

    def test_positive_data_checker(self):
        self.verify()

    def test_claim_assessment_tamper_rejected(self):
        audit = copy.deepcopy(self.audit)
        audit["claims"][10]["assessment"] = "DIRECT_PRIOR_FOUND"
        self.assert_rejected(audit=audit)

    def test_assessment_count_tamper_rejected(self):
        audit = copy.deepcopy(self.audit)
        audit["assessment_counts"]["CLOSE_PRIOR_FOUND"] = 0
        self.assert_rejected(audit=audit)

    def test_missing_n10_n11_addendum_rejected(self):
        audit = copy.deepcopy(self.audit)
        audit["audit"]["synchronization_addendum"]["added_claims"] = []
        self.assert_rejected(audit=audit)

    def test_query_ledger_gap_rejected(self):
        ledger = copy.deepcopy(self.ledger)
        del ledger["queries"][80]
        self.assert_rejected(ledger=ledger)

    def test_inaccessible_service_as_success_rejected(self):
        ledger = copy.deepcopy(self.ledger)
        next(row for row in ledger["service_status"] if row["service"] == "Google Scholar")["status"] = "accessible"
        self.assert_rejected(ledger=ledger)

    def test_unknown_evidence_source_rejected(self):
        audit = copy.deepcopy(self.audit)
        audit["claims"][0]["evidence_source_ids"].append("S99")
        self.assert_rejected(audit=audit)

    def test_forbidden_priority_wording_rejected(self):
        self.assert_rejected(narrative=self.narrative + "\nDefinitely first.\n")

    def test_unsafe_summary_rejected(self):
        audit = copy.deepcopy(self.audit)
        audit["audit"]["summary"] = "Nobody has ever found this."
        self.assert_rejected(audit=audit)

    def test_sync_fingerprint_tamper_rejected(self):
        snapshot = copy.deepcopy(self.snapshot)
        snapshot["synchronization_source_fingerprints"][0]["sha256"] = "0" * 64
        self.assert_rejected(snapshot=snapshot)


if __name__ == "__main__":
    unittest.main()
