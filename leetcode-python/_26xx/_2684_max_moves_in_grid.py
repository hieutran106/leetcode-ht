import unittest
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        move_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        def inside(i, j):
            return 0 <= i < rows and 0 <= j < cols

        dirs = [(-1, -1), (0, -1), (+1, - 1)]

        for j in range(1, cols):
            for i in range(0, rows):
                for dx, dy in dirs:
                    x = i + dx
                    y = j + dy
                    if inside(x, y) and grid[x][y] < grid[i][j]:
                        if y == 0 or move_matrix[x][y] > 0:
                            move_matrix[i][j] = max(move_matrix[i][j], move_matrix[x][y] + 1)

        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, move_matrix[i][j])
        return ans



class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.maxMoves(grid=[[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]])
        self.assertEqual(3, actual)

    def test_case_2(self):
        actual = self.s.maxMoves(grid=[[3, 2, 4], [2, 1, 9], [1, 1, 7]])
        self.assertEqual(0, actual)

    def test_case_3(self):
        actual = self.s.maxMoves(grid=[[1, 2], [3, 4]])
        self.assertEqual(1, actual)

    def test_case_4(self):
        actual = self.s.maxMoves(
            grid=[[187, 167, 209, 251, 152, 236, 263, 128, 135], [267, 249, 251, 285, 73, 204, 70, 207, 74],
                  [189, 159, 235, 66, 84, 89, 153, 111, 189], [120, 81, 210, 7, 2, 231, 92, 128, 218],
                  [193, 131, 244, 293, 284, 175, 226, 205, 245]])
        self.assertEqual(3, actual)


if __name__ == '__main__':
    unittest.main()
