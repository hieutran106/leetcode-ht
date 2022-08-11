from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    self.dfs(i, j, rows, cols, board)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '-':
                    board[i][j] = 'O'

    def dfs(self, x, y, rows, cols, board):
        visited = set()
        queue = [(x, y)]
        on_edge = False

        while len(queue) > 0:
            (i, j) = queue.pop()
            visited.add((i, j))
            if (i == 0) or (i == rows-1) or (j ==0) or (j == cols - 1):
                on_edge = True

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]

                on_board = (0 <= next_i < rows) and (0 <= next_j < cols)
                if not on_board:
                    continue
                if (next_i, next_j) in visited:
                    continue
                if board[next_i][next_j] != 'O':
                    continue

                queue.append((next_i, next_j))


        if on_edge:
            self.fill('-', visited, board)
        else:
            self.fill('X', visited, board)

    def fill(self, char, visited, board):
        for point in visited:
            board[point[0]][point[1]] = char
