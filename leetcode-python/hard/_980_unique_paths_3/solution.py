from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        zeros = 0
        sx = 0
        sy = 0
        # count the number of empty squares and determine starting pos
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    zeros += 1
                elif grid[i][j] == 1:
                    sx = i
                    sy = j
        paths = self.dfs(grid, m, n, sx, sy, zeros)
        return paths

    def dfs(self, grid: List[List[int]], m, n, x, y, zeros):
        if x < 0 or x >=m or y <0 or y >=m:
            return 0

        if grid[x][y] == 2:
            if zeros == -1:
                return 1
            else:
                return 0

        grid[x][y] = 1
        zeros -= 1
        paths = self.dfs(grid, m, n, x-1, y, zeros) + self.dfs(grid, m, n, x+1, y, zeros) + self.dfs(grid, m, n, x, y-1, zeros) + self.dfs(grid, m, n, x, y + 1, zeros)
        # backtrack
        grid[x][y] = 0
        zeros += 1
        return paths
