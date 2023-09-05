import unittest
from .solution import Solution
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])
        result = [[-1 for _ in range(cols)] for _ in range(rows + 1)]
        for i in range(cols):
            result[0][i] = i

        for i in range(1, rows + 1):
            for j in range(cols):
                prev = result[i-1][j]

                if prev == -1:
                    result[i][j] = -1
                    continue
                if grid[i-1][prev] == -1 and prev -1 >=0 and grid[i-1][prev-1] == -1:
                    result[i][j] = prev - 1
                elif grid[i-1][prev] == 1 and prev + 1 < cols and grid[i-1][prev + 1] == 1:
                    result[i][j] = prev + 1
                else:
                    result[i][j] = -1
        # print(result)
        return result[-1]


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        grid = [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]
        actual = self.s.findBall(grid)
        self.assertEqual(actual, [1, -1, -1, -1, -1])

    def test_case_2(self):
        grid = [[-1]]
        actual = self.s.findBall(grid)
        self.assertEqual(actual, [-1])

    def test_case_3(self):
        grid = [[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]
        actual = self.s.findBall(grid)
        self.assertEqual(actual, [0, 1, 2, 3, 4, -1])

    def test_case_4(self):
        grid = [[1, -1, -1, -1, 1, -1],
                [-1, -1, -1, -1, -1, 1],
                [1, 1, 1, 1, 1, -1],
                [-1, -1, 1, 1, 1, 1]
                ]
        actual = self.s.findBall(grid)
        self.assertEqual(actual, [-1, -1, 0, 3, -1, -1])


if __name__ == '__main__':
    unittest.main()
