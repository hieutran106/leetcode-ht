import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        actual = self.s.searchMatrix(matrix, target)
        self.assertEqual(True, actual)

    def test_case_2(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 13
        actual = self.s.searchMatrix(matrix, target)
        self.assertEqual(False, actual)

    def test_case_3(self):
        matrix = [[1]]
        target = 1
        actual = self.s.searchMatrix(matrix, target)
        self.assertEqual(True, actual)

    def test_case_4(self):
        matrix = [[1]]
        target = 2
        actual = self.s.searchMatrix(matrix, target)
        self.assertEqual(False, actual)

    def test_case_5(self):
        matrix = [[1, 1]]
        target = 0
        actual = self.s.searchMatrix(matrix, target)
        self.assertEqual(False, actual)

    def test_case_6(self):
        matrix = [[0, 0, 1], [1, 1, 2]]
        target = 0
        actual = self.s.searchMatrix(matrix, target)
        self.assertEqual(True, actual)

    def test_case_7(self):
        matrix = [[0, 0, 1], [1, 1, 2]]
        target = 2
        actual = self.s.searchMatrix(matrix, target)
        self.assertEqual(True, actual)

    def test_case_8(self):
        matrix = [[0, 0, 1], [1, 1, 2]]
        target = 3
        actual = self.s.searchMatrix(matrix, target)
        self.assertEqual(False, actual)

if __name__ == '__main__':
    unittest.main()

