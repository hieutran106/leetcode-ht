# tags: BFS
from typing import List, Tuple


class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        numIslands = 0
        rows = len(grid)
        cols = len(grid[0])

        map = [[0 for j in range(cols)] for i in range(rows)]

        # Loop through grid
        for i in range(rows):
            for j in range(cols):
                # Skip if current tile is land of an island
                if map[i][j] != 0:
                    continue
                # Skip if current tile is ocean
                if grid[i][j] != "1":
                    continue

                # start DFS
                numIslands += 1
                start_land = (i,j)
                queue = [start_land]
                visited = []
                while len(queue) > 0:
                    current = queue.pop()
                    visited.append(current)
                    # check adjacent tile
                    directions = [(-1, 0), (1, 0), (0, - 1), (0, 1)]
                    for direction in directions:
                        tile = (current[0] + direction[0], current[1] + direction[1])
                        (x, y) = tile
                        if self.isLand(tile, grid) and tile not in visited:
                            map[x][y] = numIslands
                            queue.append(tile)

        return numIslands



    def isLand(self, tile: Tuple[int, int], grid):
        rows = len(grid)
        cols = len(grid[0])
        (x, y) = tile
        return 0<=x<rows and 0<=y<cols and grid[x][y] == "1"





