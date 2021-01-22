from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        start_color = image[sr][sc]

        q = [(sr, sc)]

        while len(q) > 0:
            curr = q.pop()
            r = curr[0]
            c = curr[1]
            visited[r][c] = True
            for direction in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                new_r = r + direction[0]
                new_col = c + direction[1]
                if not self.valid(new_r, new_col, rows, cols):
                    continue

                if image[new_r][new_col] == start_color and not visited[new_r][new_col]:
                    q.append((new_r, new_col))

            image[r][c] = newColor

        return image

    def valid(self, r, c, rows, cols):
        return 0 <= r < rows and 0 <= c < cols
