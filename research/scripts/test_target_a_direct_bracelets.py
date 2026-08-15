import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from target_a_bracelets import enumerate_direct_q_orbits
from target_a_direct_generator_audit import (
    audit_burnside_stream,
    audit_reference_equality,
    fixed_weight_bracelet_counts,
)
from target_a_flux_search import dihedral_orbit


RUN_SLOW = os.environ.get("TARGET_A_RUN_SLOW_GENERATOR_TESTS") == "1"


class DirectBraceletTests(unittest.TestCase):
    def test_direct_generator_matches_reference_n8_22(self) -> None:
        for n in (8, 10, 12, 14, 16, 18, 20, 22):
            with self.subTest(n=n):
                self.assertEqual(audit_reference_equality(n)["status"], "PASS")

    def test_direct_generator_burnside_n24(self) -> None:
        self.assertEqual(
            audit_burnside_stream(24, measure_memory=False)["status"], "PASS"
        )

    @unittest.skipUnless(RUN_SLOW, "set TARGET_A_RUN_SLOW_GENERATOR_TESTS=1")
    def test_direct_generator_burnside_n26(self) -> None:
        self.assertEqual(
            audit_burnside_stream(26, measure_memory=False)["status"], "PASS"
        )

    @unittest.skipUnless(RUN_SLOW, "set TARGET_A_RUN_SLOW_GENERATOR_TESTS=1")
    def test_direct_generator_burnside_n28(self) -> None:
        self.assertEqual(
            audit_burnside_stream(28, measure_memory=False)["status"], "PASS"
        )

    @unittest.skipUnless(RUN_SLOW, "set TARGET_A_RUN_SLOW_GENERATOR_TESTS=1")
    def test_direct_generator_burnside_n30(self) -> None:
        self.assertEqual(
            audit_burnside_stream(30, measure_memory=False)["status"], "PASS"
        )

    def test_direct_generator_orbit_size(self) -> None:
        for n in (8, 10, 12):
            for code, orbit_size in enumerate_direct_q_orbits(n):
                self.assertEqual(orbit_size, len(dihedral_orbit(code, n)))

    def test_direct_generator_even_parity(self) -> None:
        for n in (8, 10, 12, 14):
            self.assertTrue(all(code.bit_count() % 2 == 0 for code, _ in enumerate_direct_q_orbits(n)))

    def test_direct_generator_no_duplicate(self) -> None:
        for n in (8, 10, 12, 14):
            codes = [code for code, _ in enumerate_direct_q_orbits(n)]
            self.assertEqual(len(codes), len(set(codes)))

    def test_fixed_shell_support_and_counts(self) -> None:
        n = 16
        expected = fixed_weight_bracelet_counts(n)
        for weight, count in expected.items():
            with self.subTest(weight=weight):
                records = list(enumerate_direct_q_orbits(n, weight))
                self.assertEqual(len(records), count)
                self.assertTrue(all(code.bit_count() == weight for code, _ in records))


if __name__ == "__main__":
    unittest.main()
