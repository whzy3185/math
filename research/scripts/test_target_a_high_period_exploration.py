from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from target_a_high_period_exploration import (
    DEFAULT_OUTPUT,
    direct_visited_orbit_records,
    independent_burnside_orbit_count,
    orbit_representatives,
    run,
)


class HighPeriodExplorationTests(unittest.TestCase):
    def test_small_protocol_and_zone_folding(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            payload = run([8], Path(temporary) / "result.json", 32, 32, 64)
        result = payload["results"][0]
        self.assertTrue(all(result["checks"].values()))
        self.assertEqual(result["represented_q_words"], 128)
        self.assertTrue(any(row["target_repetition"] for row in result["refined_candidates"]))
        self.assertEqual(payload["theorem_status"], "NO_THEOREM_EXTENSION")

    def test_independent_small_record_route(self) -> None:
        primary = dict(orbit_representatives(8))
        self.assertEqual(independent_burnside_orbit_count(8), len(primary))
        self.assertEqual(direct_visited_orbit_records(8), primary)

    def test_archived_period_17_to_24_table(self) -> None:
        payload = json.loads(DEFAULT_OUTPUT.read_text(encoding="utf-8"))
        expected_orbits = [2056, 3914, 7155, 13648, 25482, 48734, 92205, 176906]
        self.assertEqual(payload["periods"], list(range(17, 25)))
        self.assertEqual(
            [row["dihedral_orbits"] for row in payload["results"]], expected_orbits
        )
        for row in payload["results"]:
            self.assertTrue(all(row["checks"].values()))
            self.assertEqual(
                sum(row["exact_low_moment_partition"].values()),
                row["dihedral_orbits"],
            )


if __name__ == "__main__":
    unittest.main()
