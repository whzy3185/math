import unittest

from verify_target_a_publication_latex import verify_publication_latex


class TargetAPublicationLatexTests(unittest.TestCase):
    def test_publication_latex_gate(self):
        verify_publication_latex()


if __name__ == "__main__":
    unittest.main()
