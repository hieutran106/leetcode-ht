import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.getSkyline(buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
        self.assertEqual([[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]], actual)

    def test_case_2(self):
        actual = self.s.getSkyline(buildings = [[0,2,3],[2,5,3]])
        self.assertEqual([[0,3],[5,0]], actual)

    def test_case_3(self):
        actual = self.s.getSkyline(buildings=[[15, 20, 10], [19, 24, 8]])
        self.assertEqual([[15, 10], [20,8], [24, 0]], actual)

    def test_case_4(self):
        actual = self.s.getSkyline(buildings=[[15, 20, 10]])
        self.assertEqual([[15, 10], [20,0]], actual)

    def test_case_5(self):
        buildings = [[1,3,3], [2,4,4], [5,8,2], [6,7,4], [8,9,4]]
        actual = self.s.getSkyline(buildings=buildings)
        self.assertEqual([[1,3], [2,4], [4,0], [5,2], [6,4], [7,2], [8,4], [9,0]], actual)

    def test_case_7(self):
        buildings = [[5,8,2], [8, 9, 4]]
        actual = self.s.getSkyline(buildings=buildings)
        self.assertEqual([[5,2], [8, 4], [9,0]], actual)

    def test_case_8(self):
        buildings = [[5,8,2], [8, 9, 4], [8, 10, 6]]
        actual = self.s.getSkyline(buildings=buildings)
        self.assertEqual([[5,2], [8, 6], [10,0]], actual)

if __name__ == '__main__':
    unittest.main()

