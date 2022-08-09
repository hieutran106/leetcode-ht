from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * (n+1) for _ in range(2)]
        dp[0][1] = 0
        dp[1][1] = - prices[0]
        for i in range(2, n+1):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] + prices[i-1] - fee)
            dp[1][i] = max(dp[1][i-1], dp[0][i-1] - prices[i-1])

        return max(dp[0][n], dp[1][n])
