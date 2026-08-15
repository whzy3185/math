import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from target_a_period4_diagnostic import build_diagnostic


class Period4DiagnosticTests(unittest.TestCase):
    def test_saved_logs_build_expected_structural_table(self) -> None:
        report = build_diagnostic()
        self.assertEqual(report["status"], "OBSERVED_NUMERIC_DIAGNOSTIC")
        entries = {entry["n"]: entry for entry in report["entries"]}
        self.assertEqual(
            entries[24]["best_observed_nonoptimizer"][
                "distance_to_period4_Q_pattern"
            ],
            0,
        )
        self.assertEqual(
            entries[26]["best_observed_nonoptimizer"][
                "distance_to_period4_Q_pattern"
            ],
            1,
        )
        self.assertEqual(
            entries[28]["best_observed_nonoptimizer"][
                "distance_to_period4_Q_pattern"
            ],
            5,
        )
        self.assertNotIn(
            0,
            {
                item["distance_to_period4_Q_pattern"]
                for item in entries[28]["best_observed_by_period4_distance"]
            },
        )
        self.assertEqual(
            entries[30]["best_observed_nonoptimizer"][
                "distance_to_period4_Q_pattern"
            ],
            6,
        )
        self.assertEqual(
            {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22},
            {
                item["distance_to_period4_Q_pattern"]
                for item in entries[30]["best_observed_by_period4_distance"]
            },
        )


if __name__ == "__main__":
    unittest.main()
