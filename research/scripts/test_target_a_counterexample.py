import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from target_a_period8_family import verify_family
from target_a_rational_certificate import verify_rational_sandwich


RESEARCH_ROOT = Path(__file__).resolve().parents[1]


class CounterexampleTests(unittest.TestCase):
    def test_period8_symbolic_family(self) -> None:
        report = verify_family()
        self.assertTrue(report["result"])
        self.assertEqual(report["quadrilateral_flux_period"], [1, -1, -1, -1, 1, -1, -1, -1])

    def test_n32_independent_rational_certificate(self) -> None:
        candidate = RESEARCH_ROOT / "counterexamples" / "target_a_n32_period8.json"
        report = verify_rational_sandwich(candidate, Fraction(1561, 200))
        self.assertTrue(report["result"])
        self.assertTrue(report["ldl_matches_bareiss_minors"])

    def test_saved_certificates_are_passes(self) -> None:
        names = (
            "target_a_n32_period8_certificate.json",
            "target_a_period8_family_certificate.json",
            "target_a_n50_period10_certificate.json",
            "target_a_period10_family_certificate.json",
        )
        for name in names:
            data = json.loads((RESEARCH_ROOT / "counterexamples" / name).read_text(encoding="utf-8"))
            self.assertTrue(data["result"], name)


if __name__ == "__main__":
    unittest.main()
