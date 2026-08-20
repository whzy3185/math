import unittest

from verify_target_a_chinese_latex import verify_target_a_chinese_latex


class TargetAChineseLatexTests(unittest.TestCase):
    def test_chinese_latex_gate(self):
        verify_target_a_chinese_latex()


if __name__ == "__main__":
    unittest.main()
