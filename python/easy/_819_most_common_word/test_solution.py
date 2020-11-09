import unittest
from .solution import Solution

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = Solution()
        actual = s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
        self.assertEqual(actual, "ball")


if __name__ == '__main__':
    unittest.main()
