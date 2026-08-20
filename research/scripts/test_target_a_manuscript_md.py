import unittest

from verify_target_a_manuscript_md import (
    DEFAULT_MANUSCRIPT,
    ManuscriptVerificationError,
    verify_manuscript,
)


class ManuscriptMarkdownTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = DEFAULT_MANUSCRIPT.read_text(encoding="utf-8")

    def assert_rejected(self, text):
        with self.assertRaises(ManuscriptVerificationError):
            verify_manuscript(text)

    def test_positive_manuscript(self):
        verify_manuscript(self.text)

    def test_missing_theorem_rejected(self):
        self.assert_rejected(self.text.replace("**Theorem F (", "**Result F (", 1))

    def test_reverse_moment_implication_rejected(self):
        self.assert_rejected(self.text + "\nF_k<=0 ==> R(Q)<=8.\n")

    def test_world_first_rejected(self):
        self.assert_rejected(self.text + "\nThis is world-first.\n")

    def test_author_placeholder_rejected(self):
        self.assert_rejected(self.text + "\nLeft to the author.\n")

    def test_mutable_or_wrong_artifact_snapshot_rejected(self):
        self.assert_rejected(self.text.replace(
            "c81be34a3b12a7ac47adbb4499c475df7bf4fc04",
            "0000000000000000000000000000000000000000",
        ))

    def test_missing_radical_branch_rejected(self):
        self.assert_rejected(self.text.replace("positive square-root branch", "chosen branch"))


if __name__ == "__main__":
    unittest.main()
