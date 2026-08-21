import tempfile
import unittest
import hashlib
import json
from pathlib import Path

from target_a_record_set_audit import (
    C_SOURCE,
    DEFAULT_OUTPUT_DIR,
    PRIMARY_SOURCE,
    _build_checker,
    audit_order,
)


class RecordSetAuditTests(unittest.TestCase):
    def test_independent_record_set_equality_small_orders(self) -> None:
        with tempfile.TemporaryDirectory(prefix="target-a-record-set-test-") as temporary:
            work_dir = Path(temporary)
            binary = work_dir / "independent-orbit-scan"
            _build_checker(binary)
            for n in (8, 10, 12):
                with self.subTest(n=n):
                    result = audit_order(n, work_dir, binary)
                    self.assertEqual(result["status"], "PASS")
                    self.assertTrue(result["record_level_set_equality"])
                    self.assertEqual(result["sum_of_represented_switching_classes"], 1 << (n + 1))
            with self.assertRaisesRegex(ValueError, "even integer"):
                audit_order(9, work_dir, binary)

    def test_committed_large_order_summaries(self) -> None:
        summary = json.loads((DEFAULT_OUTPUT_DIR / "summary.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["status"], "PASS")
        self.assertEqual(summary["orders"], [24, 26, 28, 30])
        self.assertEqual(
            summary["build"]["source_sha256"],
            hashlib.sha256(C_SOURCE.read_bytes()).hexdigest(),
        )
        self.assertEqual(
            summary["execution_provenance"]["primary_generator_sha256"],
            hashlib.sha256(PRIMARY_SOURCE.read_bytes()).hexdigest(),
        )
        for expected_n, row in zip((24, 26, 28, 30), summary["results"]):
            self.assertEqual(row["order"], expected_n)
            self.assertEqual(row["status"], "PASS")
            self.assertTrue(row["record_level_set_equality"])
            detail_path = DEFAULT_OUTPUT_DIR / row["file"]
            self.assertEqual(row["file_sha256"], hashlib.sha256(detail_path.read_bytes()).hexdigest())
            detail = json.loads(detail_path.read_text(encoding="utf-8"))
            self.assertEqual(detail["status"], "PASS")
            self.assertTrue(all(detail["checks"].values()))
            self.assertEqual(
                detail["sum_of_represented_switching_classes"], 1 << (expected_n + 1)
            )
            self.assertEqual(
                sum(
                    int(size) * count
                    for size, count in detail["independent"]["orbit_size_histogram"].items()
                ),
                1 << (expected_n - 1),
            )


if __name__ == "__main__":
    unittest.main()
