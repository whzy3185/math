import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from target_a_n32_independent_reconstruction import (
    DEFAULT_FROZEN_WITNESS,
    ReconstructionError,
    TAU_PERIOD,
    reconstruct_from_definitions,
    run_independent_audit,
    switching_equivalence,
)


class IndependentN32ReconstructionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.construction = reconstruct_from_definitions()
        cls.frozen = json.loads(DEFAULT_FROZEN_WITNESS.read_text(encoding="utf-8"))
        cls.switching = switching_equivalence(cls.construction, cls.frozen)
        cls.directory = tempfile.TemporaryDirectory()
        root = Path(cls.directory.name)
        cls.audit = run_independent_audit(
            DEFAULT_FROZEN_WITNESS,
            root / "construction.json",
            root / "audit.json",
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.directory.cleanup()

    def test_01_reconstructs_tau(self) -> None:
        self.assertEqual(self.construction["tau"], TAU_PERIOD * 4)

    def test_02_reconstructs_q(self) -> None:
        self.assertEqual(self.construction["Q"], (1, -1, -1, -1) * 8)

    def test_03_reconstructs_alpha_plus_one(self) -> None:
        self.assertEqual(self.construction["alpha"], 1)

    def test_04_independent_gauge_differs_from_frozen(self) -> None:
        self.assertNotEqual(list(self.construction["step1"]), self.frozen["step1"])
        self.assertGreater(self.construction["step1"].count(-1), 1)

    def test_05_switching_vector_closes(self) -> None:
        self.assertTrue(self.switching["closes"])
        self.assertEqual(self.switching["switching_vector"][0], 1)

    def test_06_all_step1_switching_equations_pass(self) -> None:
        self.assertTrue(all(self.switching["step1_equations"]))

    def test_07_all_step2_switching_equations_pass(self) -> None:
        self.assertTrue(all(self.switching["step2_equations"]))

    def test_08_full_dad_identity_passes(self) -> None:
        self.assertTrue(self.switching["matrix_relation_exact"])

    def test_09_altered_frozen_edge_fails_switching_audit(self) -> None:
        altered = copy.deepcopy(self.frozen)
        altered["step2"][0] *= -1
        with self.assertRaisesRegex(ReconstructionError, "step-2 switching equation"):
            switching_equivalence(self.construction, altered)

    def test_10_altered_tau_fails_reconstruction(self) -> None:
        altered = list(TAU_PERIOD)
        altered[0] *= -1
        with self.assertRaisesRegex(ReconstructionError, "triangle flux input"):
            reconstruct_from_definitions(tuple(altered))

    def test_11_exact_spectral_and_counterexample_audit_passes(self) -> None:
        self.assertTrue(self.audit["charpoly_equal"])
        self.assertTrue(self.audit["charpoly_A2_equal"])
        self.assertEqual(self.audit["positive_definite_check"]["status"], "PASS")
        self.assertEqual(self.audit["threshold_check"]["status"], "PASS")
        self.assertTrue(self.audit["counterexample_check"])
        self.assertEqual(
            self.audit["overall_status"], "INDEPENDENT_N32_RECONSTRUCTION_PASS"
        )


if __name__ == "__main__":
    unittest.main()
