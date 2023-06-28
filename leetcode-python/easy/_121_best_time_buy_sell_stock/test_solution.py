import unittest
from typing import List

from .solution import Solution


class Solution:
    def maxProfit_optimized(self, prices: List[int]) -> int:
        n = len(prices)
        min_val = prices[0] # Min value from 0 index to i-1
        max_profit = 0
        for i in range(1, n):
            min_val = min(min_val, prices[i - 1])
            max_profit = max(max_profit, prices[i] - min_val)
        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n # Profit if stock is sold at day i-th
        min_val = prices[0]  # Min price from 0 -> (i-1) th
        for i in range(1, n):
            min_val = min(min_val, prices[i - 1])
            dp[i] = prices[i] - min_val
        return max(dp)


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.maxProfit(prices=[7, 1, 5, 3, 6, 4])
        self.assertEqual(5, actual)

    def test_case_2(self):
        actual = self.s.maxProfit(prices=[7, 6, 4, 3, 1])
        self.assertEqual(0, actual)

    def test_case_3(self):
        actual = self.s.maxProfit(prices=[1])
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.maxProfit(prices=[30, 1, 8, 2, 20])
        self.assertEqual(19, actual)


if __name__ == '__main__':
    unittest.main()
