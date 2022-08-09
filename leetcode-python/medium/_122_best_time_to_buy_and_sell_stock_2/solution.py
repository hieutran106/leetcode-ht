from typing import List


class Solution:
    def maxProfit(self, prices):
        """
        Dp approach
        """
        n = len(prices)
        # dp[0] --> can buy
        # dp[1] --> cannot buy/ (or can sell)
        # dp[ith] --> max profit after i-th day
        dp = [[0] * n for _ in range(2)]

        dp[0][0] = 0
        dp[1][0] = - prices[0]
        for i in range(1, n):
            # handle can buy
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] + prices[i])
            # handle can sell
            dp[1][i] = max(dp[1][i-1], dp[0][i-1] - prices[i])

        return dp[0][n - 1]


class Solution2:
    def maxProfit(self, prices):
        """
        Check all increase in the value of stock. Greedy approach
        """
        res = 0
        for i in range(1, len(prices)):
            res += max(prices[i] - prices[i-1], 0)
        return res



class Solution3:
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[None] * (n + 1) for _ in range(2)]
        res = self.top_down(n, 0, prices, dp)
        return res

    def top_down(self, i: int, can_buy: int, prices: List[int], dp):
        if i == 1 and can_buy == 0:
            return 0
        if i == 1 and can_buy == 1:
            return - prices[0]

        if dp[can_buy][i] is not None:
            return dp[can_buy][i]

        if can_buy == 0:
            value = max(self.top_down(i-1, 0, prices, dp), self.top_down(i-1, 1, prices, dp) + prices[i-1])
        else:
            value = max(self.top_down(i-1, 1, prices, dp), self.top_down(i-1, 0, prices, dp) - prices[i-1])

        return value