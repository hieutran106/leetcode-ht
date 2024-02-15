import unittest
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])
        helper = [[0 for _ in range(cols)] for _ in range(rows)]

        def falling_path_value(i, j):
            if i < 0 or i >= rows:
                return float("inf")
            if j < 0 or j >= cols:
                return float("inf")
            return helper[i][j]

        # base
        for j in range(cols):
            helper[0][j] = matrix[0][j]
        for i in range(1, rows):
            for j in range(cols):
                min_value = min(falling_path_value(i - 1, j - 1), falling_path_value(i - 1, j),
                                   falling_path_value(i - 1, j + 1))

                helper[i][j] =  min_value + matrix[i][j]

        res = helper[rows - 1][0]
        for j in range(1, cols):
            res = min(res, helper[rows - 1][j])
        return res


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.minFallingPathSum(matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]])
        self.assertEqual(13, actual)

    def test_case_2(self):
        actual = self.s.minFallingPathSum(matrix=[[-19, 57], [-40, -5]])
        self.assertEqual(-59, actual)

    def test_case_3(self):
        actual = self.s.minFallingPathSum(matrix=[[-19, 57]])
        self.assertEqual(-19, actual)


if __name__ == '__main__':
    unittest.main()
