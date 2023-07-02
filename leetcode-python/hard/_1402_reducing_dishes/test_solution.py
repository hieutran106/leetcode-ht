import unittest
from typing import List

from .solution import Solution

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        dp = [[float('-inf')] * (n+1) for _ in range(n)]
        # set first column to 0
        for i in range(n):
            dp[i][0] = 0
        # base case
        dp[0][1] = satisfaction[0]
        for i in range(1, n):
            for j in range(1, i + 2):
                dp[i][j] = max(dp[i-1][j-1] + satisfaction[i] * j, dp[i-1][j])

        return max(dp[n-1])

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.maxSatisfaction(satisfaction = [-1,-8,0,5,-9])
        self.assertEqual(14, actual)

    def test_case_2(self):
        actual = self.s.maxSatisfaction(satisfaction = [4,3,2])
        self.assertEqual(20, actual)

    def test_case_3(self):
        actual = self.s.maxSatisfaction(satisfaction = [-1,-4,-5])
        self.assertEqual(0, actual)

if __name__ == '__main__':
    unittest.main()

