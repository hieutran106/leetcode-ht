import collections
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def can_flow(ocean):
            to_ocean = [[False for _ in range(cols)] for _ in range(rows)]
            q = collections.deque()
            visit = set()
            for c in range(cols):
                if ocean == 'pacific':
                    q.append((0, c))
                else:
                    q.append((rows - 1, c))
            for r in range(rows):
                if ocean == 'pacific':
                    q.append((r, 0))
                else:
                    q.append((r, cols - 1))

            directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
            while q:
                row, col = q.popleft()
                visit.add((row, col))
                to_ocean[row][col] = True
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                            c in range(cols) and
                            heights[r][c] >= heights[row][col] and
                            (r, c) not in visit
                    ):
                        q.append((r, c))
            return to_ocean

        to_pacific = can_flow('pacific')
        to_atlantic = can_flow('atlantic')
        result = []
        for r in range(rows):
            for c in range(cols):
                if to_pacific[r][c] and to_atlantic[r][c]:
                    result.append([r, c])
        return result
