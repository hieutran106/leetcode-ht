import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.maxAreaOfIsland(
            grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                  [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                  [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])
        self.assertEqual(6, actual)

    def test_case_2(self):
        actual = self.s.maxAreaOfIsland(grid=[[0, 0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual(0, actual)

    def test_case_3(self):
        actual = self.s.maxAreaOfIsland(grid=[
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ])
        self.assertEqual(1, actual)


if __name__ == '__main__':
    unittest.main()
