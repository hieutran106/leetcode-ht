import unittest
from .solution import Solution


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = Solution()
        grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
        actual = s.maxIncreaseKeepingSkyline(grid)
        self.assertEqual(actual, 35)


if __name__ == '__main__':
    unittest.main()
