import unittest
from typing import List

# Date: 2025-11-02
# Problem: 2257 count_unguarded_cell
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        rows = m
        cols = n
        grid = [[0 for _ in range(cols)] for _ in range(rows)]
        for i,j in walls:
            grid[i][j] = 2

        for i,j in guards:
            grid[i][j] = 2

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def is_inside(i, j):
            return 0 <= i < rows and 0 <= j < cols
        def can_be_guard(i, j):
            return grid[i][j] != 2
        for x, y in guards:
            for dx,dy in directions:
                curr_x = x + dx
                curr_y = y + dy
                while is_inside(curr_x, curr_y) and can_be_guard(curr_x, curr_y):
                    grid[curr_x][curr_y] = 1
                    curr_x += dx
                    curr_y += dy

        print(grid)
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    ans += 1
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]])
        self.assertEqual(7, actual)
        
    def test_case_2(self):
        actual = self.s.countUnguarded(m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]])
        self.assertEqual(4, actual)

    def test_case_3(self):
        actual = self.s.countUnguarded(m = 2, n = 5, guards = [[0,0], [0,1], [1,3]], walls = [[0,2]])
        self.assertEqual(1, actual)

if __name__ == '__main__':
    unittest.main()

