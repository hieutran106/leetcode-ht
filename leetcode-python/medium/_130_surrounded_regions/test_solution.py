import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]
        self.s.solve(board)
        expect = [
             ["X", "X", "X", "X"],
             ["X", "X", "X", "X"],
             ["X", "X", "X", "X"],
             ["X", "O", "X", "X"]
        ]
        self.assertEqual(board, expect)

    def test_case_2(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["O", "X", "O", "X"],
            ["O", "X", "X", "X"]
        ]
        self.s.solve(board)
        expect = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["O", "X", "X", "X"],
            ["O", "X", "X", "X"]
        ]
        self.assertEqual(board, expect)

    def test_case_3(self):
        board = [["X"]]
        self.s.solve(board)
        self.assertEqual(board, [["X"]])

    def test_case_4(self):
        board = [["O"]]
        self.s.solve(board)
        self.assertEqual(board, [["O"]])

    def test_case_5(self):
        board = [["O", "X"], ["X", "O"]]
        self.s.solve(board)
        self.assertEqual(board, [["O", "X"], ["X", "O"]])


if __name__ == '__main__':
    unittest.main()
