from .solution import Solution
import unittest

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        s = Solution()
        input = [[1,2,3],
              [4,5,6],
              [7,8,9]]
        actual = s.diagonalSum(input)
        self.assertEqual(actual, 25)

    def test_case_2(self):
        s = Solution()
        input = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
        actual = s.diagonalSum(input)
        self.assertEqual(actual, 8)

    def test_case_3(self):
        s = Solution()
        input = [[5]]
        actual = s.diagonalSum(input)
        self.assertEqual(actual, 5)