import copy
import json
import unittest

from verify_target_a_submission_artifact_manifest import (
    DEFAULT_MANIFEST,
    SubmissionManifestError,
    verify_manifest,
)


class SubmissionArtifactManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(DEFAULT_MANIFEST.read_text(encoding="utf-8"))

    def test_positive_manifest(self):
        verify_manifest(self.data)

    def test_hash_tamper_rejected(self):
        data = copy.deepcopy(self.data)
        data["files"][0]["sha256"] = "0" * 64
        with self.assertRaises(SubmissionManifestError):
            verify_manifest(data)

    def test_partition_gap_rejected(self):
        data = copy.deepcopy(self.data)
        data["theorem_f"]["partition"]["moment_detected"] -= 1
        with self.assertRaises(SubmissionManifestError):
            verify_manifest(data)


if __name__ == "__main__":
    unittest.main()
