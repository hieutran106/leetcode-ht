from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #      ┌──────┐                         ┌───────────┐
        #      │ hold │                         │    hold   │
        #      │      │                         │           │
        # ┌────▼──────┴┐      buy          ┌────▼────┐      │
        # │            ├──────────────────►│ Can sell├──────┘
        # │  Can buy   │                   │         │
        # │            │                   └────┬────┘
        # └────▲───────┘                        │
        #      │                                │
        #      │                                │
        #      │                                │
        #      │  cooldown ┌────────────┐  sell │
        #      └───────────┤  Must hold ◄───────┘
        #                  │            │
        #                  └────────────┘

        n = len(prices)
        dp = [[0] * (n+1) for _ in range(3)]
        dp[0][1] = 0
        dp[1][1] = - prices[0]
        dp[2][1] = -1
        for i in range(2, n+1):
            # can buy
            dp[0][i] = max(dp[0][i-1], dp[2][i-1])
            # can sell
            dp[1][i] = max(dp[1][i-1], dp[0][i-1] - prices[i-1])
            # must hold
            dp[2][i] = dp[1][i-1] + prices[i-1]

        res = max(dp[0][n], dp[1][n], dp[2][n])
        return res
