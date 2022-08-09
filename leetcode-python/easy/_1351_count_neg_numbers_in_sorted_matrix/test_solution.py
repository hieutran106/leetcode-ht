import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
        actual = self.s.countNegatives(grid)
        self.assertEqual(actual, 8)

    def test_case2(self):
        grid = [[3,2],[1,0]]
        actual = self.s.countNegatives(grid)
        self.assertEqual(actual, 0)

    def test_case3(self):
        grid = [[1,-1],[-1,-1]]
        actual = self.s.countNegatives(grid)
        self.assertEqual(actual, 3)

    def test_case4(self):
        grid = [[-1]]
        actual = self.s.countNegatives(grid)
        self.assertEqual(actual, 1)

if __name__ == '__main__':
    unittest.main()
