from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        half = self.solve(stones, stones, total // 2)
        residual = total - half
        return abs(residual - half)

    def solve(self, values: List[int], weights: List[int], capacity: int):
        rows = len(values) + 1
        cols = capacity + 1
        dp = [[0] * cols for _ in range(rows)]
        for i in range(1, rows):
            for c in range(1, cols):
                profit1 = dp[i - 1][c]

                profit2 = 0
                curr_weight = weights[i - 1]
                if curr_weight <= c:
                    profit2 = values[i - 1] + dp[i - 1][c - curr_weight]

                # compare
                dp[i][c] = max(profit1, profit2)

        return dp[rows - 1][cols - 1]
