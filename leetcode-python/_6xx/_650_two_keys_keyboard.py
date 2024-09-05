import unittest
from typing import List
import math
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            # cal dp[i]
            res = float("inf")
            for j in range(1, i//2 + 1):
                if i % j == 0:
                    res = min(res, dp[j] + i /j )
            dp[i] = res
        return int(dp[n])
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.minSteps(3)
        self.assertEqual(3, actual)
        
    def test_case_2(self):
        actual = self.s.minSteps(1)
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.minSteps(4)
        self.assertEqual(4, actual)

    def test_case_5(self):
        actual = self.s.minSteps(6)
        self.assertEqual(5, actual)

    def test_case_6(self):
        actual = self.s.minSteps(12)
        self.assertEqual(7, actual)

    def test_case_7(self):
        actual = self.s.minSteps(18)
        self.assertEqual(8, actual)

if __name__ == '__main__':
    unittest.main()

