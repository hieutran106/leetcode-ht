from typing import List

class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        result = 0
        rows = len(grid)
        cols = len(grid[0])

        # save land position in an array
        lands = []
        for i in range(rows):
            for j in range(cols):
                value = grid[i][j]
                if value == "1":
                    lands.append((i, j))

        while len(lands) > 0:
            land = lands.pop()
            directions = [(-1, 0), (1, 0), (0, - 1), (0, 1)]
            next_lands = []
            for direction in directions:
                x = land[0] + direction[0]
                y = land[1] + direction[1]
                c = (x, y)
                if c in lands:
                    next_lands.append(c)

            if len(next_lands) == 0:
                result += 1

        return result
