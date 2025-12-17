import unittest
from typing import List

# Date: 2025-12-17
# Problem: 123 best_time_buy_sell_stock_3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        def dp(i, remaining, state):
            if i == n or (remaining == 0 and state == 'can_buy'):
                return 0
            if (i, remaining, state) in memo:
                return memo[(i, remaining, state)]
            c1, c2 = None, None
            if state == 'can_buy':
                # do nothing
                c1 = dp(i+1, remaining, 'can_buy')
                # buy
                c2 = -prices[i] + dp(i+1, remaining - 1, 'can_sell')

            elif state == 'can_sell':
                # do nothing
                c1 = dp(i+1, remaining, 'can_sell')
                c2 = prices[i] + dp(i+1, remaining, 'can_buy')
            res = max(c1, c2)
            memo[(i, remaining, state)] = res
            return res

        ans = dp(0, 2, 'can_buy')
        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.maxProfit(prices = [3,3,5,0,0,3,1,4])
        self.assertEqual(6, actual)
        
    def test_case_2(self):
        actual = self.s.maxProfit(prices = [1,2,3,4,5])
        self.assertEqual(4, actual)

    def test_case_3(self):
        actual = self.s.maxProfit(prices = [7,6,4,3,1])
        self.assertEqual(0, actual)

    def test_case4(self):
        actual = self.s.maxProfit([2, 4, 1])
        self.assertEqual(actual, 2)

    def test_case5(self):
        actual = self.s.maxProfit([3, 2, 6, 5, 0, 3])
        self.assertEqual(actual, 7)

if __name__ == '__main__':
    unittest.main()

