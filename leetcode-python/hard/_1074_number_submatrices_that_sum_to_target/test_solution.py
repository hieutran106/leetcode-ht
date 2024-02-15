import unittest
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        # calculate prefix sum matrix, note that sum matrix is bigger than original matrix
        prefix_sum = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + matrix[i-1][j-1]

        res = 0
        for i in range(rows):
            for j in range(cols):
                for k in range(i + 1, rows + 1):
                    for l in range(j + 1, cols + 1):

                        sub_matrix_sum = prefix_sum[k][l] - prefix_sum[k][j] - prefix_sum[l][i] + prefix_sum[i][j]

                        if sub_matrix_sum == target:
                            res += 1
        return res


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.numSubmatrixSumTarget(matrix=[[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0)
        self.assertEqual(4, actual)

    def test_case_2(self):
        actual = self.s.numSubmatrixSumTarget(matrix=[[1, -1], [-1, 1]], target=0)
        self.assertEqual(5, actual)

    def test_case_3(self):
        actual = self.s.numSubmatrixSumTarget(matrix=[[904]], target=0)
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.numSubmatrixSumTarget(matrix=[[999, 998, 997], [996, 1, -1], [995, -1, 1]], target=0)
        self.assertEqual(5, actual)

    def test_case_5(self):
        actual = self.s.numSubmatrixSumTarget([[0,0,0,1,1],[1,1,1,0,1],[1,1,1,1,0],[0,0,0,1,0],[0,0,0,1,1]], target=0)
        self.assertEqual(28, actual)

if __name__ == '__main__':
    unittest.main()
