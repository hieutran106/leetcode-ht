import unittest
import math
from typing import List

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = [num * num for num in range(0, math.isqrt(c) + 1)]
        l = 0
        r = len(squares) - 1
        while l <= r:
            if squares[l] + squares[r] == c:
                return True
            elif squares[l] + squares[r] < c:
                l+= 1
            else:
                r-= 1
        return False

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.judgeSquareSum(5)
        self.assertEqual(actual, True)
        
    def test_case_2(self):
        actual = self.s.judgeSquareSum(3)
        self.assertEqual(actual, False)

    def test_case_3(self):
        actual = self.s.judgeSquareSum(2)
        self.assertEqual(actual, True)

    def test_case_4(self):
        actual = self.s.judgeSquareSum(32)
        self.assertEqual(actual, True)

    def test_case_5(self):
        actual = self.s.judgeSquareSum(4)
        self.assertEqual(actual, True)


if __name__ == '__main__':
    unittest.main()

