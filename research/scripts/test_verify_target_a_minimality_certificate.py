import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from verify_target_a_minimality_certificate import (
    DEFAULT_CERTIFICATE,
    MinimalityCertificateError,
    verify_minimality_certificate,
)


class MinimalityCertificateVerifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = json.loads(DEFAULT_CERTIFICATE.read_text(encoding="utf-8"))

    def _verify_mutation_fails(self, payload: dict) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "certificate.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaises(MinimalityCertificateError):
                verify_minimality_certificate(path, run_replays=False)

    def _entry(self, payload: dict, n: int) -> dict:
        return next(
            entry for entry in payload["finite_no_counterexample_orders"]
            if entry["n"] == n
        )

    def test_committed_certificate_passes_without_replay_rerun(self) -> None:
        report = verify_minimality_certificate(run_replays=False)
        self.assertEqual(report["status"], "SMALLEST_COUNTEREXAMPLE_VERIFIED")
        self.assertEqual(report["required_orders_below_32"], list(range(8, 32, 2)))

    def test_missing_n28_entry_fails(self) -> None:
        payload = copy.deepcopy(self.certificate)
        payload["finite_no_counterexample_orders"] = [
            entry for entry in payload["finite_no_counterexample_orders"]
            if entry["n"] != 28
        ]
        self._verify_mutation_fails(payload)

    def test_modified_n30_sha_fails(self) -> None:
        payload = copy.deepcopy(self.certificate)
        self._entry(payload, 30)["source_sha256"] = "0" * 64
        self._verify_mutation_fails(payload)

    def test_first_counterexample_changed_to_34_fails(self) -> None:
        payload = copy.deepcopy(self.certificate)
        payload["claim"]["smallest_counterexample_order"] = 34
        self._verify_mutation_fails(payload)

    def test_finite_counterexample_count_one_fails(self) -> None:
        payload = copy.deepcopy(self.certificate)
        self._entry(payload, 20)["counterexamples"] = 1
        self._verify_mutation_fails(payload)

    def test_incomplete_fraction_fails(self) -> None:
        payload = copy.deepcopy(self.certificate)
        self._entry(payload, 30)["completion_fraction"] = 0.5
        self._verify_mutation_fails(payload)


if __name__ == "__main__":
    unittest.main()
