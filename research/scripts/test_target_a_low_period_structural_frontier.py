import copy
import hashlib
import json
import unittest

from target_a_low_period_structural_frontier import (
    DEFAULT_FRONTIER,
    DEFAULT_RESULT,
    EXPECTED_BASELINE_IDS,
    EXPECTED_EXCEPTION_IDS,
    EXPECTED_TARGET_IDS,
    adaptive_first_positive,
)
from verify_target_a_low_period_structural_frontier import (
    DEFAULT_SOURCE,
    StructuralFrontierVerificationError,
    verify_structural_frontier_data,
)


class LowPeriodStructuralFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = json.loads(DEFAULT_RESULT.read_text(encoding="utf-8"))
        cls.frontier = json.loads(DEFAULT_FRONTIER.read_text(encoding="utf-8"))
        cls.source_sha = hashlib.sha256(DEFAULT_SOURCE.read_bytes()).hexdigest()

    def verify(self, result=None, source_sha=None):
        verify_structural_frontier_data(
            self.result if result is None else result,
            self.frontier,
            self.source_sha if source_sha is None else source_sha,
        )

    def assert_rejected(self, result=None, source_sha=None):
        with self.assertRaises(StructuralFrontierVerificationError):
            self.verify(result, source_sha)

    def test_positive_full_checker(self):
        self.verify()

    def test_adaptive_hierarchy_examples(self):
        self.assertIsNone(adaptive_first_positive((-1, -1)))
        self.assertEqual(adaptive_first_positive((-1, -1, 1))[0], 27)

    def test_residual_partition_ids(self):
        partition = self.result["residual_partition"]
        self.assertEqual(partition["all_negative_representations"]["orbit_ids"], EXPECTED_BASELINE_IDS)
        self.assertEqual(partition["target_representations"]["orbit_ids"], EXPECTED_TARGET_IDS)
        self.assertEqual(
            [row["orbit_id"] for row in partition["exceptional_competitors"]],
            EXPECTED_EXCEPTION_IDS,
        )

    def test_compression_arithmetic(self):
        summary = self.result["compression_summary"]
        self.assertEqual(summary["competitors_proved_above_8_by_one_moment_lemma"], 2611)
        self.assertEqual(summary["all_negative_representations_proved_equal_8_by_one_baseline_lemma"], 8)
        self.assertEqual(summary["residual_endpoint_certificates"], 5)
        self.assertEqual(summary["uncertified"], 0)

    def test_status_tamper_rejected(self):
        result = copy.deepcopy(self.result)
        result["status"] = "NUMERIC_ONLY"
        self.assert_rejected(result=result)

    def test_dependency_tamper_rejected(self):
        result = copy.deepcopy(self.result)
        result["dependencies"]["Task42B_frontier"]["sha256"] = "0" * 64
        self.assert_rejected(result=result)

    def test_moment_direction_tamper_rejected(self):
        result = copy.deepcopy(self.result)
        result["moment_hierarchy"]["negative_excess_used_as_upper_bound"] = True
        self.assert_rejected(result=result)

    def test_range_tamper_rejected(self):
        result = copy.deepcopy(self.result)
        result["moment_hierarchy"]["adaptive_residual_range"] = [25, 63]
        self.assert_rejected(result=result)

    def test_all_period_overclaim_rejected(self):
        result = copy.deepcopy(self.result)
        result["scope"]["all_period_global_optimality"] = "PROVED"
        self.assert_rejected(result=result)

    def test_exception_upper_bound_overclaim_rejected(self):
        result = copy.deepcopy(self.result)
        result["scope"]["exact_upper_bound_for_four_separation4_exceptions"] = "PROVED"
        self.assert_rejected(result=result)

    def test_source_hash_tamper_rejected(self):
        self.assert_rejected(source_sha="0" * 64)


if __name__ == "__main__":
    unittest.main()
