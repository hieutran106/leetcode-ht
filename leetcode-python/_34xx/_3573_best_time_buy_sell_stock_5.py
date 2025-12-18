import unittest
from typing import List


# Date: 2025-12-17
# Problem: 3573 best_time_buy_sell_stock_5
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        memo = {}

        def dp(i, remaining, state):
            if remaining == 0 and state == 's1':
                return 0
            if i ==n:
                if state == 's1':
                    return 0
                else:
                    return float("-inf")
            if (i, remaining, state) in memo:
                return memo[(i, remaining, state)]
            if state == 's1':
                # do nothing
                c1 = dp(i + 1, remaining, 's1')
                # normal buy
                c2 = -prices[i] + dp(i + 1, remaining - 1, 's2')
                # short sell
                c3 = prices[i] + dp(i + 1, remaining - 1, 's3')
                ans = max(c1, c2, c3)
            elif state == 's2':
                c1 = dp(i + 1, remaining, 's2')
                # normal sell
                c2 = prices[i] + dp(i + 1, remaining, 's1')
                ans = max(c1, c2)
            else:
                c1 = dp(i + 1, remaining, 's3')
                # buy back
                c2 = -prices[i] + dp(i + 1, remaining, 's1')
                ans = max(c1, c2)
            memo[(i, remaining, state)] = ans
            return ans

        ans = dp(0, k, 's1')
        memo.clear() # Prevent memory limit exceeded
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.maximumProfit(prices=[1, 7, 9, 8, 2], k=2)
        self.assertEqual(14, actual)

    def test_case_2(self):
        actual = self.s.maximumProfit(prices = [12,16,19,19,8,1,19,13,9], k = 3)
        self.assertEqual(36, actual)

    def test_case_3(self):
        actual = self.s.maximumProfit(prices=[10, 2], k=2)
        self.assertEqual(8, actual)

    def test_case_4(self):
        actual = self.s.maximumProfit(prices=[2, 10], k=1)
        self.assertEqual(8, actual)


if __name__ == '__main__':
    unittest.main()
