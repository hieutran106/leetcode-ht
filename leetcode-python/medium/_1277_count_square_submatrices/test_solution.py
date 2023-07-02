import unittest
from typing import List

from .solution import Solution


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]

        for i in range(cols):
            dp[0][i] = matrix[0][i]
        for i in range(rows):
            dp[i][0] = matrix[i][0]

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        total = 0
        for i in range(rows):
            for j in range(cols):
                total += dp[i][j]

        return total


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        matrix = [
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 1, 1, 1]
        ]
        actual = self.s.countSquares(matrix)
        self.assertEqual(15, actual)

    def test_case_2(self):
        matrix = [
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 0]
        ]
        actual = self.s.countSquares(matrix)
        self.assertEqual(7, actual)

    def test_case_3(self):
        matrix = [
            [1, 0],
            [0, 1]
        ]
        actual = self.s.countSquares(matrix)
        self.assertEqual(2, actual)

    def test_case_4(self):
        matrix = [
            [1, 1],
            [1, 1]
        ]
        actual = self.s.countSquares(matrix)
        self.assertEqual(5, actual)


if __name__ == '__main__':
    unittest.main()
