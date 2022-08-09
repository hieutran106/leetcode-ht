from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k == 0 or n ==0:
            return 0
        rows = 2 * k
        dp = [[float('-inf') for _ in range(len(prices))] for _ in range(rows)]
        dp[0][0] = - prices[0]

        for i in range(1, n):
            for j in range(rows):
                if j == 0:
                    dp[0][i] = max(dp[0][i - 1], -prices[i])
                elif j % 2 == 1:
                    dp[j][i] = max(dp[j][i - 1], dp[j-1][i] + prices[i])
                else:
                    dp[j][i] = max(dp[j][i - 1], dp[j - 1][i] - prices[i])

        res = 0
        for j in range(rows):
            if dp[j][n-1] > res:
                res = dp[j][n-1]

        return res
