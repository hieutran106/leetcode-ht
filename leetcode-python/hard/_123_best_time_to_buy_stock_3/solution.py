from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[float('-inf') for _ in range(len(prices))] for _ in range(4)]
        dp[0][0] = - prices[0]
        n = len(prices)
        for i in range(1, n):
            dp[0][i] = max(dp[0][i-1], -prices[i])
            dp[1][i] = max(dp[1][i-1], dp[0][i] + prices[i])
            dp[2][i] = max(dp[2][i-1], dp[1][i] - prices[i])
            dp[3][i] = max(dp[3][i-1], dp[2][i] + prices[i])

        return max(dp[1][n-1], dp[3][n-1], 0)



    def maxProfit1(self, prices: List[int]) -> int:
        n = len(prices)
        s1 = -prices[0]
        s2 = -10000
        s3 = -10000
        s4 = -10000
        for i in range(1, len(prices)):
            s1_new = max(s1, -prices[i])
            s2_new = max(s1 + prices[i], s2)
            s3_new = max(s2 - prices[i], s3)
            s4_new = max(s3 + prices[i], s4)

            s1 = s1_new
            s2 = s2_new
            s3 = s3_new
            s4 = s4_new

        return max(s2, s4, 0)
