import math

class Solution:
    def solve(self, weights, values, max_weight):
        dp = [0 for i in range(max_weight + 1)] * (len(values) + 1)
        for i in range(len(values) + 1):
            for j in range(len(max_weight) + 1):
                without_current = dp[i - 1][j]

                with_current = 0
                weight = weights[i]
                value = values[i]
                if weight < j:
                    with_current = value + dp[i][j - weight]

                # compare
                dp[i][j] = max(without_current, with_current)


        return dp[len(values)][max_weight]