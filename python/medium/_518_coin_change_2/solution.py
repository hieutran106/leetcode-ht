from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        # base case - have 1 way to change 0 amount
        for i in range(n+1):
            dp[i][0] = 1

        for c in range(1, n+1):
            for a in range(1, amount + 1):
                coin_value = coins[c - 1]

                # not using the i-th coin, only use the first (i-1)th coin
                dp[c][a] = dp[c - 1][a]
                # can use coin_value, unlimited times
                if a >= coin_value:
                    dp[c][a] += dp[c][a - coin_value]

        return dp[n][amount]