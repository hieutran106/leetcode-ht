import unittest
from .solution import Solution
from .solution2 import Solution as Solution2

class MyTestCase(unittest.TestCase):
    @classmethod
    def setup_solution(cls):
        solution = Solution2()
        return solution

    def test_case_1(self):
        s = MyTestCase.setup_solution()
        grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 1)

    def test_case_2(self):
        s = MyTestCase.setup_solution()
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 3)

    def test_case_3(self):
        s = MyTestCase.setup_solution()
        grid = [
            ["1", "0", "0", "1", "1"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["1", "0", "0", "1", "1"]
        ]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 5)

    def test_case_4(self):
        s = MyTestCase.setup_solution()
        grid = [
            ["0"],
        ]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 0)

    def test_case_5(self):
        s = MyTestCase.setup_solution()
        grid = [
            ["1"],
        ]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 1)

    def test_case_6(self):
        s = MyTestCase.setup_solution()
        grid = [
            ["1", "1"],
            ["1", "0"]
        ]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 1)

    def test_case_7(self):
        s = MyTestCase.setup_solution()
        grid = [
            ["0"],
        ]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 0)

    def test_case_8(self):
        s = MyTestCase.setup_solution()
        grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 1)

    def test_case_9(self):
        s = MyTestCase.setup_solution()
        grid = [["1", "1", "1"], ["1", "0", "0"], ["1", "1", "1"]]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 1)

    def test_case_10(self):
        s = MyTestCase.setup_solution()
        grid = [["1", "1", "1"], ["0", "0", "1"], ["1", "1", "1"]]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 1)

    def test_case_11(self):
        s = MyTestCase.setup_solution()
        grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "0"]]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 1)

    def test_case_11(self):
        s = MyTestCase.setup_solution()
        grid = [["1", "1", "1", "1"], ["0", "0", "0", "0"], ["1", "1", "1", "1"], ["0", "0", "0", "0"], ["1", "1", "1", "1"], ["0", "0", "0", "0"]]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 3)


if __name__ == '__main__':
    unittest.main()
