import unittest

from verify_target_a_latex import verify_latex_tree


class TargetALatexTests(unittest.TestCase):
    def test_generated_source_tree_and_pdf(self):
        verify_latex_tree()


if __name__ == "__main__":
    unittest.main()
