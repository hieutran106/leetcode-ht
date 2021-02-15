from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        upscale_grid = self.upscale(grid)
        regions = self.count_regions(upscale_grid, grid)
        return regions

    def upscale(self, grid: List[str]):
        n = len(grid)
        n_upscale = 2 * n
        result = [[0 for i in range(n_upscale)] for j in range(n_upscale)]
        for r in range(n):
            for c in range(n):
                curr_char = grid[r][c]
                upscale_row = 2 * r
                upscale_col = 2 * c
                if curr_char == "/":
                    result[upscale_row][upscale_col + 1] = 1
                    result[upscale_row + 1][upscale_col] = 1
                elif curr_char == "\\":
                    result[upscale_row][upscale_col] = 1
                    result[upscale_row + 1][upscale_col + 1] = 1

        return result

    def count_regions(self, grid, original_grid):
        num_region = 0
        n = len(grid)
        for r in range(n):
            for c in range(n):
                curr = grid[r][c]
                if curr == 0:
                    num_region += 1
                    self.dfs(r, c, grid, n, original_grid)

        return num_region

    def dfs(self, start_row, start_col, grid, n, orignal_grid):
        if not (0 <= start_row < n and 0 <= start_col < n):
            return
        if grid[start_row][start_col] != 0:
            return

        grid[start_row][start_col] = -1
        self.dfs(start_row + 1, start_col, grid, n, orignal_grid)
        self.dfs(start_row - 1, start_col, grid, n, orignal_grid)
        self.dfs(start_row, start_col + 1, grid, n, orignal_grid)
        self.dfs(start_row, start_col - 1, grid, n, orignal_grid)

        orignal_row = start_row // 2
        orignal_col = start_col // 2
        if orignal_grid[orignal_row][orignal_col] == "\\":
            self.dfs(start_row + 1, start_col+1, grid, n, orignal_grid)
            self.dfs(start_row -1, start_col -1, grid, n, orignal_grid)
        elif orignal_grid[orignal_row][orignal_col] == "/":
            self.dfs(start_row + 1, start_col - 1, grid, n, orignal_grid)
            self.dfs(start_row - 1, start_col + 1, grid, n, orignal_grid)

