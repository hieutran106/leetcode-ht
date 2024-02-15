import unittest
from typing import List


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # m is rows, n is cols
        cols = n
        rows = m

        memo = {}

        def helper(i: int, j: int, move: int):
            # outside of board
            if (i < 0 or i >= rows) or (j < 0 or j >= cols):
                return 1 if move == 0 else 0
            if move == 0:
                return 0
            # inside the board
            if (i, j, move) in memo:
                return memo[(i, j, move)]
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            paths = 0
            for dx, dy in directions:
                paths = (paths + helper(i + dx, j + dy, move - 1)) % (10**9 + 7)
            memo[(i, j, move)] = paths
            return paths

        count = 0
        for move in range(1, maxMove + 1):
            count = (count + helper(startRow, startColumn, move)) % (10**9 + 7)
        return count


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0)
        self.assertEqual(6, actual)

    def test_case_2(self):
        actual = self.s.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1)
        self.assertEqual(12, actual)

    def test_case_3(self):
        actual = self.s.findPaths(m=3, n=3, maxMove=1, startRow=0, startColumn=0)
        self.assertEqual(2, actual)

    def test_case_4(self):
        actual = self.s.findPaths(m=8, n=50, maxMove=23, startRow=5, startColumn=26)
        self.assertEqual(914783380, actual)


if __name__ == '__main__':
    unittest.main()
