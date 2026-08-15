import inspect
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import target_a_minimality_search as minimality
from target_a_flux_search import (
    enumerate_q_orbits,
    q_code_from_signing,
    signing_from_q,
)


class MinimalitySearchTests(unittest.TestCase):
    def test_minimality_driver_uses_direct_generator(self) -> None:
        source = inspect.getsource(minimality)
        self.assertIn("from target_a_bracelets import enumerate_direct_q_orbits", source)
        self.assertNotIn("bytearray(1 << n)", source)
        self.assertNotIn("enumerate_q_orbits(", source)

    def test_minimality_driver_n8_reference(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = minimality.run_minimality_search(
                8,
                Path(directory),
                chunk_size=6,
                git_commit_override="test-commit",
            )
        reference = list(enumerate_q_orbits(8))
        self.assertEqual(result["status"], "VERIFIED_NO_COUNTEREXAMPLE_AT_N8")
        self.assertEqual(result["completed_q_bracelets"], len(reference))
        self.assertEqual(result["completed_spectral_states"], 2 * len(reference))
        self.assertEqual(result["represented_q_vectors"], 1 << 7)
        self.assertEqual(result["counterexamples"], [])

    def test_checkpoint_resume_matches_uninterrupted(self) -> None:
        with tempfile.TemporaryDirectory() as interrupted_directory:
            interrupted = Path(interrupted_directory)
            partial = minimality.run_minimality_search(
                8,
                interrupted,
                chunk_size=2,
                stop_after_states=10,
                git_commit_override="test-commit",
            )
            resumed = minimality.run_minimality_search(
                8,
                interrupted,
                resume=True,
                chunk_size=2,
                git_commit_override="test-commit",
            )
        with tempfile.TemporaryDirectory() as direct_directory:
            uninterrupted = minimality.run_minimality_search(
                8,
                Path(direct_directory),
                chunk_size=2,
                git_commit_override="test-commit",
            )
        self.assertEqual(partial["status"], "INCOMPLETE")
        keys = (
            "status",
            "completed_q_bracelets",
            "completed_spectral_states",
            "represented_q_vectors",
            "shell_counts_completed",
            "rayleigh_certified",
            "exact_fallbacks",
            "counterexamples",
            "ordered_input_sha256",
            "ordered_certificate_sha256",
            "checkpoint_final_chain_sha256",
        )
        self.assertEqual(
            {key: resumed[key] for key in keys},
            {key: uninterrupted[key] for key in keys},
        )

    def test_checkpoint_rejects_wrong_commit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            checkpoint_dir = Path(directory)
            minimality.run_minimality_search(
                8,
                checkpoint_dir,
                chunk_size=2,
                stop_after_states=4,
                git_commit_override="first-commit",
            )
            with self.assertRaisesRegex(minimality.SearchAbort, "git_commit"):
                minimality.run_minimality_search(
                    8,
                    checkpoint_dir,
                    resume=True,
                    chunk_size=2,
                    git_commit_override="different-commit",
                )

    def test_checkpoint_rejects_corruption(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            checkpoint_dir = Path(directory)
            minimality.run_minimality_search(
                8,
                checkpoint_dir,
                chunk_size=2,
                stop_after_states=4,
                git_commit_override="test-commit",
            )
            chunk = checkpoint_dir / "chunk_000000.json"
            payload = json.loads(chunk.read_text(encoding="utf-8"))
            payload["completed_states"] = 99
            chunk.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(minimality.SearchAbort, "content_hash"):
                minimality.run_minimality_search(
                    8,
                    checkpoint_dir,
                    resume=True,
                    chunk_size=2,
                    git_commit_override="test-commit",
                )

    def test_state_roundtrip_q_alpha(self) -> None:
        for code, _orbit_size in minimality.enumerate_direct_q_orbits(10):
            for alpha in (-1, 1):
                signing = signing_from_q(code, 10, alpha)
                self.assertEqual(q_code_from_signing(signing), (code, alpha))

    def test_completion_count_gate(self) -> None:
        expected = minimality.expected_search_space(8)
        status = minimality.determine_completion_status(
            8,
            expected,
            expected["q_bracelets"],
            expected["spectral_states"],
            expected["q_vectors"],
            expected["shell_counts"],
            expected["spectral_states"] - 1,
            0,
            [],
            {"exact": True},
        )
        self.assertEqual(status, "VERIFIED_NO_COUNTEREXAMPLE_AT_N8")

    def test_incomplete_run_cannot_report_pass(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = minimality.run_minimality_search(
                8,
                Path(directory),
                chunk_size=2,
                stop_after_states=4,
                git_commit_override="test-commit",
            )
        self.assertEqual(result["status"], "INCOMPLETE")
        self.assertNotEqual(result["completion_fraction"], 1)


if __name__ == "__main__":
    unittest.main()
