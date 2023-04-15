import unittest
from typing import List

from .solution import Solution


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(i, j, pos, visited) -> bool:
            if pos == len(word):
                return True
            inside = 0 <= i < rows and 0 <= j < cols
            if not inside:
                return False

            if (i, j) in visited or board[i][j] != word[pos]:
                return False
            # continue build solution
            visited.add((i, j))
            top = backtrack(i - 1, j, pos + 1, visited)
            down = backtrack(i + 1, j, pos + 1, visited)
            left = backtrack(i, j - 1, pos + 1, visited)
            right = backtrack(i, j + 1, pos + 1, visited)
            # backtrack
            visited.remove((i, j))
            return top or down or left or right

        for i in range(rows):
            for j in range(cols):
                visited = set()
                if backtrack(i, j, 0, visited):
                    return True

        return False


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED")
        self.assertEqual(True, actual)

    def test_case_2(self):
        actual = self.s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE")
        self.assertEqual(True, actual)

    def test_case_3(self):
        actual = self.s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB")
        self.assertEqual(False, actual)

    def test_case_4(self):
        actual = self.s.exist(board=[["a"]], word="a")
        self.assertEqual(True, actual)

    def test_case_5(self):
        actual = self.s.exist(board=[["a"]], word="b")
        self.assertEqual(False, actual)

    def test_case_6(self):
        actual = self.s.exist(board=[["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
                              word="ABCESEEEFS")
        self.assertEqual(True, actual)


if __name__ == '__main__':
    unittest.main()
