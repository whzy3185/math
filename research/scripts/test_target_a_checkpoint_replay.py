import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from target_a_checkpoint_replay import replay_saved_search
from target_a_minimality_search import run_minimality_search


class CheckpointReplayTests(unittest.TestCase):
    def test_read_only_replay_matches_small_complete_search(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            research_root = Path(directory) / "research"
            checkpoint_dir = research_root / "logs" / "checkpoints" / "n8"
            result = run_minimality_search(
                8,
                checkpoint_dir,
                chunk_size=6,
                git_commit_override="replay-test-commit",
            )
            result_path = research_root / "logs" / "target_a_search_n8.json"
            result_path.parent.mkdir(parents=True, exist_ok=True)
            result_path.write_text(json.dumps(result), encoding="utf-8")
            report = replay_saved_search(8, research_root)
        self.assertEqual(report["status"], "PASS")
        self.assertTrue(all(report["checks"].values()))


if __name__ == "__main__":
    unittest.main()
