import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        s = Solution()
        grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 1)

    def test_case_2(self):
        s = Solution()
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 3)

    def test_case_3(self):
        s = Solution()
        grid = [
            ["1", "0", "0", "1", "1"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["1", "0", "0", "1", "1"]
        ]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 5)

    def test_case_4(self):
        s = Solution()
        grid = [
            ["0"],
        ]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 0)

    def test_case_5(self):
        s = Solution()
        grid = [
            ["1"],
        ]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 1)

    def test_case_6(self):
        s = Solution()
        grid = [
            ["1", "1"],
            ["1", "0"]
        ]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 1)

    def test_case_7(self):
        s = Solution()
        grid = [
            ["0"],
        ]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 0)

    def test_case_8(self):
        s = Solution()
        grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 1)

    def test_case_9(self):
        s = Solution()
        grid = [["1", "1", "1"], ["1", "0", "0"], ["1", "1", "1"]]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 1)

    def test_case_10(self):
        s = Solution()
        grid = [["1", "1", "1"], ["0", "0", "1"], ["1", "1", "1"]]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 1)

    def test_case_11(self):
        s = Solution()
        grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "0"]]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 1)

    def test_case_11(self):
        s = Solution()
        grid = [["1", "1", "1", "1"], ["0", "0", "0", "0"], ["1", "1", "1", "1"], ["0", "0", "0", "0"], ["1", "1", "1", "1"], ["0", "0", "0", "0"]]
        actual = s.numIslands(grid)
        self.assertEqual(actual, 3)


if __name__ == '__main__':
    unittest.main()
