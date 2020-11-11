from typing import List, Tuple


class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        numIslands = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    numIslands += 1
                    self.unmark(i, j, grid)
        return numIslands


    def unmark(self, x:int, y: int, grid):
        # unmark current
        grid[x][y] = "0"
        # use BFS to unmark adjacent tiles
        directions = [(-1, 0), (1, 0), (0, - 1), (0, 1)]
        for direction in directions:
            n_x = x + direction[0]
            n_y = y + direction[1]
            if self.isLand(n_x, n_y, grid):
                self.unmark(n_x, n_y, grid)


    def isLand(self, x, y, grid):
        rows = len(grid)
        cols = len(grid[0])
        return 0<=x<rows and 0<=y<cols and grid[x][y] == "1"





