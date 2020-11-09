from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        for _ in range(k):
            last = grid[rows - 1][cols - 1]
            for i in range(rows):
                for j in range(cols):
                    temp = grid[i][j]
                    grid[i][j] = last
                    last = temp

        return grid
