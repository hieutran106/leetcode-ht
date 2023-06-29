import unittest
from typing import List

from .solution import Solution


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        def count_square_at(i: int, j: int):
            side = 0
            while i + side < rows and j + side < cols:
                flag = True
                for k in range(0, side + 1):
                    if matrix[i + side][j + k] != 1 or matrix[i + k][j + side] != 1:
                        flag = False
                        break
                if not flag:
                    break
                side += 1
                pass
            return side

        res = 0
        for i in range(rows):
            for j in range(cols):
                res += count_square_at(i, j)
        return res


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
