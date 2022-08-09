import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        grid = []
        grid.append([1, 2, 3])
        grid.append([4, 5, 6])
        grid.append([7, 8, 9])
        s = Solution()
        actual = s.shiftGrid(grid, 1)

        self.assertCountEqual([9, 1, 2], actual[0])
        self.assertCountEqual([3, 4, 5], actual[1])
        self.assertCountEqual([6, 7, 8], actual[2])

    def test_case_2(self):
        grid = []
        grid.append([3,8,1,9])
        grid.append([19,7,2,5])
        grid.append([4,6,11,10])
        grid.append([12,0,21,13])
        s = Solution()
        actual = s.shiftGrid(grid, 4)

        self.assertCountEqual([12,0,21,13], actual[0])
        self.assertCountEqual([3,8,1,9], actual[1])
        self.assertCountEqual([19,7,2,5], actual[2])
        self.assertCountEqual([4,6,11,10], actual[3])

    def test_case_3(self):
        grid = []
        grid.append([1, 2, 3])
        grid.append([4, 5, 6])
        grid.append([7, 8, 9])
        s = Solution()
        actual = s.shiftGrid(grid, 9)

        self.assertCountEqual([1,2,3], actual[0])
        self.assertCountEqual([4,5,6], actual[1])
        self.assertCountEqual([7,8,9], actual[2])

    def test_case_4(self):
        grid = []
        grid.append([1])
        s = Solution()
        actual = s.shiftGrid(grid, 5)
        self.assertCountEqual([1], actual[0])


if __name__ == '__main__':
    unittest.main()
