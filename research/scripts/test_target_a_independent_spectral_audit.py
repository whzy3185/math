from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from target_a_independent_spectral_audit import run


class IndependentSpectralAuditTests(unittest.TestCase):
    def test_small_exact_decision_route(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            summary = run([8, 10], root / "output", root / "work")
        self.assertEqual(summary["status"], "PASS")
        self.assertEqual([item["spectral_states"] for item in summary["results"]], [36, 88])
        self.assertEqual(
            [item["rayleigh_certified_nonoptimizers"] for item in summary["results"]],
            [35, 87],
        )


if __name__ == "__main__":
    unittest.main()
