import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.pacificAtlantic(
            heights=[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
        self.assertEqual([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]], actual)

    def test_case_2(self):
        actual = self.s.pacificAtlantic(heights=[[1]])
        self.assertEqual([[0, 0]], actual)

    def test_case_3(self):
        actual = self.s.pacificAtlantic(heights=[[1, 2], [3, 4]])
        self.assertEqual([[0, 1], [1, 0], [1, 1]], actual)

    def test_case_4(self):
        actual = self.s.pacificAtlantic(heights=[[1,2,3],[8,9,4],[7,6,5]])
        self.assertEqual([[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]], actual)

if __name__ == '__main__':
    unittest.main()
