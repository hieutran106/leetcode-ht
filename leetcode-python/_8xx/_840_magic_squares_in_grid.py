import unittest
from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(r, c):
            nums = set()
            for i in range(3):
                for j in range(3):
                    num = grid[r + i][c + j]
                    if num < 0 or num > 9 or num in nums:
                        return False
                    nums.add(num)
            # check sum
            positions = [
                [(0, 0), (0, 1), (0, 2)],  # rows
                [(1, 0), (1, 1), (1, 2)],
                [(2, 0), (2, 1), (2, 2)],
                [(0, 0), (1, 0), (2, 0)],  # cols
                [(0, 1), (1, 1), (2, 1)],
                [(0, 2), (1, 2), (2, 2)],
                [(0, 0), (1, 1), (2, 2)],  # diagonals
                [(0, 2), (1, 1), (2, 0)]
            ]
            for p1, p2, p3 in positions:
                if grid[r + p1[0]][c + p1[1]] + grid[r + p2[0]][c + p2[1]] + grid[r + p3[0]][c + p3[1]] != 15:
                    return False
            return True

        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic(r, c):
                    ans += 1
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.numMagicSquaresInside(grid=[[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]])
        self.assertEqual(1, actual)

    def test_case_2(self):
        actual = self.s.numMagicSquaresInside(grid=[[8]])
        self.assertEqual(0, actual)


if __name__ == '__main__':
    unittest.main()
