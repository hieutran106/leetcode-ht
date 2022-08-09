from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
                                            ___________
                                 ________ | Top floor
                    ___________ |   20
        __________ | 15 (start)
        10 (start)
        :param cost:
        :return:
        """
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])
        dp = [0] * (n + 1)
        # dp[i] is the minimum cost to reach i-th floor
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n+1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        # dp[n] is the minimum cost to reach the top floor
        return dp[n]
